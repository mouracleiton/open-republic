# OpenCredit -- Sistema de Credito Democratico

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_credit.py`

**Descricao:** ==============================================
RESOLVENDO A TENSAO FUNDAMENTAL:
  Sociedade sem moeda precisa de algum criterio para alocar o que e ESCASSO.
  Mas credito que acumula vira dinheiro. Dinheiro vira propriedade.
  Propriedade recria desigualdade.
SOLUCAO: Credito que NAO e moeda.
  1. O QUE NAO PRECISA DE CREDITO (direito garantido, sempre):
     Comida, agua, moradia, saude, educacao, transporte basico.
     Voce nao "gasta" credito. Voce ACESSE. Ponto.
  2. O QUE PRECISA DE CREDITO (bens escassos/nao-essenciais):
     Instrumentos musicais, equipamento esportivo, viagens,
     eletronicos especializados, ferramentas avancadas.
  3. CREDITO NAO E MOEDA PORQUE:
     (a) Nao acumula -- expira todo ciclo
     (b) Nao transfere -- voce nao pode dar pra outro
     (c) Nao herda -- morreu, zerou
     (d) Nao compra essenciais -- essencial e direito
     (e) Nao gera juros -- guardar nao da nada
     (f) Distribuicao e democratica -- TODOS decidem quanto cada um recebe
     (g) Baseado em contribuicao reconhecida pela comunidade
  4. COMO SE GANHA CREDITO:
     Trabalho reconhecido pela comunidade.
     Nao e "salario" -- e reconhecimento de contribuicao.
     Quem contribui mais, recebe mais credito de acesso.
     Mas o teto e baixo -- ninguem acumula fortuna.
     E o minimo garante dignidade -- ninguem fica sem.
  5. QUEM DECIDE QUANTO CADA UM RECEBE:
     A COMUNIDADE INTEIRA. Por votacao democratica direta.
     Nao e um comite. Nao e um algoritmo. Sao as pessoas.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenCredit -- Sistema de Credito Democratico
==============================================

RESOLVENDO A TENSAO FUNDAMENTAL:
  Sociedade sem moeda precisa de algum criterio para alocar o que e ESCASSO.
  Mas credito que acumula vira dinheiro. Dinheiro vira propriedade.
  Propriedade recria desigualdade.

SOLUCAO: Credito que nao e moeda.

  1. O QUE nao PRECISA DE CREDITO (direito garantido, sempre):
     Comida, agua, moradia, saude, educacao, transporte basico.
     Voce nao "gasta" credito. Voce ACESSE. Ponto.

  2. O QUE PRECISA DE CREDITO (bens escassos/nao-essenciais):
     Instrumentos musicais, equipamento esportivo, viagens,
     eletronicos especializados, ferramentas avancadas.

  3. CREDITO nao e MOEDA PORQUE:
     (a) Nao acumula -- expira todo ciclo
     (b) Nao transfere -- voce nao pode dar pra outro
     (c) Nao herda -- morreu, zerou
     (d) Nao compra essenciais -- essencial e direito
     (e) Nao gera juros -- guardar nao da nada
     (f) Distribuicao e democratica -- TODOS decidem quanto cada um recebe
     (g) Baseado em contribuicao reconhecida pela comunidade

  4. COMO SE GANHA CREDITO:
     Trabalho reconhecido pela comunidade.
     Nao e "salario" -- e reconhecimento de contribuicao.
     Quem contribui mais, recebe mais credito de acesso.
     Mas o teto e baixo -- ninguem acumula fortuna.
     e o minimo garante dignidade -- ninguem fica sem.

  5. QUEM DECIDE QUANTO CADA UM RECEBE:
     A COMUNIDADE INTEIRA. Por votacao democratica direta.
     Nao e um comite. Nao e um algoritmo. Sao as pessoas.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa numpy as np


// ============================================================================
// Enums
// ============================================================================

classe AccessTier herda de Enum:
    // Niveis de acesso a bens na Republica.
    GUARANTEED = "guaranteed"  // direito -- SEMPRE, sem credito
    STANDARD = "standard"  // cotas iguais para todos
    CREDIT = "credit"  // precisa de credito (escasso)
    LOTTERY = "lottery"  // tao escasso que sorteio
    COLLECTIVE = "collective"  // bem compartilhado (nao individual)


classe ContributionType herda de Enum:
    FOOD_PRODUCTION = "food_production"
    CONSTRUCTION = "construction"
    HEALTHCARE = "healthcare"
    EDUCATION = "education"
    CHILDCARE = "childcare"
    ELDER_CARE = "elder_care"
    MAINTENANCE = "maintenance"  // reparo de bens comuns
    RECYCLING = "recycling"
    RESEARCH = "research"
    ART = "art"
    ORGANIZATION = "organization"  // governance, mediacao
    TRANSPORT = "transport"
    SECURITY = "security"
    CLEANING = "cleaning"
    INNOVATION = "innovation"  // criar novo design/blueprint
    STEWARDSHIP = "stewardship"  // cuidar de ecossistemas


// ============================================================================
// The Catalog: what needs credit and what doesn't
// ============================================================================

// decorador: @dataclass
classe GoodOrService:
    // Um bem ou servico na Republica.
    name: texto
    tier: AccessTier
    seja credit_cost: flutuante = 0.0 // 0 para garantidos
    seja description: texto = ""
    seja category: texto = ""
    seja scarce: logico = falso // oferta limitada?


// O que cada tier significa:
CATALOG = [
    // === GARANTIDOS (sem credito, direito) ===
    GoodOrService("Comida basica (3 refeicoes)", AccessTier.GUARANTEED, 0,
                  "Direito fundamental. Sem credito. Sem fila. Acesso livre."),
    GoodOrService("Agua potavel", AccessTier.GUARANTEED, 0,
                  "Direito fundamental."),
    GoodOrService("Moradia (unidade familiar)", AccessTier.GUARANTEED, 0,
                  "Direito fundamental. Unidade designada pela comunidade."),
    GoodOrService("Atendimento medico", AccessTier.GUARANTEED, 0,
                  "Direito fundamental. Sem credito."),
    GoodOrService("Educacao (basica + continuada)", AccessTier.GUARANTEED, 0,
                  "Direito fundamental."),
    GoodOrService("Transporte publico", AccessTier.GUARANTEED, 0,
                  "Direito fundamental. Onibus/trem comunitario."),
    GoodOrService("Internet (50 GB/mes)", AccessTier.GUARANTEED, 0,
                  "Direito fundamental. Acesso digital basico."),
    GoodOrService("Energia (consumo basico)", AccessTier.GUARANTEED, 0,
                  "Direito fundamental. 300 kWh/mes."),
    GoodOrService("Roupas basicas", AccessTier.STANDARD, 0,
                  "Cota: 8 pecas/ano para todos. Sem credito."),
    GoodOrService("Cuidado infantil", AccessTier.GUARANTEED, 0,
                  "Direito. Creche comunitaria."),
    GoodOrService("Cuidado de idosos", AccessTier.GUARANTEED, 0,
                  "Direito."),

    // === CREDITO (bens escassos / nao-essenciais) ===
    GoodOrService("Instrumento musical", AccessTier.CREDIT, 10,
                  "Bem escasso. Precisa de credito de acesso."),
    GoodOrService("Equipamento esportivo", AccessTier.CREDIT, 8,
                  "Bem escasso."),
    GoodOrService("Eletronico pessoal (tablet)", AccessTier.CREDIT, 15,
                  "Acima do terminal burro comunitario."),
    GoodOrService("Viagem inter-nacao", AccessTier.CREDIT, 20,
                  "Transporte para outra nacao da Republica."),
    GoodOrService("Comida especial (restaurante)", AccessTier.CREDIT, 5,
                  "Refeicao preparada por chef (nao essencial)."),
    GoodOrService("Curso especializado (certificacao)", AccessTier.CREDIT, 12,
                  "Alem da educacao basica garantida."),
    GoodOrService("Arte/Decoracao para casa", AccessTier.CREDIT, 6,
                  "Bem nao-essencial."),
    GoodOrService("Bicicleta pessoal", AccessTier.CREDIT, 14,
                  "Alem do transporte publico."),
    GoodOrService("Hobby/colecionavel", AccessTier.CREDIT, 5,
                  "Bem nao-essencial."),
    GoodOrService("Animal de estimacao", AccessTier.CREDIT, 18,
                  "Requer credito + avaliacao de capacidade de cuidado."),
    GoodOrService("Festa/evento privado", AccessTier.CREDIT, 8,
                  "Evento pessoal (festas publicas sao gratis)."),

    // === COLETIVOS (compartilhados, sem credito individual) ===
    GoodOrService("Laboratorio/FabLab", AccessTier.COLLECTIVE, 0,
                  "Bem comum. Acesso agendado por todos."),
    GoodOrService("Veiculo compartilhado", AccessTier.COLLECTIVE, 0,
                  "Bem comum. Agendamento."),
    GoodOrService("Espaco para evento", AccessTier.COLLECTIVE, 0,
                  "Bem comum. Reserva."),
    GoodOrService("Ferramentas especializadas", AccessTier.COLLECTIVE, 0,
                  "Bem comum. Banco de ferramentas."),
]


// ============================================================================
// Credit Account (NOT a wallet -- access credits, not money)
// ============================================================================

// decorador: @dataclass
classe CreditAccount:
    // Conta de credito de acesso.

    DIFERENCA FUNDAMENTAL DE WALLET/DINHEIRO:
    - Nao acumula (expira todo ciclo)
    - Nao transfere (nao pode dar pra ninguem)
    - Nao compra essenciais (essencial e direito)
    - Nao gera juros
    - Nao e heranca
    // 
    citizen_id: texto
    name: texto
    seja current_credits: flutuante = 0.0
    seja credits_this_cycle: flutuante = 0.0
    seja credits_spent: flutuante = 0.0
    seja credits_expired: flutuante = 0.0 // nao usados, expiraram
    seja contribution_hours: flutuante = 0.0
    seja contributions: List[(ContributionType, flutuante)] = field(default_factory=list)
    seja community_recognition: flutuante = 0.0 // avaliacao pelos pares
    seja cycle: inteiro = 0 // ciclo atual

    // decorador: @property
    funcao can_spend(self) -> flutuante:
        // Quanto pode gastar neste ciclo.
        retorne maximo(0, self.current_credits)

    funcao spend(self, amount: flutuante, good_name: texto) -> {texto: qualquer}:
        // Gastar credito num bem.
        se amount > self.current_credits entao:
            retorne {"success": falso, "reason": "Crédito insuficiente",
                    "available": self.current_credits, "needed": amount}
        self.current_credits -= amount
        self.credits_spent += amount
        retorne {"success": verdadeiro, "good": good_name, "spent": amount,
                "remaining": self.current_credits}

    funcao end_cycle(self) -> {texto: qualquer}:
        // Fim do ciclo: creditos NAO usados EXPIRAM.
        expired = self.current_credits
        self.credits_expired += expired
        self.current_credits = 0
        retorne {"expired": expired, "total_expired_lifetime": self.credits_expired}


// ============================================================================
// Democratic Credit Allocator
// ============================================================================

// decorador: @dataclass
classe Citizen:
    // Cidadao da Republica.
    citizen_id: texto
    name: texto
    age: inteiro
    seja skills: [texto] = field(default_factory=list)
    seja account: CreditAccount = field(default_factory=() -> CreditAccount("", ""))


classe DemocraticCreditSystem:
    // Sistema onde TODOS decidem a distribuicao de credito.

    COMO FUNCIONA (ciclo mensal):

    1. FASE DE CONTRIBUICAO (semana 1-3)
       Cada cidadao trabalha na comunidade. O trabalho e registrado.
       Horas, tipo, e impacto sao documentados publicamente.

    2. FASE DE RECONHECIMENTO (semana 4)
       A comunidade avalia as contribuicoes de cada membro.
       Nao e so "quantas horas" -- e "quanto impactou".
       Reconhecimento por pares (peer recognition).

    3. FASE DE PROPOSTA DE CREDITO (semana 4)
       A comunidade propoe como distribuir o POOL de creditos do ciclo.
       Opcoes:
       (a) Igual para todos (cada um recebe X)
       (b) Ponderado por contribuicao (quem contribuiu mais, recebe mais)
       (c) Ponderado por necessidade (quem tem projeto util, recebe mais)
       (d) Hibrido: base igual + bonus por contribuicao

    4. FASE DE VOTACAO (semana 4)
       TODOS votam na proposta de distribuicao.
       Democracia direta. Maioria simples.

    5. DISTRIBUICAO
       Creditos aparecem nas contas.
       Validos apenas pelo proximo ciclo.
       Nao usados = expiram (nao acumulam).
    // 

    funcao __init__(self, pool_per_cycle: flutuante = 1000.0):
        self.citizens: {texto: Citizen} = {}
        self.pool_per_cycle = pool_per_cycle // pool total de creditos por ciclo
        self.cycle = 0
        self.distribution_history: [Dict] = []
        self.min_credit = 5.0 // nenhum cidadao recebe menos que isso
        self.max_credit = 50.0 // nenhum cidadao recebe mais que isso
        self.contribution_weights = {
            // PRINCIPIO: O valor da contribuicao = IMPACTO medido.
            // Nao existe funcao melhor que outra. Mas existe impacto diferente.
            // Quem ensina 100 pessoas multiplica conhecimento (macro impacto).
            // Quem limpa o esgoto evita doenca em 1000 pessoas (macro impacto).
            // Quem faz 1 cirurgia salva 1 vida (micro impacto altissimo).
            // Quem planta comida alimenta 500 pessoas (micro+macro).
            // O peso NAO e fixo por tipo -- e calculado pelo IMPACTO REAL.
            // Pesos base sao ponto de partida, ajustados por people_impacted.
            ContributionType.FOOD_PRODUCTION: 1.0,
            ContributionType.CONSTRUCTION: 1.0,
            ContributionType.HEALTHCARE: 1.0,
            ContributionType.EDUCATION: 1.0, // multiplicado por alunos x geracoes
            ContributionType.CHILDCARE: 1.0,
            ContributionType.ELDER_CARE: 1.0,
            ContributionType.MAINTENANCE: 1.0,
            ContributionType.RECYCLING: 1.0,
            ContributionType.RESEARCH: 1.0, // multiplicado por descoberta x aplicacao
            ContributionType.ART: 1.0,
            ContributionType.ORGANIZATION: 1.0,
            ContributionType.TRANSPORT: 1.0,
            ContributionType.SECURITY: 1.0,
            ContributionType.CLEANING: 1.0,
            ContributionType.INNOVATION: 1.0, // multiplicado por adocao
            ContributionType.STEWARDSHIP: 1.0,
        }

    funcao add_citizen(self, citizen: Citizen):
        citizen.account.citizen_id = citizen.citizen_id
        citizen.account.name = citizen.name
        self.citizens[citizen.citizen_id] = citizen

    funcao register_contribution(self, citizen_id: texto,
                              ctype: ContributionType, hours: flutuante,
                              seja people_impacted: inteiro = 1,
                              seja ripple_factor: flutuante = 1.0):
        // Registrar contribuicao de um cidadao.

        O valor da contribuicao e medido pelo IMPACTO:
        - people_impacted: quantas pessoas foram diretas/indiretamente afetadas
        - ripple_factor: multiplicador de propagacao
          (ensinar = 10x porque cada aluno ensina outros)
          (pesquisa = 5x porque cada descoberta se aplica a muitos)
          (cirurgia = 1x mas salva vida, impacto altissimo por pessoa)

        Exemplos:
          Medico cirurgiao: 1 cirurgia, 1 pessoa, ripple 1x -> impacto 1 (VIDA)
          Professor: 4h aula, 30 alunos, ripple 10x -> impacto 300
          Agricultor: 8h, 500 pessoas alimentadas, ripple 1x -> impacto 500
          Faxineiro: 8h, 200 pessoas usam o espaco, ripple 2x (evita doenca) -> 400
          Pesquisador: 8h, descoberta que pode ajudar milhoes, ripple 100x
        // 
        c = self.citizens.get(citizen_id)
        se nao c entao:
            retorne nulo
        base_weight = self.contribution_weights.get(ctype, 1.0)
        // Impacto = base x pessoas afetadas x fator de propagacao
        impact = base_weight * hours * (1 + math.log10(maximo(1, people_impacted)) * ripple_factor)
        weighted = impact
        c.account.contribution_hours += hours
        c.account.contributions.append((ctype, weighted))
        c.account.community_recognition += weighted

    funcao run_cycle(self) -> {texto: qualquer}:
        // Executar um ciclo completo de credito democratico.
        self.cycle += 1
        n = tamanho(self.citizens)
        se n == 0 entao:
            retorne {"error": "no citizens"}

        // 1. Expirar creditos do ciclo anterior
        expired_total = 0
        para cada c em self.citizens.values():
            exp = c.account.end_cycle()
            expired_total = expired_total + exp["expired"]

        // 2. Calcular contribuicao ponderada de cada cidadao
        contributions = {}
        para cada (cid, c) em self.citizens.items():
            weighted_sum = soma(w para _, w in c.account.contributions)
            contributions[cid] = {
                "name": c.name,
                "hours": c.account.contribution_hours,
                "weighted": weighted_sum,
                "recognition": c.account.community_recognition,
            }

        total_weighted = soma(d["weighted"] para d em contributions.values())  ou  1

        // 3. Propostas de distribuicao (a comunidade escolhe)
        proposals = self._generate_proposals(contributions, total_weighted)

        // 4. Simular votacao democratica
        winning_proposal = self._simulate_vote(proposals)

        // 5. Distribuir
        distribution = winning_proposal["distribution"]
        para cada (cid, credits) em distribution.items():
            c = self.citizens[cid]
            c.account.current_credits = credits
            c.account.credits_this_cycle = credits
            c.account.cycle = self.cycle

        // Reset contributions for next cycle
        para cada c em self.citizens.values():
            c.account.contributions = []

        result = {
            "cycle": self.cycle,
            "pool_total": self.pool_per_cycle,
            "citizens": n,
            "expired_from_last_cycle": arredonde(expired_total, 1),
            "proposals_voted": tamanho(proposals),
            "winning_proposal": winning_proposal["name"],
            "winning_description": winning_proposal["description"],
            "distribution": {contributions[cid]["name"]: arredonde(cr, 1)
                            para cid, cr in distribution.items()},
            "min_given": arredonde(minimo(distribution.values()), 1),
            "max_given": arredonde(maximo(distribution.values()), 1),
            "avg_given": arredonde(np.mean(list(distribution.values())), 1),
            "expired_pct": arredonde(expired_total / maximo(self.pool_per_cycle, 1) * 100, 1),
        }
        self.distribution_history.append(result)
        retorne result

    funcao _generate_proposals(self, contributions: Dict, total_weighted: flutuante) -> [Dict]:
        // Gerar propostas de distribuicao para votacao.
        n = tamanho(contributions)
        proposals = []

        // Proposta A: Igual para todos
        equal_share = self.pool_per_cycle / n
        equal_dist = {cid: arredonde(minimo(self.max_credit,
                            maximo(self.min_credit, equal_share)), 1)
                     para cid em contributions}
        proposals.append({
            "name": "Igualitario",
            "description": "Cada cidadao recebe {equal_share:.1f} creditos. "
                          "Igualdade absoluta independentemente de contribuicao.",
            "distribution": equal_dist,
        })

        // Proposta B: Ponderado por contribuicao
        weighted_dist = {}
        para cada (cid, data) em contributions.items():
            share = (data["weighted"] / total_weighted) * self.pool_per_cycle
            share = minimo(self.max_credit, maximo(self.min_credit, share))
            weighted_dist[cid] = arredonde(share, 1)
        proposals.append({
            "name": "Por Contribuicao",
            "description": "Quem contribuiu mais recebe mais. Teto e piso garantidos. "
                          "Diferenca maxima de 3x entre quem mais e menos recebe.",
            "distribution": weighted_dist,
        })

        // Proposta C: Hibrido (base igual + bonus)
        base = self.min_credit
        bonus_pool = self.pool_per_cycle - (base * n)
        hybrid_dist = {}
        para cada (cid, data) em contributions.items():
            bonus = (data["weighted"] / total_weighted) * bonus_pool
            total = minimo(self.max_credit, base + bonus)
            hybrid_dist[cid] = arredonde(total, 1)
        proposals.append({
            "name": "Hibrido (base + bonus)",
            "description": "Todos recebem base de {base:.0f}. Bonus por contribuicao "
                          "sobre o restante. Equilibra igualdade e incentivo.",
            "distribution": hybrid_dist,
        })

        retorne proposals

    funcao _simulate_vote(self, proposals: [Dict]) -> Dict:
        // Simular votacao democratica.

        Em operacao real, cada cidadao vota diretamente.
        Aqui simulamos baseado em auto-interesse + principio.
        // 
        votes = [0] * tamanho(proposals)
        para cada c em self.citizens.values():
            // Cada cidadao vota na proposta que mais o beneficia
            // MAS com 30% de chance vota por principio (igualitario)
            se random.random() < 0.30 entao:
                votes[0] += 1 // igualitario por principio
            senao:
                best_proposal = 0
                best_credits = 0
                para cada (i, p) em enumere(proposals):
                    credits = p["distribution"].get(c.citizen_id, 0)
                    se credits > best_credits entao:
                        best_credits = credits
                        best_proposal = i
                votes[best_proposal] += 1

        winner_idx = votes.index(maximo(votes))
        proposals[winner_idx]["votes"] = votes[winner_idx]
        proposals[winner_idx]["vote_counts"] = votes
        retorne proposals[winner_idx]

    funcao access_good(self, citizen_id: texto, good_name: texto) -> {texto: qualquer}:
        // Cidadao tenta acessar um bem.
        c = self.citizens.get(citizen_id)
        se nao c entao:
            retorne {"error": "citizen not found"}

        good = next((g para g em CATALOG if good_name.lower() in g.name.lower()), nulo)
        se nao good entao:
            retorne {"error": "good not found"}

        // Garantido: sem credito
        se good.tier == AccessTier.GUARANTEED entao:
            retorne {
                "citizen": c.name,
                "good": good.name,
                "access": "GRANTED",
                "cost": 0,
                "reason": "Direito fundamental. Sem credito necessario.",
            }

        // Coletivo: sem credito, so agendar
        se good.tier == AccessTier.COLLECTIVE entao:
            retorne {
                "citizen": c.name,
                "good": good.name,
                "access": "GRANTED (agendar)",
                "cost": 0,
                "reason": "Bem comum. Agendar uso.",
            }

        // Standard: cota igual
        se good.tier == AccessTier.STANDARD entao:
            retorne {
                "citizen": c.name,
                "good": good.name,
                "access": "GRANTED (cota)",
                "cost": 0,
                "reason": "Cota igual para todos.",
            }

        // Credito: precisa gastar
        se good.tier == AccessTier.CREDIT entao:
            result = c.account.spend(good.credit_cost, good.name)
            retorne {
                "citizen": c.name,
                "good": good.name,
                result["success"] ? "access": "GRANTED" : "DENIED",
                "cost": good.credit_cost,
                "remaining_credits": c.account.current_credits,
                "reason": result.get("reason", "Credito gasto."),
            }

        retorne {"error": "unknown tier"}


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    random.seed(42)

    imprima("=" * 75)
    imprima("  OPENCREDIT -- CREDITO DEMOCRATICO DE ACESSO")
    imprima("  'Nao e moeda. E acesso. Nao acumula. A comunidade decide.'")
    imprima("=" * 75)

    system = DemocraticCreditSystem(pool_per_cycle=1000.0)

    // Criar 10 cidadaos
    names = ["Ana", "Bruno", "Carla", "Diego", "Eva",
             "Felipe", "Gabi", "Hugo", "Iris", "Joao"]
    para cada (i, name) em enumere(names):
        skills = random.sample(["farming", "building", "healing", "teaching",
                               "cooking", "coding", "art", "organizing"], k=3)
        c = Citizen("C-{i:03d}", name, random.randint(20, 60), skills)
        system.add_citizen(c)

    // === Catalog ===
    imprima("\n\n  === CATALOGO DE BENS ===\n")

    imprima("  DIREITOS GARANTIDOS (sem credito, sempre):")
    para cada g em CATALOG:
        se g.tier == AccessTier.GUARANTEED entao:
            imprima("    {g.name}")

    imprima("\n  COTA IGUAL (sem credito):")
    para cada g em CATALOG:
        se g.tier == AccessTier.STANDARD entao:
            imprima("    {g.name}")

    imprima("\n  BENS COLETIVOS (compartilhados):")
    para cada g em CATALOG:
        se g.tier == AccessTier.COLLECTIVE entao:
            imprima("    {g.name}")

    imprima("\n  BENS QUE PRECISAM DE CREDITO:")
    imprima("  {'Bem':<35} {'Credito':>8}")
    imprima("  {'-'*45}")
    para cada g em CATALOG:
        se g.tier == AccessTier.CREDIT entao:
            imprima("  {g.name:<35} {g.credit_cost:>7.0f}")

    // === Simular 3 ciclos ===
    imprima("\n\n  === SIMULACAO: 3 CICLOS DE CREDITO DEMOCRATICO ===\n")

    contribution_types = list(ContributionType)

    para cada cycle_num em intervalo(1, 4):
        // Fase 1: cidadaos contribuem COM IMPACTO MEDIDO
        impact_examples = [
            ("medico", ContributionType.HEALTHCARE, 8, 1, 1.0),        // 1 cirurgia = 1 vida
            ("professor", ContributionType.EDUCATION, 4, 30, 10.0),     // 30 alunos x ripple 10x
            ("agricultor", ContributionType.FOOD_PRODUCTION, 8, 500, 1.0),   // 500 alimentados
            ("faxineiro", ContributionType.CLEANING, 8, 200, 2.0),       // 200 usam espaco, previne doenca
            ("pesquisador", ContributionType.RESEARCH, 8, 1000, 5.0),    // descoberta afeta 1000+
            ("construtor", ContributionType.CONSTRUCTION, 8, 50, 1.0),   // 50 moram na casa
            ("artista", ContributionType.ART, 4, 100, 3.0),              // 100 veem, se inspiram
        ]

        para cada c em system.citizens.values():
            role_data = random.choice(impact_examples)
            ctype = role_data[1]
            hours = role_data[2]
            people = role_data[3]
            ripple = role_data[4]
            system.register_contribution(c.citizen_id, ctype, hours,
                                         people_impacted = people,
                                         ripple_factor = ripple)

        // Fase 2: rodar ciclo
        result = system.run_cycle()

        imprima("  CICLO {result['cycle']}:")
        imprima("    Proposta vencedora: {result['winning_proposal']}")
        imprima("    {result['winning_description'][:70]}...")
        imprima("    Pool: {result['pool_total']:.0f} | Cidadaos: {result['citizens']}")
        imprima("    Min: {result['min_given']} | Max: {result['max_given']} "
              "| Media: {result['avg_given']}")
        imprima("    Expirado ciclo anterior: {result['expired_from_last_cycle']}")
        imprima("\n    {'Cidadao':<10} {'Horas':>6} {'Creditos':>9}")
        imprima("    {'-'*28}")

        para cada (name, credits) em ordene(result["distribution"].items()):
            c = next(c para c em system.citizens.values() if c.name == name)
            imprima("    {name:<10} {c.account.contribution_hours:>5.0f}h {credits:>8.1f}")

        // Simular alguns gastos
        imprima("\n    Gastos no ciclo:")
        spenders = random.sample(list(system.citizens.values()), 4)
        para cada c em spenders:
            credit_goods = [g para g em CATALOG if g.tier == AccessTier.CREDIT]
            good = random.choice(credit_goods)
            access = system.access_good(c.citizen_id, good.name)
            status = access.get("access", "?")
            cost = access.get("cost", 0)
            remaining = access.get("remaining_credits", 0)
            imprima("      {c.name:<10} -> {good.name[:25]:<25} "
                  "custo={cost:>3} restante={remaining:>5.1f} [{status}]")

        imprima()

    // === Explicar por que NAO e moeda ===
    imprima("\n{'='*75}")
    imprima("  POR QUE ISSO NAO E DINHEIRO")
    imprima("{'='*75}")

    imprima("""
  DIFERENCA FUNDAMENTAL: Credito de Acesso vs Moeda

  +-------------------+-------------------+-------------------+
  | Caracteristica | Moeda ($) | Credito de Acesso |
  +-------------------+-------------------+-------------------+
  | Acumula? | SIM (pode guardar)| nao (expira) |
  | Transfere? | SIM (pode dar) | nao (pessoal) |
  | Herda? | SIM (passa filhos)| nao (morreu=zerou)|
  | Compra essencial? | SIM (compra comida)| nao (direito) |
  | Gera juros? | SIM | nao |
  | Cria desigualdade?| SIM (acumula) | nao (piso+teto) |
  | Quem decide valor?| Mercado/Estado | TODOS (votacao) |
  | Especula? | SIM | IMPOSSIVEL |
  +-------------------+-------------------+-------------------+

  O CREDITO EXISTE PARA RESOLVER UMA UNICA COISA:
  Quem pega a prancha de surf quando so tem 3 e 10 pessoas querem?

  A resposta nao e: quem tem mais dinheiro.
  A resposta e: quem a comunidade reconhece que contribuiu mais,
  decidido por votacao direta de TODOS, neste ciclo.

  e no proximo ciclo, comeca de novo.
  Ninguem fica rico. Ninguem acumula.
  Mas quem contribui tem prioridade no que e escasso.
// )

    // === Resumo final ===
    imprima("{'='*75}")
    imprima("  RESUMO DO OPENCREDIT")
    imprima("{'='*75}\n")

    imprima("  1. ESSNCIAIS sao DIREITOS (sem credito):")
    imprima("     Comida, agua, moradia, saude, educacao, transporte")
    imprima("     -> Voce ACESSE. Nao compra. Nao gasta credito.\n")

    imprima("  2. BENS ESCASSOS precisam de CREDITO:")
    imprima("     Instrumentos, viagens, eletronicos especiais")
    imprima("     -> Voce gasta credito de acesso do ciclo\n")

    imprima("  3. CREDITO e distribuido por TODOS:")
    imprima("     A comunidade vota como dividir o pool")
    imprima("     Base igual para todos + bonus por contribuicao")
    imprima("     -> Quem contribui mais, tem mais acesso ao que e escasso\n")

    imprima("  4. CREDITO NAO E MOEDA:")
    imprima("     Expira todo ciclo (nao acumula)")
    imprima("     E pessoal (nao transfere)")
    imprima("     Tem piso (ninguem fica sem) e teto (ninguem domina)")
    imprima("     Nao compra essencial (essencial e direito)\n")

    imprima("  5. CONTRIBUICAO e reconhecida pela comunidade:")
    imprima("     Nao e 'salario'. E reconhecimento.")
    imprima("     Saude, educacao e comida valem mais que arte.")
    imprima("     Mas arte tambem conta.\n")

    imprima("  RESULTADO:")
    imprima("  Ninguem passa fome porque 'acabou o credito'.")
    imprima("  Ninguem acumula fortuna porque 'trabalhou mais'.")
    imprima("  Todos tem o essencial garantido.")
    imprima("  O escasso e distribuido democraticamente.")
    imprima("  A cada ciclo, recomeca. Sem aculumulo. Sem heranca.")
    imprima("  Sem classe. Sem exploracao. Sem dominacao.\n")
    imprima("{'='*75}")

```
