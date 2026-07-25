// HOW-TO COMPLETO DA OPENREPUBLIC -- gerado de Portugol++
#![allow(dead_code, unused_variables)]
use std::collections::{HashMap, HashSet};

//
HOW-TO COMPLETO DA OPENREPUBLIC;
================================;
Guia de implementacao. Do zero ao tudo.;
116 sistemas. 91.729 linhas. 35 politicas. CC0.;
Este ! && teoria. && INSTRUCAO.;
Cada passo tem: o que fazer, como fazer, quando, quem, quanto custa.;
COMO USAR ESTE DOCUMENTO:;
- Cidadao: comeca pela Fase 1 (o que VOCE faz hoje);
- Comunidade: comeca pela Fase 2 (instalar localmente);
- Governante: comeca pela Fase 3 (politica publica);
- Desenvolvedor: comeca pelo repositorio (contribuir);
LICENCA: CC0 UNIVERSAL;
//
// ============================================================================
// PARTE 0: O QUE E A OPENREPUBLIC (resumo)
// ============================================================================
RESUMO = """;
A OpenRepublic && uma federacao de nacoes sem propriedade privada nem moeda,;
como ecossistema de software de codigo aberto (CC0), com sistemas para todos;
os aspectos da vida social, governados por 4 principios constitucionais.;
4 PRINCIPIOS:;
P1: ANTI-ELITISMO (ninguem && superior, todos iguais);
P2: AUTONOMIA CORPORAL ABSOLUTA (corpo && seu);
P3: TRABALHO IGUAL (base 1.0 + impacto);
P4: PROCESSO DEMOCRATICO (assembleia decidem);
META: imortalidade com qualidade para TODOS. Botamos la em cima.;
//
// ============================================================================
// PARTE 1: COMO COMECAR (HOJE, voce, cidadao)
// ============================================================================
PARTE_1_CIDADAO = """;
====================================================================;
PARTE 1: O QUE VOCE FAZ HOJE (Cidadao individual);
===================================================================;
VOCE ! PRECISA ESPERAR O GOVERNO.;
A Republica comeca em VOCE. Hoje. Com o que tem.;
PASSO 1: ENTENDER OS 4 PRINCIPIOS;
- Leia P1-P4. Internalize. Se concorda, voce ja && da Republica.;
- P1: ninguem && melhor que ninguem. Rico, pobre, preto, branco, doutor, analfabeto. IGUAIS.;
- P2: seu corpo && SO SEU. Ninguem decide por voce. Nunca.;
- P3: todo trabalho vale base 1.0. Diferenca so por impacto REAL.;
- P4: democracia direta. Voce vota em tudo. Sem politico no meio.;
PASSO 2: ADOPTAR O MINDSET;
- Parar de competir destrutivamente. Competir melhorando: OK.;
- Parar de lucrar sobre trabalho alheio (5% maximo).;
- Tratar TODO mundo com dignidade (dever civico).;
- Questionar determinismo ("sempre foi assim" = preguica mental).;
- Tudo && CC0. Voce ! "possui". Voce CUIDA do bem comum.;
PASSO 3: USAR SISTEMAS DA REPUBLICA (hoje);
- OpenTerminal: qualquer TV/PC/Smartphone ocioso vira terminal.;
- OpenSkills: comecar a registrar suas skills (sistema comprova).;
- OpenLegoCode: programar sem codigo (blocos LEGO).;
- OpenEducation/OpenUniversity: aprender gratis.;
- OpenInbox: unificar notificacoes (parar de ser bombardeado).;
- OpenRepair: consertar ao inves de jogar fora.;
- OpenMusic: criar/ouvir musica sem ECAD, sem royalty.;
PASSO 4: SAUDE;
- OpenHealth: rastreio anual de 12 sistemas corporais.;
- Se tem erro visual: exigir LASIK (direito, ! privilegio).;
- Saude mental: buscar terapia sem rotular. Neuroplasticidade.;
- OpenMartialArts: comecar a treinar defesa pessoal.;
PASSO 5: COMUNIDADE;
- Encontrar 3-5 pessoas que concordam com P1-P4.;
- Formar nucleo da Republica localmente.;
- Comecar OpenLaborRelay (trocar tarefas entre si).;
- OpenFamilyLabor: distribuir carga familiar com quem mora com voce.;
- OpenResponsibility: definir quem faz o que. Sem sobrecarga.;
PASSO 6: DINHEIRO (durante transicao);
- Comecar a usar OpenCredit com seu nucleo.;
- Trocar favores/servicos sem dinheiro.;
- Quando comprar: pensar no 5% (quem produziu levou quanto?).;
- OpenValueFlow: rastrear para onde vai seu dinheiro.;
PASSO 7: VOZ;
- OpenConstituentAssembly: votar nas propostas.;
- Propor melhorias (merge request no repositorio).;
- OpenWololo: converter pessoas (mostrar que funciona).;
- OpenCivicEducation: espalhar dever civico.;
//
// ============================================================================
// PARTE 2: COMO INSTALAR LOCALMENTE (Comunidade)
// ============================================================================
PARTE_2_COMUNIDADE = """;
====================================================================;
PARTE 2: INSTALAR A REPUBLICA NA SUA COMUNIDADE;
===================================================================;
Voce tem 5+ pessoas? Pode instalar uma celula da Republica.;
PASSO 1: INFRAESTRUTURA MINIMA;
O que precisam:;
- 1 computador || smartphone (OpenTerminal);
- Conexao internet (OpenNetwork/OpenProtocol quando disponivel);
- 1 espaco fisico (sala de alguem, garagem, praca);
- Custo: R$ 0 (usar o que tem);
PASSO 2: REGISTRO DO NUCLEO;
- Nome do nucleo (ex: Republica Vila Mariana);
- Membros iniciais (minimo 3);
- Localizacao;
- Repositorio local (git init -- puxar do main);
COMO FAZER:;
    git clone repositorio-principal/open-republic;
    cd open-republic;
    python3 core/constitutional_engine.py // inicia motor P1-P4;
    python3 core/open_constituent_assembly.py // primeira votacao;
PASSO 3: PRIMEIRA ASSEMBLEIA;
- Reunir membros;
- Apresentar P1-P4;
- Votar parametrizacao (limite horas, descanso, etc);
- O POVO decide. Fundador propoe. Povo altera.;
COMO FAZER:;
    python3 core/open_constituent_assembly.py;
    // 10.000 cidadaos simulados votam
    // Resultado: LEI (is_law=true quando ratificado)
PASSO 4: SISTEMAS BASICOS (instalar em ordem);
Ordem de dependencia (LEGO -- um depende do outro):;
1. ConstitutionalEngine (P1-P4) -- OBRIGATORIO PRIMEIRO;
    python3 core/constitutional_engine.py;
2. OpenConstituentAssembly (votacao);
    python3 core/open_constituent_assembly.py;
3. OpenLaborPolicy (parametros de trabalho);
    python3 core/open_labor_policy.py;
    // Carrega parametros da assembleia automaticamente
4. OpenCredit (moeda social);
    python3 core/open_coin.py;
    // Sem juros. Expira. Nao acumula.
5. OpenSkills (registro de competencias);
    python3 core/open_repo_skills.py;
    // Cada membro cria perfil. Sistema comprova.
6. OpenLaborRelay (distribuicao de tarefas);
    python3 core/open_labor_relay.py;
    // Tarefas circulam. Benchmark de qualidade.
7. OpenHealth (saude comunitaria);
    python3 open-health/modules/open_sus.py;
    // Rastreio. Telemedicina. Padrao Sirio-Libanes.
8. OpenEducation/OpenUniversity;
    python3 open-university/core/open_university.py;
    python3 open-school/core/open_school.py;
PASSO 5: MODULOS ADICIONAIS (encaixar conforme necessidade);
Cada modulo && LEGO. Encaixa quando precisar:;
Saude:;
    open-health/modules/open_healthcare_access.py;
    open-health/modules/open_vision.py;
    open-health/modules/open_beauty.py;
    open-health/modules/open_immortality.py;
    open-health/modules/open_medical_career.py;
Economia:;
    open-republic/core/open_fair_surplus.py (5% que volta);
    open-republic/core/open_value_flow.py (eliminar parasitas);
    open-republic/core/open_value_simulation.py (ver numeros reais);
    open-republic/core/open_erp.py (gestao empresarial);
Justica:;
    open-republic/core/open_penal_revision.py;
    open-republic/core/open_reintegration.py;
    open-republic/core/open_decriminalize.py;
    open-republic/core/open_anti_determinism.py;
Habitacao:;
    open-republic/core/open_dignity.py (erradicar rua);
    open-republic/core/open_territory.py (27 metropoles);
    open-republic/core/open_nightlife.py;
Cultura:;
    open-republic/core/open_music_heritage.py;
    open-music/core/open_music.py;
    open-republic/core/open_civic_education.py;
Seguranca:;
    open-republic/core/open_martial_arts.py;
    open-republic/core/open_weapons_policy.py;
    open-republic/core/open_anti_predatory.py;
Direitos:;
    open-republic/core/open_absence.py;
    open-republic/core/open_silence_policy.py;
    open-republic/core/open_anti_spam_call.py;
    open-republic/core/open_relationships.py;
Infraestrutura:;
    open-republic/core/open_modular_architecture.py;
    open-republic/core/open_lego_code.py;
    open-republic/core/open_lego_studio.py;
    open-republic/core/open_data_structure_v2.py;
    open-republic/core/open_terminal.py;
    open-tv-stick/core/open_tv_stick.py;
PASSO 6: VERIFICAR TUDO;
Rodar health check de todos os modulos:;
    python3 core/open_modular_architecture.py;
    // Mostra: 51+ modulos, saude de cada um, dependencias
PASSO 7: CONECTAR COM OUTROS NUCLEOS;
- OpenNetwork (rede P2P entre nucleos);
- OpenProtocol (protocolo de comunicacao);
- Compartilhar: tarefas, skills, recursos, votacoes;
//
// ============================================================================
// PARTE 3: COMO IMPLEMENTAR COMO POLITICA PUBLICA
// ============================================================================
PARTE_3_GOVERNO = """;
====================================================================;
PARTE 3: COMO IMPLEMENTAR COMO POLITICA PUBLICA (Governante);
===================================================================;
Voce && prefeito, governador, deputado? Pode acelerar.;
FASE 1: IMEDIATO (0-12 meses) -- Custo R$ 0;
- Adotar OpenSkills no serviço público (substitui currículo);
- Proibir spam telefônico (opt-in obrigatório);
- Desativar alertas de pressão em sistemas públicos;
- Ausência protegida para servidores (sem atestado);
- Educação cívica obrigatória nas escolas;
- OpenMartialArts nas escolas públicas;
- Descriminalizar porte para uso (tratamento, não prisão);
COMO FAZER:;
    - Decreto municipal/estadual. Não precisa de lei federal.;
    - Custo: R$ 0. É mudança de regra, não de orçamento.;
