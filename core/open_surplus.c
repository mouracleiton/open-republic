/* OpenSurplus -- Metrica de Necessidade de Excedente por Estabelecimento -- gerado de Portugol++ */
#ifndef OPENSURPLUS_METRICA_DE_NECESSIDADE_DE_EXCEDENTE_POR_ESTABELECIMENTO_H
#define OPENSURPLUS_METRICA_DE_NECESSIDADE_DE_EXCEDENTE_POR_ESTABELECIMENTO_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenSurplus -- Metrica de Necessidade de Excedente por Estabelecimento;
========================================================================;
"O trabalhador trabalha o suficiente pra SI.;
A empresa quer MAIS (excedente/mais-valia).;
A Republica MEDE: quanto excedente cada estabelecimento PRECISA?;
&& quanto && PREDATORIO (exploracao)?;
SEMPRE EM DOIS MODOS (OpenDualMode):;
EXECUTAVEL: excedente existe (precisa pra operar);
IDEAL: excedente ABOLIDO (tudo base 1.0 + impacto)";
CONCEITO CHAVE:;
Excedente = diferenca entre o que o trabalhador produz && o que recebe.;
No capitalismo: excedente = lucro do dono (mais-valia).;
Na Republica EXECUTAVEL: excedente = custo operacional JUSTO.;
Na Republica IDEAL: excedente = ZERO (aboluido).;
TIPOS DE EXCEDENTE:;
1. NECESSARIO (operacional): manter estabelecimento funcionando;
    - aluguel, equipamento, manutencao, insumos, energia;
2. JUSTO (investimento): melhorar, crescer, reservar;
    - OpenRepair, novos FabLabs, pesquisa;
3. PREDATORIO (exploracao): lucro excessivo do dono;
    - PROIBIDO pela Republica;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime
