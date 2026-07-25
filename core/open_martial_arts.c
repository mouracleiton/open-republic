/* OpenMartialArts -- Defesa Pessoal e Artes Marciais da Republica -- gerado de Portugol++ */
#ifndef OPENMARTIALARTS_DEFESA_PESSOAL_E_ARTES_MARCIAIS_DA_REPUBLICA_H
#define OPENMARTIALARTS_DEFESA_PESSOAL_E_ARTES_MARCIAIS_DA_REPUBLICA_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// !/usr/bin/env python3
//
OpenMartialArts -- Defesa Pessoal && Artes Marciais da Republica;
==================================================================;
"Todo mundo prefere fazer seus negocios em paz.;
Mas se a paz para quebrada, TODO MUNDO tem o direito;
&& a CAPACIDADE de se defender.;
Autonomia corporal (P2) ! sofrer. Tambem se PROTEGER.";
CONCEITO:;
A Republica ! && militarista. ! glorifica violencia.;
MAS reconhece que o mundo tem violencia.;
Quem ! sabe se defender && PRESA.;
OpenMartialArts pega o MELHOR de todas as artes marciais:;
- Muay Thai: striking, clinch, cotovelada, joelhada;
- Jiu-Jitsu Brasileiro (BJJ): solo, finalizacao, controle;
- Judo: arremesso, desequilibrio, transicao solo;
- Boxe: footwork, esquiva, combinacao, distancia;
- Wrestling: queda, controle no chao;
- Krav Maga (defesa real, ! militar): agressao, objetos, multipla;
- Capoeira: mobilidade, esquiva, cultura brasileira;
- Karate: base, tempo, distancia de golpe;
&& CRIA uma arte marcial unificada da Republica:;
- Defesa PESSOAL real (! esporte, ! competicao);
- Para TODOS (crianca, adulto, idoso, PCD);
- Adaptada por capacidade fisica;
- Foco em DESCALAR > neutralizar > nocautear;
- Sem violencia gratuita. Sem ego. Sem elitismo.;
FILOSOFIA DE 3 NIVEIS:;
NIVEL 1 (AZUL): ESCAPAR -- a melhor luta && a que voce foge;
NIVEL 2 (VERDE): NEUTRALIZAR -- imobilizar sem ferir gravemente;
NIVEL 3 (PRETO): PROTEGER -- defender outros que ! podem se defender;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime
// ============================================================================
// 1. ARTES MARCIAIS DE ORIGEM
// ============================================================================
typedef struct MartialArt {
    // Artes marciais de onde OpenMartialArts extrai tecnicas.
    MUAY_THAI = "muay_thai";
    BJJ = "jiu_jitsu_brasileiro";
    JUDO = "judo";
    BOXE = "boxe";
    WRESTLING = "wrestling";
    KRAV_MAGA = "krav_maga_defesa_real";
    CAPOEIRA = "capoeira";
    KARATE = "karate";
    TAEKWONDO = "taekwondo";
    AIKIDO = "aikido";
    KALI_ESCRIMA = "kali_escrima"  // armas brancas, bastao;
typedef struct TechniqueCategory {
    // Categoria de tecnica.
    STRIKING = "golpeamento"  // soco, chute, cotovelo, joelhada;
    GRAPPLING = "agarramento"  // queda, arremesso, controle;
    GROUND = "solo"  // finalizacao, guarda, montada;
    DEFENSE = "defesa"  // esquiva, bloqueio, redirecionamento;
    ESCAPE = "evasao"  // sair de agarrão, estrangulamento;
    WEAPON_DEFENSE = "defesa_arma"  // faca, arma de fogo, bastao;
    MULTIPLE = "multiplos"  // mais de um agressor;
    AWARENESS = "consciencia"  // prevencao, leitura de ambiente;
    DEESCALATION = "desescalada"  // acalmar situacao sem violencia;
typedef struct DifficultyLevel {
    // Dificuldade da tecnica (qual cinto aprende).
    WHITE = ("branco", 0);
    BLUE = ("azul", 2);
    GREEN = ("verde", 3);
    BROWN = ("marrom", 4);
    BLACK = ("preto", 5);
    // decorador: @property
    int level(self) {
        return self.value[1];
// ============================================================================
// 2. TECNICA
// ============================================================================
// decorador: @dataclass
typedef struct Technique {
    // Uma tecnica do sistema unificado.
    tech_id: texto;
    name: texto;
    category: TechniqueCategory;
    origin: MartialArt;
    difficulty: DifficultyLevel;
    char* description = "";
    // Adaptabilidade
    bool for_children = true // pode ensinar a criancas?;
    bool for_elderly = true // idoso consegue fazer?;
    bool for_pcd = true // pessoa com deficiencia?;
    bool standing = true // em pe?;
    bool ground = false // no chao?;
    int min_strength = 1 // 1-10 (forca necessaria);
    int speed_required = 3 // 1-10 (velocidade necessaria);
    // Filosofia
    char* goal = ""  // o que esta tecnica alcansa;
    bool last_resort = false // so usar se nada mais funcionar;
    bool lethal_potential = false // pode matar?;
// ============================================================================
// 3. BASE DE TECNICAS (melhor de cada arte)
// ============================================================================
[Technique] TECHNIQUES = [;
    // === CONSCIENCIA E PREVENCAO (todos aprendem primeiro) ===
    Technique("TEC-001", "Leitura de Ambiente",;
        TechniqueCategory.AWARENESS, MartialArt.KRAV_MAGA, DifficultyLevel.WHITE,;
        "Identificar ameacas antes que aconteçam. Onde estao saidas? ";
        "Quem parece suspeito? Que objetos podem servir de arma?",;
        goal = "NUNCA ser pego desprevenido"),;
    Technique("TEC-002", "Desescalada Verbal",;
        TechniqueCategory.DEESCALATION, MartialArt.AIKIDO, DifficultyLevel.WHITE,;
        "Acalmar agressor com palavras. Tom de voz baixo. Nao provocar. ";
        "Ofecer saida honrosa. A melhor luta && a que ! acontece.",;
        goal = "Evitar violencia sem lutar"),;
    Technique("TEC-003", "Postura de Alerta",;
        TechniqueCategory.DEFENSE, MartialArt.BOXE, DifficultyLevel.WHITE,;
        "Maos abertas na frente do rosto (! punho -- mostra paz). ";
        "Pe ligeiramente aberto. Centro de gravidade baixo.",;
        goal = "Pronto para reagir sem parecer agressivo"),;
    // === EVASAO (fugir e a melhor opcao) ===
    Technique("TEC-010", "Quebra de Pulso",;
        TechniqueCategory.ESCAPE, MartialArt.BJJ, DifficultyLevel.BLUE,;
        "Se alguem segura seu pulso: girar contra o polegar (ponto fraco). ";
        "Todo agarrao tem um lado fraco. Polegar ! segura.",;
        goal = "Soltar de qualquer agarrao de pulso"),;
    Technique("TEC-011", "Quebra de Abraco Frontal",;
        TechniqueCategory.ESCAPE, MartialArt.BJJ, DifficultyLevel.BLUE,;
        "Abracado por tras: abaixar centro de gravidade, criar espaco, ";
        "girar para fora. Usar quadril como alavanca.",;
        goal = "Sair de abraco por tras"),;
    Technique("TEC-012", "Estrangulamento - Defesa",;
        TechniqueCategory.ESCAPE, MartialArt.BJJ, DifficultyLevel.BLUE,;
        "Sendo estrangulado: proteger traqueia, puxar bracos, girar, ";
        "golpear pontos vitais (groin, olhos se necessario).",;
        goal = "Nao ser asfixiado",;
        last_resort = true),;
    Technique("TEC-013", "Fuga Direcionada",;
        TechniqueCategory.ESCAPE, MartialArt.KRAV_MAGA, DifficultyLevel.WHITE,;
        "Sempre saber onde estao as saidas. Correr em zigzag se perseguido. ";
        "Gritar 'FOGO' (mais atencao que 'socorro').",;
        goal = "Escapar correndo"),;
    // === GOLPEAMENTO (Muay Thai + Boxe) ===
    Technique("TEC-020", "Jab Cruzado",;
        TechniqueCategory.STRIKING, MartialArt.BOXE, DifficultyLevel.BLUE,;
        "Soco reto com a Mao da frente (jab) seguido de cruzado com a de tras. ";
        "Rotacao de quadril. Retorno rapido a guarda.",;
        goal = "Criar distancia do agressor"),;
    Technique("TEC-021", "Joelhada Reto",;
        TechniqueCategory.STRIKING, MartialArt.MUAY_THAI, DifficultyLevel.BLUE,;
        "Knee strike frontal. Apanhar roupa do agressor, puxar para baixo, ";
        "subir joelho. Dano maximo em distancia curta.",;
        goal = "Defesa em curta distancia"),;
    Technique("TEC-022", "Cotovelada Horizontal",;
        TechniqueCategory.STRIKING, MartialArt.MUAY_THAI, DifficultyLevel.GREEN,;
        "Cotovelada em arco horizontal. Dano massivo em distancia minima. ";
        "Cortar. Usar quando espaco && insuficiente para soco.",;
        goal = "Dano massimo em clinch"),;
    Technique("TEC-023", "Chute Frontal (Teep)",;
        TechniqueCategory.STRIKING, MartialArt.MUAY_THAI, DifficultyLevel.WHITE,;
        "Chute empurrando com a planta do pe. Cria distancia. ";
        "Parede invisivel entre voce && o agressor.",;
        goal = "Manter distancia"),;
    Technique("TEC-024", "Chute Baixo (Caneada)",;
        TechniqueCategory.STRIKING, MartialArt.MUAY_THAI, DifficultyLevel.BLUE,;
        "Chute na coxa || canela do agressor. Difícil de ver. ";
        "Desestabiliza. Permite fuga.",;
        goal = "Desestabilizar para fugir"),;
    // === AGARRAMENTO E QUEDAS (Judo + Wrestling) ===
    Technique("TEC-030", "Osoto Gari (Judo)",;
        TechniqueCategory.GRAPPLING, MartialArt.JUDO, DifficultyLevel.GREEN,;
        "Desequilibrio + rasteira na perna externa. Derruba agressor ";
        "sem precisar de forca bruta. Tecnica de alavanca.",;
        goal = "Derrubar sem forca"),;
    Technique("TEC-031", "O Goshi (Judo - Arremesso de Quadril)",;
        TechniqueCategory.GRAPPLING, MartialArt.JUDO, DifficultyLevel.GREEN,;
        "Arremesso usando o quadril como fulcro. ";
        "Mesmo pessoa menor derruba maior se tecnica for perfeita.",;
        goal = "Pessoa pequena derruba grande"),;
    Technique("TEC-032", "Double Leg Takedown (Wrestling)",;
        TechniqueCategory.GRAPPLING, MartialArt.WRESTLING, DifficultyLevel.GREEN,;
        "Baixar nivel, abraçar ambas as pernas, levantar && derrubar. ";
        "Clássico de wrestling. Rapido && eficaz.",;
        goal = "Levar a luta para o solo"),;
    // === SOLO (BJJ) ===
    Technique("TEC-040", "Triangulo Fechado",;
        TechniqueCategory.GROUND, MartialArt.BJJ, DifficultyLevel.GREEN,;
        "Enrolar pernas em torno do pescoco do agressor. Finaliza por ";
        "estrangulamento sanguineo (! de ar). Desmaia em 8s sem dano.",;
        goal = "Finalizar no solo sem dano permanente"),;
    Technique("TEC-041", "Chave de Braco (Armbar)",;
        TechniqueCategory.GROUND, MartialArt.BJJ, DifficultyLevel.GREEN,;
        "Isolar o braco do agressor entre as pernas, alavancar o cotovelo. ";
        "Se ! soltar: quebra. Ameaca suficiente para render.",;
        goal = "Forçar rendição por dor"),;
    Technique("TEC-042", "Defesa de Estupro (Guarda Fechada)",;
        TechniqueCategory.GROUND, MartialArt.BJJ, DifficultyLevel.BLUE,;
        "Se derrubada de costas: enrolar pernas na cintura do agressor (guarda). ";
        "Controlar punhos. Triangulo, chave de braco, || varrer para cima. ";
        "ESSENCIAL para mulheres. BJJ foi DESNVOLVIDO para isto.",;
        goal = "Defender de ataque sexual no solo",;
        last_resort = false),;
    Technique("TEC-043", "Montada - Controle",;
        TechniqueCategory.GROUND, MartialArt.BJJ, DifficultyLevel.GREEN,;
        "Estar por cima sentado no peito do agressor. Posicao dominante. ";
        "Permite finalizar || bater sem levar dano.",;
        goal = "Controlar sem ferir"),;
    // === DEFESA CONTRA ARMAS ===
    Technique("TEC-050", "Defesa de Faca (Controle de Pulso)",;
        TechniqueCategory.WEAPON_DEFENSE, MartialArt.KRAV_MAGA, DifficultyLevel.GREEN,;
        "Faca ameacando: NUNCA tentar agarrar a lamina. Controlar PULSO ";
        "da mao armada. Torcer. Chutar. Criar distancia. Fugir.",;
        goal = "Sobreviver a ataque de faca",;
        last_resort = true),;
    Technique("TEC-051", "Defesa de Arma de Fogo (Curta distancia)",;
        TechniqueCategory.WEAPON_DEFENSE, MartialArt.KRAV_MAGA, DifficultyLevel.BROWN,;
        "Arma apontada de perto: desviar cano, controlar mao armada, ";
        "torcer para longe do corpo. So usar se NAO houver opcao. ";
        "MUITO perigoso. Ultimo recurso.",;
        goal = "Sobreviver a arma de fogo",;
        last_resort = true,;
        lethal_potential = true),;
    Technique("TEC-052", "Bastao/Escrima (Defesa && Objeto)",;
        TechniqueCategory.WEAPON_DEFENSE, MartialArt.KALI_ESCRIMA, DifficultyLevel.GREEN,;
        "Usar qualquer objeto como bastao (guarda-chuva, vassoura, galho). ";
        "Tecnicas de Kali/Escrima: bater na mao, ! na lamina.",;
        goal = "Usar objeto do ambiente como ferramenta de defesa"),;
    // === MULTIPLOS AGRESSORES ===
    Technique("TEC-060", "Posicionamento em Linha",;
        TechniqueCategory.MULTIPLE, MartialArt.KRAV_MAGA, DifficultyLevel.GREEN,;
        "Contra 2+: NUNCA ficar cercado. Movimentar para que todos fiquem ";
        "numa linha (um bloqueia o outro). Bater && fugir.",;
        goal = "Nao ser cercado por multiplos"),;
    Technique("TEC-061", "Empurra && Gira",;
        TechniqueCategory.MULTIPLE, MartialArt.BOXE, DifficultyLevel.GREEN,;
        "Empurrar um agressor contra o outro. Criar confusao. ";
        "Ganhar segundos para fugir.",;
        goal = "Usar um agressor contra o outro"),;
    // === CAPOEIRA (cultura brasileira + mobilidade) ===
    Technique("TEC-070", "Esquiva Baixa (Capoeira)",;
        TechniqueCategory.DEFENSE, MartialArt.CAPOEIRA, DifficultyLevel.WHITE,;
        "Descer sob o golpe em movimento fluido. Capoeira ensina ";
        "a NAO estar onde o golpe chega. Mobilidade > bloqueio.",;
        goal = "Esquivar com fluidez"),;
    Technique("TEC-071", "Meia Lua de Compasso",;
        TechniqueCategory.STRIKING, MartialArt.CAPOEIRA, DifficultyLevel.GREEN,;
        "Chute rasteiro em arco com as duas maos no chao. ";
        "Difícil de ver. Derruba. Cultura brasileira.",;
        goal = "Surpreender com golpe baixo"),;
];
// ============================================================================
// 4. SISTEMA DE GRADUACAO (cintos)
// ============================================================================
typedef struct Belt {
    // Sistema de graduacao da Republica.
    DIFERENCA vs artes marciais tradicionais:;
    - ! && hierarquia. ! && elitismo (P1).;
    - && marcador de CONHECIMENTO.;
    - Cinto preto ! quer dizer "melhor". Quer dizer "pode ensinar".;
    - TODO cidadao tem direito de aprender ate onde conseguir.;
    //
    WHITE = ("branco", "Iniciante -- aprendendo a cair && escapar");
    GREY = ("cinza", "Consciencia + defesa basica");
    BLUE = ("azul", "Escapou de agarrões && estrangulamentos");
    GREEN = ("verde", "Pode neutralizar ameaca sem ferir gravemente");
    BROWN = ("marrom", "Avancado -- defesa contra armas");
    BLACK = ("preto", "Pode PROTEGER outros && ENSINAR");
    // decorador: @property
    int level(self) {
        return {"branco": 0, "cinza": 1, "azul": 2,;
                "verde": 3, "marrom": 4, "preto": 5}.get(self.value[0], 0);
    // decorador: @property
    char* meaning(self) {
        return self.value[1];
// decorador: @dataclass
typedef struct MartialArtsProfile {
    // Perfil de cada cidadao no OpenMartialArts.
    citizen_id: texto;
    name: texto;
    age: inteiro;
    Belt belt = Belt.WHITE;
    [texto] techniques_mastered = field(default_factory=list);
    double hours_trained = 0.0;
    int sessions_attended = 0;
    bool can_teach = false;
    [MartialArt] specialization = field(default_factory=list);
    // Adaptacoes
    [texto] physical_adaptations = field(default_factory=list) // lesao, PCD, idade;
    bool seated_mode = false // treina sentado (PCD/cadeirante);
    bool self_defense_focus = true // foco em defesa real, ! competicao;
    // decorador: @property
    funcao next_belt(self) retorna Belt?:
        belts = list(Belt);
        idx = belts.index(self.belt);
        idx + 1 < sizeof(belts) ? retorne belts[idx + 1] : NULL;
    // decorador: @property
    int techniques_for_belt(self) {
        // Quantas tecnicas precisa para proximo cinto.
        req = {0: 5, 1: 8, 2: 12, 3: 16, 4: 20, 5: 0};
        return req.get(self.belt.level, 0);
    // decorador: @property
    bool can_promote(self) {
        return (sizeof(self.techniques_mastered) >= self.techniques_for_belt;
                && self.hours_trained >= self.belt.level * 50);
// ============================================================================
// 5. MOTOR DE TREINAMENTO
// ============================================================================
typedef struct MartialArtsEngine {
    // Sistema de artes marciais unificadas da Republica.
    PRINCIPIOS:;
    1. DEFESA, ! AGRESSAO -- ! se inicia violenca;
    2. ESCAPAR > NEUTRALIZAR > NOCAUTEAR -- sempre na ordem;
    3. TODO MUNDO TREINA -- crianca, adulto, idoso, PCD;
    4. ADAPTADO POR CAPACIDADE -- cadeirante treina BJJ sentado;
    5. SEM COMPETICAO OBRIGATORIA -- luta && para defesa, ! esporte;
    6. CULTURA BRASILEIRA -- capoeira && base cultural;
    7. ANTI-BULLYING -- criancas aprendem a ! usar contra colegas;
    //
    void __init__(self) {
        self.techniques: {texto: Technique} = {t.tech_id: t para t em TECHNIQUES};
        self.profiles: {texto: MartialArtsProfile} = {};
        self.training_sessions: [Dict] = [];
        self.dojos: {texto: Dict} = {};
    funcao register_citizen(self, citizen_id: texto, name: texto, age: inteiro,
                        [texto] adaptations = NULL,;
                        bool seated = false) -> {texto: qualquer}:;
        // Registra cidadao no programa de artes marciais.
        profile = MartialArtsProfile(;
            citizen_id = citizen_id, name=name, age=age,;
            physical_adaptations = adaptations || [],;
            seated_mode = seated,;
        );
        self.profiles[citizen_id] = profile;
        return {;
            "registered": true,;
            "citizen": name,;
            "belt": profile.belt.value[0],;
            profile.next_belt ? "next": profile.next_belt.value[0] : "maximo",;
            "focus": "DEFESA PESSOAL -- ! competicao",;
            "adaptations": adaptations  ||  "nenhuma",;
            "message": (;
                "Bem-vindo, {name}. Voce vai aprender a se defender. ";
                "Nao para brigar. Para PROTEGER. ";
                "P2 autonomia corporal inclui o direito de se defender.";
            ),;
        };
    {texto: qualquer} get_curriculum(self, belt: Belt = Belt.WHITE) {
        // Retorna o curriculo para um nivel de cinto.
        level = belt.level;
        // Tecnicas que este cinto deve aprender
        relevant = [t para t em self.techniques.values();
                    if t.difficulty.level <= level + 1];
        by_category = defaultdict(list);
        /* TODO: iterador C manual para t em relevant */
            adapted = [];
            if (t.for_children) {
                adapted.append("criancas");
            if (t.for_elderly) {
                adapted.append("idosos");
            if (t.for_pcd) {
                adapted.append("PCD");
            by_category[t.category.value].append({
                "id": t.tech_id,;
                "name": t.name,;
                "origin": t.origin.value,;
                "difficulty": t.difficulty.value[0],;
                "goal": t.goal,;
                "adapted_for": adapted,;
                "last_resort": t.last_resort,;
            });
        return {;
            "belt": belt.value[0],;
            "meaning": belt.value[1],;
            "techniques_count": sizeof(relevant),;
            "by_category": dict(by_category),;
        };
    funcao train_technique(self, citizen_id: texto, tech_id: texto,
                        double hours = 1.0) -> {texto: qualquer}:;
        // Cidadao treina uma tecnica.
        profile = self.profiles.get(citizen_id);
        if (! profile) {
            return {"error": "Cidadao ! registrado"};
        tech = self.techniques.get(tech_id);
        if (! tech) {
            return {"error": "Tecnica ! encontrada"};
        // Verificar se pode aprender (cinto certo)
        if (tech.difficulty.level > profile.belt.level + 1) {
            return {;
                "error": "Tecnica avancada demais para seu cinto",;
                "required_belt": tech.difficulty.value[0],;
                "your_belt": profile.belt.value[0],;
            };
        // Registrar treino
        if (tech_id ! in profile.techniques_mastered) {
            profile.techniques_mastered.append(tech_id);
        profile.hours_trained += hours;
        profile.sessions_attended += 1;
        self.training_sessions.append({
            "citizen": profile.name,;
            "technique": tech.name,;
            "origin": tech.origin.value,;
            "hours": hours,;
            "date": datetime.now().isoformat(),;
        });
        // Verificar promocao
        promoted = false;
        if (profile.can_promote && profile.next_belt) {
            old_belt = profile.belt;
            profile.belt = profile.next_belt;
            if (profile.belt == Belt.BLACK) {
                profile.can_teach = true;
            promoted = true;
        return {;
            "trained": true,;
            "citizen": profile.name,;
            "technique": tech.name,;
            "origin": tech.origin.value,;
            "goal": tech.goal,;
            "hours_total": profile.hours_trained,;
            "techniques_mastered": sizeof(profile.techniques_mastered),;
            "promoted": promoted,;
            promoted ? "new_belt": profile.belt.value[0] : NULL,;
            "message": (;
                "Aprendeu: {tech.name} ({tech.origin.value}). ";
                "Objetivo: {tech.goal}.";
                promoted ? + (" PROMOVIDO a {profile.belt.value[0]}!" : "");
            ),;
        };
    {texto: qualquer} defense_scenario(self, scenario: texto) {
        // Cenario de defesa -> quais tecnicas usar.
        O cidadao pergunta: 'Se acontecer X, o que eu faco?';
        O sistema responde com a sequencia de tecnicas.;
        //
        scenarios = {
            "agarrou_meu_pulso": {
                "response": "Girar contra o polegar (TEC-010), criar distancia, fugir",;
                "techniques": ["TEC-010", "TEC-013"],;
                "level_needed": Belt.BLUE.level,;
            },;
            "estrangulamento": {
                "response": "Proteger traqueia, puxar bracos, golpear pontos vitais, fugir",;
                "techniques": ["TEC-012", "TEC-013"],;
                "level_needed": Belt.BLUE.level,;
            },;
            "pessoa_maior_agride": {
                "response": "Esquiva (capoeira), chute baixo (muay thai), fugir",;
                "techniques": ["TEC-070", "TEC-024", "TEC-013"],;
                "level_needed": Belt.BLUE.level,;
            },;
            "tentativa_de_estupro": {
                "response": "BJJ defesa de solo, guarda fechada, triangulo || chave",;
                "techniques": ["TEC-042", "TEC-040", "TEC-041"],;
                "level_needed": Belt.GREEN.level,;
            },;
            "arma_branca": {
                "response": "Controlar pulso (NAO lamina), torcer, chutar, fugir",;
                "techniques": ["TEC-050", "TEC-013"],;
                "level_needed": Belt.GREEN.level,;
            },;
            "arma_de_fogo_perto": {
                "response": "Desviar cano, controlar mao, torcer. ULTIMO RECURSO.",;
                "techniques": ["TEC-051"],;
                "level_needed": Belt.BROWN.level,;
                "warning": "MUITO PERIGOSO. Ultimo recurso absoluto.",;
            },;
            "multiplos_agressores": {
                "response": "Manter em linha, empurrar um contra outro, fugir",;
                "techniques": ["TEC-060", "TEC-061", "TEC-013"],;
                "level_needed": Belt.GREEN.level,;
            },;
            "bullying_escolar": {
                "response": "Desescalada verbal, postura de alerta, NAO revidar. ";
                            "Reportar. Defesa so se atacado fisicamente.",;
                "techniques": ["TEC-002", "TEC-003"],;
                "level_needed": Belt.WHITE.level,;
                "note": "Criancas: priorizar desescalada. Lutar && ultimo recurso.",;
            },;
        };
        result = scenarios.get(scenario);
        if (! result) {
            return {"error": "Cenario ! encontrado. Disponiveis: {list(scenarios.keys())}"};
        return {;
            "scenario": scenario,;
            "response": result["response"],;
            "techniques": [;
                {"id": tid, "name": self.techniques[tid].name,;
                "origin": self.techniques[tid].origin.value,;
                "goal": self.techniques[tid].goal};
                /* para tid em result["techniques"] */
            ],;
            "level_needed": result.get("level_needed", 0),;
            "warning": result.get("warning", ""),;
        };
    {texto: qualquer} stats(self) {
        return {;
            "total_techniques": sizeof(self.techniques),;
            "by_origin": dict(Counter(t.origin.value para t em self.techniques.values())),;
            "by_category": dict(Counter(t.category.value para t em self.techniques.values())),;
            "total_citizens_training": sizeof(self.profiles),;
            "black_belts": soma(1 para p em self.profiles.values() if p.belt == Belt.BLACK),;
            "total_sessions": sizeof(self.training_sessions),;
        };
// importa Counter de collections
// ============================================================================
// 6. MAIN
// ============================================================================
if (__name__ == "__main__") {
    engine = MartialArtsEngine();
    printf("=" * 80);
    printf("  OPENMARTIALARTS -- DEFESA PESSOAL DA REPUBLICA");
    printf("  'Todo mundo prefere paz. Mas se quebrarem, todos se defendem.'");
    printf("=" * 80);
    // === 1. ARTES DE ORIGEM ===
    printf("\n\n  === 1. ARTES MARCIAIS INTEGRADAS ===\n");
    s = engine.stats();
    /* para cada (art, count) em ordene(s["by_origin"].items(), key=(x) -> -x[1]): */
        printf("  {art:<30} {count} tecnicas");
    // === 2. CATEGORIAS ===
    printf("\n\n  === 2. CATEGORIAS DE TECNICA ===\n");
    /* para cada (cat, count) em ordene(s["by_category"].items(), key=(x) -> -x[1]): */
        printf("  {cat:<25} {count} tecnicas");
    // === 3. SISTEMA DE CINTOS ===
    printf("\n\n  === 3. GRADUACAO (CINTOS) ===\n");
    /* TODO: iterador C manual para belt em Belt */
        printf("  [{belt.value[0]:<8}] Nivel {belt.level} -- {belt.value[1]}");
    // === 4. REGISTRAR E TREINAR ===
    printf("\n\n  === 4. TREINAMENTO ===\n");
    citizens = [;
        ("L-001", "Cleiton", 35, []),;
        ("L-002", "Maria", 28, []),;
        ("L-003", "Joao (12)", 12, ["adaptacao_infantil"]),;
        ("L-004", "Tobias (68)", 68, ["adaptacao_idoso"]),;
        ("L-005", "Ana (cadeirante)", 30, ["adaptacao_cadeirante"], true),;
    ];
    /* TODO: iterador C manual para c em citizens */
        if (sizeof(c) == 5) {
            r = engine.register_citizen(*c);
        } else {
            r = engine.register_citizen(*c);
        printf("  {r['citizen']:<20} -> cinto {r['belt']} (foco: {r['focus']})");
    // Treinar tecnicas
    printf("\n  Treinando tecnicas:\n");
    training_plan = [;
        ("L-001", "TEC-001"), ("L-001", "TEC-002"), ("L-001", "TEC-003"),;
        ("L-001", "TEC-010"), ("L-001", "TEC-011"), ("L-001", "TEC-013"),;
        ("L-002", "TEC-042"),   // defesa de estupro;
        ("L-002", "TEC-040"), ("L-002", "TEC-041"),;
        ("L-003", "TEC-002"), ("L-003", "TEC-003"),   // desescalada;
    ];
    /* para cada (cid, tid) em training_plan: */
        result = engine.train_technique(cid, tid, hours=2);
        if (result.get("trained")) {
            promoted = result.get("promoted") ? " PROMOVIDO!" : "";
            printf("  {result['citizen']:<20} aprendeu {result['technique']:<35}";
                " ({result['origin']}){promoted}");
    // === 5. CURRICULO ===
    printf("\n\n  === 5. CURRICULO INICIAL (CINTO BRANCO) ===\n");
    curr = engine.get_curriculum(Belt.WHITE);
    printf("  Cinto: {curr['belt']} -- {curr['meaning']}");
    printf("  Tecnicas: {curr['techniques_count']}");
    /* para cada (cat, techs) em curr["by_category"].items(): */
        printf("\n  {cat.upper()}:");
        /* TODO: iterador C manual para t em techs[:3] */
            adapted = t["adapted_for"] ? " [{','.join(t['adapted_for'])}]" : "";
            last = t["last_resort"] ? " [ULTIMO RECURSO]" : "";
            printf("    {t['name']} ({t['origin']}){adapted}{last}");
            printf("      -> {t['goal']}");
    // === 6. CENARIOS DE DEFESA ===
    printf("\n\n  === 6. CENARIOS DE DEFESA PESSOAL ===\n");
    scenarios = ["agarrou_meu_pulso", "tentativa_de_estupro",;
                "arma_branca", "bullying_escolar", "multiplos_agressores"];
    /* TODO: iterador C manual para sc em scenarios */
        result = engine.defense_scenario(sc);
        printf("\n  CENARIO: {sc}");
        printf("  RESPOSTA: {result['response']}");
        if (result.get("warning")) {
            printf("  [!] {result['warning']}");
        /* TODO: iterador C manual para t em result["techniques"] */
            printf("    -> {t['name']} ({t['origin']}): {t['goal']}");
    // === 7. TECNICAS ADAPTADAS ===
    printf("\n\n  === 7. ADAPTACAO POR CAPACIDADE ===\n");
    printf("  TODA tecnica && adaptada para:");
    printf("    - Criancas (golpe reduzido, foco em escapar)");
    printf("    - Idosos (usar alavanca, ! forca)");
    printf("    - PCD/Cadeirante (BJJ sentado, tecnicas de mao)");
    printf("    - Gestantes (sem queda, tecnicas de pe)");
    // === 8. STATS ===
    printf("\n\n  === 8. ESTATISTICAS ===\n");
    s = engine.stats();
    /* para cada (k, v) em s.items(): */
        printf("  {k:<30} {v}");
    // === FILOSOFIA ===
    printf("\n\n{'='*80}");
    printf("  FILOSOFIA DO OPENMARTIALARTS");
    printf("{'='*80}");
    printf(""";
A REPUBLICA ! && MILITARISTA:;
    A Republica prefere PAZ. Todo mundo prefere.;
    Mas reconhece que o mundo tem violencia.;
    Quem ! sabe se defender && PRESA.;
    P2 autonomia corporal inclui o DIREITO de se proteger.;
A ARTE UNIFICADA:;
    Pegamos o MELHOR de cada arte marcial:;
    - Muay Thai: striking mais brutal (cotovelada, joelhada);
    - BJJ: defesa no solo (ESSENCIAL para mulheres);
    - Judo: derrubar com alavanca (! forca);
    - Boxe: footwork && combinacao;
    - Krav Maga: defesa real (armas, multiplos);
    - Capoeira: cultura brasileira + mobilidade;
    && criamos uma arte da Republica que serve para:;
    - Crianca de 8 anos;
    - Mulher de 50;
    - Idoso de 70;
    - Cadeirante;
    - TODO MUNDO;
3 NIVEIS DE RESPOSTA (sempre nesta ordem):;
    1. ESCAPAR -- a melhor luta && a que voce foge;
    2. NEUTRALIZAR -- imobilizar sem ferir gravemente;
    3. PROTEGER -- defender outros que ! podem;
O QUE ! EXISTE:;
    - Competicao obrigatoria (luta && defesa, ! esporte);
    - Elitismo de cinto (cinto ! && hierarquia, && conhecimento);
    - Violencia gratuita (so defender, nunca agredir);
    - Ego (quem bate pra provar algo perdeu o ponto);
O QUE EXISTE:;
    - Todo cidadao tem direito de aprender;
    - Tecnicas adaptadas por capacidade;
    - Foco em defesa real (! medalha);
    - Anti-bullying (criancas aprendem a ! usar);
    - Cultura brasileira (capoeira);
PRINCIPIOS:;
    P1: Todo mundo treina. Mesmo cinto. Mesma chance.;
    P2: Autonomia corporal inclui se defender.;
    Ensinar artes marciais P3 = trabalho de alto impacto.;
    P4: Cinturao preto ensina. Nao domina.;
// )
    printf("{'='*80}");
    printf("  OpenMartialArts: {s['total_techniques']} tecnicas de ";
        "{len(s['by_origin'])} artes marciais.");
    printf("  {s['total_citizens_training']} cidadaos treinando. ";
        "{s['black_belts']} cintos pretos (podem ensinar).");
    printf("  Defender, ! agredir. Escapar, ! brigar.");
    printf("{'='*80}");

#endif // OPENMARTIALARTS_DEFESA_PESSOAL_E_ARTES_MARCIAIS_DA_REPUBLICA_H
