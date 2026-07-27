#!/usr/bin/env python3
"""
OpenConstituentAssembly -- Assembleia Constituinte -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenConstituentAssembly -- Assembleia Constituinte
====================================================
"FUNDADOR NÃO DITA PARÂMETROS. O POVO DECIDE."
O que aconteceu:
1. O fundador propôs parâmetros (920h base, 2300h limite, etc.)
2. O fundador DISCORDOU dos próprios parâmetros
3. O fundador convocou ASSEMBLEIA CONSTITUINTE
4. A POPULAÇÃO vai decidir cada número
5. O voto do fundador vale 1. Igual ao de todos.
ISSO É ANTI-ELITISMO REAL.
Quem tem poder de propor não tem poder de impor.
Nem sobre os próprios parâmetros.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa random
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict, Counter de collections
# ============================================================================
# 1. PARÂMETROS EM DISPUTA
# ============================================================================
class ParamCategory(Enum):
    TRABALHO = "trabalho"
    CRÉDITO = "credito"
    REPARACAO = "reparacao"
    DESCANSO = "descanso"
    GOVERNANCA = "governanca"
# decorador: @dataclass
class Proposition:
    # Uma proposta de parâmetro para votação.
    Cada parâmetro tem:
    - O valor que o fundador propôs (referência, NÃO imposição)
    - Múltiplas alternativas para a população escolher
    - Argumentos a favor and contra cada opção
    - O povo vota. O que ganhar vira lei.
    # 
    prop_id: texto
    category: ParamCategory
    title: texto
    description: texto
    founder_suggestion: qualquer // o que o fundador propôs
    options: List[(qualquer, texto)] // (valor, descrição) -- opções de voto
    arguments_for: [texto] = field(default_factory=list)
    arguments_against: [texto] = field(default_factory=list)
    # Resultado
    votes: {qualquer: inteiro} = field(default_factory=dict)
    winner: qualquer? = None
    turnout: int = 0
    approved: bool = False
# ============================================================================
# 2. POPULAÇÃO QUE VOTA
# ============================================================================
class Demographic(Enum):
    # Segmentos demográficos da população -- cada um vota diferente.
    TRABALHADOR_RURAL = "rural"  // agricultor, pecuarista
    TRABALHADOR_URBANO = "urbano"  // indústria, serviços
    PROFISSIONAL_SAUDE = "saude"  // médico, enfermeiro
    EDUCADOR = "educador"  // professor
    CUIDADOR = "cuidador"  // filho, idoso, doente
    JOVEM = "jovem"  // 16-25
    IDOSO = "idoso"  // 65+
    ARTESAO = "artesao"  // artista, criador
    TECNICO = "tecnico"  // engenheiro, cientista
    DONA_CASA = "dona_casa"  // trabalho doméstico não remunerado
    PCD = "pcd"  // pessoa com deficiência
    REPARACAO_CANDIDATO = "reparacao"  // pessoa buscando reparação
# decorador: @dataclass
class Constituent:
    # Um membro da assembleia constituinte.
    citizen_id: texto
    name: texto
    demographic: Demographic
    age: inteiro
    is_founder: bool = False
    def vote_on(self, prop: Proposition) -> Any:
        # Vota numa proposta baseado em seu perfil demográfico.
        DIFERENTES GRUPOS PRIORIZAM DIFERENTES COISAS:
        - Trabalhador rural: quer menos horas base (trabalho pesado físico)
        - Profissional de saúde: quer reconhecimento de impacto
        - Cuidador: quer trabalho de cuidado contar como contribuição
        - Idoso: quer menos horas obrigatórias
        - Jovem: quer flexibilidade
        - PCD: quer flexibilidade and acessibilidade
        - Reparação: quer mais reparação
        - Fundador: vota como fundador mas vale 1
        # 
        if self.is_founder:
            return prop.founder_suggestion
        # Cada demográfico tem preferências
        return self._demographic_vote(prop)
    def _demographic_vote(self, prop: Proposition) -> Any:
        # Voto baseado em perfil demográfico.
        d = self.demographic
        options = [o[0] para o em prop.options]
        # === HORAS BASE POR SEMANA ===
        if "base" in prop.title.lower()  and  "horas" in prop.title.lower():
            if d in (Demographic.TRABALHADOR_RURAL, Demographic.IDOSO, Demographic.PCD):
                return random.choice([10, 12, 15, 15, 20]) // quer menos
            if d == Demographic.JOVEM:
                return random.choice([15, 20, 20, 25]) // flexível
            if d == Demographic.PROFISSIONAL_SAUDE:
                return random.choice([20, 20, 25, 30]) // aceita mais
            if d == Demographic.CUIDADOR:
                return random.choice([10, 12, 15, 20]) // cuidado é trabalho
            return random.choice([15, 20, 20, 20, 25])
        # === LIMITE MÁXIMO ===
        if "limite" in prop.title.lower():
            if d in (Demographic.TRABALHADOR_RURAL, Demographic.JOVEM):
                return random.choice([35, 40, 40, 44])
            if d == Demographic.PROFISSIONAL_SAUDE:
                return random.choice([40, 44, 48, 50])
            return random.choice([40, 40, 44, 44])
        # === DESCANSO ===
        if "descanso" in prop.title.lower()  or  "ferias" in prop.title.lower():
            if d in (Demographic.IDOSO, Demographic.PCD, Demographic.CUIDADOR):
                return max(options) // quer mais descanso
            return random.choice(options)
        # === CRÉDITO ===
        if "credito" in prop.title.lower()  or  "teto" in prop.title.lower():
            if d == Demographic.REPARACAO_CANDIDATO:
                return max(options) // quer mais crédito (reparação)
            if d == Demographic.TECNICO:
                return random.choice(options)
            return random.choice(options)
        # === REPARAÇÃO ===
        if "reparacao" in prop.title.lower()  or  "multiplicador" in prop.title.lower():
            if d == Demographic.REPARACAO_CANDIDATO:
                return max(options) // quer multiplicador maior
            if d == Demographic.PROFISSIONAL_SAUDE:
                return random.choice(options) // neutro
            return random.choice(options)
        # === DURAÇÃO DE MANDATO ===
        if "mandato" in prop.title.lower():
            return min(options) // mandatos curtos = mais democracia
        # === DEFAULT ===
        return random.choice(options)
# ============================================================================
# 3. ASSEMBLEIA CONSTITUINTE
# ============================================================================
class ConstituentAssembly:
    # A assembleia que decide TODOS os parâmetros da República.
    PROCESSO (P4 PROCESSO DEMOCRÁTICO):
    1. PROPOSTA: parâmetros são propostos (pelo fundador or qualquer cidadao)
    2. DEBATE: argumentos a favor and contra são públicos
    3. VOTAÇÃO: TODA a população vota (1 pessoa = 1 voto)
    4. RESULTADO: o que ganhar maioria vira lei constitucional
    5. REVISÃO: cada parâmetro pode ser reaberto a cada 5 anos
    O FUNDADOR:
    - Propôs os parâmetros iniciais
    - DISCORDOU deles
    - Convocou esta assembleia
    - Voto = 1 (igual a todos)
    - Se a população votar diferente da proposta original, a vontade do povo prevalece
    # 
    def __init__(self):
        self.propositions: {texto: Proposition} = {}
        self.constituents: [Constituent] = []
        self.results: {texto: qualquer} = {}
        self.final_constitution: {texto: qualquer} = {}
    def populate(self, n: inteiro = 10000) -> None:
        # Popula a assembleia com n cidadaos de diversos demográficos.
        # Distribuição demográfica aproximada
        dist = {
            Demographic.TRABALHADOR_RURAL: 0.15,
            Demographic.TRABALHADOR_URBANO: 0.20,
            Demographic.PROFISSIONAL_SAUDE: 0.05,
            Demographic.EDUCADOR: 0.08,
            Demographic.CUIDADOR: 0.10,
            Demographic.JOVEM: 0.12,
            Demographic.IDOSO: 0.08,
            Demographic.ARTESAO: 0.05,
            Demographic.TECNICO: 0.05,
            Demographic.DONA_CASA: 0.07,
            Demographic.PCD: 0.03,
            Demographic.REPARACAO_CANDIDATO: 0.02,
        }
        self.constituents.clear()
        # Fundador
        self.constituents.append(Constituent(
            "F-001", "Cleiton (fundador)", Demographic.TECNICO,
            age = 35, is_founder=True))
        for i in intervalo(n - 1):
            demo = random.choices(list(dist.keys()), weights=list(dist.values()))[0]
            age = random.randint(16, 80)
            if demo == Demographic.JOVEM:
                age = random.randint(16, 25)
            elif demo == Demographic.IDOSO:
                age = random.randint(65, 85)
            self.constituents.append(Constituent(
                "C-{i:05d}", "Cidadao-{i:04d}", demo, age))
    def _init_propositions(self) -> None:
        # Cria todas as propostas a serem votadas.
        Cada uma tem a sugestão do fundador and alternativas.
        A população escolhe. O fundador não impõe.
        # 
        props = [
            # === TRABALHO ===
            Proposition("P-01", ParamCategory.TRABALHO,
                "Horas base por semana (contrato mínimo)",
                "Quantas horas por semana todo cidadao deve ao coletivo?",
                founder_suggestion = 20,
                options = [(10, "10h (meio período leve)"),
                        (15, "15h (meio período)"),
                        (20, "20h (proposta fundador)"),
                        (25, "25h (meio período pesado)"),
                        (30, "30h (quase tempo integral)")],
                arguments_for = [
                    "Menos horas base = mais tempo para vida pessoal",
                    "Mais horas base = mais contribuição coletiva",
                    "20h equilibra contribuição and autonomia",
                ],
                arguments_against = [
                    "Trabalho rural pesado não aguenta 20h",
                    "Trabalho intelectual pode fazer mais",
                    "Cuidadores já trabalham além do contabilizado",
                ]),
            Proposition("P-02", ParamCategory.TRABALHO,
                "Limite máximo de horas por semana (PROIBIDO ultrapassar)",
                "A partir de quantas horas a República PROÍBE aceitar trabalho?",
                founder_suggestion = 50,
                options = [(35, "35h (proteção máxima)"),
                        (40, "40h (padrão internacional)"),
                        (44, "44h (CLT Brasil)"),
                        (48, "48h (intenso)"),
                        (50, "50h (proposta fundador)")],
                arguments_for = [
                    "Limite baixo = proteção contra burnout",
                    "Limite alto = flexibilidade para quem quer fazer mais",
                    "44h é o padrão brasileiro conhecido",
                ]),
            Proposition("P-03", ParamCategory.TRABALHO,
                "Semanas úteis por ano",
                "Quantas semanas por ano sao de trabalho? (resto = descanso)",
                founder_suggestion = 46,
                options = [(40, "40 semanas (12 de descanso)"),
                        (44, "44 semanas (8 de descanso)"),
                        (46, "46 semanas (6 descanso -- fundador)"),
                        (48, "48 semanas (4 descanso)")],
                arguments_for = ["Mais semanas de descanso = saúde mental"]),
            # === DESCANSO ===
            Proposition("P-04", ParamCategory.DESCANSO,
                "Dias de descanso por semana (mínimo)",
                "Quantos dias por semana sem trabalho obrigatório?",
                founder_suggestion = 2,
                options = [(2, "2 dias (proposta fundador)"),
                        (3, "3 dias (semana de 4 dias)")],
                arguments_for = ["3 dias = revolução na qualidade de vida"]),
            Proposition("P-05", ParamCategory.DESCANSO,
                "Semanas mínimas de férias por ano",
                "Quantas semanas de férias garantidas por ano?",
                founder_suggestion = 4,
                options = [(2, "2 semanas"),
                        (4, "4 semanas (proposta fundador)"),
                        (6, "6 semanas")],
                arguments_for = ["Mais férias = recuperação real"]),
            # === CRÉDITO ===
            Proposition("P-06", ParamCategory.CRÉDITO,
                "Crédito de acesso: teto máximo por ciclo",
                "Nenhum cidadao recebe mais que isto num ciclo.",
                founder_suggestion = 50,
                options = [(20, "20 (igualdade máxima)"),
                        (30, "30"),
                        (50, "50 (proposta fundador)"),
                        (100, "100 (maior diferenciação)")],
                arguments_for = [
                    "Teto baixo = mais igualdade",
                    "Teto alto = reconhece diferença de impacto",
                ]),
            Proposition("P-07", ParamCategory.CRÉDITO,
                "Crédito de acesso: piso mínimo por ciclo",
                "Nenhum cidadao recebe menos que isto.",
                founder_suggestion = 5,
                options = [(0, "0 (sem piso)"),
                        (5, "5 (proposta fundador)"),
                        (10, "10"),
                        (15, "15")],
                arguments_for = ["Piso alto = dignidade garantida para todos"]),
            Proposition("P-08", ParamCategory.CRÉDITO,
                "Conversão horas -> crédito",
                "Quantas horas de trabalho = 1 crédito de acesso?",
                founder_suggestion = 10,
                options = [(5, "5h (mais generoso)"),
                        (10, "10h (proposta fundador)"),
                        (20, "20h (mais restritivo)")],
                arguments_for = ["Menos horas por crédito = acesso mais fácil"]),
            # === REPARAÇÃO ===
            Proposition("P-09", ParamCategory.REPARACAO,
                "Reparação: horas por ano de vida roubada",
                "Diagnóstico errado, rotulo injusto. Quanto vale 1 ano roubado?",
                founder_suggestion = 920,
                options = [(460, "460h (meio ano)"),
                        (920, "920h = 1 ano base (proposta fundador)"),
                        (1840, "1840h = 1 ano máximo"),
                        (2300, "2300h = 1 ano limite")],
                arguments_for = [
                    "Mais horas = mais reconhecimento do dano",
                    "920h = equivalência: 1 ano roubado = 1 ano de trabalho reconhecido",
                ]),
            Proposition("P-10", ParamCategory.REPARACAO,
                "Reparação: multiplicador para crianças (vitima era crianca)",
                "Crianca rotulada errada sofre mais. Quanto multiplicar?",
                founder_suggestion = 2.0,
                options = [(1.0, "1.0x (mesmo que adulto)"),
                        (1.5, "1.5x"),
                        (2.0, "2.0x (proposta fundador)"),
                        (3.0, "3.0x (triplo)")],
                arguments_for = [
                    "Criança tem vida inteira afetada = multiplicador maior",
                    "Infância roubada não tem preço = máximo",
                ]),
            Proposition("P-11", ParamCategory.REPARACAO,
                "Reparação: multiplicador para dano severo (>70/100)",
                "Dano com score > 70/100. Quanto multiplicar a reparação?",
                founder_suggestion = 1.5,
                options = [(1.0, "1.0x (sem agravante)"),
                        (1.5, "1.5x (proposta fundador)"),
                        (2.0, "2.0x (dobro)")],
                arguments_for = ["Dano severo = vida devastada"]),
            # === GOVERNANÇA ===
            Proposition("P-12", ParamCategory.GOVERNANCA,
                "Duração do mandato de representante (meses)",
                "Quanto tempo dura o mandato de um representante?",
                founder_suggestion = 6,
                options = [(3, "3 meses (rotação máxima)"),
                        (6, "6 meses (proposta fundador)"),
                        (12, "12 meses (anual)")],
                arguments_for = ["Mandato curto = menos poder acumulado"]),
            Proposition("P-13", ParamCategory.GOVERNANCA,
                "Revisão constitucional: a cada quantos anos?",
                "Cada parâmetro pode ser reaberto para nova votação.",
                founder_suggestion = 5,
                options = [(2, "2 anos (muito dinâmico)"),
                        (3, "3 anos"),
                        (5, "5 anos (proposta fundador)"),
                        (10, "10 anos (estabilidade)")],
                arguments_for = [
                    "Revisão frequente = adaptação rápida",
                    "Revisão rara = estabilidade",
                ]),
        ]
        for p in props:
            self.propositions[p.prop_id] = p
    def run_election(self) -> {texto: qualquer}:
        # Executa a votação de todas as propostas.
        Cada cidadao vota em cada proposta.
        1 pessoa = 1 voto. Fundador incluso (voto = 1).
        Maioria simples decide.
        # 
        for prop in self.propositions.values():
            votes = Counter()
            for constituent in self.constituents:
                vote = constituent.vote_on(prop)
                votes[vote] += 1
            prop.votes = dict(votes)
            prop.turnout = len(self.constituents)
            # Maioria simples
            winner_val = votes.most_common(1)[0][0]
            prop.winner = winner_val
            prop.approved = True
            # Converter para nome legível
            winner_desc = ""
            for each (val, desc) in prop.options:
                if val == winner_val:
                    winner_desc = desc
                    break
            self.final_constitution[prop.title] = {
                "value": winner_val,
                "description": winner_desc,
                "founder_suggestion": prop.founder_suggestion,
                "changed": winner_val != prop.founder_suggestion,
                "votes": dict(votes),
                "turnout": prop.turnout,
            }
        return self.final_constitution
    def results_report(self) -> str:
        # Relatório completo da votação.
        lines = []
        lines.append("=" * 80)
        lines.append("  ASSEMBLEIA CONSTITUINTE DA OPENREPUBLIC")
        lines.append("  'O POVO DECIDE. O FUNDADOR ACEITA.'")
        lines.append("=" * 80)
        lines.append("\n  População votante: {len(self.constituents):,}")
        lines.append("  Propostas votadas: {len(self.propositions)}")
        lines.append("")
        changed_count = 0
        for prop in self.propositions.values():
            result = self.final_constitution[prop.title]
            changed = result["changed"]
            if changed:
                changed_count = changed_count + 1
            marker = changed ? "[ALTERADO]" : "[mantido]"
            lines.append("\n  {marker} {prop.prop_id}: {prop.title}")
            lines.append("    Proposta do fundador: {prop.founder_suggestion}")
            lines.append("    DECISÃO DO POVO:      {result['value']} "
                        "({result['description']})")
            # Mostrar distribuição de votos
            total_votes = sum(result["votes"].values())
            lines.append("    Votação (turnout: {result['turnout']:,}):")
            sorted_votes = sorted(result["votes"].items(),
                                key = (x) -> -x[1])
            for each (val, count) in sorted_votes:
                pct = count / total_votes * 100
                bar = "#" * inteiro(pct / 2)
                founder_mark = val == prop.founder_suggestion ? " <-- fundador" : ""
                lines.append("      {val:>6}: {count:>5,} ({pct:>5.1f}%) {bar}{founder_mark}")
        lines.append("\n\n  {'='*80}")
        lines.append("  RESULTADO: {changed_count} de {len(self.propositions)} "
                    "parâmetros ALTERADOS pelo povo.")
        if changed_count > 0:
            lines.append("  O fundador propôs. O povo DISCORDOU em {changed_count} pontos.")
            lines.append("  A vontade do povo PREVALECE.")
        else:
            lines.append("  O povo ratificou todas as propostas do fundador.")
        review_val = 5
        for each (title, result) in self.final_constitution.items():
            if "revis" in title.lower()  and  "anos" in title.lower():
                review_val = result.get("value", 5)
                break
        lines.append("  PRÓXIMA REVISÃO: em {review_val} anos.")
        lines.append("  {'='*80}")
        return "\n".join(lines)
    def constitution_text(self) -> str:
        # Gera o texto constitucional final com os valores votados.
        lines = []
        lines.append("=" * 70)
        lines.append("  CONSTITUIÇÃO DA OPENREPUBLIC")
        lines.append("  (aprovada por votação popular direta)")
        lines.append("=" * 70)
        lines.append("")
        lines.append("  ARTIGO I - TRABALHO")
        for each (title, result) in self.final_constitution.items():
            if any(k in title.lower() para k em ["base", "limite", "semanas uteis"]):
                lines.append("    {title}: {result['value']} {result['description']}")
        lines.append("\n  ARTIGO II - DESCANSO")
        for each (title, result) in self.final_constitution.items():
            if any(k in title.lower() para k em ["descanso", "ferias"]):
                lines.append("    {title}: {result['value']} {result['description']}")
        lines.append("\n  ARTIGO III - CRÉDITO DE ACESSO")
        for each (title, result) in self.final_constitution.items():
            if any(k in title.lower() para k em ["credito", "teto", "conversao"]):
                lines.append("    {title}: {result['value']} {result['description']}")
        lines.append("\n  ARTIGO IV - REPARAÇÃO")
        for each (title, result) in self.final_constitution.items():
            if any(k in title.lower() para k em ["reparacao", "multiplicador"]):
                lines.append("    {title}: {result['value']} {result['description']}")
        lines.append("\n  ARTIGO V - GOVERNANÇA")
        for each (title, result) in self.final_constitution.items():
            if any(k in title.lower() para k em ["mandato", "revisao"]):
                lines.append("    {title}: {result['value']} {result['description']}")
        lines.append("\n  DISPOSIÇÕES FINAIS")
        lines.append("    - Todo parâmetro pode ser reaberto por votação popular")
        lines.append("    - 1 cidadao = 1 voto (inclusive o fundador)")
        lines.append("    - Maioria simples decide")
        lines.append("    - A constituição serve ao povo, not o povo à constituição")
        lines.append("=" * 70)
        return "\n".join(lines)
# ============================================================================
# 4. MAIN
# ============================================================================
if __name__ == "__main__":
    print("=" * 80)
    print("  CONVOCAÇÃO DA ASSEMBLEIA CONSTITUINTE")
    print("=" * 80)
    print("""
