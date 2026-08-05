#!/usr/bin/env python3
"""
OpenMapaMinisterios -- 13 Secretarias vs 37 Ministérios Reais
================================================================
"O governo real tem 37 ministérios. O PCU-B cobre 13.
 O que falta é burocracia que não resolve Raio X -- ou é cargo sem gente."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional


class StatusVaga(Enum):
    PREENCHIDO = "PREENCHIDO"           # tem gente com habilidade
    COBERTO = "COBERTO"                 # outra secretaria absorve
    VAZIO_CRITICO = "VAZIO_CRITICO"     # falta gente e e importante
    VAZIO_LIXO = "VAZIO_LIXO"           # cargo de burocracia (cargos...
                                          # ...fidalgos)
    FUSAO = "FUSAO"                     # foi fundido com outro


@dataclass
class Ministerio:
    """
    Um ministério real do governo federal brasileiro.

    AVISO: TODOS os nomes sao MOCK (placeholder).
    A composicao final so e definida apos analise individual.
    O sistema de medicao e REAL. As pessoas sao HIPOTETICAS.
    """
    nome: str
    area_raiox: str                     # qual eixo do Raio X atende
    status: StatusVaga
    ocupado_por: str                    # quem (nome) ou "VAZIO"
    secretaria_equivalente: str         # qual secretaria do PCU-B cobre
    resolve_raiox: bool                 # resolve algo do Raio X?
    observacao: str


def _init_ministerios() -> List[Ministerio]:
    return [
        # === PREENCHIDOS DIRETAMENTE ===
        Ministerio("Casa Civil", "gestao", StatusVaga.PREENCHIDO,
            "Camilo Santana", "Coordenação Executiva",
            True, "Centro do governo. Camilo coordena."),

        Ministerio("Saúde", "saude", StatusVaga.PREENCHIDO,
            "Jandira Feghali", "Saúde",
            True, "SUS. Emergência."),

        Ministerio("Educação", "educacao", StatusVaga.PREENCHIDO,
            "Orlando Silva", "Educação e Esporte",
            True, "PISA 377. Escola integral."),

        Ministerio("Meio Ambiente", "ambiente", StatusVaga.PREENCHIDO,
            "Marina Silva", "Ambiente e Soberania",
            True, "PPCDAm. Amazônia. -80%."),

        Ministerio("Justiça e Segurança Pública", "violencia", StatusVaga.PREENCHIDO,
            "Flavio Dino", "Justiça e Segurança",
            True, "47.500 homicídios. Desmilitarização."),

        Ministerio("Trabalho e Emprego", "emprego", StatusVaga.PREENCHIDO,
            "Paulo Paim", "Trabalho e Previdência",
            True, "Jornada 6h. Renda mínima."),

        Ministerio("Cidades", "habitacao", StatusVaga.PREENCHIDO,
            "Patrus Ananias", "Cidades e Habitação",
            True, "8M sem moradia. Imóveis vazios."),

        Ministerio("Cultura", "cultura", StatusVaga.PREENCHIDO,
            "Luiza Erundina", "Cultura",
            True, "Cotização 40%. Cordel/capoeira."),

        Ministerio("Direitos Humanos e Cidadania", "indigena", StatusVaga.PREENCHIDO,
            "Sonia Guajajara", "Direitos e Diversidade",
            True, "251 terras. LGBTQIA+."),

        Ministerio("Mulheres", "violencia", StatusVaga.PREENCHIDO,
            "Erika Hilton", "Direitos Humanos (sub)",
            True, "Feminicídio 1.8/dia."),

        # === COBERTOS POR FUSÃO ===
        Ministerio("Fazenda", "economia", StatusVaga.PREENCHIDO,
            "Fernando Haddad", "Coordenação Executiva",
            True, "ISF. Nacionalização. Auditoria dívida."),

        Ministerio("Comunicação Social", "comunicacao", StatusVaga.PREENCHIDO,
            "Jones Manoel", "Comunicação",
            True, "Democratização. Internet rural."),

        Ministerio("Desenvolvimento Agrário", "agropecuaria", StatusVaga.FUSAO,
            "Marina Silva (fam.) + Samara (reforma)",
            "Ambiente e Soberania + Programa",
            True, "Fundido: reforma agrária + agricultura familiar."),

        Ministerio("Agricultura", "soberania_alimentar", StatusVaga.FUSAO,
            "Samara Martins",
            "Ambiente e Soberania",
            True, "Fundido com ambiente. Trigo + fertilizantes."),

        Ministerio("Minas e Energia", "energia", StatusVaga.PREENCHIDO,
            "Ciro Gomes", "Infraestrutura e Energia",
            True, "Reestatização Petrobras. Tarifa social."),

        Ministerio("Transportes", "transporte", StatusVaga.PREENCHIDO,
            "Ciro Gomes", "Infraestrutura e Energia",
            True, "Tarifa zero. Ferrovias. Frota elétrica."),

        Ministerio("Desenvolvimento, Indústria e Comércio", "economia", StatusVaga.FUSAO,
            "Fernando Haddad",
            "Coordenação Executiva",
            True, "Fundido com Fazenda. Planificação."),

        # === VAZIOS CRÍTICOS (falta gente E importa) ===
        Ministerio("Relações Exteriores (Itamaraty)", "soberania_alimentar", StatusVaga.PREENCHIDO,
            "Celso Amorim", "—",
            True, "Diplomata. 2x ministro Itamaraty. Comércio Sul-Sul. Soberania."),

        Ministerio("Defesa", "violencia", StatusVaga.PREENCHIDO,
            "Aldo Rebelo", "—",
            True, "Foi ministro Defesa. Nacionalista. Soberania Amazônia. Fronteiras."),

        Ministerio("Ciência e Tecnologia", "educacao", StatusVaga.PREENCHIDO,
            "Ricardo Galvão", "—",
            True, "Físico. Ex-INPE. Defendeu dados do desmatamento. EMBRAPA. Fertilizantes."),

        Ministerio("Desenvolvimento Regional", "agua", StatusVaga.PREENCHIDO,
            "Humberto Costa", "—",
            True, "Senador NE. Gestão regional. Saneamento. Transposição."),

        Ministerio("Integração Nacional", "agua", StatusVaga.FUSAO,
            "Humberto Costa", "Desenvolvimento Regional",
            True, "Fundido com Desenvolvimento Regional. Transposição São Francisco."),

        Ministerio("Esporte", "violencia", StatusVaga.PREENCHIDO,
            "Ana Moser", "—",
            True, "Ex-vôlei. Educação popular pelo esporte. Prevenção juvenil."),

        Ministerio("Previdência Social", "emprego", StatusVaga.FUSAO,
            "Paulo Paim", "Trabalho e Previdência",
            True, "Fundido com Trabalho. 22M idosos. Senador 5x. 30 anos direitos."),

        Ministerio("Igualdade Racial", "violencia", StatusVaga.PREENCHIDO,
            "Silvio Almeida", "—",
            True, "Filósofo. Autor 'Racismo Estrutural'. Negro ganha 56%."),

        Ministerio("Povos Originários", "indigena", StatusVaga.FUSAO,
            "Sonia Guajajara", "Direitos e Diversidade",
            True, "Fundido com Direitos Humanos."),

        Ministerio("Pequenas, Micro e Médias Empresas", "emprego", StatusVaga.PREENCHIDO,
            "Eduardo Mancuso", "—",
            False, "Economia solidária. Cooperativismo. Importante mas não resolve Raio X."),

        Ministerio("Controladoria-Geral da União", "corrupcao", StatusVaga.PREENCHIDO,
            "Bruno Dantas", "—",
            True, "TCU. Auditoria. Combate corrupção. R$ 200bi/ano. Recuperar >2.5%."),

        Ministerio("Turismo", "—", StatusVaga.VAZIO_LIXO,
            "VAZIO", "—",
            False, "Não resolve Raio X. Cargo fidalgo."),

        Ministerio("Pesca", "soberania_alimentar", StatusVaga.VAZIO_LIXO,
            "VAZIO", "—",
            False, "Pode ser subsecretaria de Ambiente."),

        Ministerio("Portos e Aeroportos", "transporte", StatusVaga.VAZIO_LIXO,
            "VAZIO", "—",
            False, "Subsecretaria de Infraestrutura."),

        Ministerio("Secretaria de Governo", "gestao", StatusVaga.VAZIO_LIXO,
            "VAZIO", "—",
            False, "Burocracia de articulação. Casa Civil cobre."),

        Ministerio("Advocacia-Geral da União", "corrupcao", StatusVaga.PREENCHIDO,
            "João Paulo Lopes", "—",
            True, "Jurista. Direito constitucional popular. Lei do Confisco."),

        Ministerio("Gabinete de Segurança Institucional", "violencia", StatusVaga.VAZIO_LIXO,
            "VAZIO", "—",
            False, "Burocracia. Justiça e Segurança cobre."),

        Ministerio("Secretaria-Geral da Presidência", "gestao", StatusVaga.VAZIO_LIXO,
            "VAZIO", "—",
            False, "Casa Civil cobre."),

        Ministerio("Relações Institucionais", "gestao", StatusVaga.VAZIO_LIXO,
            "VAZIO", "—",
            False, "Articulação com Congresso. Pode ser subsecretaria."),

        Ministerio("Comunicações (telecom)", "comunicacao", StatusVaga.FUSAO,
            "Jones Manoel",
            "Comunicação",
            True, "Fundido com Comunicação Social. Anatel."),
    ]


# Typo guard: fix VUSAO -> FUSAO
for _m in _init_ministerios():
    if _m.status.value == "VUSAO":
        _m.status = StatusVaga.FUSAO


def _demo():
    ministros = _init_ministerios()

    print("=" * 95)
    print("MAPA: 13 SECRETARIAS PCU-B vs 37 MINISTÉRIOS REAIS")
    print("=" * 95)

    # Count
    preenchidos = [m for m in ministros if m.status == StatusVaga.PREENCHIDO]
    fusao = [m for m in ministros if m.status == StatusVaga.FUSAO]
    vazios_criticos = [m for m in ministros if m.status == StatusVaga.VAZIO_CRITICO]
    vazios_lixo = [m for m in ministros if m.status == StatusVaga.VAZIO_LIXO]

    print(f"""
  TOTAL: {len(ministros)} ministérios

  PREENCHIDOS:     {len(preenchidos)}  (tem gente com habilidade)
  FUNDIDOS:        {len(fusao)}  (outra secretaria absorve)
  VAZIOS CRÍTICOS: {len(vazios_criticos)}  (falta gente E resolve Raio X)
  VAZIOS LIXO:     {len(vazios_lixo)}  (burocracia. Não resolve Raio X.)
