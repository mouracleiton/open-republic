#!/usr/bin/env python3
"""
OpenConstitutionalEngine -- Motor Constitucional (logica + dados separados)
============================================================================
ARQUITETURA:
  - data.json         Toda estrutura de dados (principios, regras, thresholds)
  - disernmentos/     O raciocinio etico/filosofico de cada principio
  - este .py          Logica pura: le json, avalia regras, nao tem hardcode

O motor nao sabe quais sao os principios. Le do data.json. Se adicionar
P12 ao json, o motor valida automaticamente. Zero codigo muda.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Union
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import json
import os


# ============================================================================
# 1. DATACLASSES (estrutura de saida -- independente do data.json)
# ============================================================================

@dataclass
class CheckConformidade:
    """Resultado da verificacao de UM principio num sistema."""
    principio_id: str   # "P1", "P2", ...
    principio_nome: str
    passou: bool
    score: float        # 0-100
    notas: str = ""


@dataclass
class ViolacaoConstitucional:
    """Uma violacao detectada num sistema."""
    principio_id: str
    principio_nome: str
    severidade: str     # "menor", "maior", "critica"
    sistema_id: str
    sistema_nome: str
    descricao: str
    recomendacao: str
    detectado_em: str = ""


@dataclass
class MetadadosSistema:
    """Metadados de um sistema registrado para validacao.

    Todos os campos sao booleans/floats/strings que as regras do data.json
    consultam via 'field'. Se um principio precisar de um campo novo,
    adicione aqui E referencie no data.json.
    """
    sistema_id: str
    nome: str
    dominio: str
    caminho: str
    # P1
    criado_por: str = "comunidade"
    aprovado_por_votacao: bool = False
    votos: int = 0
    ponto_unico_falha: bool = False
    tem_sucessor: bool = False
    docs_publicos: bool = False
    # P2
    afeta_corpos: bool = False
    exige_consentimento_corporal: bool = False
    # P3
    base_trabalho_respeitada: bool = True
    coleta_dados_trabalho: bool = False
    # P4
    decisoes_opacas: bool = False
    # P5
    logs_publicos: bool = False
    caixa_preta: bool = False
    # P6
    exclui_por_dinheiro: bool = False
    exclui_por_deficiencia: bool = False
    # P7
    seguranca_acessivel: bool = False
    # P8
    usa_ia: bool = False
    humano_no_loop: bool = True
    engagement_por_furia: bool = False
    # P9
    polariza_identidade: bool = False
    # P10
    e_drone: bool = False
    drone_vigia: bool = False
    drone_arma: bool = False
    drone_espiona: bool = False
    # P11
    e_servico_digital: bool = False
    exige_smartphone: bool = False
    exige_internet: bool = False
    exige_leitura: bool = False
    tem_canal_analogico: bool = False
    ensina_dentro: bool = False
    tem_assistente_humana: bool = False
    pct_exclusao_digital: float = 0.0
    # P12
    e_sistema_cibernetico: bool = False
    infraestrutura_critica: bool = False
    tem_ids: bool = False
    cidadaos_treinados: bool = False
    # P12 proibicoes (5 NAO)
    coopta_criminosos: bool = False
    militariza_civis: bool = False
    financia_fachada: bool = False
    e_ofensivo: bool = False
    e_secreto: bool = False
    # P13
    e_agente_publico: bool = False
    recusou_divulgar: bool = False
    usou_sigilo_para_esconder: bool = False
    comunicacao_secreta_com_lobby: bool = False
    # P14
    e_custodiante_dados: bool = False
    coletou_sem_copia: bool = False
    reteve_sem_log: bool = False
    ignorou_revogacao: bool = False
    bloqueia_portabilidade: bool = False
    lucrou_sem_compensar: bool = False
    # geral
    descricao: str = ""
    conformidade: Optional[Dict[str, Any]] = None


# ============================================================================
# 2. AVALIADOR DE CONDICOES (le as regras declarativas do json)
# ============================================================================

class AvaliadorCondicao:
    """
    Avalia condicoes declarativas do data.json contra um MetadadosSistema.

    Formatos suportados no 'when':
      {"field": "X", "is": True}              -- meta.X == True
      {"field": "X", "is": "valor"}           -- meta.X == "valor"
      {"field": "X", "ne": "valor"}           -- meta.X != "valor"
      {"field": "X", "gt": 30}                -- meta.X > 30
      {"field": "X", "lt": 5}                 -- meta.X < 5
      {"all": [cond1, cond2, ...]}            -- AND
      {"any": [cond1, cond2, ...]}            -- OR
      {"all": [...], "and": [...]}            -- AND extra (alias)
      {"any": [...], "and": [...]}            -- any + and combinados
    """

    @staticmethod
    def avaliar(cond: Dict[str, Any], meta: MetadadosSistema) -> bool:
        """Retorna True se a condicao for satisfeita."""
        if "all" in cond:
            sub = cond["all"]
            if isinstance(sub, list):
                if not all(AvaliadorCondicao.avaliar(s, meta) for s in sub):
                    return False
        if "any" in cond:
            sub = cond["any"]
            if isinstance(sub, list):
                if not any(AvaliadorCondicao.avaliar(s, meta) for s in sub):
                    return False
        if "and" in cond:
            sub = cond["and"]
            if isinstance(sub, list):
                if not all(AvaliadorCondicao.avaliar(s, meta) for s in sub):
                    return False

        # condicao simples de campo
        if "field" in cond:
            fname = cond["field"]
            val = getattr(meta, fname, None)
            if "is" in cond:
                return val == cond["is"]
            if "ne" in cond:
                return val != cond["ne"]
            if "gt" in cond and val is not None:
                return val > cond["gt"]
            if "lt" in cond and val is not None:
                return val < cond["lt"]
            if "gte" in cond and val is not None:
                return val >= cond["gte"]
            if "lte" in cond and val is not None:
                return val <= cond["lte"]

        # se chegou aqui com all/any, ja foi avaliado acima
        if "all" in cond or "any" in cond or "and" in cond:
            return True

        return False

    @staticmethod
    def formatar_nota(template: str, meta: MetadadosSistema) -> str:
        """Substitui placeholders {field} e {field:fmt} no texto da nota."""
        result = template
        # {field:.0f} formatos
        import re
        for m in re.finditer(r"\{(\w+)(?::([^}]+))?\}", result):
            fname = m.group(1)
            fmt = m.group(2)
            val = getattr(meta, fname, "")
            if fmt:
                try:
                    result = result.replace(m.group(0), format(val, fmt))
                except (ValueError, TypeError):
                    result = result.replace(m.group(0), str(val))
            else:
                result = result.replace(m.group(0), str(val))
        return result


# ============================================================================
# 3. MOTOR CONSTITUCIONAL (logica pura, le data.json)
# ============================================================================

class ConstitutionalEngine:
    """
    Motor que valida qualquer sistema contra os principios definidos em data.json.

    O motor nao sabe quantos principios existem. Le do json. Se adicionar
    P12 ao json, o motor valida automaticamente.
    """

    def __init__(self, data_path: Optional[str] = None) -> None:
        if data_path is None:
            data_path = os.path.join(os.path.dirname(__file__), "data.json")
        with open(data_path, encoding="utf-8") as f:
            self.data: Dict[str, Any] = json.load(f)

        self.pass_threshold: float = float(self.data.get("pass_threshold", 60))
        self.checks_executados: int = 0
        self.violacoes: List[ViolacaoConstitucional] = []
        self.sistemas: Dict[str, MetadadosSistema] = {}

    # -- registro -----------------------------------------------------------

    def registrar_sistema(self, meta: MetadadosSistema) -> None:
        self.sistemas[meta.sistema_id] = meta

    def registrar_sistema_simples(
        self, sistema_id: str, nome: str, dominio: str, caminho: str,
        **kwargs: Any,
    ) -> MetadadosSistema:
        meta = MetadadosSistema(
            sistema_id=sistema_id, nome=nome, dominio=dominio,
            caminho=caminho, **kwargs,
        )
        self.registrar_sistema(meta)
        return meta

    # -- validacao ----------------------------------------------------------

    def validar_sistema(self, sistema_id: str) -> Dict[str, Any]:
        """Valida UM sistema contra todos os principios do data.json."""
        meta = self.sistemas.get(sistema_id)
        if meta is None:
            return {"erro": f"Sistema nao encontrado: {sistema_id}"}

        checks: List[CheckConformidade] = []
        violacoes: List[ViolacaoConstitucional] = []

        for pid, pdata in self.data["principios"].items():
            c, v = self._avaliar_principio(pid, pdata, meta)
            checks.append(c)
            violacoes.extend(v)

        # score geral
        scores = [c.score for c in checks]
        avg_score = sum(scores) / len(scores) if scores else 0.0
        all_passed = all(c.passou for c in checks)
        max_sev = self._max_severidade(violacoes)
        status = self._status_por_severidade(max_sev)

        resultado: Dict[str, Any] = {
            "sistema_id": sistema_id,
            "sistema_nome": meta.nome,
            "dominio": meta.dominio,
            "checks": [
                {
                    "principio": f"{c.principio_id} {c.principio_nome}",
                    "passou": c.passou,
                    "score": round(c.score, 1),
                    "notas": c.notas,
                }
                for c in checks
            ],
            "score_geral": round(avg_score, 1),
            "totalmente_conforme": all_passed,
            "violacao_maxima": self.data["severidades"].get(
                max_sev, {"rotulo": "?"})["rotulo"],
            "violacoes_count": len(violacoes),
            "status": status,
            "timestamp": datetime.now().isoformat(),
        }
        meta.conformidade = resultado
        self.checks_executados += 1
        self.violacoes.extend(violacoes)
        return resultado

    def _avaliar_principio(
        self, pid: str, pdata: Dict[str, Any], meta: MetadadosSistema,
    ) -> Tuple[CheckConformidade, List[ViolacaoConstitucional]]:
        """Avalia um principio contra os metadados do sistema."""
        pnome = pdata["nome"]

        # skip condicao (ex: P10 nao-drone, P11 nao-digital)
        if "skip_if" in pdata:
            if AvaliadorCondicao.avaliar(pdata["skip_if"], meta):
                skip_note = pdata.get("skip_note", "N/A.")
                return (
                    CheckConformidade(
                        principio_id=pid, principio_nome=pnome,
                        passou=True, score=100, notas=skip_note,
                    ),
                    [],
                )

        score = 100.0
        notas: List[str] = []
        eval_mode = pdata.get("eval_mode", "all")

        if eval_mode == "chain":
            # chain: primeira regra que bater define o score, para
            for rule in pdata["rules"]:
                if AvaliadorCondicao.avaliar(rule["when"], meta):
                    if "set" in rule:
                        score = float(rule["set"])
                    elif "subtract" in rule:
                        score -= rule["subtract"]
                    nota = AvaliadorCondicao.formatar_nota(rule["note"], meta)
                    notas.append(nota)
                    break  # chain para na primeira
        else:
            # all: todas as regras aplicam
            for rule in pdata["rules"]:
                if AvaliadorCondicao.avaliar(rule["when"], meta):
                    if "set" in rule:
                        score = float(rule["set"])
                    elif "subtract" in rule:
                        score -= rule["subtract"]
                    nota = AvaliadorCondicao.formatar_nota(rule["note"], meta)
                    notas.append(nota)

        score = max(0.0, score)
        passou = score >= self.pass_threshold
        pass_note = pdata.get("pass_note", "Conforme.")
        check = CheckConformidade(
            principio_id=pid, principio_nome=pnome,
            passou=passou, score=score,
            notas=" | ".join(notas) if notas else pass_note,
        )

        viol: List[ViolacaoConstitucional] = []
        if not passou:
            sev = self._resolver_severidade(pdata.get("fail_severity", "menor"), meta)
            viol.append(ViolacaoConstitucional(
                principio_id=pid, principio_nome=pnome,
                severidade=sev, sistema_id=meta.sistema_id,
                sistema_nome=meta.nome, descricao=check.notas,
                recomendacao=pdata.get("recommendation", ""),
                detectado_em=datetime.now().isoformat(),
            ))
        return check, viol

    def _resolver_severidade(
        self, spec: Union[str, Dict[str, Any]], meta: MetadadosSistema,
    ) -> str:
        """Resolve severidade que pode ser fixa ou condicional."""
        if isinstance(spec, str):
            return spec
        if isinstance(spec, dict):
            if "if" in spec:
                if AvaliadorCondicao.avaliar(spec["if"], meta):
                    return spec.get("then", "menor")
                return spec.get("else", "menor")
            if "if_any" in spec:
                conds = spec["if_any"]
                if isinstance(conds, list) and any(
                    AvaliadorCondicao.avaliar(c, meta) for c in conds
                ):
                    return spec.get("then", "menor")
                return spec.get("else", "menor")
        return "menor"

    def _max_severidade(self, violacoes: List[ViolacaoConstitucional]) -> str:
        """Retorna a severidade de maior peso entre as violacoes."""
        if not violacoes:
            return "nenhuma"
        pesos = self.data["severidades"]
        return max(
            (v.severidade for v in violacoes),
            key=lambda s: pesos.get(s, {"peso": 0})["peso"],
            default="nenhuma",
        )

    def _status_por_severidade(self, sev: str) -> str:
        """Mapeia severidade para status (usando thresholds do json)."""
        thresholds = self.data["status_thresholds"]
        pesos = self.data["severidades"]
        peso = pesos.get(sev, {"peso": 0})["peso"]
        if peso >= thresholds["banido_severidade"]:
            return self.data["status"]["banido"]["rotulo"]
        if peso >= thresholds["suspenso_severidade"]:
            return self.data["status"]["suspenso"]["rotulo"]
        if peso >= thresholds["revisao_severidade"]:
            return self.data["status"]["revisao"]["rotulo"]
        return self.data["status"]["conforme"]["rotulo"]

    def validar_todos(self) -> Dict[str, Any]:
        """Valida TODOS os sistemas registrados."""
        resultados: Dict[str, Any] = {}
        for sid in self.sistemas:
            resultados[sid] = self.validar_sistema(sid)

        conforme = sum(
            1 for r in resultados.values()
            if isinstance(r, dict) and r.get("totalmente_conforme")
        )
        total = len(resultados)
        banidos = sum(
            1 for r in resultados.values()
            if isinstance(r, dict) and "BANIDO" in r.get("status", "").upper()
        )
        suspensos = sum(
            1 for r in resultados.values()
            if isinstance(r, dict) and "SUSPENSO" in r.get("status", "").upper()
        )
        pct = (conforme / total * 100) if total else 0.0
        return {
            "total_sistemas": total,
            "totalmente_conformes": conforme,
            "suspensos": suspensos,
            "banidos": banidos,
            "precisam_revisao": total - conforme,
            "taxa_conformidade": f"{conforme}/{total} ({pct:.0f}%)",
            "resultados": resultados,
        }

    # -- consultas ----------------------------------------------------------

    def listar_principios(self) -> List[Dict[str, Any]]:
        """Lista todos os principios com texto completo (do json)."""
        return [
            {
                "id": pid,
                "numero": int(pid[1:]),
                "nome": pdata["nome"],
                "categoria": pdata.get("categoria", "operacional"),
                "modulo": pdata.get("modulo", ""),
                "texto": pdata["texto"],
            }
            for pid, pdata in self.data["principios"].items()
        ]

    def scorecard(self) -> Dict[str, Any]:
        return {
            "sistemas_registrados": len(self.sistemas),
            "checks_executados": self.checks_executados,
            "violacoes_total": len(self.violacoes),
            "violacoes_criticas": sum(
                1 for v in self.violacoes if v.severidade == "critica"
            ),
            "principios": len(self.data["principios"]),
            "pass_threshold": self.pass_threshold,
        }


# ============================================================================
# 4. DEMO
# ============================================================================

def _demo() -> None:
    eng = ConstitutionalEngine()

    print("=" * 70)
    print("OpenConstitutionalEngine -- Logica + Dados Separados")
    print("=" * 70)

    # --- Os principios (do json) ---
    print(f"\n[OS {len(eng.data['principios'])} PRINCIPIOS (de data.json)]")
    for p in eng.listar_principios():
        cat = f"[{p['categoria'].upper()}]"
        print(f"\n  {cat} {p['id']} -- {p['nome'].replace('_', ' ').title()}")
        print(f"  Modulo: {p['modulo']}")
        texto = p["texto"]
        while len(texto) > 65:
            idx = texto.rfind(" ", 0, 65)
            if idx == -1:
                idx = 65
            print(f"  {texto[:idx]}")
            texto = texto[idx:].lstrip()
        print(f"  {texto}")

    # --- Registrar sistemas de teste ---
    print("\n\n[REGISTRANDO SISTEMAS DE TESTE]")

    eng.registrar_sistema(MetadadosSistema(
        sistema_id="iara", nome="OpenIara", dominio="CORE",
        caminho="core/voz/open_iara.py", criado_por="comunidade",
        aprovado_por_votacao=True, votos=12, tem_sucessor=True,
        docs_publicos=True, logs_publicos=True, seguranca_acessivel=True,
        usa_ia=True, humano_no_loop=True,
    ))

    eng.registrar_sistema(MetadadosSistema(
        sistema_id="banco_opaco", nome="Banco Opaco (hipotetico)",
        dominio="ECONOMIA", caminho="n/a",
        criado_por="fundador", aprovado_por_votacao=False,
        decisoes_opacas=True, caixa_preta=True,
    ))

    eng.registrar_sistema(MetadadosSistema(
        sistema_id="esterilizacao", nome="Esterilizacao Forcada (hipotetico)",
        dominio="SAUDE", caminho="n/a", afeta_corpos=True,
        exige_consentimento_corporal=False,
    ))

    eng.registrar_sistema(MetadadosSistema(
        sistema_id="drone_vigia", nome="Drone de Vigilancia (hipotetico)",
        dominio="SEGURANCA", caminho="n/a",
        e_drone=True, drone_vigia=True,
    ))

    eng.registrar_sistema(MetadadosSistema(
        sistema_id="rede_furia", nome="Rede Social da Furia (hipotetico)",
        dominio="MIDIA", caminho="n/a",
        usa_ia=True, engagement_por_furia=True, humano_no_loop=False,
        polariza_identidade=True,
    ))

    eng.registrar_sistema(MetadadosSistema(
        sistema_id="gov_br_exclusivo", nome="gov.br 100% Digital (hipotetico)",
        dominio="GOVERNO", caminho="n/a",
        e_servico_digital=True, exige_smartphone=True, exige_internet=True,
        exige_leitura=True, tem_canal_analogico=False,
        ensina_dentro=False, tem_assistente_humana=False,
        pct_exclusao_digital=70.0,
    ))

    eng.registrar_sistema(MetadadosSistema(
        sistema_id="sus_inclusivo", nome="SUS Inclusivo (Republica ideal)",
        dominio="SAUDE", caminho="n/a", criado_por="comunidade",
        aprovado_por_votacao=True, tem_sucessor=True, docs_publicos=True,
        e_servico_digital=True, exige_internet=False, exige_leitura=False,
        tem_canal_analogico=True, ensina_dentro=True,
        tem_assistente_humana=True, pct_exclusao_digital=0.0,
    ))

    # --- Validar todos ---
    print("\n[VALIDACAO CONSTITUCIONAL]")
    resultado = eng.validar_todos()
    print(f"\n  Taxa de conformidade: {resultado['taxa_conformidade']}")
    print(f"  Conformes: {resultado['totalmente_conformes']}")
    print(f"  Suspensos: {resultado['suspensos']}")
    print(f"  Banidos: {resultado['banidos']}")
    print(f"  Precisam revisao: {resultado['precisam_revisao']}")

    print("\n[DETALHES POR SISTEMA]")
    for sid, res in resultado["resultados"].items():
        if not isinstance(res, dict):
            continue
        nome = res.get("sistema_nome", sid)
        status = res.get("status", "?")
        score = res.get("score_geral", 0)
        print(f"\n  {nome}")
        print(f"    Status: {status} | Score: {score}/100")
        for check in res.get("checks", []):
            icon = "[OK]  " if check["passou"] else "[FAIL]"
            print(f"    {icon} {check['principio']:<35} {check['score']}/100")
            if not check["passou"]:
                print(f"           {check['notas']}")

    # --- Scorecard ---
    print("\n\n[SCORECARD DO MOTOR]")
    sc = eng.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    print(f"\n  Arquitetura: data.json ({len(eng.data['principios'])} principios) "
          f"+ disernmentos/ + logica em .py")


if __name__ == "__main__":
    _demo()