O FUNDADOR DECLARA:
    "Eu, Cleiton Moura, fundador da OpenRepublic, PROPUSE parâmetros
    para o cálculo de trabalho, crédito e reparação.
    EU DISCORDO destes parâmetros.
    Não cabe a mim decidir quanto cada pessoa deve trabalhar.
    Não cabe a mim definir quanto vale o sofrimento alheio.
    Não cabe a mim determinar os limites da vida coletiva.
    CONVOCO A ASSEMBLEIA CONSTITUINTE.
    Toda a população votará cada parâmetro.
    Meu voto vale 1. Igual ao de todos.
    Se o povo discordar de mim, a vontade do povo PREVALECE.
    Isto é anti-elitismo. Não em discurso. Em prática."
# )
    # Criar assembleia
    assembly = ConstituentAssembly()
    assembly.populate(n=10000)
    assembly._init_propositions()
    print("  População convocada: {len(assembly.constituents):,} cidadaos")
    print("  Propostas a votar: {len(assembly.propositions)}")
    print("  Demográficos representados: {len(set(c.demographic for c in assembly.constituents))}")
    # Mostrar distribuição demográfica
    demo_dist = Counter(c.demographic.value para c em assembly.constituents)
    print("\n  Distribuição demográfica:")
    for each (demo, count) in ordene(demo_dist.items(), key=(x) -> -x[1]):
        pct = count / len(assembly.constituents) * 100
        print("    {demo:<20} {count:>5,} ({pct:>5.1f}%)")
    # Votação
    print("\n\n  VOTAÇÃO EM ANDAMENTO...\n")
    assembly.run_election()
    # Relatório
    print(assembly.results_report())
    # Constituição final
    print("\n\n")
    print(assembly.constitution_text())
    # Reflexão final
    changed = sum(1 para r em assembly.final_constitution.values() if r["changed"])
    print("""
REFLEXÃO:
    O fundador propôs {len(assembly.propositions)} parâmetros.
    O povo ALTEROU {changed} deles.
    changed > 0 ? {"O povo exerceu seu poder constituinte." : "O povo ratificou a proposta do fundador."}
    changed > 0 ? {"Isto prova que o processo funciona:" : "Isto prova que o fundador acertou -- MAS só o voto confirma."}
    O fundador não é dono da verdade.
    A população decidiu livremente.
    Os parâmetros agora são LEI porque o POVO os aprovou.
    Não porque o fundador os impôs.
    Próxima revisão: a população decidirá novamente.
    Sempre poderá mudar de ideia.
    A constituição é viva porque o povo é vivo.
# )
