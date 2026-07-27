// TEIA Terminal -- Stack Definitiva + Esqueleto -- gerado de Portugol++
package teia_terminal_stack_definitiva_esqueleto

import "fmt"

// !/usr/bin/env python3
//
TEIA Terminal -- Stack Definitiva + Esqueleto
================================================
STACK ESCOLHIDA (justificada):
================================
FRONTEND: FastAPI + Jinja2 + HTMX + Tailwind CSS + Alpine.js
BACKEND: FastAPI (Python 3.11+) + Uvicorn
DADOS: DuckDB (analitico) + SQLite (operacional)
VPN: WireGuard
AUTH: JWT + RBAC por certificacao
DEPLOY: Docker + VPS Hetzner
FUTURO: Migrar core para Rust (Leptos + Axum) apos validacao
POR QUE ! STREAMLIT:
Streamlit && prototipo. Recarrega pagina inteira. Sem RBAC granular.
Sem command palette. Sem UX de terminal. Sem VPN nativa.
POR QUE ! REACT/SPA:
JavaScript. Usuario quer eliminar JS. SPA adiciona complexidade.
HTMX da interatividade sem JS client-side.
POR QUE FASTAPI + HTMX:
1. Python (prototipo rapido, alinha com politica Python->Rust)
2. HTMX = interatividade sem JavaScript (HTML over the wire)
3. Server-rendered = SEO + performance + simplicidade
4. Tailwind = dark terminal aesthetic em minutos
5. Alpine.js = micro-interacoes (dropdowns, modals) sem framework
6. DuckDB = queries analiticas em bilhoes de rows sem PostgreSQL
7. Migration path: Jinja2 -> Askama (Rust), HTMX continua igual
ESTRUTURA DE ARQUIVOS:
================================
teia-terminal/
    main.py // FastAPI app
    config.py // Configuracao
    auth.py // JWT + RBAC
    modules.py // Modulos + certificacao + acesss
    data/
    duckdb // Banco analitico
    sqlite.db // Banco operacional (users, billing, logs)
    templates/ // Jinja2 HTML
    base.html // Layout base (dark terminal)
    dashboard.html // Dashboard principal
    dossie.html // Gerador de dossies
    simulador.html // Simulador de impacto
    admin.html // Painel admin (TEIA direto)
    static/
    css/
        terminal.css // Tema dark Bloomberg-like
    js/
        htmx.minimo.js // HTMX
        alpine.minimo.js // Alpine.js
