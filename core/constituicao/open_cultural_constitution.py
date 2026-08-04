#!/usr/bin/env python3
"""
OpenCulturalConstitution -- O Código Moral da Republica em Forma de Arte
=========================================================================
"As 95 teses de Lutero eram codigo. Mas eram ALEMÃO e eram PUBLICO.
 O brasileiro nao le em latim. Le em cordel, canta em samba,
 luta em capoeira, come na antropofagia."

Este modulo NAO substitui os principios P1-P14 do constitutional_engine.
E a TRADUCAO CULTURAL deles. A carne no osso.

O problema do .py: e tecnico. E frio. Ninguem morre por um .py.
Ninguem canta um .py. Ninguem ensina o filho com um .py.

A capoeira sobreviveu a 400 anos de proibicao porque vivia no CORPO,
na MUSICA, no RODA. O negro escravizado construiu uma constituicao
que o Estado nao conseguiu matar porque ela era ARTE.

A Republica precisa do mesmo: principios que vivem na cultura brasileira
para que sobrevivam mesmo se o .py for deletado, o servidor for derrubado,
o governante for corrupto.

OS 6 VETORES CULTURAIS (cada principio mapeado a uma forma brasileira):

  1. CORDEL -- o jornal do povo. Cada principio vira folheto.
     Literatura de bancada. 6 linhas, rima, venda na feira.
     O povo que nao le codigo le cordel.

  2. CAPOEIRA -- a defesa que vira danca. P12 em movimento.
     Mandinga, malicia, resistencia. O corpo que se defende
     sem parecer arma. O cidadao-sensor em forma de roda.

  3. ANTROPOFAGIA -- comer o estrangeiro e cuspir brasileiro.
     P6+P7+soberania. Oswald de Andrade: "Só a Antropofagia nos une."
     Devorar a tecnologia alienigena e produzir coisa nossa.

  4. SAMBA -- a memoria coletiva. O que a comunidade NAO esquece.
     P5+P13. O samba-enredo que conta a verdade que o jornal omite.
     A batucada que registra o que o Estado quer apagar.

  5. CINEMA NOVO -- a estetica da fome. Glauber: "A miséria é
     comunicada e não anulada." Mostrar a violencia do sistema,
     nao maquiar. P1 em forma de imagem.

  6. RODA DE CONVERSA -- a assembleia que nao precisa de app.
     P4 no quintal. O debate que acontece de boca em boca,
     sem servidor, sem nuvem, sem vigilancia.

O CÓDIGO MORAL (alem dos principios -- o que o povo CARRY):

  Os principios P1-P14 sao as LEIS. O codigo moral e a CONDUTA.
  A lei dita o que e PROIBIDO. O codigo moral dita o que e
  BONITO de fazer. O brasileiro nao obedece lei por lei.
  O brasileiro obedece o que e bonito, o que da orgulho,
  o que o vizinho respeita.

  Por isso a Republica precisa do codigo moral:
  - Nao "e proibido corromper" (lei). E "corrupto e vergonha" (moral).
  - Nao "e obrigatorio transparencia" (lei). E "quem esconde, carece" (moral).
  - Nao "e direito vigiar o Estado" (lei). E "cidadao fiscal e valente" (moral).

  A lei obriga. O codigo moral CONDUZ. O brasileiro responde
  melhor a conduta que a obrigacao.

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple
from enum import Enum
from dataclasses import dataclass, field
from datetime import datetime
import random


# ============================================================================
# 1. ENUMS
# ============================================================================

class AlicerceEtico(Enum):
    """
    O ALICERCE: o motivo de tudo. Antes de P1. Antes dos 5 universais.
    Antes dos 8 mandamentos. Antes dos anti-padroes.

    A etica da Republica nao e IMPOSTA. E ESCOLHIDA.
    Voce pratica porque QUER ser melhor. Nao porque tem medo.
    Nao porque e lei. Nao porque alguem ta olhando.
    Porque e quem voce decidiu ser.

    O TESTE DA PADARIA:
      Tratar CEO e faxineira igual. Nao porque o faxineiro PODE SER
      CEO disfarcado. Porque se ele for SEMPRE faxineiro, voce ainda
      trata igual. Se nao, sua etica e teatro.

    O CÉTICO E O CRENTE:
      O cético pode ser mais ético que o crente. Porque pratica
      sem promessa de recompensa divina. pratica porque escolheu.
      A etica que precisa de céu para funcionar ja falhou no teste.

    O QUE ISTO MUDA NA REPUBLICA:
      A Republica NAO impoe etica. Cria as CONDICOES pra quem QUER
      praticar. Os principios P1-P14 sao a CERCA. O alicerce e o CHAO.
      A cerca protege de quem nao quer. O chao sustenta quem quer.
    """
    ESCOLHA_NAO_IMPOSICAO = (
        "escolha",
        "Pratico porque escolhi, nao porque foi imposto",
        "A etica que e imposta ja falhou. O teste da padaria prova: "
        "trato o tiuzinho bem nao porque ele PODE ser CEO disfarcado, "
        "mas porque se ele for SEMPRE tiuzinho, trato igual. Se nao, "
        "minha etica e teatro. A Republica nao impoe etica -- cria "
        "condicoes para quem QUER praticar. A cerca (P1-P14) protege "
        "de quem nao quer. O alicerce sustenta quem quer.",
    )
    TRATAR_IGUAL = (
        "tratar_igual",
        "CEO e faxineiro recebem o mesmo tratamento",
        "O tiuzinho na padaria pode ser CEO testando se voce trata "
        "quem nao tem poder como gente. Mas se voce trata bem SO "
        "PORQUE pode ser CEO, sua etica e estrategia disfarcada. "
        "O teste real: se o faxineiro fosse SEMPRE faxineiro, voce "
        "trata igual? Se sim, genuino. Se nao, teatro. P1 na forma "
        "mais pura: nao ha elite no tratamento.",
    )
    GENUINIDADE_SOB_PRESSAO = (
        "genuinidade",
        "E quem voce e quando ninguem esta olhando",
        "O CEO disfarcado de tiuzinho so funciona como teste porque "
        "a etica genuina aparece quando ninguem sabe que esta sendo "
        "observado. A Republica nao vigia pra punir (P13 vigia Estado, "
        "nao cidadao). A Republica confia no alicerce: quem escolheu "
        "ser melhor, e melhor quando sozinho.",
    )
    CRESCER_ESPIRITUALMENTE = (
        "crescer",
        "Estar melhor amanha do que hoje (sem promessa de recompensa)",
        "Elevar espiritualmente a etica nao e religiao. E autocuidado. "
        "O cético que pratica etica sem céu e mais etico que o crente "
        "que pratica por medo do inferno. A espiritualidade aqui e "
        "SECULAR: querer ser melhor amanha. A recompensa e interna. "
        "Nao tem cunha celestial. Tem orgulho proprio.",
    )
    IMPACTO_EMOCIONAL_PERMANENTE = (
        "impacto",
        "Esquecerao seu rosto, nunca como voce os fez sentir",
        "As pessoas esquecem seu rosto, seu nome, seu cargo. "
        "Nunca esquecem como voce as fez sentir. A humilhacao do "
        "garcom, o acolhimento a quem tava quebrado, a vergonha "
        "infligida no subordinado -- isso PERMANECE no corpo do "
        "outro, por decadas. Nao se prova em log. Nao se mede em "
        "score. Mas e o que sobra de voce. A Lei de Gerson e "
        "veneno porque opera no sentimento: deixar o outro usado "
        "gera desconfianca, que vira cultura. Cultura de desconfianca "
        "e o Brasil. A Republica inverte: o fiscal que faz o cidadao "
        "se sentir ouvido. O servidor que faz o atendido se sentir "
        "gente. O politico que faz o eleitor se sentir representado. "
        "Nao e performance. E o LEGADO invisivel. O que voce deixa "
        "no outro e mais permanente que qualquer monumento.",
    )

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def disernmento(self) -> str:
        return self.value[2]


class VetorCultural(Enum):
    """Os 6 vetores culturais brasileiros que carregam a constituicao."""
    CORDEL = ("cordel", "Cordel: o jornal do povo em rima")
    CAPOEIRA = ("capoeira", "Capoeira: defesa que vira danca, resistencia no corpo")
    ANTROPOFAGIA = ("antropofagia", "Antropofagia: comer o estrangeiro, cuspir brasileiro")
    SAMBA = ("samba", "Samba: memoria coletiva que o Estado nao apaga")
    CINEMA_NOVO = ("cinema_novo", "Cinema Novo: estetica da fome, mostrar a violencia")
    RODA_CONVERSA = ("roda", "Roda de conversa: assembleia sem servidor")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class CodigoMoral(Enum):
    """O codigo moral -- o que e BONITO de fazer (alem do que e lei)."""
    HONESTIDADE_RADICAL = ("honestidade", "Honestidade radical: nao mente, nao maquia, nao omite")
    CORAGEM_CIVICA = ("coragem", "Coragem civica: fala mesmo com medo, denuncia mesmo sozinho")
    SOLIDARIEDADE_ATIVA = ("solidariedade", "Solidariedade ativa: ajuda antes de ser pedido")
    VERGONHA_DO_ILICITO = ("vergonha", "Vergonha do ilicito: corrupto e vergonha, nao esperto")
    RESPEITO_A_DIFERENCA = ("respeito", "Respeito a diferenca: discorda sem destruir")
    MEMORIA_PERSISTENTE = ("memoria", "Memoria persistente: nao esquece o que o poder fez")
    HUMILDADE_NO_PODER = ("humildade", "Humildade no poder: lembra de onde veio")
    GENEROSIDADE_COM_SABER = ("generosidade", "Generosidade com saber: ensina o que aprendeu")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class UniversalFraterna(Enum):
    """
    As 5 universais extraidas de fraternidades que sobreviveram seculos.
    Cada fraternidade (maconaria, jesuitas, sangha, irmandades negras,
    quakers, guildas, sufi, confucianismo, ubuntu) tem essas 5 em comum.
    O que varia e a casca (religiao, segredo, hierarquia) -- descartada.

    O que NAO varia e o nucleo etico. E o que incorporamos.
    """
    U1_PEDRA_BRUTA = (
        "pedra_bruta",
        "Autolapidacao diaria: voce nao nasce etico, se lapida todo dia",
        "O ser humano nasce pedra sem forma. Cada acao lapida ou quebra. "
        "Nao e evento, e PROCESSO. Maconaria (pedra bruta), jesuitas "
        "(exame diario), sangha (meditacao), sufi (dhikr) -- todos dao "
        "o mesmo recado: a etica se pratica, nao se decora.",
    )
    U2_TRANSMISSAO_PESSOAL = (
        "transmissao",
        "Transmissao pessoa-a-pessoa: corrente, nao livro; roda, nao palestra",
        "A sabedoria que sobrevive passa de BOCA pra BOCA, de CORPO pra "
        "CORPO. Nao sobrevive em PDF. Silsila sufi, roda de capoeira, "
        "guilda de artesao, vinaya budista -- a unidade de transmissao "
        "e o ENCONTRO, nao o documento.",
    )
    U3_PROVA_DE_MERITO = (
        "merito",
        "Progressao por prova: mostra que sabe, nao espera tempo",
        "Grau, cargo, responsabilidade se GANHAM por demonstracao de "
        "competencia. Aprendiz -> oficial -> mestre. O mestre que nao "
        "sabe e destituido. Sangha: mestre pode ser destituido. "
        "Confucianismo: cargo por exame. Sem isso, vira oligarquia.",
    )
    U4_SERVICO_EXTERNO = (
        "servico",
        "Servico externo: a fraternidade existe pra servir de FORA",
        "A irmandade que serve a si mesma vira mafia. A que sobreviveu "
        "serve a COMUNIDADE. Irmandade dos Pretos: caixa de alforria. "
        "Quakers: abolicionismo, assistencia social. Sufi: seva (servico). "
        "Ubuntu: 'eu sou porque nos somos'. A fraternidade existe pra fora.",
    )
    U5_MEMORIA_RITUALIZADA = (
        "memoria",
        "Memoria coletiva: canta, conta, ritualiza pra nao esquecer",
        "O que o grupo NAO esquece sobrevive. Samba lembra o que o Estado "
        "apaga. Cordel registra o que o jornal omite. Ritual repete ate "
        "virar instinto. Capoeira: o berimbari conta a historia enquanto "
        "o corpo pratica. A memoria que canta sobrevive a censura.",

    )

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def disernmento(self) -> str:
        return self.value[2]


class AntiPadraoCultural(Enum):
    """
    Os ANTI-principios da cultura brasileira que a Republica ENFRENTA.

    Nao sao ignorados. Nao sao decorados. sao CONFRONTADOS.

    Cada um tem raiz historica (nao e 'culpa do brasileiro'), mas
    tem ponto de virada onde deixa de ser resistencia e vira predacao.
    """
    LEI_DE_GERSON = (
        "lei_gerson",
        "Lei de Gerson: levar vantagem em tudo, ser honesto e ser otario",
        "RAIZ: sobrevivencia num sistema colonial hostil. O escravo que "
        "furtava comida do senhor era RESISTENTE, nao imoral. VIRAGEM: "
        "deixa de ser resistencia quando voce leva vantagem do PROPRIO "
        "POVO. O astuto que cobra dobro do vizinho brasileiro nao esta "
        "resistindo ao colonizador -- esta replicando a logica do "
        "colonizador contra o irmao. ANTROPOFAGIA MAL FEITA: engoliu o "
        "predador e cuspiu predador mais pobre.",
        UniversalFraterna.U1_PEDRA_BRUTA,  # o que substitui
    )
    DOIS_PRECOS = (
        "dois_precos",
        "Dois precos: cobra dobro do gringo, metade do conhecido",
        "RAIZ: custo de zona turistica, imposto informal, sobrevivencia. "
        "VIRAGEM: discriminacao por aparencia/idioma e ANTI-P6 (acesso "
        "universal). O mesmo produto, dois precos, seleciona quem pode. "
        "O mercadinho que cobra R$ 12 do gringo e R$ 5 do local NAO esta "
        "sendo esperto -- esta normalizando que produto tem preco de gente "
        "e preco de subgente. CULTURA PAGA PAU PRO GRINGO (adula) E COBRA "
        "DOBRO DO GRINGO (explora). Dois sintomas da mesma raiz: falta de "
        "AUTOVALOR. O brasileiro nao se ve como IGUAL ao gringo.",
        UniversalFraterna.U4_SERVICO_EXTERNO,
    )
    JEITINHO = (
        "jeitinho",
        "Jeitinho: burlar burocracia por relacionamento em vez de processo",
        "RAIZ: Estado absurdo, burocracia asfixiante, sistema que nao "
        "funciona pela via formal. VIRAGEM: o jeitinho vira CORRUPCAO "
        "de processo democratico (P4). Quem tem contato pula fila. Quem "
        "nao tem espera. O jeitinho e privatizacao do servico publico: "
        "o que era de TODOS vira de QUEM CONHECE. E Anti-P1 (elitismo).",
        UniversalFraterna.U3_PROVA_DE_MERITO,
    )
    PAGAR_PAU_PRO_GRINGO = (
        "pau_gringo",
        "Pagar pau pro gringo: adular estrangeiro, desvalorizar o proprio",
        "RAIZ: colonia, 500 anos de complexo de inferioridade. VIRAGEM: "
        "adular quem vem de fora enquanto desvaloriza quem esta aqui e "
        "ANTI-ANTROPOFAGIA. A antropofagia de Oswald DIZ: comer o "
        "estrangeiro e cuspir brasileiro. Pagar pau e o contrario: "
        "engolir o estrangeiro inteiro e cuspir nada. E submissao "
        "disfarcada de sofisticacao.",
        UniversalFraterna.U1_PEDRA_BRUTA,
    )
    CULTURA_DO_MEDO = (
        "cultura_medo",
        "Cultura do medo: nao denuncia, nao fala, nao aparece",
        "RAIZ: ditadura, violencia, retaliacao real. VIRAGEM: o silencio "
        "protege o predador, nao a vitima. A omertA da mafia funciona "
        "assim: quem cala protege quem roubou. O cidadao que cala por "
        "medo e compreensivel, mas o SISTEMA que exige silencio e a "
        "doenca. A Republica protege quem fala (P13) e expoe quem cala "
        "por interesse.",
        UniversalFraterna.U2_TRANSMISSAO_PESSOAL,
    )

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def analise(self) -> str:
        return self.value[2]

    @property
    def antidoto(self) -> UniversalFraterna:
        return self.value[3]


# ============================================================================
# 2. BANCO DE CORDEL -- cada principio em verso popular
# ============================================================================

@dataclass
class CordelPrincipio:
    """Um principio constitucional em forma de cordel."""
    principio_id: str
    titulo: str
    sextilha: List[str]  # 6 versos heptassilabos (xaxaxa)


def _init_cordel() -> List[CordelPrincipio]:
    """Os 14 principios em cordel. Linguagem do povo, nao do tecnocrata."""
    return [
        CordelPrincipio(
            "P1",
            "O Decreto de Um So",
            [
                "Ninguem manda sozinho nao",
                "na Republica do povo,",
                "o poder vem de maos dadas,",
                "decreto de um so e bobo,",
                "o que um faz sem o todos",
                "o todos joga no lixo.",
            ],
        ),
        CordelPrincipio(
            "P2",
            "O Corpo E Teu",
            [
                "O corpo e teu, minha gente,",
                "ninguem manda nele nao,",
                "nem Estado, nem marido,",
                "nem padre, nem doctorao,",
                "sem querer com vontade",
                "nao se toca, e feitorio.",
            ],
        ),
        CordelPrincipio(
            "P3",
            "Trabalho Nao Tem Dono",
            [
                "Trabalho e trabalho irmao,",
                "nao tem genero nem cor,",
                "o que muda e o impacto,",
                "nao o titulo ou furor,",
                "faxineiro e doutor",
                "comecando pelo amor.",
            ],
        ),
        CordelPrincipio(
            "P4",
            "A Votacao Que Presta",
            [
                "Voto nao se compra nao",
                "com promessa nem favor,",
                "a urna e do cidadao,",
                "o poder e do votador,",
                "quem conta em segredo nao conta",
                "quem esconde perde o amor.",
            ],
        ),
        CordelPrincipio(
            "P5",
            "Caixa-Preta Nao Tem Vez",
            [
                "Caixa-preta pra que?",
                "O que o Estado faz eu vejo,",
                "meu bolso paga o pato,",
                "meu voto da o manejo,",
                "tudo que e gasto meu",
                "tem que aparecer no espelho.",
            ],
        ),
        CordelPrincipio(
            "P6",
            "Conhecimento Nao Tem Cofre",
            [
                "Saber nao e de rico nao,",
                "nem de quem tem diploman,",
                "o livro, a rede, a escola,",
                "sao direito de crianca,",
                "o ce de estrelas e meu",
                "doente de ganancia, quica.",
            ],
        ),
        CordelPrincipio(
            "P7",
            "Seguranca e Cultura",
            [
                "Quem tem medo de nmap?",
                "So quem tem porte pra esconder,",
                "a ferramenta nao e arma,",
                "e cultura de aprender,",
                "seguranca nao e elite,",
                "e alfabetizacao do ser.",
            ],
        ),
        CordelPrincipio(
            "P8",
            "A Maquina Serve",
            [
                "A maquina pensa? Nao.",
                "Pensa e ajuda, nao substitui,",
                "o humano e que decide,",
                "a IA so assisti,",
                "furia vende clique, irmao,",
                "inteligencia nao cai.",
            ],
        ),
        CordelPrincipio(
            "P9",
            "O Estado Que Divide Cai",
            [
                "O Estado nao pode nao",
                "brigar filho contra pai,",
                "dividir pra governar",
                "e doenca, e never mais,",
                "discordar e direito sim,",
                "polarizar e jamais.",
            ],
        ),
        CordelPrincipio(
            "P10",
            "O Ceu E de Todos",
            [
                "O ceu nao e de ninguem,",
                "portanto e de todos nos,",
                "drone nao vigia nao,",
                "nao mata, nao espia, nao,",
                "entrega remedio e po,",
                "mapeia queimada, e bom.",
            ],
        ),
        CordelPrincipio(
            "P11",
            "Quem Nao Tem Celular Vota",
            [
                "Exige celular pra que?",
                "Pra votar, pra receitar?",
                "O direito nao e app,",
                "o app e que devia estar,",
                "se o Estado digitaliza,",
                "o cidadao ensina a usar.",
            ],
        ),
        CordelPrincipio(
            "P12",
            "Republica Nao Tem Exercito Secreto",
            [
                "Criminoso nao e amigo,",
                "nao e colega, nao e peao,",
                "exercito secreto nao,",
                "e Russia com gosto de paun,",
                "a Republica defende sim,",
                "mas nao ataca o irmao.",
            ],
        ),
        CordelPrincipio(
            "P13",
            "Quem Esta No Poder Mostra",
            [
                "Aceitou cargo, escuta,",
                "sua vida ali e nossa,",
                "o gasto, a agenda, a reuniao,",
                "tudo que no cargo apronta,",
                "o povo tem direito de ver,",
                "privacidade? So na frente da porta.",
            ],
        ),
        CordelPrincipio(
            "P14",
            "O Dado E Teu",
            [
                "Voce gerou, e seu irmao,",
                "a empresa so pegou emprestado,",
                "quer de volta? Ela devolve,",
                "quer apagar? Ela apaga o dado,",
                "lucrou com voce? Te paga,",
                "nao existe almoço gratis, fado.",
            ],
        ),
    ]


# ============================================================================
# 3. MAPEAMENTO PRINCIPIO -> VETOR CULTURAL
# ============================================================================

def _init_mapeamento_cultural() -> Dict[str, Dict[str, Any]]:
    """Como cada principio vive na cultura brasileira."""
    return {
        "P1": {
            "vetor": VetorCultural.RODA_CONVERSA,
            "manifestacao": (
                "A roda de conversa do quintal. P4 no nivel do chao. "
                "O vizinho que diz 'isso ninguem decidiu' e segura o decreto. "
                "A assembleia que nao precisa de app porque acontece de boca."
            ),
        },
        "P2": {
            "vetor": VetorCultural.CAPOEIRA,
            "manifestacao": (
                "O corpo que se defende. A capoeira nasceu de corpos que "
                "pertenciam a outrem. P2 e a heranca: meu corpo e MEU. "
                "Ninguem toca sem licenca. A ginga e o consentimento em movimento."
            ),
        },
        "P3": {
            "vetor": VetorCultural.SAMBA,
            "manifestacao": (
                "A bateria onde cada um faz sua parte. O surdo carrega o ritmo, "
                "a caixa responde, o repique lidera. Ninguem e mais por papel. "
                "Trabalho igual, impacto diferente. O samba ensina P3."
            ),
        },
        "P4": {
            "vetor": VetorCultural.RODA_CONVERSA,
            "manifestacao": (
                "A roda de capoeira e assembleia: todos veem, todos falam, "
                "a decisao e coletiva. Quem entra na roda aceita as regras. "
                "Ninguem decide sozinho quem joga. P4 no berimbau."
            ),
        },
        "P5": {
            "vetor": VetorCultural.SAMBA,
            "manifestacao": (
                "O samba-enredo conta o que a historia oficial omite. "
                "A escola de samba e ARQUIVO PUBLICO do povo. "
                "O que o samba conta, o Estado nao consegue apagar. "
                "P5 nao precisa de servidor. Precisa de batucada."
            ),
        },
        "P6": {
            "vetor": VetorCultural.CORDEL,
            "manifestacao": (
                "O cordel e o jornal que o povo escreve e o povo le. "
                "Nao tem paywall. Nao tem diploma. Tem rima e bancada de feira. "
                "P6 e o cordel: conhecimento universal, distribuido na praca."
            ),
        },
        "P7": {
            "vetor": VetorCultural.CAPOEIRA,
            "manifestacao": (
                "A capoeira e seguranca que virou cultura. O negro criou "
                "tecnica de defesa e a disfarçou de danca para sobreviver. "
                "P7: seguranca nao e arma de elite. E cultura do povo. "
                "O berimbau e o nmap do seculo XIX."
            ),
        },
        "P8": {
            "vetor": VetorCultural.CINEMA_NOVO,
            "manifestacao": (
                "O Cinema Novo mostrou que a camera nao substitui o olhar. "
                "A estetica amplia, nao substitui. A IA e o mesmo: assiste, "
                "nao decide. O diretor humano corta. P8 na telinha."
            ),
        },
        "P9": {
            "vetor": VetorCultural.SAMBA,
            "manifestacao": (
                "O samba uniu o que o Estado tentou dividir. Favela e asfalto "
                "na mesma batida. Branco e preto no mesmo ritmo. P9: o Estado "
                "que divide perde a roda. O samba junta."
            ),
        },
        "P10": {
            "vetor": VetorCultural.CINEMA_NOVO,
            "manifestacao": (
                "A imagem aerea no Cinema Novo mostrava o territorio. "
                "Nao para vigiar. Para CONHECER. O drone que mapeia queimada "
                "e o olho do povo sobre a propria terra. P10 sem vigilancia."
            ),
        },
        "P11": {
            "vetor": VetorCultural.CORDEL,
            "manifestacao": (
                "O cordel ensina quem le. O Estado que digitaliza sem ensinar "
                "e como vender cordel so em latin. P11: se digitaliza, ensina "
                "DENTRO, como o cordel ensina enquanto conta a historia."
            ),
        },
        "P12": {
            "vetor": VetorCultural.CAPOEIRA,
            "manifestacao": (
                "A capoeira NAO ataca primeiro. Se defende. A malicia e "
                "defensiva. O mestre diz: 'capoeira nao e pra brigar, "
                "e pra nao apanhar.' P12: defesa transparente, nunca ataque."
            ),
        },
        "P13": {
            "vetor": VetorCultural.SAMBA,
            "manifestacao": (
                "O samba nao deixa esquecer. 'O samba nao morre nao.' "
                "O que o politico fez, o samba lembra. A agenda do poderoso "
                "e memoria da comunidade. P13: o povo ve e canta."
            ),
        },
        "P14": {
            "vetor": VetorCultural.ANTROPOFAGIA,
            "manifestacao": (
                "A antropofagia de Oswald: comer o estrangeiro e fazer brasileiro. "
                "P14: o dado que a Big Tech coletou de voce, voce COME de volta. "
                "Devora, digere, e faz seu. So a antropofagia de dados nos une."
            ),
        },
    }


# ============================================================================
# 4. MANIFESTO ANTROPOFAGO DIGITAL (no espirito de Oswald de Andrade)
# ============================================================================

MANIFESTO_ANTROPOFAGO_DIGITAL = """
MANIFESTO ANTROPOFAGO DIGITAL DA REPUBLICA ABERTA
==================================================

