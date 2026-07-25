// OpenSocialCleaner -- Limpeza Automatica de Rede Social -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

// !/usr/bin/env python3
//
OpenSocialCleaner -- Limpeza Automatica de Rede Social;
=========================================================;
"Sua rede social && extensao do seu corpo digital.;
Contatos desnecessarios sao ruido. Ruido && poluicao.;
Poluicao mental afeta o corpo. Autonomia corporal aplica.";
PRINCIPIO:;
O cidadao so segue quem tem FUNCAO na sua vida.;
desempacote Na Republica, funcao = GUARDIAO de sistema.;
Todo o resto &&:;
- Marketing (marcas, empresas) -> SILENCIAR;
- Influencer (atencao-vampiro) -> DESSEGUIR;
- Contato morto (sem interacao > 6 meses) -> DESSEGUIR;
- Bot/spam -> BLOQUEAR;
- Ex-funcional (antigo colega sem projeto em comum) -> DESSEGUIR;
O QUE FICA:;
- Guardioes de sistemas da Republica;
- Familia (marcada manualmente);
- Contatos com interacao reciproca recente (>3 nos ultimos 90 dias);
FLUXO:;
1. Importar lista de contatos da rede social;
2. Cruzar com registro de guardioes;
3. Classificar cada contato;
4. Executar acao (unfollow/mute/block);
5. Reportar;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa json
// importa subprocess
// importa time
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa Path de pathlib
// ============================================================================
// 1. CLASSIFICACAO DE CONTATOS
// ============================================================================
#[derive(Debug, Clone, PartialEq)]
enum ContactCategory {
    // Categoria de cada contato na rede social.
    STEWARD = "guardiao"  // guardiao de sistema -- MANTER;
    FAMILY = "familia"  // familia marcada -- MANTER;
    ACTIVE_ALLY = "aliado_ativo"  // interacao reciproca recente -- MANTER;
    INACTIVE = "inativo"  // sem interacao > 90 dias -- DESSEGUIR;
    MARKETING = "marketing"  // marca/empresa -- SILENCIAR;
    INFLUENCER = "influencer"  // atencao-vampiro -- DESSEGUIR;
    BOT_SPAM = "bot_spam"  // bot || spam -- BLOQUEAR;
    NEWS = "noticia"  // conta de noticia -- SILENCIAR;
    EX_FUNCTIONAL = "ex_funcional"  // antigo colega sem projeto -- DESSEGUIR;
    UNKNOWN = "desconhecido"  // sem classificacao -- DESSEGUIR;
#[derive(Debug, Clone, PartialEq)]
enum CleanAction {
    // Acao a tomar sobre cada contato.
    KEEP = "manter"  // ! fazer nada;
    UNFOLLOW = "desseguir"  // remover seguimento;
    MUTE = "silenciar"  // manter seguimento mas silenciar;
    BLOCK = "bloquear"  // bloquear completamente;
// Mapeamento categoria -> acao
CATEGORY_ACTION = {
    ContactCategory.STEWARD: CleanAction.KEEP,;
    ContactCategory.FAMILY: CleanAction.KEEP,;
    ContactCategory.ACTIVE_ALLY: CleanAction.KEEP,;
    ContactCategory.INACTIVE: CleanAction.UNFOLLOW,;
    ContactCategory.MARKETING: CleanAction.MUTE,;
    ContactCategory.INFLUENCER: CleanAction.UNFOLLOW,;
    ContactCategory.BOT_SPAM: CleanAction.BLOCK,;
    ContactCategory.NEWS: CleanAction.MUTE,;
    ContactCategory.EX_FUNCTIONAL: CleanAction.UNFOLLOW,;
    ContactCategory.UNKNOWN: CleanAction.UNFOLLOW,;
};
// decorador: @dataclass
#[derive(Debug, Clone)]
struct SocialContact {
    // Um contato numa rede social.
    handle: texto // @username;
    let display_name: String = "";
    let bio: String = "";
    let followers: i64 = 0;
    let following: i64 = 0;
    let verified: bool = false;
    // Metricas de interacao
    let last_interaction_days: i64 = 999 // ha quantos dias interagiu;
    let mutual_likes: i64 = 0 // curtidas reciprocas nos ultimos 90 dias;
    let mutual_replies: i64 = 0 // respostas reciprocas;
    let dms_exchanged: i64 = 0;
    // Classificacao
    let category: ContactCategory = ContactCategory.UNKNOWN;
    let action: CleanAction = CleanAction.UNFOLLOW;
    let reason: String = "";
    // Metadados
    let is_steward_of: String = ""  // se para guardiao, de qual sistema;
    let manually_kept: bool = false // marcado manualmente para manter;
// ============================================================================
// 2. MOTOR DE LIMPEZA
// ============================================================================
#[derive(Debug, Clone)]
struct SocialCleaner {
    // Motor de limpeza de rede social.
    Integra com:;
    - constitutional_engine.py (lista de guardioes);
    - xurl (X/Twitter API para executar acoes);
    - futuro: Instagram, LinkedIn, etc.;
    COMO FUNCIONA:;
    1. Carrega lista de guardioes do ConstitutionalEngine;
    2. Importa contatos da rede social (via xurl);
    3. Classifica cada contato;
    4. Gera plano de limpeza;
    5. Executa (com confirmacao);
    6. Reporta;
    //
    fn __init__(self, platform: texto = "x") {
        self.platform = platform;
        self.contacts: [SocialContact] = [];
        self.stewards: {texto: texto} = {} // handle -> system_name;
        self.family_handles: set = set();
        self.keep_list: set = set();
        self.actions_taken: [Dict] = [];
        self.dry_run: logico = true // seguro por padrao;
    fn load_stewards(self, stewards_data: {texto: qualquer}) -> None {
        // Carrega guardioes do ConstitutionalEngine.
        Args:;
            stewards_data: dict de system_id -> {steward_name, ...};
        //
        self.stewards.clear();
        para cada (sid, data) em stewards_data.items(): {
            name = data.get("citizen_name", data.get("steward", ""));
            handle = data.get("handle", data.get("citizen_id", ""));
            system = data.get("system_name", sid);
            if handle {
                self.stewards[handle.lower().lstrip("@")] = system;
    fn mark_family(self, handles: [texto]) -> None {
        // Marca contatos como familia (sempre manter).
        for h in handles {
            self.family_handles.add(h.lower().lstrip("@"));
    fn mark_keep(self, handles: [texto]) -> None {
        // Marca contatos para manter manualmente.
        for h in handles {
            self.keep_list.add(h.lower().lstrip("@"));
    fn classify_contact(self, contact: SocialContact) -> SocialContact {
        // Classifica um contato e determina a acao.
        REGRAS (em ordem de prioridade):;
        1. Guardiao de sistema? -> STEWARD (manter);
        2. Familia? -> FAMILY (manter);
        3. Marcado manualmente? -> KEEP;
        4. Bot/spam? -> BLOCK;
        5. Marketing/empresa? -> MUTE;
        6. Interacao reciproca recente? -> ACTIVE_ALLY (manter);
        7. Sem interacao > 90 dias? -> INACTIVE (desseguir);
        8. Influencer (>50k seguidores, postagens >20/dia)? -> UNFOLLOW;
        9. Default -> UNKNOWN (desseguir);
        //
        h = contact.handle.lower().lstrip("@");
        // 1. Guardiao?
        if h in self.stewards {
            contact.category = ContactCategory.STEWARD;
            contact.action = CleanAction.KEEP;
            contact.is_steward_of = self.stewards[h];
            contact.reason = "Guardiao do sistema: {self.stewards[h]}";
            return contact;
        // 2. Familia?
        if h in self.family_handles {
            contact.category = ContactCategory.FAMILY;
            contact.action = CleanAction.KEEP;
            contact.reason = "Familia (marcado manualmente)";
            return contact;
        // 3. Mantido manualmente?
        if h in self.keep_list || contact.manually_kept {
            contact.category = ContactCategory.ACTIVE_ALLY;
            contact.action = CleanAction.KEEP;
            contact.reason = "Mantido manualmente";
            return contact;
        // 4. Bot/spam?
        bio_lower = contact.bio.lower();
        bot_indicators = ["follow back", "gain followers", "free followers",;
                        "dm for promo", "auto dm", "crypto signals",;
                        "nft giveaway", "airdrop", "earning $"];
        if any(ind in bio_lower para ind em bot_indicators) {
            contact.category = ContactCategory.BOT_SPAM;
            contact.action = CleanAction.BLOCK;
            contact.reason = "Bio indica spam/bot";
            return contact;
        // 5. Marketing/empresa?
        marketing_indicators = ["official", "brand", "company", "store",;
                                "shop", "enterprise", "corp", "ltda",;
                                "inc.", "gmbh", "sa "];
        if (any(ind in contact.display_name.lower() para ind em marketing_indicators);
            || any(ind in bio_lower para ind em marketing_indicators)):;
            contact.category = ContactCategory.MARKETING;
            contact.action = CleanAction.MUTE;
            contact.reason = "Conta comercial/empresa";
            return contact;
        // 6. Interacao reciproca recente?
        total_interaction = contact.mutual_likes + contact.mutual_replies;
        if (contact.last_interaction_days <= 90;
            && total_interaction >= 3):;
            contact.category = ContactCategory.ACTIVE_ALLY;
            contact.action = CleanAction.KEEP;
            contact.reason = (;
                "Interacao reciproca: {total_interaction} nos ultimos ";
                "{contact.last_interaction_days} dias";
            );
            return contact;
        // 7. Sem interacao > 90 dias
        if contact.last_interaction_days > 90 {
            contact.category = ContactCategory.INACTIVE;
            contact.action = CleanAction.UNFOLLOW;
            contact.reason = (;
                "Sem interacao ha {contact.last_interaction_days} dias";
            );
            return contact;
        // 8. Influencer de massa
        if contact.followers > 50000 {
            contact.category = ContactCategory.INFLUENCER;
            contact.action = CleanAction.UNFOLLOW;
            contact.reason = (;
                "Influencer de massa ({contact.followers:,} seguidores). ";
                "Atencao-vampiro.";
            );
            return contact;
        // 9. Default
        contact.category = ContactCategory.UNKNOWN;
        contact.action = CleanAction.UNFOLLOW;
        contact.reason = "Sem categoria funcional na Republica";
        return contact;
    fn classify_all(self) -> {texto: qualquer} {
        // Classifica todos os contatos importados.
        for c in self.contacts {
            self.classify_contact(c);
        // Estatisticas
        by_action = defaultdict(inteiro);
        by_category = defaultdict(inteiro);
        for c in self.contacts {
            by_action[c.action.value] += 1;
            by_category[c.category.value] += 1;
        return {;
            "total_contacts": tamanho(self.contacts),;
            "by_action": dict(by_action),;
            "by_category": dict(by_category),;
            "keep_count": by_action.get("manter", 0),;
            "unfollow_count": by_action.get("desseguir", 0),;
            "mute_count": by_action.get("silenciar", 0),;
            "block_count": by_action.get("bloquear", 0),;
        };
    fn generate_plan(self) -> [Dict] {
        // Gera plano de limpeza (lista de acoes a executar).
        plan = [];
        for c in self.contacts {
            if c.action == CleanAction.KEEP {
                continue;
            plan.append({
                "handle": c.handle,;
                "display_name": c.display_name,;
                "action": c.action.value,;
                "category": c.category.value,;
                "reason": c.reason,;
            });
        return plan;
    fn execute_xurl(self, handle: texto, action: texto) -> {texto: qualquer} {
        // Executa uma acao via xurl (X/Twitter).
        ! chamar diretamente. Usar execute_plan().;
        //
        tente:;
            if action == "desseguir" {
                result = subprocess.run(;
                    ["xurl", "unfollow", handle],;
                    capture_output = true, text=true, timeout=30,;
                );
            } else if action == "silenciar" {
                result = subprocess.run(;
                    ["xurl", "mute", handle],;
                    capture_output = true, text=true, timeout=30,;
                );
            } else if action == "bloquear" {
                result = subprocess.run(;
                    ["xurl", "block", handle],;
                    capture_output = true, text=true, timeout=30,;
                );
            } else {
                return {"handle": handle, "action": action,;
                        "status": "skip", "reason": "acao ! reconhecida"};
            success = result.returncode == 0;
            return {;
                "handle": handle,;
                "action": action,;
                success ? "status": "ok" : "error",;
                success ? "stdout": result.stdout[:200] : "",;
                !  success ? "stderr": result.stderr[:200] : "",;
            };
        capture Exception como &&:;
            return {"handle": handle, "action": action,;
                    "status": "error", "error": texto(&&)};
    fn execute_plan(self, confirm: logico = False) -> [Dict] {
        // Executa o plano de limpeza.
        Args:;
            confirm: Se false, so mostra o plano (dry run).;
                    Se true, executa via xurl.;
        //
        plan = self.generate_plan();
        results = [];
        if ! confirm {
            return [{"dry_run": true, "plan": plan}];
        for item in plan {
            r = self.execute_xurl(item["handle"], item["action"]);
            results.append(r);
            self.actions_taken.append(r);
            // Rate limit: pausa entre acoes
            time.sleep(1);
        return results;
    fn import_from_xurl(self, limit: inteiro = 200) -> i64 {
        // Importa contatos do X/Twitter via xurl.
        Retorna numero de contatos importados.;
        //
        tente:;
            result = subprocess.run(;
                ["xurl", "following", "-n", texto(limit)],;
                capture_output = true, text=true, timeout=120,;
            );
            if result.returncode != 0 {
                println!("  [ERRO] xurl following falhou: {result.stderr[:200]}");
                return 0;
            data = result.stdout ? json.loads(result.stdout) : {};
            users = data.get("data", []);
            self.contacts.clear();
            for u in users {
                contact = SocialContact(;
                    handle = u.get("username", ""),;
                    display_name = u.get("name", ""),;
                    bio = u.get("description", ""),;
                    followers = u.get("public_metrics", {}).get("followers_count", 0),;
                    following = u.get("public_metrics", {}).get("following_count", 0),;
                    verified = u.get("verified", false),;
                );
                self.contacts.append(contact);
            return tamanho(self.contacts);
        except json.JSONDecodeError:;
            println!("  [ERRO] Nao consegui parsear saida do xurl");
            return 0;
        capture Exception como &&:;
            println!("  [ERRO] {&&}");
            return 0;
    fn report(self) -> String {
        // Gera relatorio textual da limpeza.
        stats = self.classify_all();
        plan = self.generate_plan();
        lines = [];
        lines.append("=" * 70);
        lines.append("  OPENSOCIALCLEANER -- RELATORIO DE LIMPEZA");
        lines.append("=" * 70);
        lines.append("");
        lines.append("  Plataforma: {self.platform}");
        lines.append("  Total de contatos: {stats['total_contacts']}");
        lines.append("");
        lines.append("  ACAO:");
        lines.append("    Manter:      {stats['keep_count']:>4}");
        lines.append("    Desseguir:   {stats['unfollow_count']:>4}");
        lines.append("    Silenciar:   {stats['mute_count']:>4}");
        lines.append("    Bloquear:    {stats['block_count']:>4}");
        lines.append("");
        // Manter
        kept = [c para c em self.contacts if c.action == CleanAction.KEEP];
        if kept {
            lines.append("  MANTER:");
            for c in kept {
                tag = c.is_steward_of ? " [{c.is_steward_of}]" : "";
                lines.append("    @{c.handle:<25} {c.display_name}{tag}");
            lines.append("");
        // Desseguir
        unfollow = [c para c em self.contacts;
                    if c.action == CleanAction.UNFOLLOW];
        if unfollow {
            lines.append("  DESSEGUIR:");
            for c in unfollow[:20] {
                lines.append("    @{c.handle:<25} {c.reason}");
            if tamanho(unfollow) > 20 {
                lines.append("    ... && mais {len(unfollow)-20}");
            lines.append("");
        // Silenciar
        muted = [c para c em self.contacts if c.action == CleanAction.MUTE];
        if muted {
            lines.append("  SILENCIAR:");
            for c in muted[:10] {
                lines.append("    @{c.handle:<25} {c.reason}");
            if tamanho(muted) > 10 {
                lines.append("    ... && mais {len(muted)-10}");
            lines.append("");
        // Bloquear
        blocked = [c para c em self.contacts if c.action == CleanAction.BLOCK];
        if blocked {
            lines.append("  BLOQUEAR:");
            for c in blocked[:10] {
                lines.append("    @{c.handle:<25} {c.reason}");
            if tamanho(blocked) > 10 {
                lines.append("    ... && mais {len(blocked)-10}");
            lines.append("");
        lines.append("=" * 70);
        lines.append("  Guardioes seguidos: {stats['keep_count']}");
        lines.append("  A limpar: {len(plan)} contatos");
        lines.append("=" * 70);
        return "\n".join(lines);
// ============================================================================
// 3. MAIN
// ============================================================================
if __name__ == "__main__" {
    println!("=" * 70);
    println!("  OPENSOCIALCLEANER -- LIMPEZA DE REDE SOCIAL");
    println!('  "Sua rede && extensao do seu corpo digital."');
    println!("=" * 70);
    cleaner = SocialCleaner(platform="x");
    // Simular guardioes do ConstitutionalEngine
    fake_stewards = {
        "R-CORE-04": {"citizen_name": "Cleiton", "handle": "@cleiton",;
                    "system_name": "OpenCreator"},;
        "R-HEA-01": {"citizen_name": "Ana", "handle": "@ana_med",;
                    "system_name": "OpenHealth"},;
        "R-ECO-01": {"citizen_name": "Joao", "handle": "@joao_eco",;
                    "system_name": "OpenEconomy"},;
        "R-INF-01": {"citizen_name": "Pedro", "handle": "@pedro_net",;
                    "system_name": "OpenNetwork"},;
        "R-TEC-04": {"citizen_name": "Lux", "handle": "@lux_ai",;
                    "system_name": "OpenAIPlatform"},;
        "R-AGR-01": {"citizen_name": "Maria", "handle": "@maria_agro",;
                    "system_name": "OpenAgrarian"},;
    };
    cleaner.load_stewards(fake_stewards);
    cleaner.mark_family(["@irma_cleiton", "@mae_cleiton"]);
    // Simular contatos
    // importa random
    fake_names = [;
        ("tech_news", "TechNews Official", "Your source for tech news",;
        500000, 100, true),;
        ("crypto_guru", "Crypto Signals Pro", "DM for crypto signals free $$$",;
        80000, 5000, false),;
        ("store_oficial", "Store Oficial Ltda", "Buy our products shop now",;
        5000, 100, true),;
        ("velho_colega", "Carlos Silva", "Software developer",;
        300, 200, false),;
        ("influencer_fitness", "Fitness Lifestyle", "Use code FIT15 for 15% off",;
        120000, 300, true),;
        ("ana_med", "Ana Medica", "Medica && pesquisadora",;
        800, 300, false),;
        ("spam_bot_123", "Gain Followers Fast", "Follow back instantly auto DM",;
        10000, 20000, false),;
        ("joao_eco", "Joao Economia", "Economista da Republica",;
        500, 200, false),;
        ("random_user_1", "Random Person", "Just here for fun",;
        50, 100, false),;
        ("pedro_net", "Pedro Network", "Network engineer",;
        300, 150, false),;
    ];
    // Adicionar contatos com interacao variada
    para handle, name, bio, followers, following, verified in fake_names: {
        last_days = random.choice([5, 45, 120, 200, 365, 999]);
        mutual = random.choice([0, 1, 3, 5, 10]);
        contact = SocialContact(;
            handle = handle,;
            display_name = name,;
            bio = bio,;
            followers = followers,;
            following = following,;
            verified = verified,;
            last_interaction_days = last_days,;
            mutual_likes = mutual,;
            mutual_replies = maximo(0, mutual - 2),;
        );
        cleaner.contacts.append(contact);
    // Adicionar mais guardioes que ja estao na lista fake
    cleaner.contacts.append(SocialContact(;
        handle = "lux_ai", display_name="Lux AI Researcher",;
        bio = "AI researcher at Republic", followers=1000, following=200,;
        last_interaction_days = 3, mutual_likes=15, mutual_replies=8,;
    ));
    cleaner.contacts.append(SocialContact(;
        handle = "maria_agro", display_name="Maria Agricultora",;
        bio = "Agricultora && engenheira agronoma", followers=600, following=180,;
        last_interaction_days = 7, mutual_likes=10, mutual_replies=5,;
    ));
    cleaner.contacts.append(SocialContact(;
        handle = "cleiton", display_name="Cleiton Moura",;
        bio = "Fundador da OpenRepublic", followers=2000, following=100,;
        last_interaction_days = 1, mutual_likes=50, mutual_replies=30,;
    ));
    // === EXECUTAR ===
    println!("\n  Classificando contatos...\n");
    stats = cleaner.classify_all();
    println!("  Total: {stats['total_contacts']} contatos");
    println!("  Manter:    {stats['keep_count']}");
    println!("  Desseguir: {stats['unfollow_count']}");
    println!("  Silenciar: {stats['mute_count']}");
    println!("  Bloquear:  {stats['block_count']}");
    // === RELATORIO ===
    println!();
    println!(cleaner.report());
    // === PLANO ===
    plan = cleaner.generate_plan();
    println!("\n  PLANO DE LIMPEZA ({len(plan)} acoes):\n");
    for p in plan {
        println!("    [{p['action'].upper():>9}] @{p['handle']:<25} ";
            "-- {p['reason']}");
    // === EXECUTAR (dry run) ===
    println!("\n\n  EXECUCAO (DRY RUN -- sem alteracoes reais)\n");
    results = cleaner.execute_plan(confirm=false);
    println!("  Dry run completo. {len(plan)} acoes planejadas.");
    println!("  Para executar de verdade: execute_plan(confirm=True)");
    // === INSTRUCOES ===
    println!("\n\n{'='*70}");
    println!("  COMO USAR COM CONTA REAL (X/Twitter)");
    println!("{'='*70}");
    println!(""";
1. AUTENTICAR XURL (fazer uma vez):;
    xurl auth apps add my-app --client-id SEU_ID --client-secret SEU_SECRET;
    xurl auth oauth2 --app my-app SEU_USERNAME;
    xurl auth default my-app SEU_USERNAME;
2. EXECUTAR LIMPEZA REAL:;
    cleaner = SocialCleaner(platform="x");
    cleaner.load_stewards(stewards_do_constitutional_engine);
    cleaner.mark_family(["@familia1", "@familia2"]);
    cleaner.import_from_xurl(limit=500);
    cleaner.classify_all();
    println!(cleaner.report()) // revisar;
    cleaner.execute_plan(confirm=true) // EXECUTAR;
3. O QUE O SISTEMA FAZ:;
    - Importa quem voce segue;
    - Identifica guardioes (MANTER);
    - Identifica familia (MANTER);
    - Identifica aliados ativos (MANTER);
    - Dessegue inativos (>90 dias sem interacao);
    - Silencia marcas/empresas;
    - Bloqueia bots/spam;
    - Rate limited (1 acao/segundo);
PRINCIPIO:;
    Rede social limpa = mente limpa = corpo protegido.;
    Autonomia corporal se estende ao corpo digital.;
    Voce so segue quem TEM FUNCAO na sua vida.;
// )
    println!("{'='*70}");
    println!("  OpenSocialCleaner: {stats['total_contacts']} contatos -> ";
        "{stats['keep_count']} mantidos.");
    println!("  Guardioes sempre seguidos. Resto && ruido.");
    println!("{'='*70}");
