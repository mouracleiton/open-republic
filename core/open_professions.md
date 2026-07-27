# OpenProfessions -- Carreira Modular LEGO para TODAS as Profissoes

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_professions.py`

**Descricao:** ====================================================================
"Competencia > Titulo. Para TODO mundo.
 O enfermeiro melhor que medico vira tecnico reconhecido.
 O pedreiro melhor que engenheiro vira mestre reconhecido.
 O cozinheiro melhor que chef vira mestre culinario.
 Cada um faz o que PODE. Cada um e valorizado pelo que FAZ."
O QUE ISTO FAZ:
  Define carreira modular (Junior -> Pleno -> Senior -> Mestre)
  para TODAS as profissoes da Republica.
  Cada profissao tem niveis com competencias claras.
  Promocao por COMPETENCIA, nao por tempo ou diploma.
PROFISSOES COBERTAS (30+):
  Saude, Educacao, Construcao, Software, Agricultura, Musica,
  Artes, Culinaria, Seguranca, Transporte, Eletricidade,
  Encanaduria, Mecanica, Costura, Cabelereiro, Limpeza,
  Administracao, Jornalismo, Direito, Contabilidade,
  Design, Filmagem, Eletronica, Marcenaria, Pintura,
  Jardinagem, Animacao, Pesca, Apicultura, Veterinaria.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenProfessions -- Carreira Modular LEGO para TODAS as Profissoes
====================================================================

"Competencia > Titulo. Para TODO mundo.
 O enfermeiro melhor que medico vira tecnico reconhecido.
 O pedreiro melhor que engenheiro vira mestre reconhecido.
 O cozinheiro melhor que chef vira mestre culinario.
 Cada um faz o que PODE. Cada um e valorizado pelo que FAZ."

O QUE ISTO FAZ:
  Define carreira modular (Junior -> Pleno -> Senior -> Mestre)
  para TODAS as profissoes da Republica.
  Cada profissao tem niveis com competencias claras.
  Promocao por COMPETENCIA, nao por tempo ou diploma.

PROFISSOES COBERTAS (30+):
  Saude, Educacao, Construcao, Software, Agricultura, Musica,
  Artes, Culinaria, Seguranca, Transporte, Eletricidade,
  Encanaduria, Mecanica, Costura, Cabelereiro, Limpeza,
  Administracao, Jornalismo, Direito, Contabilidade,
  Design, Filmagem, Eletronica, Marcenaria, Pintura,
  Jardinagem, Animacao, Pesca, Apicultura, Veterinaria.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict, Counter de collections
// importa datetime de datetime


// ============================================================================
// 1. NIVEIS UNIVERSAIS DE CARREIRA
// ============================================================================

classe CareerLevel herda de Enum:
    // Niveis universais -- toda profissao tem estes niveis.

    DIFERENCA vs sistema atual:
    - nao ha "superior" vs "inferior"
    - Cada nivel faz o que PODE
    - Promocao por COMPETENCIA (casos resolvidos + avaliacao)
    - "Autodidata melhor que formado?" RECONHECIDO.
    // 
    APRENDIZ = ("aprendiz", 0, "Aprendendo o basico. Observa. Pratica com supervisao.")
    TECNICO = ("tecnico", 1, "Sabe o fundamental. Faz sozinho com supervisao remota.")
    JUNIOR = ("junior", 2, "Independente no comum. Basico dominado.")
    PLENO = ("pleno", 3, "Experiencia. Resolve complexo. Supervisiona junior.")
    SENIOR = ("senior", 4, "Especialista. Resolve o dificil. Ensina.")
    MESTRE = ("mestre", 5, "Referencia. Resolve o impossivel. Forma proxima geracao.")

    // decorador: @property
    funcao level_num(self) -> inteiro:
        retorne self.value[1]

    // decorador: @property
    funcao meaning(self) -> texto:
        retorne self.value[2]

    // decorador: @property
    funcao label(self) -> texto:
        retorne self.value[0]


classe SkillCategory herda de Enum:
    DIAGNOSTIC = "diagnostico"  // identificar problema
    EXECUTION = "execucao"  // fazer o trabalho
    CREATION = "criacao"  // criar algo novo
    SUPERVISION = "supervisao"  // guiar outros
    TEACHING = "ensino"  // ensinar
    EMERGENCY = "emergencia"  // resolver urgencia
    MANAGEMENT = "gestao"  // gerir equipe/operacao
    INNOVATION = "inovacao"  // melhorar processo


// ============================================================================
// 2. DEFINICAO DE PROFISSAO
// ============================================================================

// decorador: @dataclass
classe ProfessionSkill:
    // Uma skill dentro de uma profissao.
    skill_id: texto
    name: texto
    category: SkillCategory
    seja description: texto = ""
    seja min_level: CareerLevel = CareerLevel.TECNICO // nivel minimo para fazer


// decorador: @dataclass
classe Profession:
    // Uma profissao na Republica.

    Cada profissao tem:
    - Skills organizadas por nivel
    - Criterios de promocao
    - Carga de trabalho distribuida por nivel
    - Reconhecimento de autodidatas
    // 
    prof_id: texto
    name: texto                          // ex: "Pedreiro", "Programador", "Medico"
    area: texto                          // ex: "construcao", "saude", "software"
    seja description: texto = ""
    seja skills: [ProfessionSkill] = field(default_factory=list)

    // Criterios de promocao por nivel
    seja promotion_criteria: {texto: Dict} = field(default_factory=dict)

    // Distribuicao ideal de carga
    seja ideal_load: {texto: texto} = field(default_factory=dict)


// ============================================================================
// 3. CATALOGO DE PROFISSOES (30+)
// ============================================================================

funcao build_profession_catalog() -> [Profession]:
    // Constroi catalogo com 30+ profissoes.

    professions = []

    // === SAUDE ===
    professions.append(Profession(
        "PR-MED", "Medico", "saude",
        "Medicina: diagnostico, tratamento, cirurgia, prevencao.",
        skills = [
            ProfessionSkill("MED-TRI", "Triagem", SkillCategory.DIAGNOSTIC, "", CareerLevel.TECNICO),
            ProfessionSkill("MED-DIAG", "Diagnostico comum", SkillCategory.DIAGNOSTIC, "", CareerLevel.JUNIOR),
            ProfessionSkill("MED-PRES", "Prescricao basica", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("MED-COMPLEX", "Diagnostico complexo", SkillCategory.DIAGNOSTIC, "", CareerLevel.PLENO),
            ProfessionSkill("MED-STRONG", "Prescricao forte", SkillCategory.EXECUTION, "", CareerLevel.PLENO),
            ProfessionSkill("MED-SURG", "Cirurgia", SkillCategory.EXECUTION, "", CareerLevel.SENIOR),
            ProfessionSkill("MED-ANEST", "Anestesia", SkillCategory.EXECUTION, "", CareerLevel.SENIOR),
            ProfessionSkill("MED-TEACH", "Ensinar medicina", SkillCategory.TEACHING, "", CareerLevel.SENIOR),
            ProfessionSkill("MED-RARE", "Casos raros", SkillCategory.DIAGNOSTIC, "", CareerLevel.MESTRE),
        ],
        ideal_load = {
            "tecnico": "25% (triagem + procedimento)",
            "junior": "60% (comum + prescricao)",
            "pleno": "5% (complexo)",
            "senior": "8% (cirurgia)",
            "mestre": "2% (raro + ensino)",
        },
    ))

    professions.append(Profession(
        "PR-NURSE", "Tecnico Medico (ex-enfermeiro)", "saude",
        "Enfermagem elevada a tecnico medico. Faz mais. Reconhecido.",
        skills = [
            ProfessionSkill("NUR-TRI", "Triagem", SkillCategory.DIAGNOSTIC, "", CareerLevel.APRENDIZ),
            ProfessionSkill("NUR-SUTURE", "Sutura", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("NUR-INJECT", "Injecao/Medicacao", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("NUR-EMERG", "Primeiros socorros", SkillCategory.EMERGENCY, "", CareerLevel.TECNICO),
            ProfessionSkill("NUR-WOUND", "Curativo avanzado", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("NUR-LEAD", "Liderar equipe enfermagem", SkillCategory.MANAGEMENT, "", CareerLevel.SENIOR),
        ],
        ideal_load = {
            "tecnico": "faz triagem + procedimento (reconhecido)",
            "junior": "faz curativo complexo + assiste cirurgia",
            "senior": "lidera equipe + ensina",
        },
    ))

    // === EDUCACAO ===
    professions.append(Profession(
        "PR-TEACH", "Professor", "educacao",
        "Ensino: fundamental, medio, universitario. Aprender e ensinar.",
        skills = [
            ProfessionSkill("TEA-ASSIST", "Auxiliar de aula", SkillCategory.EXECUTION, "", CareerLevel.APRENDIZ),
            ProfessionSkill("TEA-BASIC", "Ensinar basico", SkillCategory.TEACHING, "", CareerLevel.TECNICO),
            ProfessionSkill("TEA-CLASS", "Dar aula completa", SkillCategory.TEACHING, "", CareerLevel.JUNIOR),
            ProfessionSkill("TEA-CURRIC", "Desenhar curriculo", SkillCategory.CREATION, "", CareerLevel.PLENO),
            ProfessionSkill("TEA-MENTOR", "Mentorar professores", SkillCategory.SUPERVISION, "", CareerLevel.SENIOR),
            ProfessionSkill("TEA-THEORY", "Teoria educacional", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
        ideal_load = {
            "tecnico": "30% (auxilia + da aula basica)",
            "junior": "50% (da aula + avalia)",
            "pleno": "15% (desenha curriculo)",
            "senior": "4% (mentora)",
            "mestre": "1% (teoria + pesquisa)",
        },
    ))

    // === CONSTRUCAO ===
    professions.append(Profession(
        "PR-BUILD", "Pedreiro/Construtor", "construcao",
        "Construcao civil: alvenaria, concreto, estrutura.",
        skills = [
            ProfessionSkill("BUI-MIX", "Preparar massa", SkillCategory.EXECUTION, "", CareerLevel.APRENDIZ),
            ProfessionSkill("BUI-BRICK", "Assentar tijolo", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("BUI-PLUMB", "Prumo e nivel", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("BUI-FOUND", "Fundacao", SkillCategory.EXECUTION, "", CareerLevel.PLENO),
            ProfessionSkill("BUI-STRUCT", "Estrutura complexa", SkillCategory.EXECUTION, "", CareerLevel.SENIOR),
            ProfessionSkill("BUI-DESIGN", "Projetar construcao", SkillCategory.CREATION, "", CareerLevel.SENIOR),
            ProfessionSkill("BUI-INNOV", "Inovar tecnica", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
        ideal_load = {
            "tecnico": "40% (alvenaria basica)",
            "junior": "35% (estrutura + acabamento)",
            "pleno": "15% (fundacao + complexo)",
            "senior": "8% (projeta + ensina)",
            "mestre": "2% (inova)",
        },
    ))

    professions.append(Profession(
        "PR-ELEC", "Eletricista", "construcao",
        "Instalacao eletrica: fiação, tomadas, quadros, solar.",
        skills = [
            ProfessionSkill("ELE-WIRE", "Passar fiação", SkillCategory.EXECUTION, "", CareerLevel.APRENDIZ),
            ProfessionSkill("ELE-OUTLET", "Instalar tomada", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("ELE-CIRCUIT", "Circuito completo", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("ELE-PANEL", "Quadro de distribuicao", SkillCategory.EXECUTION, "", CareerLevel.PLENO),
            ProfessionSkill("ELE-SOLAR", "Instalacao solar", SkillCategory.EXECUTION, "", CareerLevel.SENIOR),
            ProfessionSkill("ELE-DESIGN", "Projetar eletrica", SkillCategory.CREATION, "", CareerLevel.SENIOR),
            ProfessionSkill("ELE-SMART", "Rede inteligente", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
        ideal_load = {
            "tecnico": "45% (tomada + fiação)",
            "junior": "30% (circuito)",
            "pleno": "15% (quadro)",
            "senior": "8% (solar + projeto)",
            "mestre": "2% (inova)",
        },
    ))

    professions.append(Profession(
        "PR-PLUMB", "Encanador/Hidraulico", "construcao",
        "Hidraulica: canos, conexoes, caixa d'agua, esgoto.",
        skills = [
            ProfessionSkill("PLU-PVC", "Instalar PVC", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("PLU-FIX", "Reparar vazamento", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("PLU-SYSTEM", "Sistema hidraulico", SkillCategory.EXECUTION, "", CareerLevel.PLENO),
            ProfessionSkill("PLU-DESIGN", "Projetar hidraulica", SkillCategory.CREATION, "", CareerLevel.SENIOR),
            ProfessionSkill("PLU-SEWAGE", "Sistema de esgoto", SkillCategory.EXECUTION, "", CareerLevel.SENIOR),
        ],
    ))

    // === SOFTWARE ===
    professions.append(Profession(
        "PR-DEV", "Programador", "software",
        "Desenvolvimento de software em Rust (linguagem universal da Republica).",
        skills = [
            ProfessionSkill("DEV-HELLO", "Hello World", SkillCategory.EXECUTION, "", CareerLevel.APRENDIZ),
            ProfessionSkill("DEV-BASIC", "Codigo basico", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("DEV-FEATURE", "Implementar feature", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("DEV-ARCH", "Arquitetura de sistema", SkillCategory.CREATION, "", CareerLevel.PLENO),
            ProfessionSkill("DEV-REVIEW", "Code review", SkillCategory.SUPERVISION, "", CareerLevel.PLENO),
            ProfessionSkill("DEV-OPTIMIZE", "Otimizar performance", SkillCategory.INNOVATION, "", CareerLevel.SENIOR),
            ProfessionSkill("DEV-DESIGN", "Desenhar sistema completo", SkillCategory.CREATION, "", CareerLevel.SENIOR),
            ProfessionSkill("DEV-LANG", "Criar linguagem/protocolo", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
        ideal_load = {
            "tecnico": "20% (bug fix + basico)",
            "junior": "50% (features)",
            "pleno": "20% (arquitetura + review)",
            "senior": "8% (otimiza + ensina)",
            "mestre": "2% (cria linguagem)",
        },
    ))

    // === AGRICULTURA ===
    professions.append(Profession(
        "PR-FARM", "Agricultor", "agricultura",
        "Agricultura regenerativa: plantio, colheita, solo, irrigacao.",
        skills = [
            ProfessionSkill("FAR-SEED", "Plantar semente", SkillCategory.EXECUTION, "", CareerLevel.APRENDIZ),
            ProfessionSkill("FAR-SOIL", "Analisar solo", SkillCategory.DIAGNOSTIC, "", CareerLevel.TECNICO),
            ProfessionSkill("FAR-IRRIG", "Irrigacao", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("FAR-PEST", "Controle de pragas", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("FAR-CROP", "Gestao de safra", SkillCategory.MANAGEMENT, "", CareerLevel.PLENO),
            ProfessionSkill("FAR-ILPF", "Integracao lavoura-pecuaria", SkillCategory.INNOVATION, "", CareerLevel.SENIOR),
            ProfessionSkill("FAR-REGEN", "Agricultura regenerativa", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === CULINARIA ===
    professions.append(Profession(
        "PR-CHEF", "Cozinheiro", "culinaria",
        "Culinaria: preparar comida para comunidade. Restaurante comunitario.",
        skills = [
            ProfessionSkill("CHE-CUT", "Cortar ingredientes", SkillCategory.EXECUTION, "", CareerLevel.APRENDIZ),
            ProfessionSkill("CHE-COOK", "Cozinhar basico", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("CHE-RECIPE", "Seguir receita", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("CHE-CREATE", "Criar prato", SkillCategory.CREATION, "", CareerLevel.PLENO),
            ProfessionSkill("CHE-MENU", "Desenhar menu", SkillCategory.CREATION, "", CareerLevel.SENIOR),
            ProfessionSkill("CHE-KITCHEN", "Liderar cozinha", SkillCategory.MANAGEMENT, "", CareerLevel.SENIOR),
            ProfessionSkill("CHE-MASTER", "Culinaria mestra", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === MUSICA ===
    professions.append(Profession(
        "PR-MUSIC", "Musico", "musica",
        "Musica: criar, tocar, produzir. Todos os generos sao patrimonio.",
        skills = [
            ProfessionSkill("MUS-RHYTHM", "Manter ritmo", SkillCategory.EXECUTION, "", CareerLevel.APRENDIZ),
            ProfessionSkill("MUS-PLAY", "Tocar instrumento", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("MUS-COMPOSE", "Compor musica", SkillCategory.CREATION, "", CareerLevel.JUNIOR),
            ProfessionSkill("MUS-ARRANGE", "Arranjo", SkillCategory.CREATION, "", CareerLevel.PLENO),
            ProfessionSkill("MUS-PRODUCE", "Produzir album", SkillCategory.MANAGEMENT, "", CareerLevel.SENIOR),
            ProfessionSkill("MUS-INNOV", "Criar genero/estilo", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === SEGURANCA ===
    professions.append(Profession(
        "PR-SEC", "Agente de Seguranca", "seguranca",
        "Seguranca comunitaria: patrulha, defesa, prevencao (OpenMartialArts).",
        skills = [
            ProfessionSkill("SEC-PATROL", "Patrulhar", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("SEC-DEFEND", "Defesa pessoal", SkillCategory.EMERGENCY, "", CareerLevel.JUNIOR),
            ProfessionSkill("SEC-DEESCAL", "Desescalar conflito", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("SEC-PLAN", "Planejar seguranca", SkillCategory.MANAGEMENT, "", CareerLevel.PLENO),
            ProfessionSkill("SEC-TRAIN", "Treinar agentes", SkillCategory.TEACHING, "", CareerLevel.SENIOR),
            ProfessionSkill("SEC-STRAT", "Estrategia de seguranca", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === TRANSPORTE ===
    professions.append(Profession(
        "PR-DRIVE", "Motorista/Transportador", "transporte",
        "Transporte: carona solidaria, transporte publico, entrega.",
        skills = [
            ProfessionSkill("DRI-DRIVE", "Dirigir", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("DRI-ROUTE", "Otimizar rota", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("DRI-MAINT", "Manutencao basica", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("DRI-FLEET", "Gerir frota", SkillCategory.MANAGEMENT, "", CareerLevel.PLENO),
            ProfessionSkill("DRI-LOGISTICS", "Logistica complexa", SkillCategory.MANAGEMENT, "", CareerLevel.SENIOR),
        ],
    ))

    // === MARCENARIA ===
    professions.append(Profession(
        "PR-CARP", "Marceneiro", "construcao",
        "Marcenaria: moveis, portas, estrutura de madeira.",
        skills = [
            ProfessionSkill("CAR-CUT", "Cortar madeira", SkillCategory.EXECUTION, "", CareerLevel.APRENDIZ),
            ProfessionSkill("CAR-ASSEMB", "Montar movel", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("CAR-DESIGN", "Desenhar movel", SkillCategory.CREATION, "", CareerLevel.JUNIOR),
            ProfessionSkill("CAR-CUSTOM", "Moveis customizados", SkillCategory.CREATION, "", CareerLevel.PLENO),
            ProfessionSkill("CAR-MASTER", "Marcenaria fina", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === ELETRONICA ===
    professions.append(Profession(
        "PR-ELECTRO", "Tecnico em Eletronica", "produtividade",
        "Eletronica: consertar, fabricar, criar circuitos (FabLab).",
        skills = [
            ProfessionSkill("ELE-SOLDER", "Soldar", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("ELE-DIAG", "Diagnosticar defeito", SkillCategory.DIAGNOSTIC, "", CareerLevel.JUNIOR),
            ProfessionSkill("ELE-FIX", "Consertar placa", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("ELE-DESIGN-PCB", "Desenhar PCB", SkillCategory.CREATION, "", CareerLevel.PLENO),
            ProfessionSkill("ELE-FAB", "Fabricar no FabLab", SkillCategory.CREATION, "", CareerLevel.SENIOR),
            ProfessionSkill("ELE-CHIP", "Design de chip (RTL)", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === COSTURA ===
    professions.append(Profession(
        "PR-SEW", "Costureiro", "produtividade",
        "Costura: roupas, reparos, customizacao.",
        skills = [
            ProfessionSkill("SEW-MACHINE", "Maquina de costurar", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("SEW-PATTERN", "Seguir molde", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("SEW-CREATE", "Criar peca", SkillCategory.CREATION, "", CareerLevel.PLENO),
            ProfessionSkill("SEW-DESIGN", "Desenhar colecao", SkillCategory.CREATION, "", CareerLevel.SENIOR),
            ProfessionSkill("SEW-MASTER", "Alta costura", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === CABELEIREIRO ===
    professions.append(Profession(
        "PR-HAIR", "Cabelereiro/Barbeiro", "estetica",
        "Cabelo e barba: corte, cor, tratamento.",
        skills = [
            ProfessionSkill("HAIR-CUT", "Corte basico", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("HAIR-COLOR", "Coloracao", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("HAIR-STYLE", "Estilo avancado", SkillCategory.CREATION, "", CareerLevel.PLENO),
            falso ? SkillCategory.TEACHING : nulo, // placeholder
        falso ? ] : [
            ProfessionSkill("HAIR-CUT", "Corte basico", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("HAIR-COLOR", "Coloracao", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("HAIR-STYLE", "Estilo avancado", SkillCategory.CREATION, "", CareerLevel.PLENO),
            ProfessionSkill("HAIR-CHEMICAL", "Tratamento quimico", SkillCategory.EXECUTION, "", CareerLevel.SENIOR),
            ProfessionSkill("HAIR-MASTER", "Estilo mestre", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === JORNALISMO ===
    professions.append(Profession(
        "PR-JOUR", "Jornalista", "comunicacao",
        "Jornalismo: investigar, verificar, publicar (OpenHistory fact-check).",
        skills = [
            ProfessionSkill("JOU-REPORT", "Reportar fato", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("JOU-FACT", "Fact-check", SkillCategory.DIAGNOSTIC, "", CareerLevel.JUNIOR),
            ProfessionSkill("JOU-INVEST", "Investigar", SkillCategory.EXECUTION, "", CareerLevel.PLENO),
            ProfessionSkill("JOU-EDIT", "Editar publicacao", SkillCategory.SUPERVISION, "", CareerLevel.SENIOR),
            ProfessionSkill("JOU-LEAD", "Liderar redacao", SkillCategory.MANAGEMENT, "", CareerLevel.MESTRE),
        ],
    ))

    // === MECANICA ===
    professions.append(Profession(
        "PR-MECH", "Mecanico", "transporte",
        "Mecanica: veiculos, maquinas, motores.",
        skills = [
            ProfessionSkill("MEC-OIL", "Troca de oleo", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("MEC-DIAG", "Diagnosticar problema", SkillCategory.DIAGNOSTIC, "", CareerLevel.JUNIOR),
            ProfessionSkill("MEC-ENGINE", "Reparar motor", SkillCategory.EXECUTION, "", CareerLevel.PLENO),
            ProfessionSkill("MEC-ELECTRIC", "Eletrica veicular", SkillCategory.EXECUTION, "", CareerLevel.SENIOR),
            ProfessionSkill("MEC-DESIGN", "Projetar maquina", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === PINTURA ===
    professions.append(Profession(
        "PR-PAINT", "Pintor", "construcao",
        "Pintura: paredes, fachadas, artistica.",
        skills = [
            ProfessionSkill("PAI-ROLL", "Pintar com rolo", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("PAI-PREP", "Preparar superficie", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("PAI-DETAIL", "Acabamento fino", SkillCategory.EXECUTION, "", CareerLevel.PLENO),
            ProfessionSkill("PAI-ART", "Pintura artistica", SkillCategory.CREATION, "", CareerLevel.SENIOR),
            ProfessionSkill("PAI-MURAL", "Mural comunitario", SkillCategory.CREATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === VETERINARIA ===
    professions.append(Profession(
        "PR-VET", "Veterinario", "saude",
        "Saude animal: pets, criação, vida selvagem.",
        skills = [
            ProfessionSkill("VET-CONSULT", "Consulta basica", SkillCategory.DIAGNOSTIC, "", CareerLevel.JUNIOR),
            ProfessionSkill("VET-VACC", "Vacinar animal", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("VET-SURG", "Cirurgia animal", SkillCategory.EXECUTION, "", CareerLevel.SENIOR),
            ProfessionSkill("VET-TEACH", "Ensinar veterinaria", SkillCategory.TEACHING, "", CareerLevel.MESTRE),
        ],
    ))

    // === JARDINAGEM ===
    professions.append(Profession(
        "PR-GARDEN", "Jardineiro", "ambiente",
        "Jardinagem e paisagismo: jardins, hortas, areas verdes.",
        skills = [
            ProfessionSkill("GAR-WATER", "Regar plantas", SkillCategory.EXECUTION, "", CareerLevel.APRENDIZ),
            ProfessionSkill("GAR-PRUNE", "Podar", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("GAR-DESIGN", "Paisagismo", SkillCategory.CREATION, "", CareerLevel.PLENO),
            ProfessionSkill("GAR-MASTER", "Jardim mestre", SkillCategory.INNOVATION, "", CareerLevel.MESTRE),
        ],
    ))

    // === LIMPEZA ===
    professions.append(Profession(
        "PR-CLEAN", "Agente de Limpeza", "ambiente",
        "Limpeza: espacos publicos, hospitais, escolas. Essencial.",
        skills = [
            ProfessionSkill("CLN-BASIC", "Limpeza basica", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("CLN-DEEP", "Limpeza profunda", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("CLN-HOSPITAL", "Limpeza hospitalar", SkillCategory.EXECUTION, "", CareerLevel.PLENO),
            ProfessionSkill("CLN-LEAD", "Liderar equipe", SkillCategory.MANAGEMENT, "", CareerLevel.SENIOR),
        ],
    ))

    // === ADMINISTRACAO ===
    professions.append(Profession(
        "PR-ADMIN", "Administrador", "gestao",
        "Administracao: organizar, planejar, coordenar.",
        skills = [
            ProfessionSkill("ADM-CLERK", "Trabalho administrativo", SkillCategory.EXECUTION, "", CareerLevel.TECNICO),
            ProfessionSkill("ADM-ORG", "Organizar processo", SkillCategory.EXECUTION, "", CareerLevel.JUNIOR),
            ProfessionSkill("ADM-MANAGE", "Gerir operacao", SkillCategory.MANAGEMENT, "", CareerLevel.PLENO),
            ProfessionSkill("ADM-STRAT", "Estrategia", SkillCategory.INNOVATION, "", CareerLevel.SENIOR),
            ProfessionSkill("ADM-LEAD", "Liderar instituicao", SkillCategory.MANAGEMENT, "", CareerLevel.MESTRE),
        ],
    ))

    retorne professions


// ============================================================================
// 4. MOTOR DE PROFISSOES
// ============================================================================

classe ProfessionEngine:
    // Motor que gere todas as profissoes da Republica.

    PRINCIPIOS:
    1. COMPETENCIA > TITULO -- autodidata reconhecido
    2. CADA NIVEL FAZ O QUE PODE -- nao sobrecarrega senior
    3. PROMOCAO POR PROVA -- casos resolvidos + avaliacao
    4. TODAS AS PROFISSOES TEM O MESMO VALOR -- P1
    5. LEGO: cada profissional e uma peca que encaixa na cadeia
    // 

    funcao __init__(self):
        self.professions: {texto: Profession} = {
            p.prof_id: p para p em build_profession_catalog()
        }
        self.workers: {texto: Dict} = {}

    funcao list_professions(self) -> [Dict]:
        retorne [
            {"id": p.prof_id, "name": p.name, "area": p.area,
             "skills": tamanho(p.skills)}
            para p em self.professions.values()
        ]

    funcao get_career_path(self, prof_id: texto) -> {texto: qualquer}:
        // Mostra trilha de carreira completa de uma profissao.
        prof = self.professions.get(prof_id)
        se nao prof entao:
            retorne {"error": "Profissao nao encontrada"}

        by_level = defaultdict(list)
        para cada skill em prof.skills:
            by_level[skill.min_level.label].append(skill.name)

        retorne {
            "profession": prof.name,
            "area": prof.area,
            "description": prof.description,
            "career_path": {
                level.label: {
                    "meaning": level.meaning,
                    "skills": by_level.get(level.label, []),
                }
                para level em CareerLevel
            },
            "ideal_load": prof.ideal_load,
        }

    funcao recognize_self_taught(self, name: texto, profession: texto,
                               level: CareerLevel,
                               seja proof: texto = "",
                               seja cases: inteiro = 0) -> {texto: qualquer}:
        // Reconhece autodidata -- competência > título.

        EXEMPLO:
        - Maria aprendeu costura sozinha (mae ensinou)
        - Nunca fez curso. Mas faz vestido melhor que 'profissional'.
        - Sistema atual: 'voce nao tem diploma'.
        - Republica: RECONHECIDA. Costureira Junior. Comprovado.

        - Joao aprendeu programacao no OpenTerminal
        - Nunca fez faculdade. Mas escreveu 3 sistemas da Republica.
        - Republica: RECONHECIDO. Programador Pleno. Comprovado.
        // 
        wid = hashlib.md5("{name}{profession}".encode()).hexdigest()[:8]
        self.workers[wid] = {
            "name": name,
            "profession": profession,
            "level": level.label,
            "self_taught": verdadeiro,
            "proof": proof,
            "cases": cases,
        }
        retorne {
            "recognized": verdadeiro,
            "name": name,
            "profession": profession,
            "level": level.label,
            "self_taught": verdadeiro,
            "proof": proof,
            "message": (
                "{name} reconhecido como {profession} ({level.label}). "
                "SEM diploma. COM competencia. "
                "Prova: {proof}. "
                "Competencia > Titulo. P1 anti-elitismo."
            ),
        }

    funcao promote(self, worker_name: texto,
                new_level: CareerLevel,
                seja reason: texto = "") -> {texto: qualquer}:
        // Promove trabalhador por competencia comprovada.
        para cada (wid, w) em self.workers.items():
            se w["name"] == worker_name entao:
                old_level = w["level"]
                w["level"] = new_level.label
                retorne {
                    "promoted": verdadeiro,
                    "name": worker_name,
                    "old_level": old_level,
                    "new_level": new_level.label,
                    "reason": reason,
                    "message": (
                        "{worker_name}: {old_level} -> {new_level.label}. "
                        "Motivo: {reason}. "
                        "Competencia reconhecida."
                    ),
                }
        retorne {"error": "Trabalhador nao encontrado"}

    funcao profession_value_comparison(self) retorna List[{texto: texto}]:
        // Mostra que TODAS as profissoes tem o mesmo valor (P1).
        retorne [
            {"profissao": "Medico", "valor": "base 1.0", "por_que": "salva vidas"},
            {"profissao": "Lixeiro/Catador", "valor": "base 1.0 + impacto", "por_que": "sem eles todos adoecem"},
            {"profissao": "Professor", "valor": "base 1.0 + impacto", "por_que": "forma proxima geracao"},
            {"profissao": "Cozinheiro", "valor": "base 1.0 + impacto", "por_que": "alimenta comunidade"},
            {"profissao": "Programador", "valor": "base 1.0 + impacto", "por_que": "constroi sistemas"},
            {"profissao": "Pedreiro", "valor": "base 1.0 + impacto", "por_que": "constroi moradia"},
            {"profissao": "Costureira", "valor": "base 1.0", "por_que": "veste comunidade"},
            {"profissao": "Agricultor", "valor": "base 1.0 + impacto", "por_que": "alimenta todos"},
            {"profissao": "Musico", "valor": "base 1.0", "por_que": "cura com arte"},
            {"profissao": "Eletricista", "valor": "base 1.0 + impacto", "por_que": "sem luz nada funciona"},
            {"profissao": "Cabelereiro", "valor": "base 1.0", "por_que": "dignidade e bem-estar"},
            {"profissao": "Mecanico", "valor": "base 1.0", "por_que": "transporte funciona"},
        ]

    funcao stats(self) -> {texto: qualquer}:
        by_area = Counter(p.area para p em self.professions.values())
        retorne {
            "total_profissoes": tamanho(self.professions),
            "total_skills": soma(tamanho(p.skills) para p em self.professions.values()),
            "por_area": dict(by_area),
            "trabalhadores_reconhecidos": tamanho(self.workers),
            "autodidatas_reconhecidos": soma(
                1 para w em self.workers.values() if w.get("self_taught")),
        }


// ============================================================================
// 5. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = ProfessionEngine()

    imprima("=" * 80)
    imprima("  OPENPROFESSIONS -- CARREIRA MODULAR PARA TODAS AS PROFISSOES")
    imprima("  Competencia > Titulo. Cada um faz o que PODE.")
    imprima("=" * 80)

    // === 1. PROFISSOES REGISTRADAS ===
    imprima("\n\n  === 1. PROFISSOES ({len(engine.professions)}) ===\n")
    by_area = defaultdict(list)
    para cada p em engine.professions.values():
        by_area[p.area].append(p)
    para cada area em ordene(by_area.keys()):
        imprima("\n  {area.upper()}:")
        para cada p em by_area[area]:
            imprima("    [{p.prof_id}] {p.name:<30} {len(p.skills)} skills")

    // === 2. CARREIRA MODULAR (exemplos detalhados) ===
    imprima("\n\n  === 2. TRILHA DE CARREIRA (exemplos) ===\n")

    para cada prof_id em ["PR-MED", "PR-DEV", "PR-CHEF", "PR-BUILD"]:
        path = engine.get_career_path(prof_id)
        imprima("\n  {path['profession'].upper()} ({path['area']}):")
        para cada (level_label, data) em path["career_path"].items():
            skills = data["skills"]
            se skills entao:
                imprima("    [{level_label}] {data['meaning'][:40]}")
                imprima("      Skills: {', '.join(skills[:4])}")
        se path.get("ideal_load") entao:
            imprima("    Distribuicao ideal:")
            para cada (lvl, load) em path["ideal_load"].items():
                imprima("      {lvl}: {load}")

    // === 3. RECONHECIMENTO DE AUTODIDATAS ===
    imprima("\n\n  === 3. AUTODIDATAS RECONHECIDOS (competencia > titulo) ===\n")
    self_taught = [
        ("Maria das Dores", "Costureira", CareerLevel.PLENO,
         "Faz vestido de noiva melhor que atelier. 30 anos de experiencia."),
        ("Joao Silva", "Programador", CareerLevel.PLENO,
         "Aprendeu no OpenTerminal. Escreveu 3 sistemas da Republica em Rust."),
        ("Seu Ze", "Eletricista", CareerLevel.SENIOR,
         "40 anos de experiencia. Resolve quadro eletrico que engenheiro nao acha."),
        ("Dona Rita", "Cozinheira", CareerLevel.SENIOR,
         "Cozinha para 500 pessoas/dia no restaurante comunitario. Receitas proprias."),
        ("Carlos", "Marceneiro", CareerLevel.MESTRE,
         "Nunca fez curso. Faz moveis que parecem obra de arte. 50 anos de oficio."),
        ("Ana", "Agricultora", CareerLevel.PLENO,
         "Transformou terreno baldio em horta que alimenta 200 familias."),
    ]
    para name, prof, level, proof in self_taught:
        r = engine.recognize_self_taught(name, prof, level, proof)
        imprima("  {r['name']:<20} -> {r['profession']:<15} ({r['level']})")
        imprima("    {r['message'][:80]}")

    // === 4. PROMOCAO ===
    imprima("\n\n  === 4. PROMOCAO POR COMPETENCIA ===\n")
    r = engine.promote("Joao Silva", CareerLevel.SENIOR,
                       "Criou OpenModularArchitecture. 100+ modulos conectados.")
    imprima("  {r['message']}")

    // === 5. VALOR IGUAL PARA TODAS AS PROFISSOES ===
    imprima("\n\n  === 5. TODAS AS PROFISSOES TEM O MESMO VALOR (P1) ===\n")
    comparisons = engine.profession_value_comparison()
    imprima("  {'Profissao':<25} {'Valor':<18} {'Por que'}")
    imprima("  {'-'*70}")
    para cada c em comparisons:
        imprima("  {c['profissao']:<25} {c['valor']:<18} {c['por_que']}")

    imprima("\n  SEM 'superior' vs 'inferior'.")
    imprima("  Medico NAO vale mais que lixeiro.")
    imprima("  Advogado NAO vale mais que cozinheiro.")
    imprima("  Todos base 1.0 + impacto.")

    // === 6. STATS ===
    imprima("\n\n  === 6. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        imprima("  {k:<35} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA: CARREIRA MODULAR PARA TODOS")
    imprima("{'='*80}")
    imprima("""
  COMPETENCIA > TITULO (P1 anti-elitismo):
    O sistema atual diz: 'voce precisa de diploma para ser alguem.'
    A Republica diz: 'voce precisa de COMPETENCIA.'

    Maria aprendeu costura com a mae. Nunca fez curso.
    Mas faz vestido melhor que atelier de luxo.
    Sistema atual: 'voce nao e profissional.'
    Republica: COSTUREIRA PLENO. Reconhecida. Valorizada.

    Joao aprendeu Rust no OpenTerminal. Nunca fez faculdade.
    Mas escreveu 3 sistemas da Republica.
    Sistema atual: 'voce nao tem diploma de CI.'
    Republica: PROGRAMADOR PLENO. Reconhecido. Valorizado.

  6 NIVEIS UNIVERSAIS (toda profissao tem):
    APRENDIZ -- aprendendo o basico, observa
    TECNICO -- sabe o fundamental, faz com supervisao
    JUNIOR -- independente no comum
    PLENO -- experiencia, resolve complexo, supervisiona
    SENIOR -- especialista, resolve dificil, ensina
    MESTRE -- referencia, forma proxima geracao

  CARGA DISTRIBUIDA (ninguem sobrecarregado):
    Tecnico faz 30-45% (o basico)
    Junior faz 35-50% (o comum)
    Pleno faz 15-20% (o complexo)
    Senior faz 4-8% (o dificil)
    Mestre faz 1-2% (o impossivel + ensino)

    Resultado: Senior nao perde tempo com basico.
    Junior ganha experiencia. Tecnico faz o que sabe.
    Todo mundo desafogado.

  TODAS AS PROFISSOES TEM O MESMO VALOR:
    Medico base 1.0. Lixeiro base 1.0. Professor base 1.0.
    Diferenca so por IMPACTO (medido, nao opinado).
    Quem salva vidas tem alto impacto.
    Quem limpa o hospital TAMBEM salva vidas (sem limpeza, infeccao).
    Quem ensina tem alto impacto (forma geracao).
    Quem cozinha tem alto impacto (alimenta quem trabalha).

    nao HA 'profissao superior'.
    nao HA 'profissao inferior'.
    HA competencias diferentes. Todas necessarias.

  PRINCIPIOS:
    P1: Titulo nao faz superior. Competencia faz. Todas iguais.
    P2: Cada profissional escolhe sua carreira. Autonomia.
    P3: Todos trabalham base 1.0 + impacto. Sem salario diferente por cargo.
    P4: Promocao por competencia comprovada (casos + avaliacao).
// )
    imprima("{'='*80}")
    imprima("  OpenProfessions: {s['total_profissoes']} profissoes, "
          "{s['total_skills']} skills, "
          "{s['autodidatas_reconhecidos']} autodidatas reconhecidos.")
    imprima("  Competencia > Titulo. Cada um faz o que PODE.")
    imprima("{'='*80}")

```