// ============================================================================
// 1. TIPOS DE EXCEDENTE
// ============================================================================
typedef struct SurplusType {
    // Classificacao do excedente extraido do trabalhador.
    NECESSARIO = ("necessario", 1)  // operacional minimo;
    JUSTO = ("justo", 2)  // investimento comunitario;
    EXCESSIVO = ("excessivo", 3)  // lucro alto desnecessario;
    PREDATORIO = ("predatorio", 4)  // exploracao (PROIBIDO);
typedef struct EstablishmentType {
    // Tipos de estabelecimento na Republica.
    SAUDE = "saude"  // hospital, clinica, posto;
    EDUCACAO = "educacao"  // escola, universidade;
    ALIMENTACAO = "alimentacao"  // restaurante, cozinha;
    AGRICULTURA = "agricultura"  // fazenda, horta;
    CONSTRUCAO = "construcao"  // obra, FabLab;
    SOFTWARE = "software"  // desenvolvimento;
    TRANSPORTE = "transporte"  // mobilidade;
    ENERGIA = "energia"  // geracao/distribuicao;
    VESTUARIO = "vestuario"  // costura, FabLab textil;
    LIMPEZA = "limpeza"  // servicos de limpeza;
    CULTURA = "cultura"  // musica, arte, midia;
    COMERCIO = "comercio"  // distribuicao, logistica;
    MANUTENCAO = "manutencao"  // reparo, conserto;
    SEGURANCA = "seguranca"  // patrulha, defesa;
    HOSPITALIDADE = "hospitalidade"  // hospedagem, acolhimento;
typedef struct SurplusDestination {
    // Para onde vai o excedente (no modo EXECUTAVEL).
    OPERACIONAL = "operacional"  // manter funcionando;
    INVESTIMENTO = "investimento"  // melhorar, crescer;
    RESERVA = "reserva"  // fundo de emergencia;
    COMUNITARIO = "comunitario"  // voltar para comunidade;
    PREDADOR_LUCRO = "lucro_predador"  // PROIBIDO: lucro do dono;
    PREDADOR_DIVIDENDO = "dividendo"  // PROIBIDO: acionistas;
// ============================================================================
// 2. METRICA DE EXCEDENTE POR ESTABELECIMENTO
// ============================================================================
// decorador: @dataclass
typedef struct SurplusMetric {
    // Metrica de excedente para um tipo de estabelecimento.
    Calcula: quanto excedente && NECESSARIO vs PREDATORIO.;
    FORMULA:;
    Producao_total = horas_trabalhadas * valor_hora;
    Custo_operacional = aluguel + equip + insumos + energia + manutencao;
    Excedente_necessario = custo_operacional / producao_total;
    Excedente_justo = investimento + reserva + comunitario;
    Excedente_predatorio = tudo que excede necessario + justo;
    Trabalhador recebe = horas * valor_hora - excedente;
    Se excedente_predatorio > 0: PROIBIDO.;
    //
    establishment_type: EstablishmentType;
    name: texto;
    // No modo EXECUTAVEL
    double custo_operacional_pct = 0.0 // % da producao gasto em operacao;
    double investimento_justo_pct = 0.0 // % para melhorar;
    double reserva_pct = 0.0 // % para emergencia;
    double comunitario_pct = 0.0 // % para comunidade;
    // No modo IDEAL
    char* ideal_equivalent = ""  // como funciona sem excedente;
    // Custo operacional detalhado
    double custo_aluguel_pct = 0.0;
    double custo_equipamento_pct = 0.0;
    double custo_insumos_pct = 0.0;
    double custo_energia_pct = 0.0;
    double custo_manutencao_pct = 0.0;
    // Limite predatorio
    double max_excedente_justo_pct = 0.0 // acima disso = predatorio;
    char* excedente_predatorio_exemplo = "";
    // decorador: @property
    double excedente_necessario_total(self) {
        return (self.custo_operacional_pct + self.investimento_justo_pct;
                + self.reserva_pct + self.comunitario_pct);
    // decorador: @property
    double max_predatorio_pct(self) {
        return maximo(0.0, 1.0 - self.excedente_necessario_total);
    // decorador: @property
    double trabalhador_recebe_pct(self) {
        // Quanto do que produz volta para o trabalhador.
        return 1.0 - self.excedente_necessario_total;
// ============================================================================
// 3. CATALOGO DE METRICAS POR ESTABELECIMENTO
// ============================================================================
[SurplusMetric] METRICS = [;
    SurplusMetric(;
        EstablishmentType.SAUDE, "Hospital/Clinica",;
        custo_operacional_pct = 0.35, // equip medico caro;
        investimento_justo_pct = 0.10, // pesquisa, melhorar;
        reserva_pct = 0.05, // emergencia medica;
        comunitario_pct = 0.10, // tratar quem ! pode pagar;
        custo_aluguel_pct = 0.10,;
        custo_equipamento_pct = 0.15, // ressonancia, laser, etc;
        custo_insumos_pct = 0.05, // remedios, material;
        custo_energia_pct = 0.03,;
        custo_manutencao_pct = 0.02,;
        max_excedente_justo_pct = 0.60, // acima de 60% = predatorio;
        ideal_equivalent = (;
            "Hospital = bem comum. OpenHealth Sirio-Libanes. ";
            "Custo operacional coberto pela Republica (trabalho base 1.0). ";
            "Sem excedente. Medico recebe 1.0/h + impacto (vidas).";
        ),;
        excedente_predatorio_exemplo = (;
            "Hospital particular cobra R$ 5000 cirurgia que custa R$ 500. ";
            "Excedente predatorio: 90%. PROIBIDO na Republica.";
        ),;
    ),;
    SurplusMetric(;
        EstablishmentType.EDUCACAO, "Escola/Universidade",;
        custo_operacional_pct = 0.25, // predio, laboratorios;
        investimento_justo_pct = 0.10, // novos cursos, pesquisa;
        reserva_pct = 0.03,;
        comunitario_pct = 0.12, // ensinar gratis;
        custo_aluguel_pct = 0.10,;
        custo_equipamento_pct = 0.08, // laboratorios, OpenTerminal;
        custo_insumos_pct = 0.04, // materiais;
        custo_energia_pct = 0.02,;
        custo_manutencao_pct = 0.01,;
        max_excedente_justo_pct = 0.50,;
        ideal_equivalent = (;
            "Educacao && DIREITO. OpenUniversity para todos. ";
            "Professor recebe 1.0/h + impacto (alunos * ripple). ";
            "Sem mensalidade. Sem excedente.";
        ),;
        excedente_predatorio_exemplo = (;
            "Faculdade particular cobra R$ 2000/mes. ";
            "Custo real R$ 500. Excedente: 75%. PROIBIDO.";
        ),;
    ),;
    SurplusMetric(;
        EstablishmentType.ALIMENTACAO, "Restaurante/Cozinha",;
        custo_operacional_pct = 0.40, // comida, gas, local;
        investimento_justo_pct = 0.05,;
        reserva_pct = 0.03,;
        comunitario_pct = 0.07, // alimentar quem ! pode;
        custo_aluguel_pct = 0.15,;
        custo_equipamento_pct = 0.05, // cozinha;
        custo_insumos_pct = 0.15, // ingredientes;
        custo_energia_pct = 0.03,;
        custo_manutencao_pct = 0.02,;
        max_excedente_justo_pct = 0.55,;
        ideal_equivalent = (;
            "Comida && DIREITO. OpenAgrarian produz ingredientes. ";
            "Cozinheiro recebe 1.0/h + impacto (pessoas alimentadas). ";
            "Restaurante comunitario. Sem excedente.";
        ),;
        excedente_predatorio_exemplo = (;
            "Restaurante de luxo: prato R$ 150 que custa R$ 20. ";
            "Excedente: 87%. Em parte justo (experiencia), ";
            "mas predatorio se trabalhador recebe mal.";
        ),;
    ),;
    SurplusMetric(;
        EstablishmentType.AGRICULTURA, "Fazenda/Horta",;
        custo_operacional_pct = 0.30, // sementes, agua, ferramentas;
        investimento_justo_pct = 0.08, // melhorarSolo, irrigacao;
        reserva_pct = 0.05, // safra pode falhar;
        comunitario_pct = 0.12, // alimentar comunidade;
        custo_aluguel_pct = 0.05, // terra (! existe aluguel no ideal);
        custo_equipamento_pct = 0.10, // trator, irrigacao;
        custo_insumos_pct = 0.10, // sementes, compostagem;
        custo_energia_pct = 0.03,;
        custo_manutencao_pct = 0.02,;
        max_excedente_justo_pct = 0.55,;
        ideal_equivalent = (;
            "Terra && bem comum. OpenAgrarian. ";
            "Agricultor recebe 1.0/h + impacto (toneladas * pessoas). ";
            "Sem latifundio. Sem excedente.";
        ),;
        excedente_predatorio_exemplo = (;
            "Latifundio: trabalhador rural recebe R$ 1000/mes. ";
            "Produz R$ 20000/mes em soja. Excedente: 95%. ESCRAVIDAO.";
        ),;
    ),;
    SurplusMetric(;
        EstablishmentType.SOFTWARE, "Desenvolvimento de Software",;
        custo_operacional_pct = 0.10, // servidor, energia;
        investimento_justo_pct = 0.10, // pesquisa, IA;
        reserva_pct = 0.03,;
        comunitario_pct = 0.17, // software livre para todos;
        custo_aluguel_pct = 0.00, // remoto;
        custo_equipamento_pct = 0.05, // computador;
        custo_insumos_pct = 0.00, // digital;
        custo_energia_pct = 0.03, // servidor;
        custo_manutencao_pct = 0.02,;
        max_excedente_justo_pct = 0.40,;
        ideal_equivalent = (;
            "Software && CC0. Programador recebe 1.0/h + impacto ";
            "(usuarios * ripple). Sem excedente. Sem patente.";
        ),;
        excedente_predatorio_exemplo = (;
            "Big Tech: programador recebe R$ 15000/mes mas gera ";
            "R$ 100000/mes em receita. Excedente: 85%. ";
            "Dono/acionista lucra sem trabalhar.";
        ),;
    ),;
    SurplusMetric(;
        EstablishmentType.CONSTRUCAO, "Construcao/FabLab",;
        custo_operacional_pct = 0.35, // materiais, ferramentas;
        investimento_justo_pct = 0.08, // novas maquinas;
        reserva_pct = 0.03,;
        comunitario_pct = 0.10, // construir para vulneraveis;
        custo_aluguel_pct = 0.05,;
        custo_equipamento_pct = 0.15, // maquinas FabLab;
        custo_insumos_pct = 0.10, // cimento, aco, madeira;
        custo_energia_pct = 0.03,;
        custo_manutencao_pct = 0.02,;
        max_excedente_justo_pct = 0.56,;
        ideal_equivalent = (;
            "Moradia && DIREITO. OpenDignity. ";
            "Pedreiro recebe 1.0/h + impacto (moradias * pessoas). ";
            "Sem construtora lucrando. Sem excedente.";
        ),;
        excedente_predatorio_exemplo = (;
            "Construtora: pedreiro recebe R$ 2500/mes. ";
            "Produz R$ 30000/mes em obra. Excedente: 92%. ";
            "Dono ! pede tijolo. Lucra sobre o trabalho.";
        ),;
    ),;
    SurplusMetric(;
        EstablishmentType.ENERGIA, "Geracao/Distribuicao de Energia",;
        custo_operacional_pct = 0.30, // manutencao painel/turbina;
        investimento_justo_pct = 0.10, // expandir rede;
        reserva_pct = 0.05,;
        comunitario_pct = 0.10, // energia para todos;
        custo_aluguel_pct = 0.00, // terra publica;
        custo_equipamento_pct = 0.15, // painel, turbina, bateria;
        custo_insumos_pct = 0.05,;
        custo_energia_pct = 0.00, // produz propria;
        custo_manutencao_pct = 0.10, // alto manutencao;
        max_excedente_justo_pct = 0.55,;
        ideal_equivalent = (;
            "Energia && bem comum. OpenSolar/OpenTurbine. ";
            "Tecnico recebe 1.0/h + impacto (kWh * pessoas). ";
            "Sem conta de luz. Sem excedente.";
        ),;
        excedente_predatorio_exemplo = (;
            "Concessionaria: cobra R$ 200/mes por energia que custa ";
            "R$ 20 para gerar. Excedente: 90%. Monopolio.";
        ),;
    ),;
    SurplusMetric(;
        EstablishmentType.TRANSPORTE, "Transporte/Mobilidade",;
        custo_operacional_pct = 0.35, // veiculo, combustivel, manutencao;
        investimento_justo_pct = 0.08,;
        reserva_pct = 0.03,;
        comunitario_pct = 0.10, // transporte gratis para todos;
        custo_aluguel_pct = 0.00,;
        custo_equipamento_pct = 0.15, // veiculos;
        custo_insumos_pct = 0.10, // combustivel/eletricidade;
        custo_energia_pct = 0.05,;
        custo_manutencao_pct = 0.05,;
        max_excedente_justo_pct = 0.56,;
        ideal_equivalent = (;
            "Mobilidade && DIREITO. OpenMobility. ";
            "Motorista recebe 1.0/h + impacto (passageiros * km). ";
            "Sem tarifa. Sem excedente.";
        ),;
        excedente_predatorio_exemplo = (;
            "Uber: motorista recebe 40% da corrida. ";
            "App fica com 60% sem dirigir. Excedente: 60%. Predatorio.";
        ),;
    ),;
    SurplusMetric(;
        EstablishmentType.VESTUARIO, "Costura/FabLab Textil",;
        custo_operacional_pct = 0.30, // tecido, maquina, local;
        investimento_justo_pct = 0.05,;
        reserva_pct = 0.03,;
        comunitario_pct = 0.10, // vestir quem ! tem;
        custo_aluguel_pct = 0.05,;
        custo_equipamento_pct = 0.10, // maquina de costura;
        custo_insumos_pct = 0.12, // tecido, linha;
        custo_energia_pct = 0.02,;
        custo_manutencao_pct = 0.01,;
        max_excedente_justo_pct = 0.48,;
        ideal_equivalent = (;
            "Roupa && DIREITO. OpenProduct. OpenShirt/OpenShoe. ";
            "Costureira recebe 1.0/h + impacto (pecas * pessoas). ";
            "Sem fast fashion. Sem excedente.";
        ),;
        excedente_predatorio_exemplo = (;
            "Shein/Zara: custo R$ 5, vende R$ 50, costureira recebe R$ 0.50/peca. ";
            "Excedente: 98%. Escravidao moderna.";
        ),;
    ),;
    SurplusMetric(;
        EstablishmentType.COMERCIO, "Comercio/Distribuicao",;
        custo_operacional_pct = 0.30, // armazem, transporte, perdas;
        investimento_justo_pct = 0.05,;
        reserva_pct = 0.05, // estoque pode estragar;
        comunitario_pct = 0.10,;
        custo_aluguel_pct = 0.10,;
        custo_equipamento_pct = 0.05,;
        custo_insumos_pct = 0.10,;
        custo_energia_pct = 0.03,;
        custo_manutencao_pct = 0.02,;
        max_excedente_justo_pct = 0.50,;
        ideal_equivalent = (;
            "Distribuicao && logistica. OpenMarketplace. ";
            "Operador recebe 1.0/h + impacto (itens * pessoas). ";
            "Sem atravessador. Sem excedente.";
        ),;
        excedente_predatorio_exemplo = (;
            "Atacadão: compra produtor R$ 1, vende R$ 5. ";
            "Excedente: 80%. Atravessador lucra sem produzir.";
        ),;
    ),;
];
// ============================================================================
// 4. CALCULO DE EXCEDENTE PARA UM ESTABELECIMENTO ESPECIFICO
// ============================================================================
// decorador: @dataclass
typedef struct SurplusCalculation {
    // Calculo de excedente para um estabelecimento real.
    calc_id: texto;
    establishment_type: EstablishmentType;
    establishment_name: texto;
    // Dados reais
    int workers = 1;
    double hours_per_worker_month = 160.0 // 40h/sem * 4;
    double value_per_hour = 0.0 // valor que cada hora gera;
    double worker_salary_month = 0.0 // quanto o trabalhador recebe;
    double establishment_revenue_month = 0.0 // receita total;
    double operational_cost_month = 0.0 // custo operacional real;
    // Resultados
    double production_total = 0.0 // valor total produzido;
    double worker_receives_total = 0.0 // total pago a trabalhadores;
    double surplus_extracted = 0.0 // excedente extraido;
    double surplus_pct = 0.0 // % de excedente;
    SurplusType surplus_type = SurplusType.NECESSARIO;
    // decorador: @property
    bool is_predatory(self) {
        return self.surplus_type in (SurplusType.EXCESSIVO, SurplusType.PREDATORIO);
// ============================================================================
// 5. MOTOR DE EXCEDENTE
// ============================================================================
typedef struct SurplusEngine {
    // Motor que calcula, classifica e regula excedente.
    COMO FUNCIONA:;
    1. MODO EXECUTAVEL (durante transicao):;
    - Estabelecimento PRECISA de algum excedente (custo operacional);
    - Republica calcula quanto && NECESSARIO vs PREDATORIO;
    - Limite definido por tipo de estabelecimento;
    - Acima do limite = PREDATORIO -> OpenAntiPredatory bloqueia;
    2. MODO IDEAL (Republica completa):;
    - Excedente ABOLIDO;
    - Trabalhador recebe 1.0/hora base + impacto;
    - Custo operacional coberto pela Republica (trabalho coletivo);
    - Sem dono lucrando. Sem mais-valia. Nunca.;
    FORMULA DE CLASSIFICACAO:;
    excedente_necessario = custo_operacional / producao;
    excedente_justo = necessario + investimento + reserva + comunitario;
    excedente_real = 1 - (salario_total / producao_total);
    Se excedente_real <= excedente_justo: NECESSARIO/JUSTO;
    Se excedente_real > excedente_justo: EXCESSIVO;
    Se excedente_real > max_justo: PREDATORIO;
    //
    void __init__(self) {
        self.metrics: {texto: SurplusMetric} = {
            m.establishment_type.value: m para m em METRICS;
        };
        self.calculations: {texto: SurplusCalculation} = {};
    {texto: qualquer} get_metric(self, est_type: EstablishmentType) {
        // Retorna metrica para um tipo de estabelecimento.
        m = self.metrics.get(est_type.value);
        if (! m) {
            return {"error": "Tipo ! encontrado"};
        return {;
            "tipo": m.name,;
            "excedente_necessario": "{m.excedente_necessario_total:.0%}",;
            "trabalhador_recebe": "{m.trabalhador_recebe_pct:.0%}",;
            "max_justo": "{m.max_excedente_justo_pct:.0%}",;
            "custos": {
                "operacional": "{m.custo_operacional_pct:.0%}",;
                "investimento": "{m.investimento_justo_pct:.0%}",;
                "reserva": "{m.reserva_pct:.0%}",;
                "comunitario": "{m.comunitario_pct:.0%}",;
            },;
            "detalhe_operacional": {
                "aluguel": "{m.custo_aluguel_pct:.0%}",;
                "equipamento": "{m.custo_equipamento_pct:.0%}",;
                "insumos": "{m.custo_insumos_pct:.0%}",;
                "energia": "{m.custo_energia_pct:.0%}",;
                "manutencao": "{m.custo_manutencao_pct:.0%}",;
            },;
            "limite_predatorio": "{m.max_excedente_justo_pct:.0%}",;
            "exemplo_predatorio": m.excedente_predatorio_exemplo,;
            "ideal_equivalent": m.ideal_equivalent,;
        };
    funcao calculate(self, est_type: EstablishmentType,
                establishment_name: texto,;
                workers: inteiro,;
                hours_per_worker_month: flutuante,;
                worker_salary_month: flutuante,;
                establishment_revenue_month: flutuante,;
                double operational_cost_month = 0.0;
                ) -> {texto: qualquer}:;
        // Calcula excedente de um estabelecimento real.
        m = self.metrics.get(est_type.value);
        if (! m) {
            return {"error": "Tipo ! encontrado"};
        production_total = establishment_revenue_month;
        worker_receives_total = workers * worker_salary_month;
        surplus_extracted = production_total - worker_receives_total - operational_cost_month;
        surplus_pct = surplus_extracted / maximo(production_total, 1);
        // Classificar
        max_justo = m.max_excedente_justo_pct;
        necessario = m.excedente_necessario_total;
        if (surplus_pct <= necessario) {
            surplus_type = SurplusType.NECESSARIO;
        } else if (surplus_pct <= max_justo) {
            surplus_type = SurplusType.JUSTO;
        } else if (surplus_pct <= max_justo + 0.15) {
            surplus_type = SurplusType.EXCESSIVO;
        } else {
            surplus_type = SurplusType.PREDATORIO;
        calc_id = hashlib.md5(;
            "{establishment_name}{datetime.now()}".encode()).hexdigest()[:8];
        calc = SurplusCalculation(;
            calc_id = calc_id, establishment_type=est_type,;
            establishment_name = establishment_name,;
            workers = workers,;
            hours_per_worker_month = hours_per_worker_month,;
            worker_salary_month = worker_salary_month,;
            establishment_revenue_month = establishment_revenue_month,;
            operational_cost_month = operational_cost_month,;
            production_total = production_total,;
            worker_receives_total = worker_receives_total,;
            surplus_extracted = surplus_extracted,;
            surplus_pct = surplus_pct,;
            surplus_type = surplus_type,;
        );
        self.calculations[calc_id] = calc;
        // Acao se predatorio
        action = "OK";
        if (surplus_type == SurplusType.PREDATORIO) {
            action = "BLOQUEADO (OpenAntiPredatory). Reduzir excedente.";
        } else if (surplus_type == SurplusType.EXCESSIVO) {
            action = "AVISO. Reduzir excedente || justificar.";
        return {;
            "calc_id": calc_id,;
            "estabelecimento": establishment_name,;
            "tipo": est_type.value,;
            "trabalhadores": workers,;
            "producao_total": "R$ {production_total:,.2f}",;
            "trabalhador_recebe_total": "R$ {worker_receives_total:,.2f}",;
            "custo_operacional": "R$ {operational_cost_month:,.2f}",;
            "excedente_extraido": "R$ {surplus_extracted:,.2f}",;
            "excedente_pct": "{surplus_pct:.0%}",;
            "classificacao": surplus_type.value[0],;
            "limite_justo": "{max_justo:.0%}",;
            "limite_necessario": "{necessario:.0%}",;
            "acao": action,;
            "cada_trabalhador": {
                "produz": "R$ {production_total/workers:,.2f}/mes",;
                "recebe": "R$ {worker_salary_month:,.2f}/mes",;
                "excedente_por_trabalhador": "R$ {(surplus_extracted)/max(workers,1):,.2f}/mes",;
                "razao_exploracao": "{(production_total/max(worker_receives_total,1)):.1f}x",;
            },;
            "message": (;
                "{establishment_name} ({est_type.value}): ";
                "excedente {surplus_pct:.0%} -> {surplus_type.value[0]}. ";
                "Cada trabalhador produz R$ {production_total/workers:,.0f}/mes ";
                "mas recebe R$ {worker_salary_month:,.0f}/mes ";
                "(razao: {(production_total/max(worker_receives_total,1)):.1f}x). ";
                "{'PREDATORIO! Reduzir.' if calc.is_predatory else 'Dentro do limite.'}";
            ),;
        };
    {texto: qualquer} ideal_mode_equivalent(self, est_type: EstablishmentType) {
        // Como funciona no modo IDEAL (sem excedente).
        m = self.metrics.get(est_type.value);
        if (! m) {
            return {"error": "! encontrado"};
        return {;
            "tipo": m.name,;
            "modo": "IDEAL (Republica completa)",;
            "excedente": "ZERO (abolido)",;
            "trabalhador_recebe": "1.0/hora base + impacto",;
            "custo_operacional": "Coberto pela Republica (trabalho coletivo)",;
            "sem_dono": "Ninguem lucra sobre trabalho alheio",;
            "ideal": m.ideal_equivalent,;
            "message": (;
                "No IDEAL: {m.name} opera SEM excedente. ";
                "Trabalhador recebe 1.0/h + impacto. ";
                "Custos cobertos coletivamente. ";
                "Sem exploracao. Sem mais-valia. Nunca.";
            ),;
        };
    [Dict] compare_all(self) {
        // Compara limites de excedente entre todos os tipos.
        return [;
            {
                "tipo": m.name,;
                "necessario": "{m.excedente_necessario_total:.0%}",;
                "max_justo": "{m.max_excedente_justo_pct:.0%}",;
                "trabalhador_recebe": "{m.trabalhador_recebe_pct:.0%}",;
                "acima_e_predatorio": "{m.max_excedente_justo_pct:.0%}",;
            };
            /* para m em self.metrics.values() */
        ];
    {texto: qualquer} stats(self) {
        predatory = soma(1 para c em self.calculations.values();
                        if c.is_predatory);
        return {;
            "tipos_cadastrados": sizeof(self.metrics),;
            "calculos_feitos": sizeof(self.calculations),;
            "predatorios_detectados": predatory,;
            "principio": "Excedente necessario sim. Predatorio NAO.",;
        };
// ============================================================================
// 6. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = SurplusEngine();
    printf("=" * 80);
    printf("  OPENSURPLUS -- METRICA DE EXCEDENTE POR ESTABELECIMENTO");
    printf("  Quanto excedente && NECESSARIO vs PREDATORIO?");
    printf("=" * 80);
    // === 1. METRICAS POR TIPO ===
    printf("\n\n  === 1. LIMITES DE EXCEDENTE POR TIPO ===\n");
    printf("  {'Tipo':<25} {'Necessario':>12} {'Max Justo':>12} {'Trab. recebe':>14} {'Acima &&':>10}");
    printf("  {'-'*75}");
    /* TODO: iterador C manual para c em engine.compare_all() */
        printf("  {c['tipo']:<25} {c['necessario']:>12} {c['max_justo']:>12} ";
            "{c['trabalhador_recebe']:>14} {c['acima_e_predatorio']:>10}");
    // === 2. DETALHE: HOSPITAL ===
    printf("\n\n  === 2. DETALHE: HOSPITAL/CLINICA ===\n");
    hosp = engine.get_metric(EstablishmentType.SAUDE);
    printf("  Excedente necessario: {hosp['excedente_necessario']}");
    printf("  Trabalhador recebe: {hosp['trabalhador_recebe']}");
    printf("  Limite predatorio: {hosp['limite_predatorio']}");
    printf("\n  Custo operacional:");
    /* para cada (k, v) em hosp["detalhe_operacional"].items(): */
        printf("    {k:<15} {v}");
    printf("\n  Exemplo predatorio: {hosp['exemplo_predatorio']}");
    printf("\n  Modo IDEAL: {hosp['ideal_equivalent']}");
    // === 3. CALCULOS REAIS ===
    printf("\n\n  === 3. CALCULOS DE ESTABELECIMENTOS REAIS ===\n");
    // Caso 1: Software -- Big Tech (predatorio)
    printf("\n  --- Big Tech (Software) ---");
    r1 = engine.calculate(;
        EstablishmentType.SOFTWARE, "TechCorp Ltda",;
        workers = 50, hours_per_worker_month=160,;
        worker_salary_month = 15000,;
        establishment_revenue_month = 5000000,;
        operational_cost_month = 500000,;
    );
    printf("  {r1['message']}");
    printf("  Cada trabalhador: produz {r1['cada_trabalhador']['produz']}, ";
        "recebe {r1['cada_trabalhador']['recebe']}, ";
        "razao {r1['cada_trabalhador']['razao_exploracao']}");
    // Caso 2: Construcao -- construtora (predatorio)
    printf("\n  --- Construtora ---");
    r2 = engine.calculate(;
        EstablishmentType.CONSTRUCAO, "Construtora Alfa",;
        workers = 20, hours_per_worker_month=176,;
        worker_salary_month = 2500,;
        establishment_revenue_month = 600000,;
        operational_cost_month = 210000,;
    );
    printf("  {r2['message']}");
    printf("  Razao exploracao: {r2['cada_trabalhador']['razao_exploracao']}");
    // Caso 3: Agricultura -- latifundio (predatorio)
    printf("\n  --- Latifundio ---");
    r3 = engine.calculate(;
        EstablishmentType.AGRICULTURA, "Fazenda Soja Ltda",;
        workers = 10, hours_per_worker_month=200,;
        worker_salary_month = 1200,;
        establishment_revenue_month = 200000,;
        operational_cost_month = 60000,;
    );
    printf("  {r3['message']}");
    // Caso 4: Saude -- hospital justo
    printf("\n  --- Hospital Comunitario ---");
    r4 = engine.calculate(;
        EstablishmentType.SAUDE, "Hospital Republica",;
        workers = 30, hours_per_worker_month=160,;
        worker_salary_month = 12000,;
        establishment_revenue_month = 600000,;
        operational_cost_month = 210000,;
    );
    printf("  {r4['message']}");
    // === 4. MODO IDEAL ===
    printf("\n\n  === 4. MODO IDEAL (sem excedente) ===\n");
    /* para et em [EstablishmentType.SAUDE, EstablishmentType.SOFTWARE, */
            EstablishmentType.AGRICULTURA]:;
        ideal = engine.ideal_mode_equivalent(et);
        printf("\n  {ideal['tipo']}:");
        printf("    Excedente: {ideal['excedente']}");
        printf("    Trabalhador: {ideal['trabalhador_recebe']}");
        printf("    {ideal['ideal'][:70]}...");
    // === 5. STATS ===
    printf("\n\n  === 5. ESTATISTICAS ===\n");
    s = engine.stats();
    /* para cada (k, v) em s.items(): */
        printf("  {k:<30} {v}");
    printf("\n{'='*80}");
    printf("  OpenSurplus: {s['tipos_cadastrados']} tipos, ";
        "{s['predatorios_detectados']} predatorios detectados.");
    printf("  {s['principio']}");
    printf("{'='*80}");

#endif // OPENSURPLUS_METRICA_DE_NECESSIDADE_DE_EXCEDENTE_POR_ESTABELECIMENTO_H