(Sobre o espirito do Manifesto Antropofago, Oswald de Andrade, 1928)

Contra toda technologie que nos e dada como prato feito.
Contra o app que coleta em silencio.
Contra o codigo fechado que chamam de presente.
Contra a AI que vigia em nome da seguranca.

So a Antropofagia Digital nos une. Socialmente.

Comemos o algoritmo do Silicon Valley.
Deglutimos o framework opensource.
Mastigamos o protocolo.
E cuspimos brasileiro.

O dado que saiu de nos, devolvemos pra nos.
A AI que veio da nuvem, trazemos pro chao.
O hardware fabricado la fora, refazemos aqui dentro.

Nao somos contra o estrangeiro.
Somos contra a digestao passiva.
O brasileiro nao engole inteiro.
O brasileiro mastiga, escolhe, transforma.

Tupy, or not tupy: that is the question.
Python, or not python: that is the answer.
Mas o python que roda no chao de brasilia,
nao o python que vigia de menlo park.

So a Antropofagia nos une.
Socialmente. Tecnicamente. Constitucionalmente.

Contra o 95 teses de Lutero: 14 principios vivos.
Contra o codigo morto: cultura que canta.
Contra o Estado opaco: roda que ve.
Contra o dado roubado: boca que devolve.

P1 a P14 sao o DIGERIDO.
O manifesto e a FOME.

