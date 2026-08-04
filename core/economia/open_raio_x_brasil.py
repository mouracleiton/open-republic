#!/usr/bin/env python3
"""
OpenRaioXBrasil -- Diagnostico Nacional da Republica
======================================================
"O Brasil precisa de um checkup. Raio X, sangue, urina.
 Nao sabemos como o paciente esta porque o medico pergunta
 pro doente como ele se sente e anota a resposta."

PRIORIDADE #1 DA REPUBLICA.

O Censo da Republica e o diagnostico. Sem diagnostico,
qualquer tratamento e chuto. Qualquer politica e palpite.

METODOLOGIA:
  Automatizar o maximo (OSINT, sensor, satelite).
  Preencher gaps com forca tarefa (cidadao no campo).
  Cruzar tudo. Classificar (FATO/DADO/OPINIAO).
  Publicar diagnostico continuo.

A METAFORA MEDICA:

  DOMINIO                    EXAME MEDICO EQUIVALENTE
  Populacao                  Biometria (quem e o paciente)
  Saude                      Exame de sangue + checkup
  Agua                       Exame de urina (o que sai do corpo)
  Alimentacao                Exame nutricional
  Educacao                   Ressonancia mental (como pensa)
  Violencia                  Raio X (fratura exposta)
  Emprego                    Eletrocardiograma (coracao bomba)
  Inflacao                   Pressao arterial
  Energia                    Bateria (tem forca?)
  Habitacao                  Raio X osseo (estrutura)
  Ambiente                   Biopsia (tecido vivo?)
  Transporte                 Teste de esforco (mobilidade)

AUTOMACAO vs FORCA TAREFA:
  ~60% automatizavel (OSINT, satelite, sensor, API)
  ~30% forca tarefa (cidadao vai la)
  ~10% especializado (medicao fisica, pericia)

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field


# ============================================================================
# 1. ENUMS
# ============================================================================

class TipoExame(Enum):
    """Tipo de exame na bateria diagnostica."""
    RAIO_X = ("raio_x", "Raio X: ver atraves (OSINT satelite)")
    SANGUE = ("sangue", "Exame de Sangue: amostra profunda (sensor + medicao)")
    URINA = ("urina", "Exame de Urina: o que o sistema excreta (agua, esgoto)")
    BIOMETRIA = ("biometria", "Biometria: quem e o paciente (populacao, ID)")
    RESSONANCIA = ("ressonancia", "Ressonancia: como pensa (educacao, letramento)")
    ELETRO = ("eletro", "Eletrocardiograma: coracao (economia, emprego)")
    PRESSAO = ("pressao", "Pressao Arterial: inflacao, custo de vida")
    BIOPSIA = ("biopsia", "Biopsia: tecido vivo (ambiente, biodiversidade)")
    TESTE_ESFORCO = ("esforco", "Teste de Esforco: mobilidade (transporte)")
    CHECKUP = ("checkup", "Checkup Geral: habitacao, infraestrutura")
    TOXICOLOGICO = ("toxico", "Toxicologico: violencia, drogas, crime")
    GENETICO = ("genetico", "Genetico: raca, origem, migracao (sem juizo)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelAutomacao(Enum):
    """Quanto pode ser automatizado."""
    TOTAL = ("total", "100% automatizavel: OSINT/satelite/API", 100)
    ALTO = ("alto", "~75% automatizavel: OSINT + pouco humano", 75)
    MEDIO = ("medio", "~50%: metade automato, metade campo", 50)
    BAIXO = ("baixo", "~25%: pouco automato, muito campo", 25)
    MANUAL = ("manual", "0%: so cidadao no campo", 0)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def pct(self) -> int:
        return self.value[2]


class UrgenciaDiagnostica(Enum):
    """Urgencia de cada exame (o que fazer PRIMEIRO)."""
    U1_EMERGENCIA = ("u1", "Emergencia: vidas em risco AGORA")
    U2_URGENTE = ("u2", "Urgente: deteriorando rapido")
    U3_ALTA = ("u3", "Alta: precisa saber quanto antes")
    U4_ROTINA = ("u4", "Rotina: verificar periodicamente")
    U5_BASELINE = ("u5", "Baseline: referencia pra comparar")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass
class ExameNacional:
    """Um exame na bateria diagnostica do Brasil."""
    dominio: str              # chave do dominio do censo
    exame: TipoExame          # tipo de exame medico equivalente
    urgencia: UrgenciaDiagnostica
    automacao: NivelAutomacao
    indicadores: List[str]    # o que medir
    fonte_automatica: List[str]   # OSINT, satelite, API, sensor
    fonte_humana: List[str]       # cidadao, comunidade, perito
    tempo_estimado: str          # "tempo real", "semanal", "anual"
    custo_estimado: str          # estimativa de custo
    gap_principal: str           # o que NAO sabemos hoje


# ============================================================================
# 3. BATERIA DE EXAMES (o checkup completo)
# ============================================================================

def _init_exames() -> List[ExameNacional]:
    return [
        # ====================================================================
        # EMERGENCIA
        # ====================================================================
        ExameNacional(
            "violencia", TipoExame.TOXICOLOGICO,
            UrgenciaDiagnostica.U1_EMERGENCIA,
            NivelAutomacao.MEDIO,
            ["homicidios (tempo real)", "tiroteio (localizacao)",
             "violencia domestica (denuncia)", "violencia policial",
             "faccao/territorio", "desaparecidos"],
            ["denuncia app (anonima)", "OSINT: noticias locais",
             "sensor: deteccao acustica de tiro"],
            ["denuncia cidadao", "comunidade assina", "depoimento"],
            "tempo real",
            "R$ 5M/ano (infra + app)",
            "Nao sabemos onde tiroteio acontece em tempo real. SINESP tem 6-12h de atraso.",
        ),
        ExameNacional(
            "saude", TipoExame.SANGUE,
            UrgenciaDiagnostica.U1_EMERGENCIA,
            NivelAutomacao.MEDIO,
            ["mortalidade infantil (tempo real)", "mortalidade materna",
             "fila SUS", "medicamento disponivel", "postos funcionando",
             "doencas endemicas (dengue, malaria)", "saude mental",
             "desnutricao infantil"],
            ["API DATASUS (mortalidade)", "sensor: fluxo de posto",
             "OSINT: relatos sociais"],
            ["cidadao visita posto", "comunidade relata",
             "medicao: peso/altura crianca"],
            "semanal",
            "R$ 10M/ano",
            "Mortalidade infantil real e subnotificada. FILA nao existe como metrica.",
        ),
        ExameNacional(
            "alimentacao", TipoExame.CHECKUP,
            UrgenciaDiagnostica.U1_EMERGENCIA,
            NivelAutomacao.BAIXO,
            ["fome real (0 refeicoes/dia)", "inseguranca alimentar",
             "merenda escolar (verificar entrega)", "cesta basica por bairro"],
            ["API mercado (preco)", "sensor: peso em escola"],
            ["cidadao relata fome", "comunidade assina",
             "verificacao merenda (censo escolar)"],
            "mensal",
            "R$ 3M/ano",
            "33 milhoes passam fome. IBGE mede bienal. Fome muda em dias.",
        ),

        # ====================================================================
        # URGENTE
        # ====================================================================
        ExameNacional(
            "agua", TipoExame.URINA,
            UrgenciaDiagnostica.U2_URGENTE,
            NivelAutomacao.MEDIO,
            ["quem tem agua potavel (medido)", "quantos dias/semana chega",
             "cloro residual (medido)", "esgoto: rede/fossa/nada",
             "qualidade do rio (PH, turbidez, coliformes)"],
            ["sensor IoT: PH/cloro na torneira", "satelite: rio (cor/turbidez)",
             "OSINT: SNIS (cruzamento)"],
            ["cidadao mede agua", "amostra de rio", "comunidade relata"],
            "semanal",
            "R$ 8M/ano (sensores + campo)",
            "35 milhoes sem agua tratada. SNIS e auto-relato da empresa.",
        ),
        ExameNacional(
            "ambiente", TipoExame.BIOPSIA,
            UrgenciaDiagnostica.U2_URGENTE,
            NivelAutomacao.TOTAL,
            ["queimada (foco, area)", "desmatamento",
             "qualidade do ar (PM2.5)", "rio (PH, turbidez, mercurio)",
             "lixo (destino real)"],
            ["Sentinel-2 (queimada)", "MapBiomas (desmatamento)",
             "INPE (foco)", "sensor PM2.5", "satelite: lixao"],
            ["cidadao fotografa lixo no rio", "denuncia garimpo"],
            "semanal",
            "R$ 2M/ano (maioria OSINT gratis)",
            "Sabe onde queima. Nao sabe quem queima. Falta cruzar com CAR.",
        ),
        ExameNacional(
            "educacao", TipoExame.RESSONANCIA,
            UrgenciaDiagnostica.U2_URGENTE,
            NivelAutomacao.ALTO,
            ["ver open_censo_escolar.py",
             "analfabetismo funcional real", "evasao",
             "professor presente (verificado)", "escola com agua/luz/internet"],
            ["OSINT: street view escola", "Sentinel-2",
             "API INEP (cruzamento)", "satelite: predio existe?"],
            ["cidadao vai escola (16 passos)", "comunidade assina"],
            "semestral",
            "R$ 15M/ano",
            "INEP diz 6 salas. Realidade: 3. Ninguem foi verificar.",
        ),
        ExameNacional(
            "indigena", TipoExame.BIOMETRIA,
            UrgenciaDiagnostica.U2_URGENTE,
            NivelAutomacao.ALTO,
            ["populacao por etnia", "terra demarcada vs invadida",
             "malario/desnutricao", "garimpo ilegal (mercurio)",
             "madeireira ilegal", "escola/saude indigena"],
            ["Sentinel-2 (garimpo/desmatamento)", "MapBiomas",
             "satelite: invasao de terra"],
            ["lider indigena coleta (app offline)", "denuncia garimpo"],
            "semestral",
            "R$ 4M/ano",
            "100.000+ indigenas invisiveis. Garimpo cresce sem ninguem ver.",
        ),

        # ====================================================================
        # ALTA
        # ====================================================================
        ExameNacional(
            "emprego", TipoExame.ELETRO,
            UrgenciaDiagnostica.U3_ALTA,
            NivelAutomacao.MEDIO,
            ["ocupacao formal vs informal", "salario real (nao carteira)",
             "trabalho infantil", "trabalho escravo",
             "app-worker (Uber/iFood)", "desemprego real"],
            ["API CAGED (formal)", "OSINT: vagas online"],
            ["comunidade: quem trabalha quanto ganha",
             "denuncia trabalho escravo"],
            "mensal",
            "R$ 3M/ano",
            "Informal e 40% da forca de trabalho. PNAD estima por amostra.",
        ),
        ExameNacional(
            "inflacao", TipoExame.PRESSAO,
            UrgenciaDiagnostica.U3_ALTA,
            NivelAutomacao.ALTO,
            ["preco arroz/feijao/oleo/leite por bairro",
             "gas/onibus/luz/remedio",
             "cesta basica por cidade", "IPCA periferia"],
            ["API mercado (preco)", "web scraping: supermercado online",
             "sensor: display de preco fotografado"],
            ["cidadao fotografa precinho", "feira: preco de produtor"],
            "diario",
            "R$ 2M/ano",
            "IPCA mede 16 capitais. Periferia e interior: invisivel.",
        ),
        ExameNacional(
            "energia", TipoExame.CHECKUP,
            UrgenciaDiagnostica.U3_ALTA,
            NivelAutomacao.ALTO,
            ["quem tem luz", "quantas horas/dia", "qualidade (pisca?)",
             "preco da conta", "quem tem geladeira",
             "energia solar comunitaria", "gato (roubo energia)"],
            ["sensor IoT: voltagem/frequencia/queda",
             "satelite noturno: luz (VIIRS)"],
            ["cidadao relata", "comunidade assina"],
            "trimestral",
            "R$ 4M/ano",
            "1.8M sem energia eletrica. Qualidade nunca medida.",
        ),

        # ====================================================================
        # ROTINA
        # ====================================================================
        ExameNacional(
            "habitacao", TipoExame.RAIO_X,
            UrgenciaDiagnostica.U4_ROTINA,
            NivelAutomacao.MEDIO,
            ["tipo de construcao", "material", "favela vs formal",
             "sem-teto (contagem real)", "despejo"],
            ["satelite: favela cresce?", "Street View: material",
             "OSINT: mapa de area"],
            ["cidadao conta sem-teto", "comunidade relata despejo"],
            "trimestral",
            "R$ 3M/ano",
            "Sem-teto nao existe no IBGE. Favela cresce sem medicao.",
        ),
        ExameNacional(
            "transporte", TipoExame.TESTE_ESFORCO,
            UrgenciaDiagnostica.U4_ROTINA,
            NivelAutomacao.ALTO,
            ["tempo casa->trabalho", "frequencia onibus", "lotacao",
             "bicicleta como transporte", "estrada: asfalto/terra/rio"],
            ["GPS cidadao (tempo real)", "satelite: estrada",
             "sensor: lotacao onibus"],
            ["cidadao relata", "comunidade: estrada cortada?"],
            "trimestral",
            "R$ 2M/ano",
            "Tempo de deslocamento periferia->centro nunca medido.",
        ),
        ExameNacional(
            "agro", TipoExame.BIOPSIA,
            UrgenciaDiagnostica.U4_ROTINA,
            NivelAutomacao.TOTAL,
            ["area plantada", "producao", "familiar vs agronegocio",
             "agrotoxico no rio", "trabalho escravo rural"],
            ["Sentinel-2 (area plantada)", "MapBiomas (uso solo)",
             "sensor: agrotoxico no rio"],
            ["denuncia trabalho escravo", "cidadao: quem planta?"],
            "semestral",
            "R$ 2M/ano",
            "Censo agro e decadal. Agronegocio muda em meses.",
        ),
        ExameNacional(
            "quilombola", TipoExame.BIOMETRIA,
            UrgenciaDiagnostica.U4_ROTINA,
            NivelAutomacao.ALTO,
            ["populacao", "territorio certificado vs ameacado",
             "saude/escola/agua/luz", "ameaca (grileiro)"],
            ["OSINT: satelite territorio", "MapBiomas"],
            ["lider quilombola coleta", "denuncia grilo"],
            "semestral",
            "R$ 2M/ano",
            "200.000+ invisiveis. Titulacao parada ha anos.",
        ),
        ExameNacional(
            "ribeirinha", TipoExame.BIOMETRIA,
            UrgenciaDiagnostica.U4_ROTINA,
            NivelAutomacao.BAIXO,
            ["populacao por comunidade", "acesso (barco, dias ate cidade)",
             "saude (malario?)", "energia (solar?)", "agua (rio? potavel?)"],
            ["satelite: comunidade existe?", "Sentinel-2: inundacao"],
            ["lider ribeirinho coleta (app offline)",
             "sincroniza quando chega rede"],
            "semestral",
            "R$ 5M/ano (logistica)",
            "500.000+ invisiveis. IBGE nao chega. So de barco.",
        ),

        # ====================================================================
        # BASELINE
        # ====================================================================
        ExameNacional(
            "populacao", TipoExame.BIOMETRIA,
            UrgenciaDiagnostica.U5_BASELINE,
            NivelAutomacao.MEDIO,
            ["contagem populacional", "faixa etaria", "genero",
             "raca/cor", "migracao"],
            ["satelite: construcao/densidade", "OSINT: IBGE legado"],
            ["cidadao: contagem comunitaria", "registro civil"],
            "anual",
            "R$ 5M/ano",
            "Censo demografico 4 anos atrasado. 4.5M invisiveis.",
        ),
        ExameNacional(
            "registro", TipoExame.GENETICO,
            UrgenciaDiagnostica.U5_BASELINE,
            NivelAutomacao.MEDIO,
            ["nascimento (certidao digital)", "obito (causa real)",
             "casamento", "SEM cartorio (indigena/ribeirinho)"],
            ["API registro civil", "API DATASUS"],
            ["cidadao: registro comunitario", "app: certidao digital"],
            "tempo real",
            "R$ 3M/ano",
            "Indigena sem certidao. Obito sem causa. Ribeirinho sem cartorio.",
        ),
        ExameNacional(
            "geografia", TipoExame.RAIO_X,
            UrgenciaDiagnostica.U5_BASELINE,
            NivelAutomacao.TOTAL,
            ["mapa atualizado", "rua aberta vs fechada",
             "ponte existe vs caida", "limite municipal"],
            ["OpenStreetMap + satelite", "Sentinel-2",
             "Street View: rua existe?"],
            ["cidadao edita OSM", "comunidade: nova rua"],
            "anual",
            "R$ 1M/ano",
            "Mapa IBGE desatualizado. Rua nova nao aparece.",
        ),
    ]


# ============================================================================
# 4. PIPELINE DE AUTOMACAO
# ============================================================================

class PipelineAutomacao:
    """O que roda automaticamente vs o que precisa humano."""

    def exames_automaticos(self, exames: List[ExameNacional]) -> List[ExameNacional]:
        return [e for e in exames if e.automacao.pct >= 75]

    def exames_manuais(self, exames: List[ExameNacional]) -> List[ExameNacional]:
        return [e for e in exames if e.automacao.pct <= 25]

    def exames_hibridos(self, exames: List[ExameNacional]) -> List[ExameNacional]:
        return [e for e in exames if 25 < e.automacao.pct < 75]

    def por_urgencia(self, exames: List[ExameNacional]) -> List[ExameNacional]:
        return sorted(exames, key=lambda e: e.urgencia.id)

    def custo_total(self, exames: List[ExameNacional]) -> int:
        """Extrai custo numerico de cada exame."""
        total = 0
        for e in exames:
            custo_str = e.custo_estimado.replace("R$ ", "").replace("/ano", "").replace(" (maioria OSINT gratis)", "").replace(" (infra + app)", "").replace(" (sensores + campo)", "").replace(" (logistica)", "")
            # pegar numero
            num = ""
            for c in custo_str:
                if c.isdigit():
                    num += c
            if num:
                total += int(num)
        return total


# ============================================================================
# 5. SISTEMA RAIO X
# ============================================================================

class RaioXBrasil:
    """
    Diagnostico Nacional. O checkup do Brasil.

    PRIORIDADE #1. Sem diagnostico, tratamento e chuto.
    """

    NOME = "OpenRaioXBrasil"
    VERSAO = "0.1.0-spec"

    def __init__(self) -> None:
        self.exames: List[ExameNacional] = _init_exames()
        self.pipeline: PipelineAutomacao = PipelineAutomacao()

    # -- bateria completa --------------------------------------------------

    def bateria_completa(self) -> List[Dict[str, Any]]:
        return [
            {
                "dominio": e.dominio,
                "exame": e.exame.id,
                "exame_rotulo": e.exame.rotulo,
                "urgencia": e.urgencia.id,
                "urgencia_rotulo": e.urgencia.rotulo,
                "automacao": e.automacao.id,
                "automacao_pct": e.automacao.pct,
                "indicadores": e.indicadores,
                "fonte_auto": e.fonte_automatica,
                "fonte_humana": e.fonte_humana,
                "frequencia": e.tempo_estimado,
                "custo": e.custo_estimado,
                "gap": e.gap_principal,
            }
            for e in self.exames
        ]

    # -- por urgencia -------------------------------------------------------

    def emergencia(self) -> List[ExameNacional]:
        return [e for e in self.exames if e.urgencia == UrgenciaDiagnostica.U1_EMERGENCIA]

    def urgente(self) -> List[ExameNacional]:
        return [e for e in self.exames if e.urgencia == UrgenciaDiagnostica.U2_URGENTE]

    # -- automacao ----------------------------------------------------------

    def o_que_roda_sozinho(self) -> List[ExameNacional]:
        return self.pipeline.exames_automaticos(self.exames)

    def o_que_precisa_humano(self) -> List[ExameNacional]:
        return self.pipeline.exames_manuais(self.exames)

    def o_que_e_hibrido(self) -> List[ExameNacional]:
        return self.pipeline.exames_hibridos(self.exames)

    # -- custos -------------------------------------------------------------

    def custo_total(self) -> Dict[str, Any]:
        total = self.pipeline.custo_total(self.exames)
        return {
            "total_anual_milhoes": f"R$ {total} milhoes",
            "comparativo_ibge_censo": f"{total / 2300:.0%} do Censo IBGE 2022 (R$ 2.3bi)",
            "comparativo_bolsa_familia": f"{total / 35000:.1f}% do Bolsa Familia (R$ 35bi/ano)",
            "comparativo_gripen": f"{total / 36000:.2f}% dos 36 cacas (R$ 36bi)",
            "custo_por_habitante": f"R$ {total * 1_000_000 / 215_000_000:.2f}/pessoa/ano",
        }

    # -- metricas -----------------------------------------------------------

    def metricas(self) -> Dict[str, Any]:
        return {
            "total_exames": len(self.exames),
            "emergencia": len(self.emergencia()),
            "urgente": len(self.urgente()),
            "automatizaveis_total": len(self.o_que_roda_sozinho()),
            "manuais_puros": len(self.o_que_precisa_humano()),
            "hibridos": len(self.o_que_e_hibrido()),
            "pct_automatizavel_medio": sum(e.automacao.pct for e in self.exames) // len(self.exames),
        }

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        sc = self.metricas()
        sc["sistema"] = self.NOME
        sc["versao"] = self.VERSAO
        return sc


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo() -> None:
    rx = RaioXBrasil()

    print("=" * 70)
    print(f"{rx.NOME} v{rx.VERSAO} -- Checkup do Brasil")
    print("=" * 70)

    # --- Bateria por urgencia ---
    print(f"\n[BATERIA DE EXAMES POR URGENCIA]\n")
    ordenados = sorted(rx.exames, key=lambda e: e.urgencia.id)
    print(f"  {'URG':<5} {'DOMINIO':<14} {'EXAME':<18} {'AUTO':>6} {'FREQ':<12} {'GAP'}")
    print(f"  {'-'*90}")
    for e in ordenados:
        print(f"  {e.urgencia.id:<5} {e.dominio:<14} {e.exame.id:<18} "
              f"{e.automacao.pct:>4}% {e.tempo_estimado:<12} {e.gap_principal[:30]}")

    # --- Emergencia ---
    print(f"\n\n[EMERGENCIA -- vidas em risco AGORA ({len(rx.emergencia())})]\n")
    for e in rx.emergencia():
        print(f"  [{e.exame.id.upper()}] {e.dominio}")
        print(f"  Indicadores: {', '.join(e.indicadores[:4])}")
        print(f"  Automacao: {e.automacao.pct}%")
        print(f"  Gap: {e.gap_principal}")
        print()

    # --- Automacao ---
    print(f"[AUTOMACAO vs HUMANO]\n")
    print(f"  Totalmente automatizavel: {len(rx.o_que_roda_sozinho())}")
    for e in rx.o_que_roda_sozinho():
        print(f"    - {e.dominio} ({e.automacao.pct}%)")
    print(f"\n  Hibrido (auto + campo): {len(rx.o_que_e_hibrido())}")
    for e in rx.o_que_e_hibrido():
        print(f"    - {e.dominio} ({e.automacao.pct}%)")
    print(f"\n  Manual puro (so cidadao): {len(rx.o_que_precisa_humano())}")
    for e in rx.o_que_precisa_humano():
        print(f"    - {e.dominio} ({e.automacao.pct}%)")

    # --- Custo ---
    print(f"\n\n[CUSTO DO CHECKUP ANUAL]\n")
    custo = rx.custo_total()
    for k, v in custo.items():
        print(f"  {k}: {v}")

    # --- Metricas ---
    print(f"\n\n[METRICAS]")
    for k, v in rx.metricas().items():
        print(f"  {k:.<32} {v}")

    # --- Scorecard ---
    print(f"\n\n[SCORECARD]")
    sc = rx.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")


if __name__ == "__main__":
    _demo()
