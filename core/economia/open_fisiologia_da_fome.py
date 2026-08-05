#!/usr/bin/env python3
"""
OpenFisiologiaDaFome -- A Ciência do Que a Fome Faz no Corpo
================================================================
"Não é 'estar com fome'. É o corpo comendo a si mesmo."
"""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List


class FaseFome(Enum):
    DIGESTAO_NORMAL = "0-4h (normal)"
    GLICOSE_BAIXANDO = "4-12h (jejum curto)"
    GLICOGENOLISE = "12-24h (reservas)"
    GLICONEOGENESE = "24-72h (corpo adapta)"
    CETOSE = "3-7 dias (fígado queima gordura)"
    CETOACIDOSE_LEVE = "1-2 semanas (físico se desgasta)"
    CATABOLISMO_MUSCULAR = "2-4 semanas (corpo consome músculo)"
    DESNUTRICAO_GRAVE = "1-3 meses (órgãos comprometidos)"
    MORTE = "3+ meses (falência múltipla)"


@dataclass
class EstagioFome:
    """Um estágio fisiológico da fome."""
    fase: FaseFome
    descricao: str
    o_que_acontece: List[str]       # mecanismos biológicos
    crianca_vulneravel: str         # o que acontece especificamente com criança
    fonte: str


def _init_estagios() -> List[EstagioFome]:
    return [
        EstagioFome(FaseFome.DIGESTAO_NORMAL,
            "Digestão normal. Energia vem da última refeição.",
            [
                "Glicose no sangue: 70-100 mg/dL (normal)",
                "Insulina transporta glicose para células",
                "Leptina (hormônio da saciedade) alta",
                "Ghrelina (hormônio da fome) baixa",
                "Cérebro funciona normalmente. 20% da energia vai pro cérebro.",
            ],
            "Criança: cresce, brinca, aprende. Tudo normal.",
            "Guyton & Hall, Fisiologia Médica, 14ª ed."),

        EstagioFome(FaseFome.GLICOSE_BAIXANDO,
            "Glicose caindo. O corpo sente fome.",
            [
                "Glicose: 60-70 mg/dL (baixa)",
                "Ghrelina aumenta -- estômago ruge",
                "Leptina diminui -- saciedade some",
                "Cortisol sobe -- estresse metabólico",
                "Corpo começa a buscar energia alternativa",
            ],
            "Criança: irritabilidade, choro, dificuldade de concentração.",
            "Guyton & Hall; NEJM 2023."),

        EstagioFome(FaseFome.GLICOGENOLISE,
            "Reservas de glicogênio (fígado + músculos) sendo consumidas.",
            [
                "Glicogênio hepático esgotando (100g no fígado)",
                "Glicogênio muscular esgotando (400g nos músculos)",
                "Glucagon alto -- sinaliza 'queime reservas'",
                "Insulina baixíssima",
                "Fisiológicamente: o corpo entra em modo economia",
            ],
            "Criança: letargia, menos movimento, poupa energia. Não brinca.",
            "Guyton & Hall; Lancer [sic] 2024."),

        EstagioFome(FaseFome.GLICONEOGENESE,
            "Corpo fabrica glicose a partir de aminoácidos (proteínas).",
            [
                "Fígado quebra aminoácidos para produzir glicose",
                "Cortisol e glucagon elevados",
                "Início do catabolismo protéico (quebra de tecido)",
                "pH sanguíneo começa a cair (acidose leve)",
                "Físico sente fraqueza extrema, tontura",
            ],
            "Criança: desenvolvimento estagnado. Altura e peso param de crescer.",
            "Waterlow, Protein-Energy Malnutrition, 2024 ed."),

        EstagioFome(FaseFome.CETOSE,
            "Fígado começa a queimar gordura para produzir corpos cetônicos.",
            [
                "Beta-hidroxibutirato e acetoacetato no sangue",
                "Cérebro passa a usar corpos cetônicos (70% da energia)",
                "Hálito com odor de acetona",
                "Perda de peso acelerada (massa gorda)",
                "Corpo entra em modo de sobrevivência prolongada",
            ],
            "Criança: Emaciação. Gordura subcutânea desaparece. 'Pele e osso'.",
            "Waterlow; Golden 2023 (desnutrição infantil)."),

        EstagioFome(FaseFome.CETOACIDOSE_LEVE,
            "Acumulação de corpos cetônicos. pH sanguíneo cai.",
            [
                "pH sanguíneo: 7.35 -> 7.30 (acidose)",
                "Respiração de Kussmaul (ofegante, compensatória)",
                "Arritmias cardíacas leves",
                "Deficiências de potássio, magnésio, fósforo",
                "Sistema imunológico começa a falhar",
            ],
            "Criança: infecções oportunistas. Pneumonia. Diarreia. Mortalidade sobe.",
            "WHO Technical Report Series 2024; Golden MH."),

        EstagioFome(FaseFome.CATABOLISMO_MUSCULAR,
            "Gordura esgotada. Corpo começa a consumir músculo (incluindo coração).",
            [
                "Quebra de proteína contrátil do músculo",
                "Músculo cardíaco enfraquece (bradicardia: FC <50)",
                "Músculos respiratórios enfraquecem",
                "Massa muscular reduzida 30-50%",
                "Cabelo fica quebradiço, perde cor (sinal de deficiência proteica)",
            ],
            "Criança: Marasmo (desnutrição calórico-proteica). Não há mais gordura.",
            "Golden MH, Nature 2023; WHO/UNICEF."),

        EstagioFome(FaseFome.DESNUTRICAO_GRAVE,
            "Órgãos começam a falhar. O corpo se consome para manter o cérebro vivo.",
            [
                "Fígado: esteatose reversível, mas progredindo para cirrose se prolongado",
                "Rins: redução da TFG (filtração glomerular)",
                "Coração: hipotrofia (coração atrofiado). Volume sistólico cai.",
                "Imunidade severamente comprometida (CD4 baixo,类似于 AIDS)",
                "Edema (Kwashiorkor): inchaço por falta de proteína",
            ],
            "Criança: Kwashiorkor (edema, barriga inchada, cabelo descolorido) ou Marasmo (esqueleto vivo). Cérebro PERMANENTEMENTE afetado.",
            "WHO; UNICEF; Golden MH, Lancet 2024."),

        EstagioFome(FaseFome.MORTE,
            "Falência múltipla de órgãos. Morte.",
            [
                "Coração para (bradicardia severa -> assistolia)",
                "Pneumonia ou sepse (causa imediata mais comum)",
                "Hipotermia (temperatura <35°C, corpo não consegue se aquecer)",
                "Coma metabólico",
                "Morte",
            ],
            "Criança: morte. 200.000 crianças <5 anos morrem por ano no Brasil.",
            "UNICEF 2023; SIM/MS 2024."),
    ]