(Antes dos portugueses descobrirem o Brasil,
o Brasil ja tinha se descoberto.
Antes do codigo definir o cidadao,
o cidadao ja era codigo.)
"""


# ============================================================================
# 5. ENGINE
# ============================================================================

class CulturalConstitutionEngine:
    """
    Gera a expressao cultural dos principios constitucionais.

    Faz tres coisas:
    1. Gera CORDEL para cada principio (o povo le)
    2. MAPEIA cada principio a um vetor cultural (como vive no povo)
    3. PRODUZ o codigo moral (o que e bonito de fazer)
    """

    def __init__(self) -> None:
        self.cordeis: List[CordelPrincipio] = _init_cordel()
        self.mapeamento: Dict[str, Dict[str, str]] = _init_mapeamento_cultural()

    # -- cordel ------------------------------------------------------------

    def cordel_do(self, principio_id: str) -> Optional[CordelPrincipio]:
        for c in self.cordeis:
            if c.principio_id == principio_id:
                return c
        return None

    def todos_cordeis(self) -> List[Dict[str, Any]]:
        return [
            {
                "principio": c.principio_id,
                "titulo": c.titulo,
                "verso": " / ".join(c.sextilha),
            }
            for c in self.cordeis
        ]

    def imprimir_cordel(self, principio_id: str) -> str:
        """Imprime o cordel de um principio em formato de folheto."""
        c = self.cordel_do(principio_id)
        if c is None:
            return f"Sem cordel para {principio_id}"
        linhas = [
            f"+{'-'*40}+",
            f"|  {c.titulo:<38} |",
            f"|  (Cordel do principio {c.principio_id}){' '*(16)}|",
            f"+{'-'*40}+",
        ]
        for verso in c.sextilha:
            linhas.append(f"|  {verso:<38} |")
        linhas.append(f"+{'-'*40}+")
        return "\n".join(linhas)

    # -- mapeamento cultural -----------------------------------------------

    def manifestacao_cultural(self, principio_id: str) -> Optional[Dict[str, Any]]:
        m = self.mapeamento.get(principio_id)
        if m is None:
            return None
        vetor = m["vetor"]
        return {
            "principio": principio_id,
            "vetor": vetor.id,
            "vetor_rotulo": vetor.rotulo,
            "manifestacao": m["manifestacao"],
        }

    def todos_mapeamentos(self) -> List[Dict[str, Any]]:
        result: List[Dict[str, Any]] = []
        for pid in sorted(self.mapeamento):
            m = self.manifestacao_cultural(pid)
            if m is not None:
                result.append(m)
        return result

    # -- codigo moral -------------------------------------------------------

    def codigo_moral(self) -> List[Dict[str, str]]:
        """O que e BONITO de fazer (alem do que e lei)."""
        return [{"id": m.id, "rotulo": m.rotulo} for m in CodigoMoral]

    # -- universais fraternas -----------------------------------------------

    def alicerce_etico(self) -> List[Dict[str, str]]:
        """O motivo de tudo. Antes de P1. Antes dos universais."""
        return [{"id": a.id, "rotulo": a.rotulo, "disernmento": a.disernmento}
                for a in AlicerceEtico]

    def universais_fraternas(self) -> List[Dict[str, str]]:
        """As 5 universais extraidas de fraternidades que sobreviveram seculos."""
        return [{"id": u.id, "rotulo": u.rotulo, "disernmento": u.disernmento}
                for u in UniversalFraterna]

    # -- anti-padroes culturais ---------------------------------------------

    def anti_padroes(self) -> List[Dict[str, str]]:
        """Os ANTI-principios da cultura brasileira que a Republica ENFRENTA."""
        return [
            {
                "id": a.id,
                "rotulo": a.rotulo,
                "analise": a.analise,
                "antidoto": a.antidoto.rotulo,
            }
            for a in AntiPadraoCultural
        ]

    # -- manifesto ----------------------------------------------------------

    def manifesto(self) -> str:
        return MANIFESTO_ANTROPOFAGO_DIGITAL.strip()

    # -- scorecard ----------------------------------------------------------

    def scorecard(self) -> Dict[str, Any]:
        return {
            "principios_com_cordel": len(self.cordeis),
            "principios_mapeados": len(self.mapeamento),
            "vetores_culturais": len(list(VetorCultural)),
            "itens_codigo_moral": len(list(CodigoMoral)),
            "alicerce_etico": len(list(AlicerceEtico)),
            "universais_fraternas": len(list(UniversalFraterna)),
            "anti_padroes_catalogados": len(list(AntiPadraoCultural)),
            "manifesto": "Antropofago Digital (no espirito de Oswald, 1928)",
        }


# ============================================================================
# 6. DEMO
# ============================================================================

def _demo() -> None:
    eng = CulturalConstitutionEngine()

    print("=" * 70)
    print("OpenCulturalConstitution -- A Constituicao que Canta")
    print("=" * 70)

    # --- Cordel de cada principio ---
    print(f"\n[OS {len(eng.cordeis)} CORDEIS CONSTITUCIONAIS]")
    print("  (cada principio em verso popular -- P1 a P14)")
    for c in eng.cordeis:
        print(f"\n  {eng.imprimir_cordel(c.principio_id)}")

    # --- Mapeamento cultural ---
    print(f"\n\n[OS {len(eng.mapeamento)} PRINCIPIOS NA CULTURA]")
    for m in eng.todos_mapeamentos():
        print(f"\n  {m['principio']} -> {m['vetor'].upper()}")
        print(f"  {m['vetor_rotulo']}")
        # wrap manifestacao
        texto = m["manifestacao"]
        while len(texto) > 65:
            idx = texto.rfind(" ", 0, 65)
            if idx == -1:
                idx = 65
            print(f"  {texto[:idx]}")
            texto = texto[idx:].lstrip()
        print(f"  {texto}")

    # --- Os 6 vetores ---
    print(f"\n\n[OS {len(list(VetorCultural))} VETORES CULTURAIS]")
    for v in VetorCultural:
        print(f"  {v.id:<16} {v.rotulo}")

    # --- O alicerce etico ---
    print(f"\n\n[ALICERCE ETICO ({len(list(AlicerceEtico))} PILARES)]")
    print("  (o motivo de tudo. Antes de P1. Antes dos universais.)")
    for a in eng.alicerce_etico():
        print(f"\n  {a['id'].upper()} -- {a['rotulo']}")
        texto = a["disernmento"]
        while len(texto) > 67:
            idx = texto.rfind(" ", 0, 67)
            if idx == -1:
                idx = 67
            print(f"    {texto[:idx]}")
            texto = texto[idx:].lstrip()
        print(f"    {texto}")

    # --- O codigo moral ---
    print(f"\n\n[O CODIGO MORAL ({len(list(CodigoMoral))} MANDAMENTOS)]")
    print("  (o que e BONITO de fazer, alem do que e lei)")
    for i, m in enumerate(eng.codigo_moral(), 1):
        print(f"  {i}. {m['rotulo']}")

    # --- As 5 universais fraternas ---
    print(f"\n\n[AS {len(list(UniversalFraterna))} UNIVERSAIS FRATERNAS]")
    print("  (extraidas de maconaria, jesuitas, sangha, irmandades negras,")
    print("   quakers, guildas, sufi, confucianismo, ubuntu. Casca descartada.)")
    for u in eng.universais_fraternas():
        print(f"\n  {u['id'].upper()} -- {u['rotulo']}")
        # wrap disernmento
        texto = u["disernmento"]
        while len(texto) > 67:
            idx = texto.rfind(" ", 0, 67)
            if idx == -1:
                idx = 67
            print(f"    {texto[:idx]}")
            texto = texto[idx:].lstrip()
        print(f"    {texto}")

    # --- Os anti-padroes culturais ---
    print(f"\n\n[OS {len(list(AntiPadraoCultural))} ANTI-PADROES CONFRONTADOS]")
    print("  (o que a Republica ENFRENTA -- nao ignora, nao decora)")
    for a in eng.anti_padroes():
        print(f"\n  {a['id'].upper()}")
        print(f"  Rotulo: {a['rotulo']}")
        print(f"  Antidoto: {a['antidoto']}")
        # wrap analise
        texto = a["analise"]
        while len(texto) > 67:
            idx = texto.rfind(" ", 0, 67)
            if idx == -1:
                idx = 67
            print(f"  {texto[:idx]}")
            texto = texto[idx:].lstrip()
        print(f"  {texto}")

    # --- Manifesto ---
    print("\n\n" + "=" * 70)
    print(eng.manifesto())
    print("=" * 70)

    # --- Filosofia ---
    print("""