""")

    print(f"{'='*95}")
    print(f"PREENCHIDOS ({len(preenchidos)})")
    print(f"{'='*95}")
    for m in preenchidos:
        print(f"\n  [{m.nome}]")
        print(f"    OCUPADO POR: {m.ocupado_por}")
        print(f"    SECRETARIA: {m.secretaria_equivalente}")
        print(f"    RIO X: {m.area_raiox}")
        print(f"    OBS: {m.observacao}")

    print(f"\n{'='*95}")
    print(f"FUNDIDOS ({len(fusao)})")
    print(f"{'='*95}")
    for m in fusao:
        print(f"\n  [{m.nome}]")
        print(f"    ABSORVIDO POR: {m.ocupado_por}")
        print(f"    SECRETARIA: {m.secretaria_equivalente}")
        print(f"    RIO X: {m.area_raiox}")

    print(f"\n{'='*95}")
    print(f"VAZIOS CRÍTICOS ({len(vazios_criticos)}) -- PRECISA DE GENTE")
    print(f"{'='*95}")
    for m in vazios_criticos:
        print(f"\n  [{m.nome}]")
        print(f"    RIO X: {m.area_raiox}")
        print(f"    RESOLVE RIO X: {'SIM' if m.resolve_raiox else 'NÃO'}")
        print(f"    OBS: {m.observacao}")

    print(f"\n{'='*95}")
    print(f"VAZIOS LIXO ({len(vazios_lixo)}) -- BIRÔCRATA, NÃO RESOLVE")
    print(f"{'='*95}")
    for m in vazios_lixo:
        print(f"\n  [{m.nome}]")
        print(f"    RIO X: {m.area_raiox if m.area_raiox != '—' else 'NENHUM'}")
        print(f"    OBS: {m.observacao}")

    print(f"\n{'='*95}")
    print("VEREDITO")
    print(f"{'='*95}")
    print(f"""
  37 ministérios reais mapeados.

  PREENCHIDOS:     {len(preenchidos)}  -- gente com habilidade no cargo
  FUNDIDOS:        {len(fusao)}  -- absorvidos por secretaria maior
  VAZIOS CRÍTICOS: {len(vazios_criticos)}  -- PRECISA de gente URGENTE
  VAZIOS LIXO:     {len(vazios_lixo)}  -- cargo fidalgo. Extingue ou vira subsecretaria.

  COBERTURA REAL: {len(preenchidos) + len(fusao)} de {len(ministros)} ({(len(preenchidos) + len(fusao)) / len(ministros) * 100:.0f}%)

  OS {len(vazios_criticos)} BURACOS QUE IMPORTAM:

  1. ITAMARATY (Relações Exteriores)
     Sem diplomata no time. Comércio Sul-Sul, fim de remessas, soberania.
     Quem faz? Ninguém ainda.

  2. DEFESA
     Sem militar/diplomata. Soberania da Amazônia. Fronteiras.
     Quem faz? Ninguém ainda.

  3. CIÊNCIA E TECNOLOGIA
     Sem cientista. EMBRAPA, fertilizantes, transição energética.
     Quem faz? Ninguém ainda.

  4. DESENVOLVIMENTO REGIONAL + INTEGRAÇÃO NACIONAL
     Sem gente. Transposição São Francisco. Semi-árido.
     Ciro toca parte mas não é nordestino de gestão regional.

  5. ESPORTE
     Sem gente. Prevenção juvenil = reduz homicídio.
     Orlando toca parte mas não é especialista.

  6. PREVIDÊNCIA
     Paim cobre mas e só 1 pessoa pra 22M idosos.

  7. IGUALDADE RACIAL
     Sem gente específica. Negro ganha 56%. Precisa de secretaria própria.

  8. CONTROLADORIA + AGU
     Sem gente. R$ 200bi/ano em corrupção. Recuperado: 2.5%.
     E o buraco mais caro do Brasil.

  {len(vazios_lixo)} cargos são lixo burocrático. Extingue.
  {len(vazios_criticos)} cargos são buracos que sangram.
  Encha os {len(vazios_criticos)} antes de pensar nos {len(vazios_lixo)}.
""")


if __name__ == "__main__":
    _demo()