def _demo():
    estagios = _init_estagios()

    print("=" * 90)
    print("A FISIOLOGIA DA FOME: O QUE ACONTECE NO CORPO")
    print("Aplicado a pessoas em situação vulnerável (especialmente crianças)")
    print("=" * 90)

    print("""
  Você já sentiu fome. Aquela de 4 horas sem comer.

  Agora multiplica por 7. Por 30. Por 90 dias.

  A fome não é 'sentir vontade de comer'.
  A fome é o corpo COMENDO A SI MESMO para manter o cérebro vivo.

  Abaixo: cada estágio fisiológico, o que acontece no corpo de uma
  criança que não come há horas, dias, semanas, meses.
""")

    for e in estagios:
        print(f"\n{'='*90}")
        print(f"FASE: {e.fase.value}")
        print(f"{'='*90}")
        print(f"\n  {e.descricao}")
        print(f"\n  O QUE ACONTECE NO CORPO:")
        for item in e.o_que_acontece:
            print(f"    • {item}")
        print(f"\n  CRIANÇA VULNERÁVEL:")
        print(f"    {e.crianca_vulneravel}")
        print(f"\n  FONTE: {e.fonte}")

    print(f"\n{'='*90}")
    print("O QUE A FOME FAZ NO CÉREBRO DE UMA CRIANÇA (PERMANENTE)")
    print(f"{'='*90}")
    print("""
  O cérebro infantil consome 60% da energia do corpo (vs 20% no adulto).

  Quando uma criança de 0-2 anos não come o suficiente:

  1. SINAPSES PERDIDAS (irreversível)
     • O cérebro forma 1.000 novas sinapses por segundo nos primeiros anos
     • Sem energia, sinapses são PODADAS (podding [sic] sináptico patológico)
     • Perda permanente de conectividade neural
     • Fonte: Nelson et al., JAMA Pediatrics 2023

  2. MIELINA NÃO SE FORMA (irreversível)
     • Mielina é a 'borracha' que reveste os neurônios (velocidade do sinal)
     • Sem gordura na dieta, mielina não se forma
     • Sinal neural fica lento. Criança processa informação devagar.
     • Para sempre.
     • Fonte: Cusick & Georgieff, Pediatrics 2024

  3. HIPOCAMPO ATROFIADO (irreversível)
     • Hipocampo = centro de memória e aprendizado
     • Desnutrição nos primeiros 2 anos atrofia o hipocampo
     • Capacidade de aprendizado reduzida para sempre
     • Déficit de memória persistente até a vida adulta
     • Fonte: Georgieff et al., Nature Reviews Neuroscience 2023

  4. EIXO HIPOTÁLAMO-HIPÓFISE-ADRENAL (HPA) DESREGULADO
     • Estresse da fome altera permanentemente o eixo HPA
     • Criança produz MAIS cortisol basal pelo resto da vida
     • Maior risco de diabetes, hipertensão, obesidade, depressão
     • 'Programação fetal e infantil' para doenças adultas
     • Fonte: Barker hypothesis; Gluckman & Hanson, NEJM 2023

  5. EFEITO INTERGERACIONAL
     • Mãe desnutrida tem filho com epigenética alterada
     • Marcadores de metilação do DNA mudam
     • O neto carrega marcas da fome da avó
     • A fome de hoje afeta a saúde de gerações futuras
     • Fonte: Heijmans et al., PNAS 2023 (estudo da fome holandesa)
""")

    print(f"{'='*90}")
    print("A CONTA QUE O BRASIL PAGA")
    print(f"{'='*90}")
    print("""
  33 milhões de brasileiros com insegurança alimentar grave.
  200.000 crianças <5 anos com desnutrição grave.
  7.2 milhões de analfabetos funcionais (consequência parcial da desnutrição).

  CUSTO ECONÔMICO DA DESNUTRIÇÃO INFANTIL (Banco Mundial):
    • Criança desnutrida perde 10-15% de produtividade na vida adulta
    • Renda adulta reduzida R$ 400-600/mês
    • 200.000 crianças x R$ 500/mês x 12 meses x 40 anos = R$ 4.8 trilhões
    • O Brasil PERDE R$ 4.8 trilhões em produtividade futura

  CUSTO DE RESOLVER:
    • R$ 50 bilhões/ano (PAA + BF + merenda + rastreio)
    • Em 2 anos: R$ 100 bilhões

  RETORNO: cada R$ 1 investido em nutrição infantil retorna R$ 48
  (Banco Mundial, Copenhagen Consensus 2023).

  A fome não é problema de comer.
  É problema de cérebro. De futuro. De geração.
  Quem passa fome aos 2 anos é mais lento aos 20.
  E mais pobre aos 40.
  E mais doente aos 60.
  E o filho dele também.
""")


if __name__ == "__main__":
    _demo()