FILOSOFIA -- A Constituicao que Sobrevive na Cultura

O PROBLEMA DO .py:

  O .py e tecnico. E frio. Ninguem morre por um .py.
  Ninguem canta um .py. Ninguem ensina o filho com um .py.
  Se o servidor cai, o .py some. Se o governante quer, o .py muda.

A SOLUCAO BRASILEIRA:

  A capoeira sobreviveu a 400 anos de proibicao.
  Nao porque era codificada num livro.
  Porque vivia no CORPO, na MUSICA, na RODA.
  O negro escravizado construiu uma constituicao
  que o Estado nao conseguiu matar.

  A Republica precisa do mesmo.
  Os principios P1-P14 sao o ESQUELETO.
  A cultura e a CARNE que faz andar.

  O cordel ensina quem nao le codigo.
  O samba lembra o que o Estado quer apagar.
  A capoeira defende sem parecer arma.
  A antropofagia devora o estrangeiro e faz brasileiro.

O CODIGO MORAL:

  A lei dita o PROIBIDO.
  O codigo moral dita o BONITO.
  O brasileiro nao obedece lei por lei.
  O brasileiro obedece o que da orgulho.

  - Nao "e proibido corromper" (lei).
    E "corrupto e vergonha" (moral).
  - Nao "e obrigatorio transparencia" (lei).
    E "quem esconde, carece" (moral).

  A lei obriga. O codigo moral CONDUZ.

MARTINHO LUTERO E NOS:

  Lutero pregou 95 teses numa porta. Em alemao. Para o povo ler.
  Mudou a civilizacao porque era ACESSIVEL (P6) e PUBLICO (P5).

  Mas Lutero pregou em porta de IGREJA.
  A Republica nao tem igreja. Tem FEIRA.
  Tem RODA. Tem SAMBA. Tem CORDEL na bancada.

  Os 14 principios sao o DIGERIDO.
  O manifesto e a FOME.
  O cordel e o PRATO.
  O samba e a MEMORIA.

So a Antropofagia nos une. Socialmente. Constitucionalmente.
""")


if __name__ == "__main__":
    _demo()