Author: TEIA / OpenRepublic Team
//
// importa annotations de __future__
// importa json
// importa hashlib
// importa time
// importa datetime, timedelta de datetime
// importa Any, Dict, List, Optional de typing
// importa dataclass, field de dataclasses
// importa Enum de enum
// importa Path de pathlib
// importa FastAPI, Request, Response, HTTPException, Depends, status de fastapi
// importa StaticFiles de fastapi.staticfiles
// importa Jinja2Templates de fastapi.templating
// importa HTMLResponse, JSONResponse, RedirectResponse de fastapi.responses
// importa HTTPBearer, HTTPAuthorizationCredentials de fastapi.security
// importa BaseModel de pydantic
// ============================================================================
// 1. CONFIG
// ============================================================================
TEIA_VERSION = "0.1.0"
TEIA_ENV = "development"  // production quando em VPN
// ============================================================================
// 2. AUTH + RBAC (baseado no teia_terminal_economy.py)
// ============================================================================
type CertLevel int
const (
    NONE = 0
    BASE = 1
    ANALISTA = 2
    ESPECIALISTA = 3
    TEIA_DIRETO = 99 // acesso total
// decorador: @dataclass
type User struct {
    user_id: texto
    name: texto
    email: texto
    cert_level: CertLevel
    is_teia_direct := false // bool
    is_active := true // bool
    vpn_key_active := true // bool
    monthly_paid := true // bool
    artifacts_generated := 0 // int64
    revenue_generated := 0.0 // float64
    joined_at := field(default_factory=time.time) // float64
// Modulos e requisitos (do teia_terminal_economy.py)
MODULES = {
    "fome":             {"name": "Segurança Alimentar",      "cert": CertLevel.BASE,        "sensitive": false, "teia_only": false},
    "saneamento":       {"name": "Saneamento",              "cert": CertLevel.BASE,        "sensitive": false, "teia_only": false},
    "emprego":          {"name": "Emprego (CAGED)",          "cert": CertLevel.BASE,        "sensitive": false, "teia_only": false},
    "educacao":         {"name": "Educação (INEP)",          "cert": CertLevel.BASE,        "sensitive": false, "teia_only": false},
    "impacto_fiscal":   {"name": "Impacto Fiscal (35 pol.)",  "cert": CertLevel.ANALISTA,    "sensitive": false, "teia_only": false},
    "simulador":        {"name": "Simulador de Cenários",     "cert": CertLevel.ANALISTA,    "sensitive": false, "teia_only": false},
    "negativados":      {"name": "Negativados (SPC)",        "cert": CertLevel.ANALISTA,    "sensitive": false, "teia_only": false},
    "due_diligence":    {"name": "Due Diligence",            "cert": CertLevel.ESPECIALISTA,"sensitive": false, "teia_only": false},
    "parecer_juridico": {"name": "Parecer Jurídico-Político", "cert": CertLevel.ESPECIALISTA,"sensitive": false, "teia_only": false},
    "juros_spread":     {"name": "Juros && Spread Bancário",  "cert": CertLevel.ESPECIALISTA, "sensitive": false, "teia_only": false},
    "comunidades_reais":{"name": "Comunidades Reais",        "cert": CertLevel.ESPECIALISTA,"sensitive": true,  "teia_only": true},
    "saude_individual": {"name": "Saúde Individual",         "cert": CertLevel.ESPECIALISTA,"sensitive": true,  "teia_only": true},
    "banco_palmas":     {"name": "Dados Banco Palmas",       "cert": CertLevel.ESPECIALISTA,"sensitive": true,  "teia_only": true},
    "open_credit":      {"name": "OpenCredit",               "cert": CertLevel.ESPECIALISTA,"sensitive": false, "teia_only": true},
}
func check_module_access(user: User, module_id: texto) {texto: qualquer} {
    // Verifica acesso do usuário a um módulo.
    mod = MODULES.get(module_id)
    if ! mod {
        return {"allowed": false, "reason": "Módulo '{module_id}' não existe."}
    if user.is_teia_direct {
        return {"allowed": true, "reason": "TEIA direto."}
    if mod["sensitive"] {
        return {
            "allowed": false,
            "reason": "DADO SENSÍVEL. '{mod['name']}' é restrito à equipe TEIA. LGPD/sigilo."
        }
    if mod["teia_only"] {
        return {
            "allowed": false,
            "reason": "'{mod['name']}' é operação interna TEIA. Contrate TEIA direto."
        }
    if user.cert_level.value < mod["cert"].value {
        return {
            "allowed": false,
            "reason": "'{mod['name']}' requer certificação {mod['cert'].name}. Faça treinamento."
        }
    if ! user.vpn_key_active {
        return {"allowed": false, "reason": "VPN inativa. Renove mensalidade."}
    if ! user.monthly_paid {
        return {"allowed": false, "reason": "Mensalidade em atraso. Regularize."}
    return {"allowed": true, "reason": "Acesso autorizado."}
// ============================================================================
// 3. USUÁRIOS DEMO
// ============================================================================
USERS = {
    "cleiton": User(
        user_id = "cleiton", name="Cleiton", email="cleiton@teia.dev",
        cert_level = CertLevel.TEIA_DIRETO, is_teia_direct=true,
    ),
    "demo_base": User(
        user_id = "demo_base", name="Revendedor Base", email="base@demo.com",
        cert_level = CertLevel.BASE,
    ),
    "demo_analista": User(
        user_id = "demo_analista", name="Revendedor Analista", email="analista@demo.com",
        cert_level = CertLevel.ANALISTA,
    ),
    "demo_espec": User(
        user_id = "demo_espec", name="Revendedor Especialista", email="espec@demo.com",
        cert_level = CertLevel.ESPECIALISTA,
    ),
}
// ============================================================================
// 4. DADOS (simulados para Gate D -- depois conecta DuckDB real)
// ============================================================================
DADOS = {
    "fome": {
        "inseguranca_grave_milhoes": 33.8,
        "inseguranca_total_pct": 58.7,
        "fonte": "VIGISAN/IBGE 2022",
        "paa_orcamento_2023_mi": 500,
        "paa_pico_2012_bi": 2.4,
        "multiplicador_paa": 3.0,
    },
    "saneamento": {
        "sem_agua_milhoes": 35,
        "sem_esgoto_milhoes": 100,
        "esgoto_tratado_pct": 50,
        "investimento_necessario_bi": 700,
        "multiplicador_saude": 4.0,
        "fonte": "SNIS 2023",
    },
    "negativados": {
        "total_milhoes": 63.1,
        "ate_2sm_pct": 77,
        "divida_media": 4515,
        "cartao_rotativo_pct": 78,
        "fonte": "SPC/Peic 2024",
    },
    "juros_spread": {
        "juros_divida_bi": 950.4,
        "impacto_1pp_selic_bi": 31.4,
        "divida_pib_pct": 80.4,
        "carga_tributaria_pct": 32.2,
        "fonte": "Bacen/STN 2024",
    },
    "impacto_fiscal": {
        "saude_bi": 231,
        "educacao_bi": 208,
        "bolsa_familia_bi": 170,
        "bolsa_familia_familias_m": 21,
        "fonte": "LOA 2024",
    },
}
// ============================================================================
// 5. DADOS VALIDADOS (Gate A)
// ============================================================================
VALIDACOES_GATE_A = [
    {"claim": "33.8M em insegurança alimentar grave", "valor": 33.8, "oficial": 33.8, "fonte": "VIGISAN/IBGE 2022", "status": "EXATO"},
    {"claim": "35M sem água tratada", "valor": 35, "oficial": 35, "fonte": "SNIS 2023", "status": "EXATO"},
    {"claim": "100M sem coleta de esgoto", "valor": 100, "oficial": 100, "fonte": "SNIS 2023", "status": "EXATO"},
    {"claim": "63.1M negativados", "valor": 63, "oficial": 63.1, "fonte": "SPC/Peic 2024", "status": "ACEITÁVEL"},
    {"claim": "Juros R$950.4bi", "valor": 950.4, "oficial": 950.4, "fonte": "STN 2024", "status": "EXATO"},
    {"claim": "1pp Selic = R$31.4bi", "valor": 31.4, "oficial": 31.4, "fonte": "Bacen 2024", "status": "EXATO"},
]
// ============================================================================
// 6. FASTAPI APP
// ============================================================================
app = FastAPI(title="TEIA Terminal", version=TEIA_VERSION)
// Static e templates (quando rodar local, cria diretorios)
BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"
// Criar diretorios se nao existem
TEMPLATES_DIR.mkdir(exist_ok=true)
STATIC_DIR.mkdir(exist_ok=true)
(STATIC_DIR / "css").mkdir(exist_ok=true)
(STATIC_DIR / "js").mkdir(exist_ok=true)
templates = Jinja2Templates(directory=texto(TEMPLATES_DIR))
app.mount("/static", StaticFiles(directory=texto(STATIC_DIR)), name="static")
// Simular sessão (em producao: JWT cookie)
_current_user_id := "cleiton"  // default: Cleiton (TEIA direto) // texto?
func get_current_user() User {
    if _current_user_id && _current_user_id in USERS {
        return USERS[_current_user_id]
    lance HTTPException(status_code=401, detail="Não autenticado")
// ============================================================================
// 7. ROTAS
// ============================================================================
// decorador: @app.get("/")
func dashboard(request: Request) {
    // Dashboard principal -- Bloomberg Terminal style.
    user = get_current_user()
    // Modulos acessiveis
    modulos_acessiveis = []
    modulos_bloqueados = []
    para cada (mid, minfo) em MODULES.items(): {
        access = check_module_access(user, mid)
        entry = {
            "id": mid,
            "name": minfo["name"],
            "cert_required": minfo["cert"].name,
            "sensitive": minfo["sensitive"],
            "teia_only": minfo["teia_only"],
            "allowed": access["allowed"],
            "reason": access["reason"],
        }
        if access["allowed"] {
            modulos_acessiveis.append(entry)
        } else {
            modulos_bloqueados.append(entry)
    return templates.TemplateResponse(request, "dashboard.html", {
        "request": request,
        "user": user,
        "modulos_acessiveis": modulos_acessiveis,
        "modulos_bloqueados": modulos_bloqueados,
        "dados": DADOS,
        "validacoes": VALIDACOES_GATE_A,
        "version": TEIA_VERSION,
        "cert_label": {
            CertLevel.NONE: "Sem certificação",
            CertLevel.BASE: "TEIA Base",
            CertLevel.ANALISTA: "TEIA Analista",
            CertLevel.ESPECIALISTA: "TEIA Especialista",
            CertLevel.TEIA_DIRETO: "TEIA Direto (acesso total)",
        }.get(user.cert_level, "???"),
    })
// decorador: @app.get("/modulo/{module_id}")
func view_module(request: Request, module_id: texto) {
    // Visualiza um módulo específico.
    user = get_current_user()
    access = check_module_access(user, module_id)
    if !  access["allowed"] {
        return templates.TemplateResponse(request, "blocked.html", {
            "request": request,
            "module_id": module_id,
            "module_name": MODULES.get(module_id, {}).get("name", module_id),
            "reason": access["reason"],
            "user": user,
        })
    mod_info = MODULES[module_id]
    mod_data = DADOS.get(module_id, {})
    mod_data_clean = {k: v para k, v in mod_data.items() if k != "fonte"}
    mod_fonte = mod_data.get("fonte", "")
    return templates.TemplateResponse(request, "modulo.html", {
        "request": request,
        "user": user,
        "module_id": module_id,
        "module_name": mod_info["name"],
        "module_data": mod_data_clean,
        "module_fonte": mod_fonte,
        "all_data": DADOS,
    })
// decorador: @app.get("/simulador/{modelo}")
func simulador(request: Request, modelo: texto) {
    // Simulador de impacto.
    user = get_current_user()
    access = check_module_access(user, "simulador")
    if !  access["allowed"] {
        return templates.TemplateResponse(request, "blocked.html", {
            "request": request, "module_id": "simulador",
            "module_name": "Simulador", "reason": access["reason"], "user": user,
        })
    return templates.TemplateResponse(request, "simulador.html", {
        "request": request,
        "user": user,
        "modelo": modelo,
        "dados": DADOS,
    })
// decorador: @app.get("/api/simular")
func api_simular(modelo: texto, valor: flutuante) {
    // API HTMX para simulação em tempo real.
    user = get_current_user()
    access = check_module_access(user, "simulador")
    if !  access["allowed"] {
        return JSONResponse({"error": access["reason"]}, status_code=403)
    if modelo == "paa" {
        multiplicador = DADOS["fome"]["multiplicador_paa"]
        resultado = valor * multiplicador
        saude = resultado * 0.67 // ~2/3 do multiplicador vai para saúde
        familias = valor * 1000 / 500 // R$500/família/ano
        return {
            "modelo": "Multiplicador PAA",
            "investimento": valor,
            "economia_local": resultado,
            "economia_saude": saude,
            "familias_beneficiadas": inteiro(familias),
            "multiplicador": multiplicador,
            "intervalo": "R${resultado*0.85:.1f} - R${resultado*1.15:.1f} bi (±15%)",
            "fonte": "MDIC/IEPS 2022",
        }
    } else if modelo == "selic" {
        impacto = valor * DADOS["juros_spread"]["impacto_1pp_selic_bi"]
        paa_equivalente = impacto / 0.5 // quantos PAAs cabem
        bolsa_equivalente = impacto / 170
        return {
            "modelo": "Impacto Selic",
            "delta_selic": valor,
            "impacto_orcamento": impacto,
            "equivalente_paa": "{paa_equivalente:.0f}x orçamento PAA",
            "equivalente_bolsa": "{bolsa_equivalente:.1f}x Bolsa Família",
            "intervalo": "R${impacto*0.92:.1f} - R${impacto*1.08:.1f} bi (±8%)",
            "fonte": "Bacen 2024",
        }
    } else if modelo == "saneamento" {
        investimento = valor
        economia_saude = investimento * DADOS["saneamento"]["multiplicador_saude"]
        return {
            "modelo": "Retorno Saneamento",
            "investimento": investimento,
            "economia_saude": economia_saude,
            "pessoas_atendidas": inteiro(investimento * 1_000_000 / 2000),   // ~R$2000/pessoa
            "intervalo": "R${economia_saude*0.85:.1f} - R${economia_saude*1.15:.1f} bi (±15%)",
            "fonte": "Opas/OMS 2019",
        }
    return JSONResponse({"error": "Modelo não encontrado"}, status_code=404)
// decorador: @app.get("/gerar/dossie")
func gerar_dossie(request: Request) {
    // Gerador de dossiê -- gera, revisa, aprova.
    user = get_current_user()
    return templates.TemplateResponse(request, "gerar_dossie.html", {
        "request": request,
        "user": user,
        "dados": DADOS,
        "validacoes": VALIDACOES_GATE_A,
    })
// decorador: @app.get("/validacao")
func validacao_gate_a(request: Request) {
    // Painel de validação Gate A -- mostra dados validados.
    user = get_current_user()
    return templates.TemplateResponse(request, "validacao.html", {
        "request": request,
        "user": user,
        "validacoes": VALIDACOES_GATE_A,
    })
// decorador: @app.get("/switch-user/{user_id}")
func switch_user(user_id: texto) {
    // Trocar usuário (demo -- em produção seria login JWT).
    // variavel global: _current_user_id
    if user_id in USERS {
        _current_user_id = user_id
    return RedirectResponse(url="/", status_code=302)
// decorador: @app.get("/health")
func health() {
    return {"status": "ok", "version": TEIA_VERSION, "env": TEIA_ENV}
// ============================================================================
// 8. RUN
// ============================================================================
if __name__ == "__main__" {
    // importa uvicorn
    fmt.Println("TEIA Terminal v{TEIA_VERSION}")
    fmt.Println("Ambiente: {TEIA_ENV}")
    fmt.Println("URL: http://localhost:8000")
    fmt.Println("Usuários demo: cleiton, demo_base, demo_analista, demo_espec")
    fmt.Println("Trocar usuário: /switch-user/<id>")
    fmt.Println()
    uvicorn.run(app, host="0.0.0.0", port=8000)