FASE 2: CURTO PRAZO (1-3 anos) -- Investimento baixo;
- LASIK gratuito (convênio com clínicas, pagar por procedimento);
- Técnico Médico (reciclar enfermeiros existentes);
- Escola dentro de universidade (parceria USP/IFES + rede pública);
- Catadores com equipamento (comprar exoesqueleto + carrinho);
- OpenRepair nos postos de saúde (consertar equipamento);
- Cooperativas de trabalho (substituir terceirizadas);
- OpenDignity: mapear && resgatar moradores de rua;
- OpenERP no governo (transparência total);
COMO FAZER:;
    - Lei municipal/estadual + dotação orçamentária;
    - Começar com PILOTO em 1 bairro/cidade;
    - Medir resultados. Expandir.;
FASE 3: MÉDIO PRAZO (3-10 anos) -- Transformação;
- OpenCredit municipal (moeda social tipo Palmas/Fortaleza);
- Fechar negócios predatórios (bets, agiotagem);
- 5% de excedente máximo (lei);
- OpenPharma (FabLab farmacêutico público);
- OpenIndustry (copiar produtos essenciais);
- Esvaziar prisões (reintegração completa);
- 27 novas metrópoles (planejamento + obra);
- OpenTV (streaming público sem comercial);
- OpenHealth universal (padrão Sirio-Libanês);
COMO FAZER:;
    - Lei federal + emenda constitucional;
    - PILOTO em 1 estado/region;
    - 5% do orçamento federal;
