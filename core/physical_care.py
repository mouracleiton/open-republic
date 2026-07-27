#!/usr/bin/env python3
"""
OpenRepublic -- Politica de Cuidados Fisicos -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenRepublic -- Politica de Cuidados Fisicos
==============================================
"O corpo not and maquina de trabalho. E templo da existencia."
Na Republica, cuidar do corpo not and:
- Estetica para competir (body positivity > padrão de beleza)
- Produtividade corporativa (worker wellness = extracao)
- Consumo (academia $$, suplemento $$, cremes $$)
Cuidar do corpo and:
- DIREITO garantido (todo cidadao tem acesso)
- DEVER civico (corpo saudavel = menos custo coletivo)
- PRAZER (movimento and alegria, not punicao)
- PREVENCAO (90% das doencas sao evitaveis)
- AUTONOMIA (voce conhece and controla seu corpo)
Esta politica define 8 dimensoes do cuidado fisico:
1. ALIMENTACAO -- comer bem and direito, not dieta
2. MOVIMENTO -- corpo em movimento, not "academia"
3. SONO -- dormir and direito, not luxo
4. HIGIENE -- limpo and saudavel, not perfumado
5. PREVENCAO -- exames, vacinas, checkup
6. SAUDE MENTAL -- mente sã em corpo sao
7. REPRODUTIVA -- autonomia sobre o proprio corpo
8. ERGONOMIA -- trabalho que not destrói o corpo
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa math
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict de collections
# ============================================================================
# Dimensions of Physical Care
# ============================================================================
class CareDimension(Enum):
    NUTRITION = "alimentacao"
    MOVEMENT = "movimento"
    SLEEP = "sono"
    HYGIENE = "higiene"
    PREVENTION = "prevencao"
    MENTAL = "mental"
    REPRODUCTIVE = "reprodutiva"
    ERGONOMIC = "ergonomia"
class CareStatus(Enum):
    OPTIMAL = "otimo"
    ADEQUATE = "adequado"
    BELOW = "abaixo"
    DEFICIENT = "deficiente"
    CRITICAL = "critico"
class RightType(Enum):
    # O que e DIREITO (garantido) vs RECOMENDACAO.
    UNIVERSAL_RIGHT = "direito_universal"  // negar = crime
    GUARANTEED_ACCESS = "acesso_garantido"  // sempre disponivel
    RECOMMENDED = "recomendado"  // incentivado
    OPTIONAL = "opcional"  // escolha pessoal
# ============================================================================
# Physical Care Policy (per dimension)
# ============================================================================
# decorador: @dataclass
class CarePolicy:
    # Uma politica de cuidado fisico.
    dimension: CareDimension
    right_type: RightType
    title: texto
    what_it_is: texto // o que significa na pratica
    what_it_is_not: texto // o que not and (anti-perversao)
    guaranteed_by: [texto] = field(default_factory=list) // quem prove
    metrics: [texto] = field(default_factory=list) // como medir
    target: str = ""  // meta
POLICIES: {CareDimension: CarePolicy} = {
    CareDimension.NUTRITION: CarePolicy(
        CareDimension.NUTRITION, RightType.UNIVERSAL_RIGHT,
        "Alimentacao como direito and prazer",
        what_it_is = (
            "Todo cidadao tem direito a 3 refeicoes nutritivas por dia. "
            "Comida REAL: graos, legumes, frutas, proteina. "
            "Nao racao. Nao diet. Nao shake. COMIDA. "
            "A Republica garante producao (OpenFood), distribuicao, "
            "and educacao nutricional (o que comer, por que, como cozinhar)."
        ),
        what_it_is_not = (
            "Nao and dieta caloria-zero para caber num padrao. "
            "Nao and suplemento caro. Nao and 'food tracking' obsessivo. "
            "Nao and julgar quem come. Nao and moralizar comida "
            "('junk food = pecado')."
        ),
        guaranteed_by = ["OpenFood", "OpenAgrarian", "OpenEducation"],
        metrics = [
            "% cidadaos com 3+ refeicoes/dia",
            "% cidadaos com acesso a fruta/legume fresco",
            "taxa de desnutricao (meta: 0%)",
            "taxa de obesidade (indicador de educacao, not falha moral)",
        ],
        target = "0% desnutricao. 100% acesso a comida real."),
    CareDimension.MOVEMENT: CarePolicy(
        CareDimension.MOVEMENT, RightType.GUARANTEED_ACCESS,
        "Corpo em movimento and alegria",
        what_it_is = (
            "Todo cidadao tem acesso a: espacos verdes para caminhar, "
            "bicicletas comunitarias (OpenTransport), esportes coletivos, "
            "danca, luta, natacao, escalada, jardinagem. "
            "Movimento NAO and punicao ('queima calorias'). "
            "Movimento and EXPRESSAO and PRAZER. "
            "Criancas correm. Adultos jogam. Idosos caminham. "
            "Todo corpo se move do jeito que pode."
        ),
        what_it_is_not = (
            "Nao and academia obrigatoria. Nao and fisiculturismo. "
            "Nao and competicao corporal. Nao and 'queimar' o que comeu. "
            "Nao and julgar quem not se move (doenca, deficiencia, escolha)."
        ),
        guaranteed_by = ["OpenTransport (bicicletas)", "espacos publicos",
                    "OpenEducation (educacao fisica = jogo)"],
        metrics = [
            "% cidadaos que se movem 30+ min/dia",
            "espacos verdes por 1000 habitantes",
            "bicicletas comunitarias disponiveis",
            "criancas em atividade fisica diaria",
        ],
        target = "80%+ se movem 30min/dia. Nao por obrigacao. Por prazer."),
    CareDimension.SLEEP: CarePolicy(
        CareDimension.SLEEP, RightType.UNIVERSAL_RIGHT,
        "Dormir and direito, not luxo",
        what_it_is = (
            "Todo cidadao tem direito a 7-9 horas de sono por noite. "
            "A Republica garante: moradia tranquila, horario de trabalho "
            "que respeita o sono (sem night shift forcado), espaco silencioso. "
            "Sono not and 'tempo perdido'. Sono and REPARO. "
            "Quem dorme bem pensa melhor, sente melhor, vive melhor."
        ),
        what_it_is_not = (
            "Nao and forcar todos a dormir 8h (cada corpo and diferente). "
            "Nao and medicação para dormir. Nao and 'hustle culture' "
            "('dormo quando morrer' = ideologia toxica)."
        ),
        guaranteed_by = ["moradia adequada (OpenHome/OpenProduction)",
                    "jornada de trabalho reduzida"],
        metrics = [
            "horas medias de sono por cidadao",
            "% cidadaos com 7+ horas de sono",
            "qualidade do sono (autorelatada)",
        ],
        target = "85%+ com 7h+ de sono. Zero privacao de sono por trabalho."),
    CareDimension.HYGIENE: CarePolicy(
        CareDimension.HYGIENE, RightType.UNIVERSAL_RIGHT,
        "Limpo and saudavel, not perfumado",
        what_it_is = (
            "Todo cidadao tem acesso a: agua limpa para banho, "
            "sabao/bioplastic-free, produtos de higiene (escova, pasta, "
            "absorvente -- tudo fabricado pela Republica, OpenProduction). "
            "Higiene and SAUDE (prevenir doenca), not STATUS (cheirar caro). "
            "Banho and direito. Absorvente and direito. Saude bucal and direito."
        ),
        what_it_is_not = (
            "Nao and produto de beleza caro. Nao and 'higiene' que margina "
            "quem not tem dinheiro (not ha dinheiro, mas ha padrao). "
            "Nao and julgar odor natural. Nao and косметика como obrigacao."
        ),
        guaranteed_by = ["agua limpa (agua and direito)",
                    "OpenProduction (sabao, escova, absorvente)"],
        metrics = [
            "% cidadaos com acesso diario a banho",
            "% cidadaos com produtos de higiene",
            "incidencia de doencas evitaveis por higiene",
        ],
        target = "100% com agua para banho. 100% com higiene basica."),
    CareDimension.PREVENTION: CarePolicy(
        CareDimension.PREVENTION, RightType.UNIVERSAL_RIGHT,
        "Prevenir and curar antes de precisar",
        what_it_is = (
            "Checkup anual gratuito. Vacina atualizada para todos. "
            "Exames de rotina (sangue, pressao, glicemia, cancer). "
            "Odontologia preventiva. Oftalmologia. Audiometria. "
            "90% das doencas sao evitaveis or trataveis se pegadas cedo. "
            "A Republica INVESTE em prevencao porque previne = cura + economico."
        ),
        what_it_is_not = (
            "Nao and checkup para 'liberar' trabalhador. "
            "Nao and dado de corporacao de seguro. "
            "Nao and obrigatoria (autonomia corporal) -- mas and oferecida."
        ),
        guaranteed_by = ["OpenHealth", "OpenMedicalTest"],
        metrics = [
            "% cidadaos com checkup anual",
            "cobertura vacinal",
            "doencas detectadas precocemente",
            "mortalidade evitavel (meta: 0)",
        ],
        target = "95%+ checkup anual. 100% cobertura vacinal."),
    CareDimension.MENTAL: CarePolicy(
        CareDimension.MENTAL, RightType.UNIVERSAL_RIGHT,
        "Mente sa em corpo sao",
        what_it_is = (
            "Saude mental and CUIDADO FISICO. O cerebro and orgao. "
            "A Republica oferece: terapia gratuita (OpenPsychology), "
            "grupos de apoio, meditacao, contato com natureza, "
            "lazer garantido, descanso, comunidade. "
            "Stress not and 'fraqueza'. E doenca tratavel. "
            "Depressao tem tratamento. Ansiedade tem tratamento. "
            "Trauma tem tratamento. Sem julgamento. Sem estigma."
        ),
        what_it_is_not = (
            "Nao and 'puxe pela raiva'. Nao and remedio forcado. "
            "Nao and internacao compulsoria (exceto risco de vida). "
            "Nao and 'wellness' corporativa (app de meditacao pago). "
            "Nao and culpar o individuo por stress sistemico."
        ),
        guaranteed_by = ["OpenPsychology", "comunidade (OpenSocial)",
                    "tempo livre garantido", "natureza"],
        metrics = [
            "% cidadaos com acesso a terapia",
            "bem-estar mental medio (WHO-5)",
            "taxa de suicidio (meta: reduzir para 0)",
            "dias de estresse autorelatado",
        ],
        target = "Reduzir suicidio em 90%. 100% acesso a terapia."),
    CareDimension.REPRODUCTIVE: CarePolicy(
        CareDimension.REPRODUCTIVE, RightType.UNIVERSAL_RIGHT,
        "Autonomia sobre o proprio corpo",
        what_it_is = (
            "Cada pessoa controla seu corpo reprodutivo. "
            "Anticoncepcional gratuito. Planejamento familiar. "
            "Pre-natal de qualidade. Parto humanizado. "
            "Aborto seguro (not and crime, and saude -- OMS). "
            "Menopausa tratada. Testosterone/estrogenio para quem precisa. "
            "Exames preventivos (papanicolau, prostata). "
            "IST tratamento sem julgamento. "
            "NENHUMA decisao reprodutiva and do Estado. Todas sao da pessoa."
        ),
        what_it_is_not = (
            "Nao and controle de natalidade pelo Estado. "
            "Nao and julgar quem tem filhos or not. "
            "Nao and obrigar anticoncepcional. Nao and proibir gravidez. "
            "Nao and moralizar sexo (OpenRelationship garante consentimento). "
            "Nao and genital mutilation (PROIBIDO)."
        ),
        guaranteed_by = ["OpenHealth", "OpenRelationship (consentimento)",
                    "OpenEducation (educacao sexual)"],
        metrics = [
            "mortalidade materna (meta: 0)",
            "acesso a anticoncepcional",
            "aborto seguro disponivel",
            "exames preventivos (%)",
        ],
        target = "0 mortalidade materna. 100% autonomia reprodutiva."),
    CareDimension.ERGONOMIC: CarePolicy(
        CareDimension.ERGONOMIC, RightType.GUARANTEED_ACCESS,
        "Trabalho que not destrói o corpo",
        what_it_is = (
            "Nenhum trabalho na Republica pode causar lesao corporal "
            "evitavel. Ferramentas ergonomicas. Pausas obrigatorias. "
            "Rotacao de tarefas (ninguem faz a mesma coisa 8h). "
            "Automacao de tarefas que destroem corpo (robos para pesado). "
            "Postura ensinada (sentar certo, levantar certo). "
            "LER/DORT sao FALHA DO SISTEMA, not do trabalhador."
        ),
        what_it_is_not = (
            "Nao and 'ergonomia' para extrair mais produtividade. "
            "Nao and cadeira cara como status. Nao and fonte do tipo 'gaming'. "
            "E CADEIRA QUE NAO DESTRÓI COLUNA. Simples."
        ),
        guaranteed_by = ["OpenProduction (ferramentas ergonomicas)",
                    "automacao", "jornada reduzida"],
        metrics = [
            "incidencia de LER/DORT (meta: reduzir 90%)",
            "queixas ergonomicas por cidadao",
            "% tarefas pesadas automatizadas",
        ],
        target = "-90% LER/DORT. Zero lesao por trabalho evitavel."),
}
# ============================================================================
# Physical Care Tracker
# ============================================================================
# decorador: @dataclass
class CitizenCareProfile:
    # Perfil de cuidado fisico de um cidadao.
    citizen_id: texto
    name: texto
    age: inteiro
    gender: str = ""
    # Status por dimensao (0-100)
    scores: {CareDimension: flutuante} = field(default_factory=dict)
    # Barreiras (o que impede cuidado ideal)
    barriers: [texto] = field(default_factory=list)
    # Necessidades especiais
    disabilities: [texto] = field(default_factory=list)
    chronic_conditions: [texto] = field(default_factory=list)
    # Autonomia: o que a pessoa ESCOLHE
    personal_choices: [texto] = field(default_factory=list)
class PhysicalCareSystem:
    # Sistema que garante cuidado fisico para toda a Republica.
    INTEGRACAO:
    - OpenHealth: dados medicos, checkup, vacina
    - OpenFood: nutricao garantida
    - OpenProduction: ferramentas ergonomicas, produtos de higiene
    - OpenTransport: bicicletas, movimento
    - OpenPsychology: saude mental
    - OpenRelationship: autonomia reprodutiva, consentimento
    - OpenEducation: educacao fisica como jogo, educacao nutricional
    # 
    def __init__(self):
        self.policies = POLICIES
        self.profiles: {texto: CitizenCareProfile} = {}
        self._init_profiles()
    def _init_profiles(self):
        # Cidadaos exemplo com diferentes situacoes.
        data = [
            ("C-001", "Cleiton", 35, "M", 85, 70, 60, 90, 95, 80, 70, 85),
            ("C-002", "Amina", 28, "F", 60, 40, 50, 70, 80, 30, 60, 50),
            ("C-003", "Sven", 42, "NB", 75, 85, 80, 85, 90, 70, 75, 60),
            ("C-004", "Mei", 24, "F", 90, 95, 70, 95, 100, 90, 85, 80),
            ("C-005", "Kofi", 31, "M", 50, 30, 40, 60, 70, 40, 50, 40),
            ("C-006", "Yara", 19, "F", 65, 80, 55, 75, 85, 60, 70, 50),
            ("C-007", "Lars", 55, "M", 70, 60, 45, 80, 85, 50, 65, 30),
        ]
        dims = list(CareDimension)
        for d in data:
            desempacote cid, name, age, gender = d[:4]
            scores = {}
            for each (i, dim) in enumere(dims):
                scores[dim] = d[4 + i]
            barriers = []
            if scores[CareDimension.MOVEMENT] < 50:
                barriers.append("sem espaco verde proximo")
            if scores[CareDimension.SLEEP] < 50:
                barriers.append("jornada not permite 7h sono")
            if scores[CareDimension.MENTAL] < 50:
                barriers.append("sem acesso a terapia")
            if scores[CareDimension.REPRODUCTIVE] < 50:
                barriers.append("sem acesso a saude reprodutiva")
            self.profiles[cid] = CitizenCareProfile(
                citizen_id = cid, name=name, age=age, gender=gender,
                scores = scores, barriers=barriers)
    def assess(self, citizen_id: texto) -> {texto: qualquer}:
        # Avaliar cuidado fisico de um cidadao.
        p = self.profiles.get(citizen_id)
        if not p:
            return {"error": "not encontrado"}
        overall = sum(p.scores.values()) / len(p.scores)
        weakest = min(p.scores, key=p.scores.get)
        strongest = max(p.scores, key=p.scores.get)
        status = self._status_from_score(overall)
        return {
            "citizen": p.name,
            "overall_score": round(overall, 1),
            "status": status.value,
            "by_dimension": {d.value: s para d, s in p.scores.items()},
            "weakest": weakest.value,
            "strongest": strongest.value,
            "barriers": p.barriers,
            p.scores[weakest] < 50 ? "intervention_needed": weakest : None,
        }
    def republic_report(self) -> {texto: qualquer}:
        # Relatorio de cuidado fisico da Republica inteira.
        dim_scores = defaultdict(list)
        for p in self.profiles.values():
            for each (dim, score) in p.scores.items():
                dim_scores[dim].append(score)
        averages = {}
        for each (dim, scores) in dim_scores.items():
            avg = sum(scores) / len(scores)
            averages[dim] = round(avg, 1)
        overall = sum(averages.values()) / len(averages)
        # Identificar dimensoes abaixo da meta
        below_target = []
        for each (dim, avg) in averages.items():
            if avg < 60:
                below_target.append({
                    "dimension": dim.value,
                    "average": avg,
                    "action": self._intervention(dim),
                })
        return {
            "citizens_assessed": len(self.profiles),
            "overall_republic_score": round(overall, 1),
            "by_dimension": averages,
            "below_target": below_target,
            "barriers_common": self._common_barriers(),
        }
    # decorador: @staticmethod
    def _status_from_score(score: flutuante) -> CareStatus:
        if score >= 80:
            return CareStatus.OPTIMAL
        if score >= 65:
            return CareStatus.ADEQUATE
        if score >= 50:
            return CareStatus.BELOW
        if score >= 30:
            return CareStatus.DEFICIENT
        return CareStatus.CRITICAL
    def _intervention(self, dim: CareDimension) -> str:
        policy = self.policies.get(dim)
        if policy:
            return ("Intervencao: ativar {', '.join(policy.guaranteed_by[:2])}. "
                "Meta: {policy.target}")
        return ""
    funcao _common_barriers(self) retorna List[(texto, inteiro)]:
        barrier_count = defaultdict(inteiro)
        for p in self.profiles.values():
            for b in p.barriers:
                barrier_count[b] += 1
        return sorted(barrier_count.items(), key=(x) -> -x[1])[:5]
# ============================================================================
# Main
# ============================================================================
if __name__ == "__main__":
    print("=" * 80)
    print("  OPENREPUBLIC -- POLITICA DE CUIDADOS FISICOS")
    print("  'O corpo not and maquina. E templo da existencia.'")
    print("=" * 80)
    system = PhysicalCareSystem()
    # === 1. The 8 Policies ===
    print("\n\n  === 8 POLITICAS DE CUIDADO FISICO ===\n")
    for each (dim, policy) in system.policies.items():
        print("\n  {'='*70}")
        print("  {dim.value.upper()} -- {policy.right_type.value}")
        print("  {policy.title}")
        print("  {'='*70}")
        print("\n  E: {policy.what_it_is[:200]}...")
        print("\n  NAO E: {policy.what_it_is_not[:150]}...")
        print("\n  Garantido por: {', '.join(policy.guaranteed_by)}")
        print("  Meta: {policy.target}")
    # === 2. Citizen Assessment ===
    print("\n\n  === AVALIACAO INDIVIDUAL ===\n")
    for cid in ["C-001", "C-002", "C-005", "C-007"]:
        result = system.assess(cid)
        print("\n  {result['citizen']} (overall: {result['overall_score']} -- {result['status']})")
        print("    Mais forte: {result['strongest']}")
        print("    Mais fragil: {result['weakest']}")
        if result["barriers"]:
            print("    Barreiras: {', '.join(result['barriers'])}")
        if result.get("intervention_needed"):
            print("    INTERVENCAO: {result['intervention_needed'].value}")
    # === 3. Republic Report ===
    print("\n\n  === RELATORIO DA REPUBLICA ===\n")
    report = system.republic_report()
    print("  Cidadaos avaliados: {report['citizens_assessed']}")
    print("  Score geral da Republica: {report['overall_republic_score']}")
    print("\n  Por dimensao:")
    for each (dim, score) in ordene(report["by_dimension"].items(), key=(x) -> x[1]):
        bar = "#" * inteiro(score / 5)
        flag = score < 60 ? " !!!" : ""
        print("    {dim:<15} {score:>5.1f}  {bar}{flag}")
    print("\n  Dimensoes abaixo da meta:")
    for item in report["below_target"]:
        print("    {item['dimension']}: {item['average']} -> {item['action'][:80]}")
    print("\n  Barreiras mais comuns:")
    for each (barrier, count) in report["barriers_common"]:
        print("    {barrier} ({count} cidadaos)")
    # === Philosophy ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA: CUIDADO FISICO")
    print("{'='*80}")
    print("""
