# OpenAntiPredatory -- Politica Anti Competicao Predatoria

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_anti_predatory.py`

**Descricao:** ==========================================================
"Competicao que DESTROI o competidor nao e competicao.
 E GUERRA economic. A Republica PROIBE.
 Competir melhorando = SIM. Competir destruindo = NAO."
O QUE E COMPETICAO PREDATORIA:
  - Predatory pricing (vendem abaixo do custo para matar concorrente)
  - Monopolio (unica empresa domina mercado)
  - Cartel (combinam precos para lucrar)
  - Dumping (produto barato ate matar competencia, depois sobe preco)
  - Buy-and-kill (compra concorrente para FECHAR)
  - Walled garden (tranca usuario no ecossistema)
  - Vendor lock-in (dependencia forçada)
  - Planned obsolescence (produto quebra de proposito)
NA REPUBLICA:
  Dinheiro nao existe. Propriedade nao existe.
  Mas COMPETICAO por RECURSOS, INFLUENCIA e ATENCAO existe.
  Predacao tambem existe (tentar dominar, excluir, monopolizar).
  A Republica garante:
  - COMPETICAO SAUDAVEL: quem faz melhor, ganha reconhecimento
  - ANTI-PREDATORIA: quem tenta destruir/dominar, BLOQUEADO
  - COLABORACAO > COMPETICAO: LEGO modular. Encaixa, nao exclui.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenAntiPredatory -- Politica Anti Competicao Predatoria
==========================================================

"Competicao que DESTROI o competidor nao e competicao.
 e GUERRA economic. A Republica PROIBE.
 Competir melhorando = SIM. Competir destruindo = nao."

O QUE e COMPETICAO PREDATORIA:
  - Predatory pricing (vendem abaixo do custo para matar concorrente)
  - Monopolio (unica empresa domina mercado)
  - Cartel (combinam precos para lucrar)
  - Dumping (produto barato ate matar competencia, depois sobe preco)
  - Buy- e -kill (compra concorrente para FECHAR)
  - Walled garden (tranca usuario no ecossistema)
  - Vendor lock-in (dependencia forçada)
  - Planned obsolescence (produto quebra de proposito)

NA REPUBLICA:
  Dinheiro nao existe. Propriedade nao existe.
  Mas COMPETICAO por RECURSOS, INFLUENCIA e ATENCAO existe.
  Predacao tambem existe (tentar dominar, excluir, monopolizar).

  A Republica garante:
  - COMPETICAO SAUDAVEL: quem faz melhor, ganha reconhecimento
  - ANTI-PREDATORIA: quem tenta destruir/dominar, BLOQUEADO
  - COLABORACAO > COMPETICAO: LEGO modular. Encaixa, nao exclui.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. TIPOS DE PREDACAO
// ============================================================================

classe PredationType herda de Enum:
    MONOPOLY = "monopolio"  // dominar mercado todo
    CARTEL = "cartel"  // combinar para dominar
    PREDATORY_PRICING = "preco_predatorio"  // vender abaixo do custo pra matar
    DUMPING = "dumping"  // barato ate matar, depois sobe
    BUY_AND_KILL = "comprar_e_matinar"  // comprar concorrente pra fechar
    WALLED_GARDEN = "jardim_fechado"  // tranca usuario no ecossistema
    VENDOR_LOCKIN = "dependencia_forcada"  // usuario nao pode sair
    PLANNED_OBSCOLESCENCE = "obsolescencia_programada"  // quebra de proposito
    EXCLUSION = "exclusao"  // excluir competidor de plataforma
    RESOURCE_HOARDING = "acumulacao_recursos"  // acumular recursos para dominar
    INFLUENCE_MONOPOLY = "monopolio_influencia"  // dominar atencao/narrativa
    SABOTAGE = "sabotagem"  // sabotar sistema/modulo alheio


classe PredationSeverity herda de Enum:
    BLOCKED = ("bloqueado", 5)       #acao imediata: BLOQUEAR
    SEVERE = ("severo", 4)  // acao rapida: corrigir
    MODERATE = ("moderado", 3)  // acao: monitorar + corrigir
    WARNING = ("aviso", 2)  // observar
    SUSPECT = ("suspeito", 1)  // investigar


classe AntiPredationAction herda de Enum:
    BLOCK_IMMEDIATE = "bloquear_imediato"
    FORCE_OPEN = "forcar_abertura"  // abrir o que foi fechado
    REDISTRIBUTE = "redistribuir"  // redistribuir recursos monopolizados
    INVESTIGATE = "investigar"
    MONITOR = "monitorar"
    WARNING = "avisar"
    ASSEMBLY_REVIEW = "assembleia_revisar"


// ============================================================================

// decorador: @dataclass
classe PredationCase:
    // Caso de competicao predatoria detectado.
    seja case_id: texto = ""
    seja predator: texto = ""
    seja victim: texto = ""
    seja predation_type: PredationType = PredationType.MONOPOLY
    seja severity: PredationSeverity = PredationSeverity.WARNING
    seja description: texto = ""
    seja evidence: [texto] = field(default_factory=list)
    seja action: AntiPredationAction = AntiPredationAction.WARNING
    seja status: texto = "detectado"
    seja date: texto = ""


// ============================================================================

classe AntiPredationEngine:
    // Motor que detecta e bloqueia competicao predatoria.

    PRINCIPIOS:
    1. COMPETIR MELHORANDO = OK (fazer melhor ganha reconhecimento)
    2. COMPETIR DESTRUINDO = BLOQUEADO (predatorio)
    3. COLABORACAO > COMPETICAO (LEGO: encaixa, nao exclui)
    4. MONOPOIO = contra P1 (ninguem domina)
    5. TRANSPARENCIA TOTAL (tudo auditavel)

    DETECCAO AUTOMATICA:
    - Resource hoarding: alguem acumulando >20% de recursos?
    - Influence monopoly: alguauem dominando >30% de atencao?
    - Walled garden: sistema nao conecta com outros?
    - Vendor lock-in: dados presos, sem export?
    - Exclusion: sistema bloqueia concorrente?
    - Sabotage: codigo que quebra modulo alheio?
    // 

    THRESHOLDS = {
        "resource_hoard_pct": 0.20,      // >20% recursos = suspeito
        "influence_monopoly_pct": 0.30,   // >30% atencao = suspeito
        "market_dominance_pct": 0.40,     // >40% mercado = monopolio
    }

    funcao __init__(self):
        self.cases: {texto: PredationCase} = {}
        self.blocked_count: inteiro = 0
        self.corrected_count: inteiro = 0

    funcao detect(self, predator: texto, predation_type: PredationType,
               description: texto, evidence: [texto] = nulo,
               seja victim: texto = "") -> {texto: qualquer}:
        // Detecta e processa caso de predacao.
        cid = hashlib.md5(
            "{predator}{predation_type.value}{datetime.now()}".encode()
        ).hexdigest()[:8]

        severity = self._assess_severity(predation_type)
        action = self._decide_action(severity)

        case = PredationCase(
            case_id = cid, predator=predator, victim=victim,
            predation_type = predation_type, severity=severity,
            description = description, evidence=evidence ou [],
            action = action, date=datetime.now().isoformat(),
        )
        self.cases[cid] = case

        se action == AntiPredationAction.BLOCK_IMMEDIATE entao:
            self.blocked_count += 1
            case.status = "bloqueado"

        retorne {
            "case_id": cid,
            "predator": predator,
            "type": predation_type.value,
            "severity": severity.value[0],
            "action": action.value,
            "status": case.status,
            "message": self._action_message(action, predator, predation_type),
        }

    funcao _assess_severity(self, ptype: PredationType) -> PredationSeverity:
        severity_map = {
            PredationType.MONOPOLY: PredationSeverity.BLOCKED,
            PredationType.CARTEL: PredationSeverity.BLOCKED,
            PredationType.PREDATORY_PRICING: PredationSeverity.SEVERE,
            PredationType.DUMPING: PredationSeverity.SEVERE,
            PredationType.BUY_AND_KILL: PredationSeverity.BLOCKED,
            PredationType.WALLED_GARDEN: PredationSeverity.SEVERE,
            PredationType.VENDOR_LOCKIN: PredationSeverity.SEVERE,
            PredationType.PLANNED_OBSCOLESCENCE: PredationSeverity.BLOCKED,
            PredationType.EXCLUSION: PredationSeverity.SEVERE,
            PredationType.RESOURCE_HOARDING: PredationSeverity.MODERATE,
            PredationType.INFLUENCE_MONOPOLY: PredationSeverity.MODERATE,
            PredationType.SABOTAGE: PredationSeverity.BLOCKED,
        }
        retorne severity_map.get(ptype, PredationSeverity.WARNING)

    funcao _decide_action(self, severity: PredationSeverity) -> AntiPredationAction:
        action_map = {
            5: AntiPredationAction.BLOCK_IMMEDIATE,
            4: AntiPredationAction.FORCE_OPEN,
            3: AntiPredationAction.REDISTRIBUTE,
            2: AntiPredationAction.MONITOR,
            1: AntiPredationAction.INVESTIGATE,
        }
        retorne action_map.get(severity.value[1], AntiPredationAction.WARNING)

    funcao _action_message(self, action: AntiPredationAction,
                        predator: texto, ptype: PredationType) -> texto:
        messages = {
            AntiPredationAction.BLOCK_IMMEDIATE: (
                "BLOQUEADO: {predator} tentou {ptype.value}. "
                "A Republica BLOQUEOU imediatamente. "
                "Ninguem domina. Ninguem exclui."
            ),
            AntiPredationAction.FORCE_OPEN: (
                "FORCAR ABERTURA: {predator} tem {ptype.value}. "
                "Sistema FORCA abertura. Dados liberados. Lock-in quebrado."
            ),
            AntiPredationAction.REDISTRIBUTE: (
                "REDISTRIBUIR: {predator} acumulou demais ({ptype.value}). "
                "Recursos redistribuidos. Ninguem monopoliza."
            ),
            AntiPredationAction.MONITOR: (
                "MONITORAR: {predator} sob observacao ({ptype.value}). "
                "Se piorar, acao automatica."
            ),
        }
        retorne messages.get(action, "Caso registrado: {ptype.value}.")

    funcao check_market_dominance(self, entity: texto,
                               market_share: flutuante) -> {texto: qualquer}:
        // Verifica se entidade domina demais.
        threshold = self.THRESHOLDS["market_dominance_pct"]
        se market_share > threshold entao:
            retorne self.detect(
                entity, PredationType.MONOPOLY,
                "{entity} domina {market_share:.0%} do mercado (limite: {threshold:.0%})",
                ["Market share: {market_share:.0%}"],
            )
        retorne {"status": "OK", "share": "{market_share:.0%}", "message": "Dentro do limite."}

    funcao check_resource_hoarding(self, entity: texto,
                                resource_pct: flutuante) -> {texto: qualquer}:
        // Verifica acumulacao de recursos.
        threshold = self.THRESHOLDS["resource_hoard_pct"]
        se resource_pct > threshold entao:
            retorne self.detect(
                entity, PredationType.RESOURCE_HOARDING,
                "{entity} acumulou {resource_pct:.0%} dos recursos (limite: {threshold:.0%})",
                ["Resource share: {resource_pct:.0%}"],
            )
        retorne {"status": "OK"}

    funcao check_walled_garden(self, system_name: texto,
                            connects_with_others: logico,
                            data_exportable: logico) -> {texto: qualquer}:
        // Verifica se sistema e jardim fechado.
        se nao connects_with_others ou nao data_exportable entao:
            retorne self.detect(
                system_name, PredationType.WALLED_GARDEN,
                "{system_name} nao conecta com outros ou nao exporta dados",
                ["Conecta: {connects_with_others}", "Exporta: {data_exportable}"],
            )
        retorne {"status": "OK"}

    funcao check_planned_obsolescence(self, product: texto,
                                   lifespan_years: flutuante,
                                   repairable: logico) -> {texto: qualquer}:
        // Verifica obsolescencia programada.
        se lifespan_years < 3 ou nao repairable entao:
            retorne self.detect(
                product, PredationType.PLANNED_OBSCOLESCENCE,
                "{product}: vida util {lifespan_years} anos, reparavel: {repairable}",
                ["Lifespan: {lifespan_years} anos", "Repairable: {repairable}"],
            )
        retorne {"status": "OK"}

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_casos": tamanho(self.cases),
            "bloqueados": self.blocked_count,
            "corrigidos": self.corrected_count,
            "tipos_detectados": tamanho(set(c.predation_type para c em self.cases.values())),
        }


// ============================================================================

se __name__ == "__main__" entao:
    engine = AntiPredationEngine()

    imprima("=" * 80)
    imprima("  OPENANTIPREDATORY -- POLITICA ANTI COMPETICAO PREDATORIA")
    imprima("  Competir melhorando = OK. Competir destruindo = BLOQUEADO.")
    imprima("=" * 80)

    // === 1. TIPOS DE PREDACAO ===
    imprima("\n\n  === 1. TIPOS DE COMPETICAO PREDATORIA ({len(PredationType)}) ===\n")
    para cada pt em PredationType:
        sev = engine._assess_severity(pt)
        imprima("  [{sev.value[0]:<12}] {pt.value}")

    // === 2. CASOS DE DETECCAO ===
    imprima("\n\n  === 2. CASOS DETECTADOS ===\n")

    cases = [
        ("TechGiant Corp", PredationType.MONOPOLY,
         "Domina 80% do mercado de OS. Exclui concorrentes.",
         ["Market share: 80%", "Exclui OpenOS de lojas"]),
        ("Banco Malvado", PredationType.VENDOR_LOCKIN,
         "Dados do cliente presos. Nao exporta. Nao libera.",
         ["Sem export de dados", "Taxa para sair: R$ 500"]),
        ("FoneQuebra", PredationType.PLANNED_OBSCOLESCENCE,
         "Fone quebra em 1 ano. Bateria colada. Irreparavel.",
         ["Vida util: 1 ano", "Bateria colada", "Sem peca de reposicao"]),
        ("RedeSocial Fechada", PredationType.WALLED_GARDEN,
         "Nao conecta com outras redes. Dados presos.",
         ["Sem API publica", "Sem export", "Sem federacao"]),
        ("PredatorPrice", PredationType.PREDATORY_PRICING,
         "Vende abaixo do custo por 2 anos para matar OpenEquivalent.",
         ["Preco < custo por 24 meses", "Objetivo: monopolio depois"]),
        ("Cartel Telecom", PredationType.CARTEL,
         "3 operadoras combinam preco. Sem competencia real.",
         ["Precos identicos", "Dividem territorio"]),
        ("BuyCorp", PredationType.BUY_AND_KILL,
         "Comprou startup concorrente e FECHOU o produto.",
         ["Comprou por R$ 50M", "Produto descontinuado"]),
    ]
    para predator, ptype, desc, evidence in cases:
        r = engine.detect(predator, ptype, desc, evidence)
        imprima("\n  [{r['severity'].upper()}] {r['predator']}")
        imprima("  Tipo: {r['type']}")
        imprima("  Acao: {r['action']}")
        imprima("  {r['message'][:70]}")

    // === 3. CHECKS AUTOMATICOS ===
    imprima("\n\n  === 3. CHECKS AUTOMATICOS ===\n")

    // Market dominance
    r = engine.check_market_dominance("TechGiant", 0.45)
    imprima("  Market dominance check: {r.get('status', r.get('action', '?'))}")

    // Resource hoarding
    r = engine.check_resource_hoarding("Acumulador", 0.35)
    imprima("  Resource hoarding check: {r.get('status', r.get('action', '?'))}")

    // Walled garden
    r = engine.check_walled_garden("RedeFechada", falso, falso)
    imprima("  Walled garden check: {r.get('status', r.get('action', '?'))}")

    // Planned obsolescence
    r = engine.check_planned_obsolescence("FoneDescartavel", 1.5, falso)
    imprima("  Obsolescence check: {r.get('status', r.get('action', '?'))}")

    // === 4. STATS ===
    imprima("\n\n  === 4. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<25} {v}")

    imprima("\n{'='*80}")
    imprima("  AntiPredatory: {s['bloqueados']} bloqueados. Competir destruindo = PROIBIDO.")
    imprima("{'='*80}")

```