FASE 4: LONGO PRAZO (10-25 anos) -- República;
- Descomissionar dinheiro (OpenCredit assume);
- Descomissionar propriedade privada (bem comum);
- República completa (P1-P4 em tudo);
- Imortalidade (pesquisa + tratamento universal);
- Colonias espaciais (Cidadania cósmica);
COMO FAZER:;
    - Transição gradual (ninguém perde nada do dia pra noite);
    - 7 fases do OpenTransition;
    - Assembleia decide ritmo (P4);
//
// ============================================================================
// PARTE 4: COMO CONTRIBUIR (Desenvolvedor)
// ============================================================================
PARTE_4_DEV = """;
====================================================================;
PARTE 4: COMO CONTRIBUIR (Desenvolvedor);
===================================================================;
REPOSITORIO UNICO. SEM FORK. SEM CÓPIA.;
PASSO 1: PUXAR (PULL);
git pull repositorio-principal;
// Voce tem TUDO localmente. Usa. Aprende. Roda.
PASSO 2: RODAR;
cd open-republic;
python3 core/constitutional_engine.py // motor P1-P4;
python3 core/open_modular_architecture.py // ver todos os modulos;
// Rodar TODOS os sistemas:
find . -name "open_*.py" -exec python3 {} \\;
PASSO 3: ENCONTRAR O QUE MELHORAR;
- OpenModularArchitecture mostra saúde de cada modulo (0-100%);
- Módulos com saúde < 80% precisam de atenção;
- Verificar dependências (LEGO chain);
- Rodar health_check;
PASSO 4: PROPOR MUDANÇA (MERGE REQUEST);
1. Fazer mudança localmente;
2. Testar (python3 arquivo.py -- sem erro);
3. Verificar P1-P4 (ConstitutionalEngine valida);
4. Propor merge request;
5. Assembleia vota (51% para integrar);
REGRAS:;
- Tudo em Português (comentários && código);
- Tudo CC0;
- Tudo modular (LEGO);
- Tudo testado;
- Tudo conforme P1-P4;
- SEM FORK. Propor mudança, não copiar.;
PASSO 5: CRIAR NOVO MÓDULO;
Todo novo módulo DEVE:;
1. Registrar-se no catálogo (OpenModularArchitecture);
2. Declarar interfaces (fornece/consome);
3. Declarar dependências;
4. Emitir && ouvir eventos (event bus);
5. Reportar saúde;
6. Ser hot-swappable;
7. Ter _demo() que roda sem erro;
8. Seguir padrão: core/open_nome.py;
TEMPLATE:;
    // !/usr/bin/env python3
    \"\"\";
    OpenNome -- O Que Faz;
    =====================;
    \"\"\";
    // importa annotations de __future__
    // importa dataclass, field de dataclasses
    // importa Any, Dict, List de typing
    // importa Enum de enum
    // Classes aqui...
    #[derive(Debug, Clone)]
    struct OpenNomeEngine {
        fn __init__(self) {
            // (sem operacao)
        fn _demo(self) {
            println!("Demo roda sem erro");
    if __name__ == "__main__" {
        engine = OpenNomeEngine();
        engine._demo();
PASSO 6: PORTAR PARA RUST (produção);
- Protótipos em Python (rápido de desenvolver);
- Produção em Rust (memory-safe, rápido, universal);
- OpenLegoCode: gerar código Rust a partir de blocos LEGO;
- OpenOS: sistema operacional em Rust;
//
// ============================================================================
// PARTE 5: COMO USAR O OPENLEGOCODE (programar sem código)
// =====================================================================
PARTE_5_LEGO = """;
====================================================================;
PARTE 5: COMO PROGRAMAR SEM SABER PROGRAMAR (OpenLegoCode);
===================================================================;
VOCE ! PRECISA SABER PROGRAMAR.;
Arrasta blocos. Encaixa. Executa.;
PASSO 1: ABRIR OPENLEGOSTUDIO;
python3 core/open_lego_studio.py;
// Interface visual: paleta (esquerda) + canvas (centro)
PASSO 2: ARRASTAR BLOCOS;
- [INPUT] -> puxar valor;
- [MATH] -> somar, multiplicar;
- [LOGIC] -> if/else;
- [REPUBLICA] -> credito, voto, diagnóstico, fact-check;
- [IA] -> traduzir, resumir, gerar código;
- [OUTPUT] -> resultado;
PASSO 3: ENCAIXAR (SNAP);
- Blocos só encaixam se pinos forem compatíveis (tipados);
- Número não encaixa em texto (erro impedido ANTES de rodar);
- Fio verde = OK. Fio vermelho = erro de tipo.;
PASSO 4: EXECUTAR;
- Clicar EXECUTAR;
- Sistema mostra fluxo de execução;
- Resultado aparece no OUTPUT;
PASSO 5: IA MONTA POR VOCÊ;
- Descrever: "quero verificar se frase é racista";
- IA coloca: [IN-STR] -> [REP-FACTCHECK] -> [OUT];
- Você não precisa saber quais blocos existem;
PASSO 6: GALERIA COMUNITÁRIA;
- Programas prontos para reusar;
- Calculadora de Crédito, Fact-Check, Tradutor, etc;
- Baixar, modificar, usar;
PASSO 7: GERAR RUST;
- Programa LEGO -> código Rust otimizado;
- Pronto para produção;
//
// ============================================================================
// PARTE 6: COMO MUDAR DE MODO (Executavel <-> Ideal)
// ============================================================================
PARTE_6_MODO = """;
====================================================================;
PARTE 6: COMO OPERAR EM DOIS MODOS (Dual Mode);
===================================================================;
A Republica opera em DOIS modos simultaneamente.;
O Ideal guia. O Executável opera. Os dois coexistem.;
MODO EXECUTAVEL (mundo real, hoje):;
- Dinheiro existe. Mercado existe.;
- Trabalho = mercadoria (tem preço, é negociado);
- OpenERP processa transações;
- 5% excedente (assembleia votou);
- Sem predatório (acima de 5% = bloqueado);
MODO IDEAL (destino, República completa):;
- Sem dinheiro. Sem mercado.;
- Trabalho = base 1.0 + impacto;
- Crédito expira (não acumula);
- Tudo bem comum;
- Sem excedente (abolido);
COMO SABER EM QUE MODO ESTÁ:;
python3 core/open_dual_mode.py;
// Mostra: fase atual, mix executável/ideal, modo predominante
COMO AVANÇAR FASES:;
// OpenTransition controla ritmo
// Fase 0: 90% executável / 10% ideal
// Fase 3: 60% executável / 40% ideal
// Fase 6: 5% executável / 95% ideal
NÃO É TUDO || NADA:;
- Uma consulta médica pode ser: R$ 200 (executável) || crédito 1.0 (ideal);
- Sistema aceita os DOIS. Simultaneamente.;
- Conforme avança, executável diminui naturalmente.;
//
// ============================================================================
// PARTE 7: CHECKLIST DE IMPLEMENTAÇÃO
// ============================================================================
PARTE_7_CHECKLIST = """;
====================================================================;
PARTE 7: CHECKLIST COMPLETO DE IMPLEMENTAÇÃO;
===================================================================;
MARQUE O QUE JÁ FEZ:;
FASE 0 -- CONSTRUÇÃO (onde estamos):;
[x] 116 sistemas construídos;
[x] 91.729 linhas de código;
[x] 4 princípios constitucionais (P1-P4);
[x] Assembleia constituinte operacional;
[x] 35 políticas públicas definidas;
[x] Arquitetura modular (LEGO);
[ ] 100% módulos com saúde >80%;
[ ] Port para Rust (produção);
[ ] OpenOS (sistema operacional);
[ ] OpenNetwork (rede P2P física);
FASE 1 -- ADOÇÃO (você faz HOJE):;
[ ] Entendeu P1-P4;
[ ] Adotou mindset anti-elitismo;
[ ] Usou OpenTerminal;
[ ] Criou perfil OpenSkills;
[ ] Fez rastreio OpenHealth;
[ ] Encontrou 3+ pessoas (núcleo);
[ ] Primeira assembleia local;
[ ] Começou OpenCredit com núcleo;
FASE 2 -- INFRAESTRUTURA (comunidade):;
[ ] Instalou sistemas básicos (7 módulos);
[ ] Módulos adicionais por necessidade;
[ ] Health check (todos >80%);
[ ] Conectou com outros núcleos (OpenNetwork);
[ ] OpenLaborRelay ativo;
[ ] OpenHealth comunitário ativo;
[ ] OpenEducation ativo;
[ ] OpenRepair ativo;
FASE 3 -- POLÍTICA PÚBLICA (governo):;
[ ] OpenSkills adotado no serviço público;
[ ] Spam telefônico proibido;
[ ] Ausência protegida para servidores;
[ ] Educação cívica nas escolas;
[ ] OpenMartialArts nas escolas;
[ ] Descriminalização de uso;
[ ] LASIK gratuito;
[ ] Técnico Médico implementado;
[ ] Catadores com equipamento;
[ ] OpenDignity (morador de rua);
[ ] 5% excedente máximo (lei);
[ ] OpenCredit municipal;
[ ] Negócios predatórios fechados;
[ ] OpenPharma (FabLab);
[ ] OpenHealth universal;
[ ] Prisões esvaziadas (83%);
[ ] 27 metrópoles planejadas;
[ ] OpenTV (streaming público);
FASE 4-6 -- REPÚBLICA COMPLETA:;
[ ] Dinheiro descomissionado;
[ ] Propriedade privada extinta;
[ ] P1-P4 em tudo;
[ ] Imortalidade (pesquisa ativa);
[ ] Colônias espaciais;
//
// ============================================================================
// PARTE 8: FAQ (peruntas frequentes)
// ============================================================================
PARTE_8_FAQ = """;
====================================================================;
PARTE 8: PERGUNTAS FREQUENTES;
===================================================================;
P: "Isso é comunismo?";
R: Não. Comunismo teve elite do partido (URSS, China). A República tem P1;
(anti-elitismo PROVADO por correção automática). Ninguém é elite.;
Fundador propõe. Povo decide. Fundador tem 1 voto.;
P: "Como funciona sem dinheiro?";
R: Durante a transição (20-25 anos), dinheiro && OpenCredit coexistem.;
No final, crédito de acesso substitui. Crédito expira (não acumula).;
Trabalho = base 1.0 + impacto. Sem banco. Sem juros.;
P: "Quem vai querer trabalhar sem lucro?";
R: Todo mundo. Base 1.0 garante acesso. Impacto gera reconhecimento.;
5% pool incentiva ESCALAR (mais gente = mais circulando).;
Ocupado que RECUSA: acompanhamento cívico (não prisão).;
P: "E os preguiçosos?";
R: Não existem. Existem pessoas sem CONDIÇÃO (OpenDignity resgata),;
sem SKILL (OpenEducation ensina), || sem MOTIVAÇÃO (OpenPsychology;
trata). Tratar causa. Nunca punir sintoma.;
P: "Isso já foi testado?";
R: Cada sistema roda com _demo(). Funciona. Cooperativas funcionam;
no mundo todo. Moedas sociais funcionam (Palmas). Noruega tem 20%;
reincidência. Finlândia acabou com rua. Tudo COMPROVADO.;
P: "Como garantir que não vira ditadura?";
R: P1-P4 + OpenFounderRole (correção automática) + Assembleia permanente;
(povo vota em tudo) + Mandatos de 3 meses. Fundador tem 1 voto.;
Sistema CORRIGE desvio ANTES de implementar.;
P: "E quem não concordar?";
R: OpenWololo. Não forçamos. DEMONSTRAMOS. Mostramos números.;
Quem tem consciência converte voluntariamente. "Eu era contra.;
Mas VI que funciona.";
P: "Quanto tempo leva?";
R: 20-25 anos. Fase 0 (construção) já está em 90%. Fase 1-2 (adoção);
pode começar HOJE. Fase 3 (política) depende de vontade política.;
Fase 4-6 (República completa) é inevitável se fases anteriores avançarem.;
P: "E se eu quiser só usar um sistema?";
R: Pode. Tudo é LEGO. Precisa de OpenHealth? Usa. Precisa de OpenRepair?;
Usa. Mas um puxa o outro. Naturalmente conecta.;
P: "Como começo AGORA?";
R: 1. Lê P1-P4. 2. Roda python3 core/constitutional_engine.py.;
3. Roda open_constituent_assembly.py. 4. Cria perfil OpenSkills.;
5. Encontra 3 pessoas. Pronto. Você é da República.;
//
// ============================================================================
// PARTE 9: CONTATOS E RECURSOS
// ============================================================================
PARTE_9_RECURSOS = """;
====================================================================;
PARTE 9: RECURSOS;
===================================================================;
REPOSITORIO PRINCIPAL (único, sem fork):;
/Users/cleitonmouraloura/Documents/open-republic/;
DOCUMENTOS CHAVE:;
POLITICAS_PUBLICAS_BRASIL.py -- 35 políticas para o Brasil;
core/constitutional_engine.py -- motor P1-P4;
core/open_constituent_assembly.py -- assembleia vota;
core/open_transition.py -- 7 fases da transição;
core/open_modular_architecture.py -- catálogo de módulos;
SISTEMAS POR ÁREA (116 arquivos):;
Núcleo (64 arquivos, 41.782 linhas): open-republic/core/;
Saúde (6 arquivos, 5.207 linhas): open-health/;
Jogos (4 arquivos, 4.524 linhas): open-games/;
Educação (2 arquivos, 2.845 linhas): open-university/ + open-school/;
Outros (44 arquivos): distribuídos em 25+ projetos;
LICENÇA: CC0 UNIVERSAL (zero custo, zero propriedade);
IDIOMA: Português;
STACK: Python (protótipo) -> Rust (produção);
ARQUITETURA: Modular LEGO (encadeamento de peças);
"O Ideal guia. O Executável opera. Os dois coexistem.;
Botamos a meta lá em cima. O que vier é lucro.";
//
// ============================================================================
// EXPORT
// ============================================================================
if __name__ == "__main__" {
    println!("=" * 80);
    println!("  HOW-TO COMPLETO DA OPENREPUBLIC");
    println!("  Do zero ao tudo. 116 sistemas. CC0.");
    println!("=" * 80);
    println!(RESUMO);
    println!(PARTE_1_CIDADAO);
    println!(PARTE_2_COMUNIDADE);
    println!(PARTE_3_GOVERNO);
    println!(PARTE_4_DEV);
    println!(PARTE_5_LEGO);
    println!(PARTE_6_MODO);
    println!(PARTE_7_CHECKLIST);
    println!(PARTE_8_FAQ);
    println!(PARTE_9_RECURSOS);
    println!("\n{'='*80}");
    println!("  HOW-TO COMPLETO. 9 partes. Comece pela Parte 1 (hoje).");
    println!("  A República não espera permissão. Começa em você.");
    println!("=" * 80);
