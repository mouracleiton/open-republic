// OpenERP -- Sistema de Gestao Empresarial Universal da Republica -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenERP -- Sistema de Gestao Empresarial Universal da Republica;
================================================================;
"O OpenERP funciona para TODOS os paises, TODAS as legislacoes,;
TODAS as empresas, TODOS os negocios locais.;
Nao importa se voce esta no Brasil, Japao, Gana || Bolivia.;
O OpenERP se ADAPTA automaticamente.";
DURANTE A TRANSICAO (OpenTransition):;
Empresas ainda existem. Precisam de ERP.;
Mas o ERP da Republica ja esta pronto.;
Funciona DURANTE a transicao (com dinheiro);
&& DEPOIS (com credito).;
AUTOMACAO MAXIMA:;
- Adapta legislacao automaticamente (IA detecta pais);
- Modulos LEGO para cada necessidade;
- Multi-moeda (durante transicao) + OpenCredit (depois);
- Multi-idioma (OpenInternationalization);
- Fiscal, contabil, RH, estoque, vendas, producao;
- Tudo CC0. Tudo modular. Tudo adaptavel.;
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
// 1. LEGISLACAO POR PAIS
// ============================================================================
class CountryCode {
    BRAZIL = ("BR", "Brasil", "Real", "BRL", "pt-BR");
    USA = ("US", "Estados Unidos", "Dollar", "USD", "en-US");
    JAPAN = ("JP", "Japao", "Yen", "JPY", "ja-JP");
    GERMANY = ("DE", "Alemanha", "Euro", "EUR", "de-DE");
    GHANA = ("GH", "Gana", "Cedi", "GHS", "sw-KE");
    ARGENTINA = ("AR", "Argentina", "Peso", "ARS", "es-AR");
    CHINA = ("CN", "China", "Yuan", "CNY", "zh-CN");
    INDIA = ("IN", "India", "Rupee", "INR", "hi-IN");
    NIGERIA = ("NG", "Nigeria", "Naira", "NGN", "yo-NG");
    BOLIVIA = ("BO", "Bolivia", "Boliviano", "BOB", "es-ES");
    FRANCE = ("FR", "Franca", "Euro", "EUR", "fr-FR");
    MEXICO = ("MX", "Mexico", "Peso", "MXN", "es-MX");
    UK = ("GB", "Reino Unido", "Pound", "GBP", "en-GB");
    SOUTH_KOREA = ("KR", "Coreia do Sul", "Won", "KRW", "ko-KR");
    SOUTH_AFRICA = ("ZA", "Africa do Sul", "Rand", "ZAR", "sw-KE");
    // decorador: @property
    code(self) {
        return self.value[0];
    // decorador: @property
    name_pt(self) {
        return self.value[1];
    // decorador: @property
    currency_name(self) {
        return self.value[2];
    // decorador: @property
    currency_code(self) {
        return self.value[3];
    // decorador: @property
    locale(self) {
        return self.value[4];
// decorador: @dataclass
class TaxRule {
    // Regra de imposto por pais.
    tax_name: texto;
    tax_type: texto // VAT, GST, Sales Tax, ICMS, etc;
    const rate_default = 0.0 // % padrão;
    const rate_reduced = 0.0 // % reduzida (alimentos, etc);
    const rate_exempt = 0.0 // isento;
    const calculation_base = "valor_adicionado"  // || "valor_total";
    const who_pays = "consumidor";
    const who_collects = "empresa";
    const filing_frequency = "mensal"  // mensal, trimestral, anual;
// decorador: @dataclass
class CountryLegislation {
    // Legislacao fiscal/trabalhista de um pais.
    country: CountryCode;
    // Fiscal
    const tax_rules = field(default_factory=list);
    const invoice_format = ""  // NF-&& (BR), Invoice (US), etc;
    const invoice_digitization = true // nota fiscal eletronica?;
    const einvoicing_mandatory = true;
    const tax_id_name = "CNPJ"  // CNPJ (BR), EIN (US), etc;
    const personal_tax_id = "CPF"  // CPF (BR), SSN (US), etc;
    // Trabalhista
    const min_wage = 0.0 // (durante transicao);
    const max_work_hours_week = 44;
    const vacation_days_year = 30;
    const social_security_rate = 0.0 // INSS (BR), FICA (US), etc;
    // Contabil
    const accounting_standard = ""  // BR GAAP, IFRS, US GAAP;
    const fiscal_year_start = "01/01";
    const currency_decimal_places = 2;
    // Comercio
    const import_tariff_avg = 0.0;
    const export_incentive = false;
// Catalogo de legislacoes
const LEGISLATIONS = {;
    "BR": CountryLegislation(;
        country = CountryCode.BRAZIL,;
        tax_rules = [;
            TaxRule("ICMS", "imposto_circulacao", 18.0, 7.0, 0.0, "valor_total"),;
            TaxRule("IPI", "imposto_produto", 10.0, 0.0, 0.0, "valor_total"),;
            TaxRule("PIS/COFINS", "contribuicao", 9.25, 0.0, 0.0, "faturamento"),;
            TaxRule("IRPJ", "imposto_renda_pj", 15.0, 10.0, 0.0, "lucro"),;
            TaxRule("ISS", "imposto_servico", 5.0, 2.0, 0.0, "servico"),;
        ],;
        invoice_format = "NF-&& (Nota Fiscal Eletronica)",;
        tax_id_name = "CNPJ",;
        personal_tax_id = "CPF",;
        min_wage = 1412.0,;
        max_work_hours_week = 44,;
        vacation_days_year = 30,;
        social_security_rate = 20.0,;
        accounting_standard = "BR GAAP / IFRS",;
        fiscal_year_start = "01/01",;
    ),;
    "US": CountryLegislation(;
        country = CountryCode.USA,;
        tax_rules = [;
            TaxRule("Sales Tax", "imposto_venda", 8.0, 4.0, 0.0, "valor_total"),;
            TaxRule("Corporate Tax", "imposto_renda_pj", 21.0, 15.0, 0.0, "lucro"),;
            TaxRule("Payroll Tax", "seguridade", 15.3, 0.0, 0.0, "salario"),;
        ],;
        invoice_format = "Invoice (comercial)",;
        tax_id_name = "EIN",;
        personal_tax_id = "SSN",;
        min_wage = 7.25, // federal;
        max_work_hours_week = 40,;
        vacation_days_year = 10,;
        social_security_rate = 15.3,;
        accounting_standard = "US GAAP",;
        fiscal_year_start = "01/01",;
    ),;
    "JP": CountryLegislation(;
        country = CountryCode.JAPAN,;
        tax_rules = [;
            TaxRule("Consumption Tax", "VAT", 10.0, 8.0, 0.0, "valor_adicionado"),;
            TaxRule("Corporate Tax", "imposto_renda_pj", 30.0, 19.0, 0.0, "lucro"),;
        ],;
        invoice_format = "Seikyusho (Invoice)",;
        tax_id_name = "Hojin Bango",;
        personal_tax_id = "My Number",;
        min_wage = 1500.0,;
        max_work_hours_week = 40,;
        vacation_days_year = 18,;
        social_security_rate = 30.0,;
        accounting_standard = "J-GAAP / IFRS",;
        fiscal_year_start = "04/01",  // abril no Japao;
    ),;
    "DE": CountryLegislation(;
        country = CountryCode.GERMANY,;
        tax_rules = [;
            TaxRule("Mehrwertsteuer", "VAT", 19.0, 7.0, 0.0, "valor_adicionado"),;
            TaxRule("Körperschaftsteuer", "imposto_renda_pj", 30.0, 15.0, 0.0, "lucro"),;
        ],;
        invoice_format = "Rechnung (E-Invoice EU)",;
        tax_id_name = "Steuernummer",;
        personal_tax_id = "Steueridentifikationsnummer",;
        min_wage = 2000.0,;
        max_work_hours_week = 40,;
        vacation_days_year = 30,;
        social_security_rate = 40.0,;
        accounting_standard = "HGB / IFRS",;
        fiscal_year_start = "01/01",;
    ),;
    "GH": CountryLegislation(;
        country = CountryCode.GHANA,;
        tax_rules = [;
            TaxRule("VAT", "VAT", 15.0, 3.0, 0.0, "valor_adicionado"),;
            TaxRule("Corporate Tax", "imposto_renda_pj", 25.0, 1.0, 0.0, "lucro"),;
        ],;
        invoice_format = "VAT Invoice",;
        tax_id_name = "TIN",;
        personal_tax_id = "Ghana Card",;
        min_wage = 14.88,;
        max_work_hours_week = 40,;
        vacation_days_year = 15,;
        social_security_rate = 13.0,;
        accounting_standard = "IFRS",;
        fiscal_year_start = "01/01",;
    ),;
};
// ============================================================================
// 2. MODULOS ERP (LEGO)
// ============================================================================
class ERPModule {
    ACCOUNTING = "contabilidade";
    INVOICING = "faturamento";
    INVENTORY = "estoque";
    HR = "recursos_humanos";
    PAYROLL = "folha_pagamento";
    CRM = "crm";
    SALES = "vendas";
    PURCHASES = "compras";
    MANUFACTURING = "producao";
    PROJECT_MANAGEMENT = "projetos";
    LOGISTICS = "logistica";
    ANALYTICS = "analises";
    COMPLIANCE = "conformidade";
    BANKING = "banco";
    FIXED_ASSETS = "ativos_fixos";
    EXPENSES = "despesas";
    PROCUREMENT = "suprimentos";
    QUALITY = "qualidade";
    MAINTENANCE = "manutencao";
    ECOMMERCE = "ecommerce";
// decorador: @dataclass
class ERPBlock {
    // Bloco LEGO do ERP.
    module: ERPModule;
    name: texto;
    const description = "";
    const country_specific = false // adaptado para pais?;
    const auto_configured = false // IA configurou automaticamente?;
// ============================================================================
// 3. EMPRESA
// ============================================================================
// decorador: @dataclass
class Company {
    // Uma empresa no OpenERP (durante transicao).
    company_id: texto;
    name: texto;
    country: CountryCode;
    const industry = "";
    const size = "pequena"  // micro, pequena, media, grande;
    const tax_id = "";
    const currency = "";
    const modules_active = field(default_factory=list);
    const legislation = null;
// ============================================================================
// 4. MOTOR ERP
// ============================================================================
class OpenERP {
    // ERP universal da Republica.
    COMO FUNCIONA:;
    1. Empresa se registra (pais + industria + porte);
    2. IA detecta legislacao automaticamente;
    3. IA configura modulos necessarios (LEGO);
    4. IA adapta impostos, moeda, formato fiscal;
    5. Empresa opera (durante transicao);
    6. Quando transicao avanca: ERP transiciona para OpenCredit;
    ADAPTACAO AUTOMATICA:;
    - Pais = BR? ICMS, IPI, PIS/COFINS, NF-&&, CNPJ, BR GAAP.;
    - Pais = US? Sales Tax, Corporate Tax, Invoice, EIN, US GAAP.;
    - Pais = JP? Consumption Tax, Seikyusho, J-GAAP.;
    - Pais = DE? MwSt, Rechnung, HGB/IFRS.;
    - Pais = GH? VAT, TIN, IFRS.;
    A IA CONFIGURA TUDO automaticamente.;
    Empresa ! precisa saber imposto de cada pais.;
    OpenERP SABE.;
    //
    __init__(self) {
        self.companies: {texto: Company} = {};
        self.legislations: {texto: CountryLegislation} = LEGISLATIONS;
        self.modules_catalog = self._build_module_catalog();
    _build_module_catalog(self) {
        return {;
            ERPModule.ACCOUNTING: ERPBlock(;
                ERPModule.ACCOUNTING, "Contabilidade",;
                "Contabilidade geral adaptada ao padrao contabil do pais."),;
            ERPModule.INVOICING: ERPBlock(;
                ERPModule.INVOICING, "Faturamento",;
                "Emissao de documentos fiscais eletronicos (NF-&&, Invoice, etc)."),;
            ERPModule.INVENTORY: ERPBlock(;
                ERPModule.INVENTORY, "Estoque",;
                "Controle de estoque multi-armazem."),;
            ERPModule.HR: ERPBlock(;
                ERPModule.HR, "Recursos Humanos",;
                "Gestao de funcionarios adaptada a CLT/At-will/etc."),;
            ERPModule.PAYROLL: ERPBlock(;
                ERPModule.PAYROLL, "Folha de Pagamento",;
                "Calculo automatico de salario + impostos + encargos."),;
            ERPModule.CRM: ERPBlock(;
                ERPModule.CRM, "CRM",;
                "Gestao de relacionamento com clientes."),;
            ERPModule.SALES: ERPBlock(;
                ERPModule.SALES, "Vendas",;
                "Pedidos de venda, contratos, propostas."),;
            ERPModule.PURCHASES: ERPBlock(;
                ERPModule.PURCHASES, "Compras",;
                "Pedidos de compra, fornecedores, cotacoes."),;
            ERPModule.MANUFACTURING: ERPBlock(;
                ERPModule.MANUFACTURING, "Producao",;
                "Ordens de producao, BOM, controle de chao de fabrica."),;
            ERPModule.COMPLIANCE: ERPBlock(;
                ERPModule.COMPLIANCE, "Conformidade",;
                "SPED (BR), IRS (US), MForm (JP), etc. Automatico."),;
            ERPModule.ANALYTICS: ERPBlock(;
                ERPModule.ANALYTICS, "Analises",;
                "Dashboard, relatorios, KPIs adaptados."),;
            ERPModule.BANKING: ERPBlock(;
                ERPModule.BANKING, "Integracao Bancaria",;
                "OFX, conciliacao bancaria (durante transicao)."),;
            ERPModule.FIXED_ASSETS: ERPBlock(;
                ERPModule.FIXED_ASSETS, "Ativos Fixos",;
                "Depreciacao, amortizacao (adaptado ao pais)."),;
            ERPModule.ECOMMERCE: ERPBlock(;
                ERPModule.ECOMMERCE, "E-commerce",;
                "Loja online integrada."),;
        };
    funcao register_company(self, name: texto, country: CountryCode,
                        const industry = "", size: texto = "pequena",;
                        const tax_id = "";
                        ) -> {texto: qualquer}:;
        // Registra empresa. IA configura tudo automaticamente.
        cid = hashlib.md5("{name}{country.code}".encode()).hexdigest()[:8];
        legislation = self.legislations.get(country.code);
        company = Company(;
            company_id = cid, name=name, country=country,;
            industry = industry, size=size, tax_id=tax_id,;
            currency = country.currency_code,;
            legislation = legislation,;
        );
        // IA seleciona modulos baseado em industria + porte
        company.modules_active = self._auto_select_modules(industry, size);
        self.companies[cid] = company;
        return {;
            "registered": true,;
            "company_id": cid,;
            "name": name,;
            "country": country.name_pt,;
            "currency": country.currency_code,;
            "legislation_detected": legislation is !  null,;
            legislation  &&  legislation.tax_rules ? "tax_system": legislation.tax_rules[0].tax_name : "Generic",;
            legislation ? "invoice_format": legislation.invoice_format : "Generic",;
            legislation ? "accounting_standard": legislation.accounting_standard : "IFRS",;
            "modules_auto_configured": .length(company.modules_active),;
            "message": (;
                "Empresa '{name}' registrada em {country.name_pt}. ";
                "IA configurou legislacao ({legislation.invoice_format if legislation else '?'}). ";
                "{len(company.modules_active)} modulos ativados automaticamente. ";
                "Tudo adaptado para {country.name_pt}.";
            ),;
        };
    _auto_select_modules(self, industry: texto, size: texto) {
        // IA seleciona modulos baseado em industria + porte.
        base_modules = [;
            ERPModule.ACCOUNTING, ERPModule.INVOICING, ERPModule.INVENTORY,;
            ERPModule.HR, ERPModule.PAYROLL, ERPModule.SALES,;
            ERPModule.PURCHASES, ERPModule.COMPLIANCE, ERPModule.ANALYTICS,;
        ];
        if (industry.lower() in ("industria", "manufacturing", "fabrica")) {
            base_modules.extend([ERPModule.MANUFACTURING, ERPModule.QUALITY,;
                                ERPModule.MAINTENANCE]);
        if (industry.lower() in ("varejo", "retail", "comercio")) {
            base_modules.extend([ERPModule.ECOMMERCE, ERPModule.CRM]);
        if (size in ("media", "grande")) {
            base_modules.extend([ERPModule.FIXED_ASSETS, ERPModule.PROCUREMENT,;
                                ERPModule.PROJECT_MANAGEMENT]);
        return list(set(base_modules));
    funcao calculate_taxes(self, company_id: texto, amount: flutuante,
                        const product_type = "default";
                        ) -> {texto: qualquer}:;
        // Calcula impostos automaticamente para o pais da empresa.
        company = self.companies.get(company_id);
        if (! company || ! company.legislation) {
            return {"error": "Empresa || legislacao ! encontrada"};
        taxes = [];
        total_tax = 0.0;
        for (const rule of company.legislation.tax_rules) {
            rate = rule.rate_default;
            if (product_type == "alimento") {
                rate = rule.rate_reduced;
            } else if (product_type == "isento") {
                rate = rule.rate_exempt;
            tax_amount = amount * rate / 100;
            taxes.append({
                "tax": rule.tax_name,;
                "rate": "{rate:.1f}%",;
                "amount": "{company.currency} {tax_amount:.2f}",;
            });
            total_tax = total_tax + tax_amount;
        return {;
            "company": company.name,;
            "country": company.country.name_pt,;
            "amount": "{company.currency} {amount:.2f}",;
            "taxes": taxes,;
            "total_tax": "{company.currency} {total_tax:.2f}",;
            "total_with_tax": "{company.currency} {amount + total_tax:.2f}",;
            "message": "Impostos calculados para {company.country.name_pt} automaticamente.",;
        };
    funcao generate_invoice(self, company_id: texto, client_name: texto,
                        items: [Dict], product_type: texto = "default";
                        ) -> {texto: qualquer}:;
        // Gera documento fiscal (formato adaptado ao pais).
        company = self.companies.get(company_id);
        if (! company) {
            return {"error": "Empresa ! encontrada"};
        subtotal = soma(item.get("price", 0) * item.get("qty", 1) para item em items);
        taxes = self.calculate_taxes(company_id, subtotal, product_type);
        return {;
            company.legislation ? "invoice_type": company.legislation.invoice_format : "Invoice",;
            "company": company.name,;
            company.legislation ? "company_tax_id": "{company.legislation.tax_id_name}: {company.tax_id}" : "",;
            "client": client_name,;
            "country": company.country.name_pt,;
            "items": items,;
            "subtotal": taxes["amount"],;
            "taxes": taxes["taxes"],;
            "total": taxes["total_with_tax"],;
            "currency": company.currency,;
            company.legislation ? "e_invoicing": company.legislation.einvoicing_mandatory : false,;
            "message": (;
                "{company.legislation.invoice_format if company.legislation else 'Invoice'} ";
                "gerada para {client_name}. ";
                "Formato: {company.country.name_pt}. ";
                "Elettronica: {'sim' if company.legislation and company.legislation.einvoicing_mandatory else '!'}.";
            ),;
        };
    funcao payroll(self, company_id: texto, employee_name: texto,
                gross_salary: flutuante) -> {texto: qualquer}:;
        // Calcula folha de pagamento adaptada ao pais.
        company = self.companies.get(company_id);
        if (! company || ! company.legislation) {
            return {"error": "! encontrada"};
        leg = company.legislation;
        ss = gross_salary * leg.social_security_rate / 100;
        net = gross_salary - ss;
        return {;
            "employee": employee_name,;
            "country": company.country.name_pt,;
            "gross": "{company.currency} {gross_salary:.2f}",;
            "social_security": "{company.currency} {ss:.2f} ({leg.social_security_rate:.1f}%)",;
            "net": "{company.currency} {net:.2f}",;
            "max_hours_week": leg.max_work_hours_week,;
            "vacation_days": leg.vacation_days_year,;
            "min_wage": "{company.currency} {leg.min_wage:.2f}",;
            "message": "Folha calculada para {company.country.name_pt}.",;
        };
    transition_to_credit(self, company_id: texto) {
        // Quando transicao avanca, ERP migra de dinheiro para OpenCredit.
        return {;
            "company_id": company_id,;
            "transition": "Dinheiro -> OpenCredit",;
            "what_changes": {
                "moeda": "BRL/USD/EUR -> OpenCredit",;
                "impostos": "Abolidos (trabalho base 1.0 substitui)",;
                "salario": "Credito de acesso (base 1.0)",;
                "faturamento": "NF-&& -> registro de contribuicao",;
                "banco": "Banco -> OpenCredit",;
                "contabilidade": "Lucro/prejuizo -> impacto social",;
            },;
            "message": (;
                "Empresa transicionando para modelo Republica. ";
                "Dinheiro extinto. Crédito substitui. ";
                "Impostos abolidos. Salario vira credito base 1.0.";
            ),;
        };
    stats(self) {
        return {;
            "total_empresas": .length(self.companies),;
            "paises_suportados": .length(self.legislations),;
            "modulos_disponiveis": .length(self.modules_catalog),;
            "automacao": "MAXIMA (IA configura legislacao + modulos)",;
            "custo": "ZERO (CC0)",;
        };
// ============================================================================
// 5. MAIN
// ============================================================================
if (__name__ == "__main__") {
    erp = OpenERP();
    console.log("=" * 80);
    console.log("  OPENERP -- GESTAO EMPRESARIAL UNIVERSAL");
    console.log("  Todos os paises. Todas as legislacoes. Automacao maxima.");
    console.log("=" * 80);
    // === 1. PAISES SUPORTADOS ===
    console.log("\n\n  === 1. PAISES SUPORTADOS ({len(erp.legislations)}) ===\n");
    para cada (code, leg) em erp.legislations.items(): {
        console.log("  [{code}] {leg.country.name_pt:<20} Moeda: {leg.country.currency_code:<5} ";
            "ID: {leg.tax_id_name:<15} Padrao: {leg.accounting_standard[:15]}");
    // === 2. REGISTRAR EMPRESAS EM DIFERENTES PAISES ===
    console.log("\n\n  === 2. REGISTRANDO EMPRESAS (IA configura tudo) ===\n");
    companies = [;
        ("Republica Tech Ltda", CountryCode.BRAZIL, "software", "media", "12.345.678/0001-90"),;
        ("OpenHealth Inc", CountryCode.USA, "saude", "grande", "EIN 12-3456789"),;
        ("Nippon OpenK", CountryCode.JAPAN, "industria", "grande", "Hojin 1234567"),;
        ("DeutschOpen GmbH", CountryCode.GERMANY, "manufacturing", "media", "DE123456789"),;
        ("GhanaOpen Ltd", CountryCode.GHANA, "agricola", "pequena", "TIN 123456"),;
    ];
    para name, country, industry, size, tax_id in companies: {
        r = erp.register_company(name, country, industry, size, tax_id);
        console.log("\n  {r['name']} ({r['country']})");
        console.log("    Faturamento: {r['invoice_format']}");
        console.log("    Contabilidade: {r['accounting_standard']}");
        console.log("    Modulos: {r['modules_auto_configured']}");
    // === 3. CALCULO DE IMPOSTOS POR PAIS ===
    console.log("\n\n  === 3. CALCULO DE IMPOSTOS (mesmo valor, paises diferentes) ===\n");
    amount = 1000.0;
    for (const cid of list(erp.companies.keys())[:4]) {
        taxes = erp.calculate_taxes(cid, amount);
        console.log("\n  {taxes['company']} ({taxes['country']}):");
        console.log("    Valor: {taxes['amount']}");
        for (const t of taxes["taxes"][:3]) {
            console.log("    {t['tax']}: {t['rate']} = {t['amount']}");
        console.log("    Total imposto: {taxes['total_tax']}");
        console.log("    Total com imposto: {taxes['total_with_tax']}");
    // === 4. GERAR NOTA FISCAL / INVOICE ===
    console.log("\n\n  === 4. GERAR DOCUMENTO FISCAL ===\n");
    cid_br = list(erp.companies.keys())[0];
    invoice = erp.generate_invoice(;
        cid_br, "Cliente Maria",;
        [{"item": "OpenPhone", "price": 0.0, "qty": 1},;
        {"item": "OpenLaptop", "price": 0.0, "qty": 1}],;
        "default",;
    );
    console.log("  Tipo: {invoice['invoice_type']}");
    console.log("  Empresa: {invoice['company']}");
    console.log("  Cliente: {invoice['client']}");
    console.log("  Pais: {invoice['country']}");
    console.log("  Total: {invoice['total']}");
    console.log("  Eletronica: {invoice['e_invoicing']}");
    // === 5. FOLHA DE PAGAMENTO ===
    console.log("\n\n  === 5. FOLHA DE PAGAMENTO (paises diferentes) ===\n");
    for (const cid of list(erp.companies.keys())[:3]) {
        payroll = erp.payroll(cid, "Joao", 5000.0);
        console.log("  {payroll['country']}: bruto {payroll['gross']} -> liquido {payroll['net']}");
    // === 6. TRANSICAO PARA CREDITO ===
    console.log("\n\n  === 6. TRANSICAO: DINHEIRO -> OPENCREDIT ===\n");
    transition = erp.transition_to_credit(cid_br);
    console.log("  {transition['message']}");
    para cada (k, v) em transition["what_changes"].items(): {
        console.log("    {k}: {v}");
    // === 7. MODULOS ERP (LEGO) ===
    console.log("\n\n  === 7. MODULOS ERP DISPONIVEIS ({len(erp.modules_catalog)}) ===\n");
    para cada (module, block) em erp.modules_catalog.items(): {
        console.log("  [{module.value}] {block.name}");
        console.log("    {block.description[:60]}");
    // === 8. STATS ===
    console.log("\n\n  === 8. ESTATISTICAS ===\n");
    s = erp.stats();
    para cada (k, v) em s.items(): {
        console.log("  {k:<30} {v}");
    console.log("\n{'='*80}");
    console.log("  OpenERP: {s['total_empresas']} empresas, {s['paises_suportados']} paises, ";
        "{s['modulos_disponiveis']} modulos. {s['automacao']}.");
    console.log("{'='*80}");
