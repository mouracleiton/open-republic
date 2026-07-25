# OpenRepublic -- Solucoes para os 3 Gargalos Restantes do Sahel

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/sahel_solutions.py`

**Descricao:** ================================================================
1. Cuidado Infantil (300% sobrecarga, 1 pessoa para 300 criancas)
2. Agricultura (167% sobrecarga, faltam sementes/irrigacao/pessoas)
3. Habitacao (167% sobrecarga, faltam unidades e construtores)
Em uma sociedade sem propriedade privada e sem dinheiro, as solucoes
NAO sao "contratar mais gente" ou "comprar equipamento". Sao:
- AUTOMATIZACAO: maquinas fazem o trabalho repetitivo
- ROTACAO COMUNITARIA: todos contribuem um pouco
- REDES DE AUTOAJUDA: os proprios usuarios se ajudam
- TRANSFERENCIA INTER-NACAO: quem sabe ensina quem precisa
- DESIGN INTELIGENTE: permacultura, arquitetura passiva, cohousing
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Solucoes para os 3 Gargalos Restantes do Sahel
================================================================

1. Cuidado Infantil (300% sobrecarga, 1 pessoa para 300 criancas)
2. Agricultura (167% sobrecarga, faltam sementes/irrigacao/pessoas)
3. Habitacao (167% sobrecarga, faltam unidades e construtores)

Em uma sociedade sem propriedade privada e sem dinheiro, as solucoes
nao sao "contratar mais gente" ou "comprar equipamento". Sao:

- AUTOMATIZACAO: maquinas fazem o trabalho repetitivo
- ROTACAO COMUNITARIA: todos contribuem um pouco
- REDES DE AUTOAJUDA: os proprios usuarios se ajudam
- TRANSFERENCIA INTER-NACAO: quem sabe ensina quem precisa
- DESIGN INTELIGENTE: permacultura, arquitetura passiva, cohousing

Author: OpenRepublic Team
// 

// importa annotations de __future__
// importa math
// importa random
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Tuple de typing
// importa Enum de enum
// importa numpy as np


// ============================================================================
// SOLUCAO 1: CUIDADO INFANTIL COMUNITARIO
// ============================================================================

classe ChildcareSolution:
    // Como cuidar de 300 criancas com poucos adultos dedicados.

    Resposta: nao precisa de 30 adultos全职.
    Precisa de um SISTEMA onde cada adulto contribui um pouco
    e as proprias criancas se organizam em rede de mutualidade.
    // 

    // decorador: @staticmethod
    funcao calculate(population: inteiro, children_0_12: inteiro,
                  dedicated_workers: inteiro) -> {texto: qualquer}:
        // Calcula o plano de cuidado infantil comunitario.

        // === Fonte 1: Rotacao parental ===
        // Cada pai/mae contribui 4 horas/semana de cuidado comunitario
        // Assumindo 2 responsaveis por crianca (pai+mae ou rede familiar)
        parents = children_0_12 * 2
        parental_hours_week = parents * 4 // 4h/semana por responsavel
        parental_equiv = parental_hours_week / 40 // equivalente a trabalhadores全职

        // === Fonte 2: Idosos (60+) ===
        // Aposentados nao "aposentam" -- mudam de funcao
        // Cuidar de criancas e uma das atividades mais valorizadas
        elderly = inteiro(population * 0.12) // ~12% sao idosos
        elderly_active = inteiro(elderly * 0.6) // 60% podem ajudar
        elderly_hours_week = elderly_active * 10 // 10h/semana cada
        elderly_equiv = elderly_hours_week / 40

        // === Fonte 3: Jovens 13-17 (mentores) ===
        // Adolescentes cuidam de menores -- aprendem responsabilidade
        // e recebem reconhecimento (sistema de mentorship)
        teens = inteiro(population * 0.10)
        teen_mentors = inteiro(teens * 0.4) // 40% participam
        teen_hours_week = teen_mentors * 6 // 6h/semana
        teen_equiv = teen_hours_week / 40

        // === Fonte 4: IA + Automacao ===
        // Estacoes de aprendizado autonomo (tablets com curriculum)
        // Reduz necessidade de supervisao constante
        ai_stations = minimo(children_0_12 // 8, 40) // 1 estacao por 8 criancas
        ai_reduction_pct = 0.25 // IA reduz 25% da necessidade de adultos
        ai_adjusted_children = inteiro(children_0_12 * (1 - ai_reduction_pct))

        // === Fonte 5: Trabalhadores dedicados ===
        dedicated = dedicated_workers

        // Total de capacidade equivalente
        total_equiv = parental_equiv + elderly_equiv + teen_equiv + dedicated

        // Demanda: 1 adulto equivalente para cada 8 criancas (ajustado por IA)
        needed_equiv = ai_adjusted_children / 8

        ratio = total_equiv / maximo(needed_equiv, 1)
        gap = maximo(0, needed_equiv - total_equiv)

        retorne {
            "criancas_0_12": children_0_12,
            "demanda_ajustada_por_ia": ai_adjusted_children,
            "fontes_de_cuidado": {
                "trabalhadores_dedicados": {
                    "pessoas": dedicated,
                    "horas_semana": dedicated * 40,
                    "equiv_fulltime": arredonde(dedicated, 1),
                },
                "rotacao_parental_4h_semana": {
                    "pessoas": parents,
                    "horas_semana": parental_hours_week,
                    "equiv_fulltime": arredonde(parental_equiv, 1),
                    "principio": "Cada responsavel contribui 4h/semana",
                },
                "idosos_ativos_mentores": {
                    "pessoas": elderly_active,
                    "horas_semana": elderly_hours_week,
                    "equiv_fulltime": arredonde(elderly_equiv, 1),
                    "principio": "60+ nao se aposentam, mudam de funcao",
                },
                "adolescentes_mentores_13_17": {
                    "pessoas": teen_mentors,
                    "horas_semana": teen_hours_week,
                    "equiv_fulltime": arredonde(teen_equiv, 1),
                    "principio": "Mais velhos cuidam dos menores + aprendem",
                },
                "estacoes_ia_aprendizado": {
                    "estacoes": ai_stations,
                    "reducao_necessidade": "{ai_reduction_pct:.0%}",
                    "principio": "Curriculum autonomo reduz supervisao",
                },
            },
            "capacidade_total_equiv": arredonde(total_equiv, 1),
            "demanda_total_equiv": arredonde(needed_equiv, 1),
            "cobertura": "{min(100, ratio * 100):.0f}%",
            "gap_residual": arredonde(gap, 1),
            "viavel": ratio >= 1.0,
        }


// ============================================================================
// SOLUCAO 2: AGRICULTURA ESCALAVEL SEM DIINHEIRO
// ============================================================================

classe AgricultureSolution:
    // Como alimentar 40.000 pessoas no Sahel (deserto/savana).

    Com agua agora disponivel (Acao 1 do plano), o gargalo muda
    de agua para: sementes, maquinario, conhecimento, e pessoas.

    Solucao: agricultural tecnologica aberta + permacultura +
    transferencia de conhecimento da Amazonia.
    // 

    // decorador: @staticmethod
    funcao calculate(population: inteiro, current_kg_month: flutuante,
                  needed_kg_month: flutuante) -> {texto: qualquer}:

        // Demanda: 12kg/pessoa/mes de comida
        gap_kg_month = needed_kg_month - current_kg_month

        // === Estrategia 1: Hidroponia automatizada ===
        // 10x mais produtiva por m2 que solo, usa 90% menos agua
        // Sistema automatizado: 1 pessoa cuida de 500m2 de hidroponia
        hydro_yield_kg_m2_month = 4.0 // 4kg/m2/mes (alface, tomate, ervas)
        hydro_needed_m2 = gap_kg_month / hydro_yield_kg_m2_month
        hydro_workers = math.ceil(hydro_needed_m2 / 500)
        hydro_water_liters_day = hydro_needed_m2 * 2 // 2L/m2/dia (recircula 95%)

        // === Estrategia 2: Permacultura desertica ===
        // Sistema de swales, nitrogen-fixing trees, mulching
        // Uma vez estabelecido, e auto-sustentavel (3 anos para maturar)
        perm_yield_kg_hectare_month = 300 // menor que hidroponia mas auto-sustentavel
        perm_needed_hectares = (gap_kg_month * 0.4) / perm_yield_kg_hectare_month // 40% do gap
        perm_workers = math.ceil(perm_needed_hectares / 5) // 1 pessoa por 5 hectares
        perm_establishment_months = 36

        // === Estrategia 3: Aquaponia (peixe + planta) ===
        // Fecha o ciclo: peixes fertilizam plantas, plantas filtram agua
        // Produz proteina (peixe) + vegetais no mesmo sistema
        aquaponics_tanks = math.ceil(gap_kg_month * 0.2 / 50) // 50kg/tanque/mes
        aquaponics_workers = math.ceil(aquaponics_tanks / 10) // 1 pessoa por 10 tanques

        // === Estrategia 4: Automacao (Open-Agrarian) ===
        // Sensores IoT de umidade/nutrientes monitoram 24/7
        // Drones mapeiam pragas e irrigam com precisao
        // Reduz necessidade de trabalho manual em 40%
        iot_sensors = inteiro(hydro_needed_m2 / 50) // 1 sensor por 50m2
        drones = math.ceil(hydro_needed_m2 / 10000) // 1 drone por hectare

        // === Estrategia 5: Banco de sementes comunitario ===
        // Sementes open-pollinated (nao hibridas, nao transgenicas)
        // Cada colheita gera sementes para a proxima + excedente para doar
        // Rede de troca: Amazonia troca sementes tropicais por deserticas
        seed_bank_varieties = 200 // 200 variedades adaptadas ao deserto

        // === Estrategia 6: Transferencia de conhecimento ===
        // Amazonia (especialidade: permacultura) envia 5 agronomos
        // Permanecem 6 meses, treinam 50 pessoas locais
        // Cada treinado vira treinador (cascata exponencial)
        knowledge_transfer = {
            "de": "Amazonia (especialidade: biodiversidade, permacultura)",
            "para": "Sahel",
            "especialistas_enviados": 5,
            "duracao_meses": 6,
            "pessoas_treinadas": 50,
            "multiplicadores_cascata": "Cada treinado treina 5 mais",
            "apos_12_meses": "50 + 250 = 300 pessoas capacitadas",
        }

        // Total de trabalhadores necessarios (com automacao)
        total_workers = hydro_workers + perm_workers + aquaponics_workers
        // Automacao reduz 40%
        total_workers_adjusted = math.ceil(total_workers * 0.6)

        total_new_production = (hydro_needed_m2 * hydro_yield_kg_m2_month +
                               perm_needed_hectares * perm_yield_kg_hectare_month +
                               aquaponics_tanks * 50)

        retorne {
            "gap_alimentar": "{gap_kg_month:,.0f} kg/mes",
            "estrategias": {
                "hidroponia_automatizada": {
                    "area_m2": arredonde(hydro_needed_m2),
                    "producao_kg_mes": arredonde(hydro_needed_m2 * hydro_yield_kg_m2_month),
                    "trabalhadores": hydro_workers,
                    "agua_litros_dia": arredonde(hydro_water_liters_day),
                    "eficiencia": "10x mais que solo, 90% menos agua",
                },
                "permacultura_desertica": {
                    "area_hectares": arredonde(perm_needed_hectares, 1),
                    "producao_kg_mes": arredonde(perm_needed_hectares * perm_yield_kg_hectare_month),
                    "trabalhadores": perm_workers,
                    "maturacao": "{perm_establishment_months} meses",
                    "principio": "Swales + arvores fixadoras de nitrogenio + mulching",
                },
                "aquaponia_peixe_planta": {
                    "tanques": aquaponics_tanks,
                    "producao_kg_mes": aquaponics_tanks * 50,
                    "trabalhadores": aquaponics_workers,
                    "principio": "Peixes fertilizam plantas, plantas filtram agua",
                },
                "automacao_iot_drones": {
                    "sensores": iot_sensors,
                    "drones": drones,
                    "reducao_trabalho": "40%",
                    "principio": "Monitoramento 24/7 + irrigacao de precisao",
                },
                "banco_sementes_comunitario": {
                    "variedades": seed_bank_varieties,
                    "tipo": "Open-pollinated (reprodutivel)",
                    "troca_inter_nacao": "Amazonia <-> Sahel",
                },
                "transferencia_conhecimento": knowledge_transfer,
            },
            "producao_total_nova_kg_mes": arredonde(total_new_production),
            "trabalhadores_necessarios": total_workers_adjusted,
            "reducao_por_automacao": "40% menos trabalho manual",
            "auto_sustentavel_apos": "36 meses (permacultura matura)",
            "cobre_gap": total_new_production >= gap_kg_month,
        }


// ============================================================================
// SOLUCAO 3: HABITACAO EM MASSA SEM DINHEIRO
// ============================================================================

classe HousingSolution:
    // Como construir moradia para 40.000 pessoas no deserto.

    Sem dinheiro, sem empreiteira, sem hipoteca.
    Como? Automacao + materiais locais + construcao comunitaria +
    design inteligente (passive cooling para deserto).
    // 

    // decorador: @staticmethod
    funcao calculate(population: inteiro, current_units: inteiro,
                  needed_units: inteiro) -> {texto: qualquer}:

        gap_units = needed_units - current_units
        people_housed_per_unit = 3 // media de 3 pessoas por unidade

        // === Estrategia 1: Impressao 3D de casas ===
        // Printer extruda terra/cimento/gesso em camadas
        // 1 casa em 24-48 horas, 1 operador por printer
        printers_3d = 4 // 4 maquinas
        hours_per_house = 30 // 30h por casa
        houses_per_printer_month = (30 * 24) / hours_per_house // ciclos por mes
        houses_3d_month = printers_3d * houses_per_printer_month
        material_per_house_m3 = 15 // 15m3 de material por casa
        material_cost_equiv = "Terra local + 5% cimento = quase gratuito"

        // === Estrategia 2: Adobe/BTC (Blocos de Terra Comprimida) ===
        // Solo local + 5% cimento + prensa manual
        // Cada pessoa pode produzir 100 blocos/dia
        // Casa media: 3000 blocos
        block_presses = 10
        blocks_per_press_day = 500
        blocks_per_house = 3000
        houses_adobe_month = (block_presses * blocks_per_press_day * 25) / blocks_per_house
        workers_adobe = block_presses * 3 // 3 pessoas por prensa

        // === Estrategia 3: Construcao modular (prefab) ===
        // Fablab local produz paineis modulares
        // Montagem tipo LEGO, 4 pessoas montam 1 casa em 2 dias
        fablab_panels_month = 60 // 60 kits de paineis por mes
        workers_fablab = 8
        houses_modular_month = fablab_panels_month

        // === Estrategia 4: Swarm construction (mutirao) ===
        // Evento comunitario: 100 pessoas constroem 10 casas em 1 semana
        // Cada um contribui conforme sua habilidade (pedreiro, eletricista, cozinheiro)
        swarm_events_per_month = 2
        houses_per_swarm = 10
        houses_swarm_month = swarm_events_per_month * houses_per_swarm
        swarm_participants = 100

        // === Estrategia 5: Design passivo desertico ===
        // NAO precisa ar condicionado (que consume energia)
        // - Paredes de terra de 40cm (massa termica)
        // - Ventilacao cruzada (tower effect)
        // - Patio interno com vegetacao
        // - Telhado branco (albedo)
        // - Orientacao solar (janelas ao sul, sombra ao norte)
        passive_features = {
            "massa_termica": "Paredes 40cm terra/adobe (refresca de dia, esquenta de noite)",
            "ventilacao_cruzada": "Tower effect + aberturas opostas",
            "patio_interno": "Vegetacao + agua evaporativa",
            "telhado_alto_albedo": "Cor branca reflete 80% radiacao solar",
            "orientacao": "Janelas ao sul, paredo cega ao norte (hemisferio norte)",
        }

        // === Estrategia 6: Transferencia inter-nacao ===
        // Nordica envia planos de housing modular
        // Pacifico envia tecnicos de construcao
        // Amazonia envia conhecimento de bioconstrucao
        transfer = {
            "Nordica": "Planos de housing modular (Open-Desktop/CAD)",
            "Pacifico": "3 tecnicos de construcao (6 meses)",
            "Amazonia": "Bioconstrucao: bamboo, fibra de coco, terra crua",
        }

        // Total
        total_houses_month = (houses_3d_month + houses_adobe_month +
                             houses_modular_month + houses_swarm_month)
        months_to_fill_gap = math.ceil(gap_units / maximo(total_houses_month, 1))

        total_workers = (printers_3d * 2 + workers_adobe + workers_fablab +
                        swarm_participants / 4) // swarm e rotacional

        retorne {
            "gap_habitacional": "{gap_units} unidades",
            "estrategias": {
                "impressao_3d": {
                    "printers": printers_3d,
                    "casas_por_mes": arredonde(houses_3d_month),
                    "tempo_por_casa": "{hours_per_house}h",
                    "material": material_cost_equiv,
                    "operadores": printers_3d * 2,
                },
                "adobe_btc_prensa": {
                    "prensas": block_presses,
                    "casas_por_mes": arredonde(houses_adobe_month),
                    "material": "Solo local + 5% cimento",
                    "trabalhadores": workers_adobe,
                },
                "modular_fablab": {
                    "kits_por_mes": fablab_panels_month,
                    "casas_por_mes": houses_modular_month,
                    "trabalhadores": workers_fablab,
                    "principio": "Paineis prefabricados, montagem tipo LEGO",
                },
                "mutirao_comunitario": {
                    "eventos_por_mes": swarm_events_per_month,
                    "casas_por_evento": houses_per_swarm,
                    "participantes": swarm_participants,
                    "principio": "100 pessoas constroem 10 casas em 1 semana",
                },
                "design_passivo_desertico": passive_features,
                "transferencia_inter_nacao": transfer,
            },
            "casas_por_mes_total": arredonde(total_houses_month),
            "meses_para_cobrir_gap": months_to_fill_gap,
            "trabalhadores_necessarios": math.ceil(total_workers),
            "custo_monetario": "R$ 0 (sem dinheiro, sem empreiteira)",
            "material_principal": "Terra local + cimento (5%) + bamboo/fibra",
            "energia_necessaria": "Minima (design passivo = sem ar condicionado)",
        }


// ============================================================================
// MAIN
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 75)
    imprima("  SOLUCOES PARA OS 3 GARGALOS DO SAHEL")
    imprima("  Sem dinheiro. Sem empreiteira. Sem 'contratar'.")
    imprima("  Com automatizacao + comunidade + conhecimento aberto.")
    imprima("=" * 75)

    // === SOLUCAO 1: CUIDADO INFANTIL ===
    imprima("\n\n" + "=" * 75)
    imprima("  GARGALO 1: CUIDADO INFANTIL (300% sobrecarga)")
    imprima("  1 pessoa tentando cuidar de 300 criancas")
    imprima("=" * 75)

    childcare = ChildcareSolution.calculate(
        population = 40000, children_0_12=6000, dedicated_workers=6)

    imprima("\n  Crianças 0-12 anos: {childcare['criancas_0_12']:,}")
    imprima("  Demanda ajustada (IA reduz 25%): {childcare['demanda_ajustada_por_ia']:,}")
    imprima("\n  FONTES DE CUIDADO:")
    imprima("  {'Fonte':<35} {'Pessoas':>8} {'Equiv FT':>10}")
    imprima("  {'-'*55}")
    para cada (fonte, dados) em childcare['fontes_de_cuidado'].items():
        se 'pessoas' in dados entao:
            imprima("  {fonte.replace('_', ' ').title():<35} {dados['pessoas']:>8} "
                  "{dados['equiv_fulltime']:>10}")
        senao se 'estacoes' in dados entao:
            imprima("  {fonte.replace('_', ' ').title():<35} {dados['estacoes']:>8} estacoes")
    imprima("  {'-'*55}")
    imprima("  {'CAPACIDADE TOTAL':<35} {'':>8} {childcare['capacidade_total_equiv']:>10}")
    imprima("  {'DEMANDA TOTAL':<35} {'':>8} {childcare['demanda_total_equiv']:>10}")
    imprima("\n  COBERTURA: {childcare['cobertura']}")
    imprima("  VIÁVEL: {'SIM' if childcare['viavel'] else 'NAO'}")
    imprima("\n  PRINCIPIO: Nao se trata de contratar 75 profissionais.")
    imprima("  Trata-se de ativar a COMUNIDADE INTEIRA:")
    imprima("    - Cada pai/mae: 4h/semana")
    imprima("    - Cada idoso ativo: 10h/semana (continuar contribuindo)")
    imprima("    - Cada adolescente: 6h/semana (mentoria + responsabilidade)")
    imprima("    - Estacoes de IA: 25% do aprendizado e autonomo")
    imprima("  Resultado: a comunidade SE cuida. Nao precisa de Estado.")

    // === SOLUCAO 2: AGRICULTURA ===
    imprima("\n\n" + "=" * 75)
    imprima("  GARGALO 2: AGRICULTURA (167% sobrecarga)")
    imprima("  Faltam 2.000 kg/mes de comida para 40.000 pessoas")
    imprima("=" * 75)

    agriculture = AgricultureSolution.calculate(
        population = 40000, current_kg_month=3000, needed_kg_month=5000)

    imprima("\n  Gap alimentar: {agriculture['gap_alimentar']}")
    imprima("\n  ESTRATEGIAS:")
    imprima("  {'Estrategia':<30} {'Escala':>15} {'Producao':>12} {'Pessoas':>8}")
    imprima("  {'-'*68}")
    para cada (nome, dados) em agriculture['estrategias'].items():
        se isinstance(dados, dict) entao:
            escala = ""
            prod = ""
            pessoas = ""
            se 'area_m2' in dados entao:
                escala = "{dados['area_m2']} m2"
                prod = "{dados['producao_kg_mes']} kg"
                pessoas = texto(dados.get('trabalhadores', ''))
            senao se 'area_hectares' in dados entao:
                escala = "{dados['area_hectares']} ha"
                prod = "{dados['producao_kg_mes']} kg"
                pessoas = texto(dados.get('trabalhadores', ''))
            senao se 'tanques' in dados entao:
                escala = "{dados['tanques']} tanques"
                prod = "{dados['producao_kg_mes']} kg"
                pessoas = texto(dados.get('trabalhadores', ''))
            senao se 'sensores' in dados entao:
                escala = "{dados['sensores']} sensores"
                prod = dados.get('reducao_trabalho', '')
                pessoas = ""
            senao se 'variedades' in dados entao:
                escala = "{dados['variedades']} variedades"
                prod = ""
            senao se 'especialistas_enviados' in dados entao:
                escala = "{dados['especialistas_enviados']} de {dados['de'][:12]}"
                pessoas = texto(dados.get('pessoas_treinadas', ''))
            imprima("  {nome.replace('_', ' ').title():<30} {escala:>15} {prod:>12} {pessoas:>8}")

    imprima("\n  {'PRODUCAO NOVA TOTAL':<30} {'':>15} {agriculture['producao_total_nova_kg_mes']:>9} kg/mes")
    imprima("  {'TRABALHADORES':<30} {'':>15} {'':>12} {agriculture['trabalhadores_necessarios']:>8}")
    imprima("  COBRE O GAP: {'SIM' if agriculture['cobre_gap'] else 'NAO'}")
    imprima("  AUTO-SUSTENTAVEL APOS: {agriculture['auto_sustentavel_apos']}")
    imprima("\n  PRINCIPIO: Hidroponia (10x mais por m2) + permacultura")
    imprima("  (auto-sustentavel apos 3 anos) + aquaponia (proteina + vegetais)")
    imprima("  + automacao IoT (40% menos trabalho) + conhecimento da Amazonia")

    // === SOLUCAO 3: HABITACAO ===
    imprima("\n\n" + "=" * 75)
    imprima("  GARGALO 3: HABITACAO (167% sobrecarga)")
    imprima("  Faltam ~2.000 unidades para 40.000 pessoas")
    imprima("=" * 75)

    housing = HousingSolution.calculate(
        population = 40000, current_units=3000, needed_units=5000)

    imprima("\n  Gap habitacional: {housing['gap_habitacional']}")
    imprima("\n  ESTRATEGIAS:")
    imprima("  {'Estrategia':<25} {'Unid/mes':>10} {'Material':<25} {'Pessoas':>8}")
    imprima("  {'-'*70}")
    para cada (nome, dados) em housing['estrategias'].items():
        se isinstance(dados, dict)  e  ('casas_por_mes' in dados  ou  'kits_por_mes' in dados) entao:
            unid = dados.get('casas_por_mes', dados.get('kits_por_mes', '?'))
            mat = dados.get('material', dados.get('principio', ''))[:24]
            pessoas = dados.get('trabalhadores', dados.get('operadores',
                     dados.get('participantes', '')))
            imprima("  {nome.replace('_', ' ').title():<25} {unid:>10} {mat:<25} {pessoas:>8}")
        senao se isinstance(dados, dict)  e  'massa_termica' in dados entao:
            imprima("  {'Design Passivo':<25} {'N/A':>10} {'Sem ar condicionado':<25}")

    imprima("\n  {'TOTAL':<25} {housing['casas_por_mes_total']:>10}")
    imprima("  MESES PARA COBRIR GAP: {housing['meses_para_cobrir_gap']}")
    imprima("  TRABALHADORES: {housing['trabalhadores_necessarios']}")
    imprima("  CUSTO: {housing['custo_monetario']}")
    imprima("  MATERIAL: {housing['material_principal']}")
    imprima("\n  PRINCIPIO: Terra local e gratuita. Prensa manual faz bloco.")
    imprima("  Impressora 3D faz casa em 30h. Mutirao constroi 10 casas/semana.")
    imprima("  Design passivo: 40cm de parede de terra = sem ar condicionado.")

    // === RESUMO INTEGRADO ===
    imprima("\n\n" + "=" * 75)
    imprima("  RESUMO: COMO RESOLVER OS 3 GARGALOS SEM DINHEIRO")
    imprima("=" * 75)
    imprima("""
  +-----------+----------------+------------------+----------+--------+
  | Gargalo | Solucao | Como | Pessoas | Tempo |
  +-----------+----------------+------------------+----------+--------+
  | Creche | Rede comunita- | Pais 4h/sem + | Toda a | 1 mes |
  | 300% | ria de cuidado | Idosos 10h/sem + | comunida-| |
  | | + IA + teen | Adolescentes 6h | de ativa | |
  +-----------+----------------+------------------+----------+--------+
  | Agricult. | Hidroponia + | 10x mais/m2 + | ~35 + | 3-36 |
  | 167% | permacultura + | Automacao IoT + | IoT sen- | meses |
  | | aquaponia + | Conhecimento AMZ | sores + | |
  | | automacao | | drones | |
  +-----------+----------------+------------------+----------+--------+
  | Habitacao | 3D imprima + | Terra local | ~40 + | 6-12 |
  | 167% | BTC/adobe + | (gratis) + | mutirao | meses |
  | | modular + | prensa manual + | (100 sem.| |
  | | mutirao | fablab local | por even)| |
  +-----------+----------------+------------------+----------+--------+

  PRINCIPIO FUNDAMENTAL:

  Em uma sociedade sem propriedade privada, os recursos existem.
  A terra existe. A agua existe (agora). O conhecimento existe.
  As pessoas existem. O que falta e ORGANIZACAO, nao dinheiro.

  - Nao se "contrata" trabalhadores -- se ORGANIZA a comunidade
  - Nao se "compra" material -- se USA o que existe localmente
  - Nao se "pagam" especialistas -- se TROCA conhecimento entre nacoes
  - Nao se "financia" construcao -- se CONSTROI junto (mutirao)

  O custo real de resolver os 3 gargalos: ZERO moeda.
  O custo real: trabalho comunitario + conhecimento aberto + organizacao.
// )

```