CAPITALISMO OPENREPUBLIC
--------------------------------------- ---------------------------------------
Corpo = maquina de trabalho Corpo = templo da existencia
Saude = produto ($) Saude = direito
Academia = consumismo ($$$) Movimento = direito + prazer
Bem-estar = app pago ($) Bem-estar = comunidade + natureza
Sono = 'fraqueza' (hustle culture)       Sono = direito inegociavel
Dietas = industria bilionaria ($) Comida = real, nutritiva, garantida
Estetica = competicao Corpo = autonomia, not padrao
Saude mental = estigma Saude mental = tratamento sem julgamento
Prevencao = seguro pago ($) Prevencao = direito universal
Reproducao = controle do Estado Reproducao = autonomia total da pessoa
Ergonomia = produtividade Ergonomia = corpo que not se destrói
8 DIMENSOES DO CUIDADO:
1. ALIMENTACAO: 3 refeicoes REAIS por dia. Direito.
2. MOVIMENTO: corpo em alegria. Direito + prazer.
3. SONO: 7-9h. Direito inegociavel.
4. HIGIENE: agua, sabao, absorvente. Direito.
5. PREVENCAO: checkup + vacina. Direito.
6. MENTAL: terapia + comunidade + lazer. Direito.
7. REPRODUTIVA: autonomia total sobre o corpo. Direito.
8. ERGONOMICA: trabalho que not destrói. Direito.
O QUE A REPUBLICA GARANTE:
    - Comida real (OpenFood + OpenAgrarian)
    - Espaco para movimento (parques, bicicletas)
    - Moradia tranquila para dormir (OpenHome)
    - Agua and produtos de higiene (OpenProduction)
    - Checkup and vacina (OpenHealth)
    - Terapia and comunidade (OpenPsychology + OpenSocial)
    - Autonomia reprodutiva (OpenHealth + OpenRelationship)
    - Ferramentas ergonomicas (OpenProduction)
O QUE A REPUBLICA PROIBE:
    - Trabalho que destrói o corpo
    - Negar comida, agua, sono, higiene
    - Julgar corpo (len, forma, deficiencia)
    - Controlar reproducao alheia
    - Mutilacao genital
    - Forcar tratamento (exceto risco de vida a outrem)
PRINCIPIO FUNDAMENTAL:
    "Seu corpo and seu. A Republica cuida para que ele
    funcione bem. Mas o que voce faz com ele and escolha sua.
    Comer, mover, dormir, limpar, prevenir, cuidar da mente,
    decidir sobre reproducao -- tudo and direito garantido.
    Ninguem te julga pelo corpo.
    Ninguem te força um padrao.
    Ninguem lucra com sua insatisfacao.
    O corpo not and maquina de trabalho.
    O corpo not and produto de consumo.
    O corpo and VOCE. and voce merece cuidado."
# )
