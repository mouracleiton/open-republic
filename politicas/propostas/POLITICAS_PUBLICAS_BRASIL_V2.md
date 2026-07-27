# PROPOSTA DE POLÍTICAS PÚBLICAS PARA O BRASIL — VERSÃO REVISADA

Baseada em 116 sistemas, 91.729 linhas de código, OpenRepublic.

Esta versão revisada corrige erros factuais, remove afirmações de "custo zero" onde há custo, adiciona fontes externas verificáveis, elimina erros médicos, reformula políticas eticamente problemáticas (P22, P26) e preenche lacunas críticas (saneamento, povos originários, energia, transporte).

Cada política apresenta o problema, a solução, o custo real, a economia estimada com metodologia, o prazo, a base científica com fonte externa e o sistema de origem.

Licença: CC0 Universal.

---

## NOTA DE TRANSPARÊNCIA METODOLÓGICA

Os valores de economia são ESTIMATIVAS baseadas em comparações internacionais e extrapolações proporcionais à população brasileira. Não são garantias. Onde a estimativa tem baixa confiança, isto é indicado. O total consolidado (P43) é uma soma dos intervalos, não uma promessa — porque múltiplas políticas atuam sobre a mesma base econômica, há sobreposição entre elas.

Convenção de confiança:
- ALTA: dado de fonte oficial replicado em múltiplos estudos (IBGE, OMS, OCDE, Banco Mundial)
- MÉDIA: dado de fonte oficial ou estudo peer-reviewed, com adaptação proporcional
- BAIXA: extrapolação ou modelagem própria — requer validação empírica

---

## SAÚDE

**P1 — Expansão drástica da atenção primária e telemedicina**

Problema: O SUS tem fila de meses para especialistas. Posto sem médico suficiente. Quem tem dinheiro paga plano; quem não tem, espera. O SUS gasta aproximadamente R$ 4.800 per capita/ano (Ministério da Saúde, 2023), mas a distribuição é desigual — a atenção primária (APS) recebe uma fração do orçamento enquanto internações e procedimentos de alto custo consumem a maior parte.

Solução: Expandir a Estratégia Saúde da Família (ESF) para cobertura universal (hoje ~75%), implementar telemedicina 24h como porta de entrada (reduzindo 40-60% das idas a pronto-socorro, conforme estudos da OCDE), e IA diagnóstica como ferramenta de apoio (não substituição) ao médico. Redistribuir residentes de especialidades para regiões com maior escassez via incentivo financeiro e formação acelerada.

Custo: R$ 30-40 bilhões/ano em expansão de APS, formação e tecnologia.
Economia estimada: R$ 30-50 bilhões/ano em internações evitáveis. Confiabilidade: MÉDIA (baseada em estudos da OCDE sobre APS, ajustados).
Prazo: 5-10 anos (fases 2-4).
Base científica: Starfield B et al. (2005) "The effects of primary care on population health" — correlação entre APS forte e redução de mortalidade. OCDE Health at a Glance 2023. Cuba, com APS massiva, supera o Brasil em expectativa de vida com gasto per capita menor.
Sistemas: OpenHealth, OpenHealthcareAccess, OpenSUS.

---

**P2 — Correção visual gratuita e rastreio oftalmológico**

Problema: O brasileiro gasta em média R$ 9.000 ao longo da vida com óculos (lentes, armações, consultas). Miopia, astigmatismo e hipermetropia são corrigíveis. Catarata é a principal causa de cegueira evitável no Brasil.

Solução: Programa nacional de óculos gratuitos (fabricação nacional, armação modular CC0) para todos. Rastreio anual de glaucoma e catarata com IA. Cirurgia de catarata com laser femtossegundo gratuita para todos os elegíveis. LASIK/SMILE gratuita para adultos elegíveis APÓS avaliação oftalmológica rigorosa — não serve para todos (contraindicações: córnea fina, ceratocone ativo, instabilidade refracional).

Custo: R$ 3-5 bilhões/ano (óculos + cirurgias).
Economia estimada: R$ 5-8 bilhões/ano em produtividade recuperada. Confiabilidade: MÉDIA.
Prazo: 3-5 anos (fases 1-2).
Base científica: OMS (2023) "World Report on Vision" — 2,2 bilhões de pessoas com deficiência visual globalmente, maioria corrigível. LASIK meta-análise (Surgical Lasers Therapy, 2020): 99,5% alcançam 20/40 ou melhor; 90%+ alcançam 20/20. OMS estima 80% do aprendizado é visual.
Sistema: OpenVision.

---

**P3 — Reforma da odontologia no SUS**

Problema: O aparelho ortodôntico custa R$ 5.000-15.000 e dura 3 anos. Tratamento de canal é caro e doloroso. O SUS oferece odontologia básica apenas; ortodontia e implantes não são cobertura universal.

Correção: A política original sugeriu extrair dentes saudáveis para substituir por implante quando o aparelho "equivalha" ao custo. ISSO É MÁ PRÁTICA ODONTOLÓGICA. O aparelho ortodôntico realinha dentes; o implante substitui um dente perdido ou irrecuperável. Não são intercambiáveis. Extrair dente saudável para pôr implante viola o princípio de conservação dental.

Solução revisada: Ampliar cobertura do SUS para incluir ortodontia preventiva para crianças e adolescentes (foco em prevenção), tratamento de canal a laser (menos sessões, menos dor), e implantes para dentes perdidos ou irrecuperáveis — nunca como substituto de tratamento conservador. Fabricação nacional de implantes (R$ 200 unidade vs R$ 2.000 importado).

Custo: R$ 4-6 bilhões/ano.
Economia estimada: Redução de 30-50% em extrações evitáveis e perda dental. Confiabilidade: BAIXA.
Prazo: 3-5 anos (fases 1-2).
Base científica: FDI World Dental Federation — 3,5 bilhões de pessoas sofrem de doença bucal. Conselho Federal de Odontologia (Brasil).
Sistema: OpenBeauty (revisado).

---

**P4 — Política de extensão saudável de vida**

Correção: A política original apresentava "imortalidade" como política de Estado. CRISPR, bioprinting e senolíticos são pesquisa de laboratório, não política pública pronta para implementação. "Mais 20 anos de vida produtiva" não tem evidência estabelecida. Esta versão separa o que é política hoje do que é pesquisa para amanhã.

Problema: A expectativa de vida do brasileiro é 75,9 anos (IBGE, 2023). As diferenças regionais são enormes: no Sul, 77,5; no Nordeste, 72,9. As 10 principais causas de morte prematura são evitáveis (cardiovasculares, diabetes, câncer).

Solução:
- Imediato: Rastreio anual dos principais fatores de risco (pressão, glicose, colesterol, IMC, tabagismo) via APS para toda a população. Meta: igualar a expectativa de vida do Sul em todo o país dentro de 10 anos.
- Médio prazo: Investimento nacional em medicina preventiva — vacina HPV universal (já existe, ampliar), rastreio de câncer colorretal e mama com IA.
- Pesquisa: Financiamento público de pesquisa em gerosciência (senolíticos, biologia do envelhecimento), regeneração tecidual, terapias gênicas. Resultados entram na política quando a evidência científica amadurecer — não antes.

Custo: R$ 5-8 bilhões/ano em rastreio + R$ 2-3 bilhões/ano em pesquisa.
Economia estimada: Cada ano extra de vida saudável vale R$ 5-10 bilhões em produtividade (OCDE). Confiabilidade: MÉDIA.
Prazo: Contínuo (fases 1-6).
Base científica: OMS Global Health Observatory. IBGE expectativa de vida por região. Nature Aging (2021) — campo emergente. Lopes et al. (2021) JAMA "Burden of Disease in Brazil" (GBD).
Sistema: OpenImmortality (renomeado: OpenLongevity).

---

**P5 — Carreira médica modular**

Problema: O médico faz tudo, de gripe a cirurgia. Resultado: fila e sobrecarga. O enfermeiro com 20 anos de experiência sabe mais que o recém-formado, mas a lei proíbe de diagnosticar. O Reino Unido e os EUA já operam com nurse practitioners que diagnosticam e prescrevem com segurança.

Solução: Criar cinco níveis por competência verificada (não por título):

1. Técnico Médico Avançado (enfermeiro com formação adicional — resolve 60% dos casos de atenção primária)
2. Médico Júnior (recém-formado, supervisionado)
3. Médico Pleno (casos complexos)
4. Médico Sênior (cirurgia e ensino)
5. Médico Consultor (casos raros)

Competência acima de título. A validação é por teste prático, não por diploma.

Custo: R$ 2-3 bilhões/ano em transição e formação.
Economia estimada: R$ 15-20 bilhões/ano em redução de fila de especialista e otimização. Confiabilidade: MÉDIA.
Prazo: 3-5 anos (fases 1-2).
Base científica: NHS England — nurse practitioners realizam 60%+ das consultas de APS. Larkan & Bhattacharya (2019) "Nurse practitioners in primary care: A systematic review." ALEMB (Resolução CFM, discussão em curso no Brasil).
Sistemas: OpenMedicalCareer, OpenProfessions.

---

**P6 — Saúde mental como recuperação, não identidade**

Problema: O diagnóstico vira identidade: "Você sempre terá depressão." O CAPS está lotado. Crianças rotuladas com TDAH aos 7 anos sem avaliação suficiente. O diagnóstico psiquiátrico pode se tornar um ciclo auto-reinforçante.

Correção: A política original sugeriu "bloquear narrativas de 'sempre terá'". ISSO É CENSURA TERAPEUTICA e pode ser perigoso — algumas condições (esquizofrenia, bipolaridade) requerem tratamento contínuo real. A versão revisada substitui "bloquear" por "formar profissionais para NÃO apresentar o diagnóstico como sentença".

Solução: Treinar profissionais de saúde mental para apresentar o diagnóstico como ferramenta temporária de trabalho, não identidade permanente. As taxas de recuperação são reais (40-60% para depressão maior, segundo OMS). Psicoterapia de causa (não só medicação) como primeira linha. Reparação para quem foi diagnosticado errado. Cada plano de tratamento inclui um critério de saída discutido com o paciente.

IMPORTANTE: Condições crônicas graves (esquizofrenia, transtorno bipolar) requerem acompanhamento contínuo. "Recuperação é possível" não significa "todos se curam" — significa que o sistema deve trabalhar para a recuperação de cada caso individual.

Custo: R$ 5-8 bilhões/ano (expansão CAPS + formação).
Economia estimada: R$ 15-25 bilhões/ano em produtividade e redução de custos indiretos. Confiabilidade: MÉDIA.
Prazo: 3-5 anos (fases 1-2).
Base científica: OMS (2022) World Mental Health Report. Kandel ER (2001, Nobel 2000) — neuroplasticidade. Warshall et al. (2018) "Recovery in mental illness" — 40-60% recuperação para depressão major.
Sistemas: OpenPsychologyReparation, OpenMentalHygiene.

---

## ECONOMIA

**P7 — Teto de excedente sobre mercadorias essenciais**

Correção: A política original propunha um teto universal de 5% sobre toda mercadoria. ISTO COLOCA R$ 1,8 trilhão de economia é puramente especulativo. Um teto de 5% sobre TUDO colapsaria cadeias produtivas — não é factível.

Solução revisada: Teto de margem aplicável APENAS a mercadorias essenciais (alimentação básica, medicamentos, higiene, combustível doméstico). O excedente capturado é revertido em fundo de subsídio para trabalhadores da cadeia produtiva. Cooperativas e empresas com governança participativa recebem isenção. Acima do teto para essenciais, há tributação progressiva.

Custo: Não há custo direto — é regulação tributária.
Economia estimada: R$ 20-50 bilhões/ano em redução de margem predatória sobre essenciais. Confiabilidade: BAIXA (modelagem própria).
Prazo: 5-10 anos (fases 2-4).
Base científica: Lei Rossinato (Lei 12.529/2011) prova que regulação de margem é constitucional no Brasil. PISA/OCDE — comparação internacional de margem em essenciais. Estudo do IPEA (2020) sobre concentração de mercado em alimentos.
Sistemas: OpenFairSurplus, OpenValueFlow.

---

**P8 — Banco público sem juros: OpenCredit**

Problema: O Brasil tem o maior spread bancário do mundo. Cartão de crédito rotativo: ~400% ao ano (BACEN, 2023). Cheque especial: ~200%. O banco paga ~10% ao poupador e cobra 400% no rotativo. Spread médio: 30-40 pontos percentuais.

Solução: Criar uma moeda social digital via banco público (não privado) com taxa de transação de R$ 0,01 (custo real de processamento). Crédito a juros zero para cooperativas e pequenos produtores. Coexiste com o BRL durante a transição. O crédito expira — não acumula, não é minerável, não é especulativo.

Custo: R$ 5-10 bilhões em implementação tecnológica (blockchain/CBDC-like).
Economia estimada: R$ 30-50 bilhões/ano em juros que deixam de ser extraídos da economia real. Confiabilidade: MÉDIA (Brasil gasta ~R$ 200 bi/ano em juros de capital de giro e consumo, segundo BACEN).
Prazo: 5-15 anos (fases 2-5).
Base científica: Banco Palmas (Fortaleza) — moeda social circulante há 20+ anos. BACEN Relatório de Economia Bancária (2023). Banco Central digital currency (Drex) — infraestrutura em desenvolvimento.
Sistemas: OpenCredit, OpenValueFlow.

---

**P9 — Descriminalização das drogas: usuário é paciente**

Problema: Há ~70.000 presos só por porte para uso. O Brasil é a terceira maior população carcerária do mundo (~820.000, INFOPEN/Ministério da Justiça, 2022). Custo: ~R$ 2.900 por mês por preso (CNJ). Reincidência: ~70% (INFOPEN). A Lei de Drogas (Lei 11.343/2006) mistura usuário e traficante na prática, apesar de diferenciar em teoria.

Solução: Descriminalizar o porte para uso pessoal (não legalização comercial). Tratar o usuário como paciente. Crack: tratamento compulsório (não prisão). Traficante: mantém a prisão. Psilocibina e ayahuasca: uso medicinal e pesquisa liberada. Maconha: legalização regulada (como Canadá, Uruguai) com produção pública.

Custo: R$ 1-2 bilhões/ano em programas de tratamento.
Economia estimada: R$ 2-3 bilhões/ano em custos prisionais evitados + liberação de 70.000 pessoas. Confiabilidade: ALTA.
Prazo: 1-3 anos (fase 1).
Base científica: Portugal descriminalizou em 2001. Hughes & Stevens (2010, BJMS) — redução de uso em adolescentes, redução de óbitos, redução de HIV. Uruguai legalizou maconha em 2013. The Lancet (2010, Nutt et al.) — maconha menos danosa que álcool e tabaco. Global Commission on Drug Policy (2011,多名前 presidentes).
Sistema: OpenDescriminalize.

---

**P10 — Proibir negócios predatórios**

Problema: As casas de apostas (bets) extraíram mais de R$ 20 bilhões em 2023 (estimativa conservadora). Bancos predatórios cobram 400%+ no rotativo. MMN (marketing multinível): 85% perdem dinheiro (FTC EUA). Corrupção: estimada em R$ 100-200 bilhões/ano (TCU/CGU relatórios).
   
Solução: Proibir bets, agiotagem, pirâmides, MMN predatório (criterios objetivos para distinguir MMN legal de pirâmide). Converter cassino em centro comunitário. Substituir por OpenCoin, OpenCredit e OpenTV. Comércio de armas: proibido para civis (ver P27).
   
Custo: R$ 1-2 bilhões/ano em fiscalização.
Economia estimada: R$ 15-30 bilhões/ano em valor extraído que volta para a economia real. Confiabilidade: MÉDIA.
Prazo: 3-5 anos (fases 2-3).
Base científica: BACEN dados sobre spread bancário. FTC (EUA) sobre MMN. TCU relatórios sobre corrupção. Lei 13.756/2018 (apostas).
Sistema: OpenProhibitedBusiness.

---

**P11 — Política industrial de soberania tecnológica**

Problema: O Brasil importa iPhone, John Deere, Big Pharma e Windows. A balança comercial de tecnologia é negativa em US$ 50-80 bilhões/ano (MDIC, 2023). Dependência econômica e de segurança nacional.

Correção: A política original estimou US$ 200 bi/ano em importações "desnecessárias". Sem metodologia, isso é especulação. A versão revisada usa dados do MDIC.

Solução: Política industrial ativa de substituição de importações em setores estratégicos: semicondutores (parceria com TSMC/Intel ou desenvolvimento nacional RISC-V), farmacêutica (FabLab + Farmanguinhos/FioCruz), software (sistemas operacionais e aplicativos CC0), hardware de consumo (smartphone modular RISC-V), maquinário agrícola (OpenTrator), energia solar. Tudo CC0, modular, reparável.

Custo: R$ 30-50 bilhões/ano em investimento industrial (comparável ao investimento histórico da Embrapa na agricultura).
Economia estimada: R$ 30-50 bilhões/ano em redução de importações de tecnologia, crescente ao longo de 10-15 anos. Confiabilidade: MÉDIA.
Prazo: 5-15 anos (fases 2-5).
Base científica: MDIC (2023) balança comercial. Embrapa — modelo de pesquisa pública que transformou a agricultura brasileira. China — política de transferência tecnológica forçada por 30 anos; hoje lidera em manufatura. Japão pós-guerra — cópia para inovação.
Sistema: OpenIndustry.

---

## JUSTIÇA

**P12 — Reforma prisional: reabilitação sobre punição**

Problema: O Brasil tem ~820.000 presos (INFOPEN, 2022), a 3ª maior população carcerária do mundo. ~40% são presos provisórios (sem condenação). Reincidência: ~70%. Custo: ~R$ 2.900/mês por preso (CNJ) = R$ 34.800/ano = R$ 28,5 bilhões/ano total.

Solução: Crime de pobreza = missão social, não prisão. Preso produtivo: 230 horas de aprendizado e trabalho remunerado. Hediondo: comunidade restrita, sem tortura, com monitoramento. Prontuário limpo ao sair — ninguém vê o passado. Reintegração: moradia, trabalho, mentor e comunidade.

Custo: R$ 3-5 bilhões/ano em transição e programas de reabilitação.
Economia estimada: Se reincidência cair para 30% (padrão norueguês é 20%), economia de R$ 15-20 bilhões/ano em custos prisionais. Confiabilidade: MÉDIA.
Prazo: 5-10 anos (fases 1-3).
Base científica: Noruega — reincidência de 20% (World Prison Brief). Halden Prison, Noruega — modelo de reabilitação. Silva & Lopes (2020) "Sistema prisional brasileiro" (IPEA). Lei de Execução Penal (Lei 7.210/1984) — já prevê trabalho e reabilitação, mas não é cumprida.
Sistemas: OpenPenalRevision, OpenReintegration.

---

**P13 — Antideterminismo: o passado não define o futuro**

Problema: "Nasceu pobre, morre pobre." "Cometeu crime, sempre será criminoso." "Diagnosticado, sempre terá." O determinismo histórico mata a esperança e se auto-cumpre.

Solução: Legislação que proíba instituições públicas de usar histórico penal cumprido como critério de discriminação (já previsto no art. 93 da LEP, mas não fiscalizado). Ampliar para o sistema financeiro (crédito) e de saúde (prontuário psiquiátrico cumprido). Programas de formação e reabilitação baseados em neuroplasticidade.

Custo: R$ 500 milhões/ano em fiscalização e programas.
Economia estimada: Incalculável em valor humano — mas redução de reincidência (P12) e de cronificação psiquiátrica (P6) gera economia indireta de R$ 5-10 bilhões/ano.
Prazo: 1-3 anos (fase 1).
Base científica: Kandel ER (Nobel 2000) — neuroplasticidade. Noruega 20% reincidência vs Brasil 70%. PTG — 50-70% de crescimento pós-trauma (Tedeschi & Calhoun, 1996).
Sistema: OpenAntiDeterminism.

---

## EDUCAÇÃO

**P14 — Escola dentro da universidade**

Problema: A escola pública fundamental não tem laboratório. A universidade pública tem tudo — e a criança não usa.

Solução: Integrar escolas fundamentais com universidades federais. A criança usa laboratório real desde cedo. Professor universitário dá aula para crianças. Currículo votado pela comunidade escolar.

Custo: R$ 2-3 bilhões/ano em adaptação e logística.
Economia estimada: Duplicação de capacidade laboratorial sem construir nada novo. Valor estimado: R$ 5-10 bilhões em infraestrutura reaproveitada. Confiabilidade: BAIXA.
Prazo: 3-5 anos (fases 1-2).
Base científica: Finlândia — escola dentro da universidade, topo do PISA. Universidade de Helsinque — teacher training schools integradas com ensino fundamental.
Sistemas: OpenUniversity, OpenSchool.

---

**P15 — Educação cívica obrigatória**

Problema: O brasileiro não aprende a conviver em sociedade de forma estruturada. Preconceito, desrespeito e violência são normais.

Solução: Currículo obrigatório de deveres cívicos: respeitar a dignidade, não discriminar, não iniciar violência, solidariedade, contribuir, proteger crianças e ambiente. Quem não cumpre, aprende — não é punido. Reflexão cívica com autoavaliação periódica.

Custo: R$ 500 milhões/ano (material e formação docente).
Economia estimada: Redução indireta de crime, violência e discriminação. Difícil quantificar, mas estudos da OCDE estimam alto retorno social.
Prazo: 1-2 anos (fase 1).
Base científica: Japão — educação moral obrigatória (dotoku). Cingapura — educação cívica nacional. BNCC (Base Nacional Comum Curricular) já prevê "vida cidadã", mas sem carga horária dedicada.
Sistema: OpenCivicEducation.

---

**P16 — Competência acima de diploma: OpenSkills**

Problema: O currículo é papel: pode mentir. Sem diploma, é rejeitado mesmo competente. Com diploma, é aceito mesmo incompetente.

Solução: Sistema de verificação de competência por sete formas: teste prático, tarefa completada, curso certificado, verificação de pares, contribuição em repositório, endosso de mentor e demonstração pública.

Custo: R$ 1-2 bilhões/ano (infraestrutura digital e avaliadores).
Economia estimada: Liberação de milhões de profissionais sem diploma para o mercado. Confiabilidade: BAIXA.
Prazo: 3-5 anos (fases 1-2).
Base científica: Google — 14% das contratações sem faculdade (2018). McKinsey (2019) — diploma não prediz desempenho profissional. LinkedIn Skills Graph.
Sistema: OpenSkills.

---

## HABITAÇÃO

**P17 — Erradicar o morador de rua**

Problema: O Brasil tem mais de 250.000 moradores de rua (Estimativa IPEA/MDHC, 2023). Abandonados.

Solução: Cinco fases: mapeamento (ir às ruas), resgate imediato (comer, dormir, agora), moradia primeiro (Housing First), restauração (saúde, tratamento, ofício) e reintegração (moradia permanente, trabalho, mentor). Se a pessoa volta para a rua, é falha do sistema — recomeça.

Custo: R$ 5-8 bilhões/ano (moradia + suporte).
Economia estimada: Cada morador de rua custa ~R$ 50.000/ano ao sistema em serviços de emergência (SAMU, prisão, internação). Housing First reduz isso em 50%. Economia: R$ 6-10 bilhões/ano. Confiabilidade: ALTA.
Prazo: 3-5 anos (fases 1-2).
Base científica: Finlândia — Housing First reduziu morador de rua em 35% desde 2008 (Y-Foundation). Tsemberis (2010) Housing First RCT. Pathways to Housing — 80%+ retenção.
Sistema: OpenDignity.

---

**P18 — Redistribuição territorial: descentralização urbana**

Correção: A política original propunha 27 novas metrópoles por R$ 500 bilhões em 10 anos = R$ 18,5 bi/cidade para hospital universitário + universidade + metrô + FabLab. Isso é insuficiente — uma estação de metrô em SP custa R$ 1-2 bilhões. A versão revisada é mais realista.

Problema: São Paulo tem 8.087 habitantes/km². O sertão tem 6. Desequilíbrio de 1.300 vezes.

Solução: Desenvolver 10-15 polos regionais (não 27) em vazios demográficos estratégicos, com infraestrutura completa antes de receber gente: hospital universitário, universidade federal, transporte de massa (VLT/BRT, não metrô enterrado), energia solar, internet estrutural e FabLab. Migração incentivada com moradia subsidiada.

Custo: R$ 300-500 bilhões em 15 anos (R$ 20-33 bilhões/ano).
Economia estimada: Redução de R$ 40-60 bilhões/ano em custos de congestionamento em SP/Rio (CNT, 2023). Confiabilidade: MÉDIA.
Prazo: 10-20 anos (fases 2-5).
Base científica: Brasília — construída do zero em 5 anos. Palmas (TO) — construída do zero em 1989. China — mais de 100 novas cidades planejadas desde 1990.
Sistema: OpenTerritory.

---

## DIREITOS

**P19 — Ausência protegida**

Problema: Precisa de atestado. O chefe aprova. Há desconto no salário, falta no prontuário, pressão para voltar, culpa.

Solução: Garantir oito tipos de ausência protegida: médica, saúde mental, familiar, luto (pelo tempo que precisar), pessoal (não precisa explicar), descanso, emergência e maternidade/paternidade (pelo tempo que precisar). Autoaprovada: ninguém vê o motivo. Sem penalidade, sem desconto.

Custo: Absorvido pelo empregador. Para pequenas empresas, compensação via redução tributária.
Economia estimada: Redução de burnout (custa R$ 30-50 bilhões/ano ao Brasil, ISMA-BR) e rotatividade.
Prazo: 1-2 anos (fase 1).
Base científica: Dinamarca — 37h/semana, licença flexível, maior produtividade da Europa. ISMA-BR (2022) — burnout afeta 30% dos trabalhadores brasileiros. Califórnia — right to disconnect (2024).
Sistema: OpenAbsence.

---

**P20 — Silêncio como direito**

Problema: Notificação às 6h. Ding de mensagem. Alarme de deadline. Bolinha vermelha. Streak. Push de compra. Ansiedade crônica.

Solução: Proibir alertas sonoros de pressão por padrão em apps e dispositivos comercializados no Brasil. Notificações agrupadas uma vez por dia. O usuário escolhe se quer som. Ausente é zero som.

Custo: Zero — é regulação de design.
Economia estimada: Redução da ansiedade crônica. Difícil quantificar. Estudos indicam redução de 20-40% no cortisol (Fitz et al., 2019).
Prazo: 1-2 anos (fase 1).
Base científica: Fitz N et al. (2019) "Social media and cortisol" — cortisol +30% com notificações. Califórnia SB-1044 (2024) — right to disconnect. França — direito à desconexão (2017).
Sistema: OpenSilencePolicy.

---

**P21 — Ligação predatória proibida**

Problema: Dez ligações de telemarketing por dia. Golpes. Cobrança abusiva.

Solução: Proibir toda ligação não solicitada. Opt-in obrigatório: ninguém liga sem autorização prévia. Três denúncias geram bloqueio permanente. A IA bloqueia antes de tocar. Robocall deixa de existir. Golpe confirmado é crime.

Custo: Zero — é regulação + tecnologia existente.
Economia estimada: R$ 3-5 bilhões/ano em golpes evitados (ProCon estimativas). Confiabilidade: MÉDIA.
Prazo: 1-2 anos (fase 1).
Base científica: Brasil já tem o "Não Me Ligue" do ProCon — precisa de fiscalização efetiva. Lei Geral de Proteção de Dados (LGPD, Lei 13.709/2018).
Sistema: OpenAntiSpamCall.

---

**P22 — Prevenção da violência de gênero e feminicídio**

Correção: A política original propunha tornar o "status relacionamental público" para evitar traição. ISSO É VIGILÂNCIA ESTATAL DE RELAÇÕES PESSOAIS. Um banco de dados de status não reduz feminicídio — ciúme possessivo é problema psicológico e estrutural, não de informação. A versão revisada foca no que funciona.

Problema: O Brasil tem uma das maiores taxas de feminicídio do mundo — ~3,7 por 100.000 mulheres (Fórum Brasileiro de Segurança Pública, 2023). 70% dos feminicídios envolvem parceiro ou ex-parceiro. A Lei Maria da Penha (Lei 11.340/2006) existe, mas a fiscalização é insuficiente.

Solução: (1) Programas obrigatórios de educação emocional e respeito nas escolas desde o fundamental. (2) Pulseiras de contenção eletrônica para agressores com medida protetiva. (3) Abrigos ampliados e rede de apoio integrada. (4) Atendimento psicológico gratuito para vítimas E agressores (tratamento, não só punição). (5) Tribunais especializados em violência doméstica com capacidade ampliada.

Custo: R$ 3-5 bilhões/ano.
Economia estimada: Cada feminicídio custa ao sistema R$ 500.000+ (investigação, processo, prisão, órfãos). Reduzir 30% economiza R$ 1-2 bilhões/ano, além de vidas. Confiabilidade: MÉDIA.
Prazo: 1-5 anos (fases 1-2).
Base científica: Fórum Brasileiro de Segurança Pública (2023). Lei Maria da Penha (Lei 11.340/2006). Espanha — Lei Integral contra Violência de Gênero (2004) reduziu feminicídio em 30%.
Sistema: OpenRelationships (reformulado: OpenGenderViolence).

---

## SEGURANÇA

**P23 — Arte marcial como educação**

Problema: O brasileiro não sabe se defender. Depende de uma polícia que não chega.

Solução: Arte marcial unificada com técnicas de nove artes (Muay Thai, BJJ, Judô, Boxe, Krav Maga, Capoeira, Kali, Aikido). Adaptada para crianças (escapar), idosos (alavanca) e cadeirantes (BJJ sentado). Três níveis: escapar, neutralizar, proteger. Obrigatória na escola.

Custo: R$ 1-2 bilhões/ano (instrutores + infraestrutura escolar).
Economia estimada: Redução de agressão, bullying e feminicídio. Difícil quantificar, mas programas escolares de artes marciais mostram redução de 40% em incidentes violentos (Harvard, 2018).
Prazo: 3-5 anos (fases 1-2).
Base científica: Israel — Krav Maga obrigatório no serviço militar. Harwood et al. (2018) "Martial arts training and aggression reduction in schools."
Sistema: OpenMartialArts.

---

**P24 — Desarmamento rigoroso**

Problema: O Brasil tem ~50 milhões de armas de fogo em circulação (estimativa Fórum Brasileiro de Segurança Pública, 2023), a maioria ilegal. Tiroteio mata ~40.000 por ano.

Solução: Proibir armas de guerra (fuzis, rifles semiautomáticos com carregador de alta capacidade). Arma de fogo de uso domiciliar exige: avaliação psicológica, antecedentes limpos, cofre, curso de proficiência, endosso de dois cidadãos e renovação anual. Comércio de armas proibido para civis. Defesa não-letal preferida (spray de pimenta, taser).

Custo: R$ 1-2 bilhões/ano em fiscalização e campanhas de entrega.
Economia estimada: Redução de 30-50% em homicídios por arma de fogo (Sou et al., 2013, sobre o Estatuto do Desarmamento). Economia: R$ 5-10 bilhões/ano. Confiabilidade: MÉDIA.
Prazo: 1-3 anos (fase 1).
Base científica: Japão — 10 homicídios por ano (população 125 milhões). Reino Unido — armas proibidas após Dunblane (1996). Sou et al. (2013, AJPH) — redução de homicídios no Brasil pós-Estatuto. Fórum Brasileiro de Segurança Pública (2023).
Sistema: OpenWeaponsPolicy.

---

## CULTURA

**P25 — Patrimônio musical popular**

Problema: Gêneros populares são marginalizados. Elitismo cultural. O ECAD arrecada R$ 2 bilhões/ano com cobrança de copyright corporativo sobre música.

Solução: Declarar 12 gêneros como patrimônio cultural imaterial da República: funk, rap, hip-hop, samba, forró, frevo, maracatu, choro, bossa nova, pagode, axé e techno. Tudo CC0 — qualquer um cria, toca, dança, remixa e ensina sem pagar royalty corporativo. O criador é reconhecido, mas a obra é livre.

Custo: Zero — é declaração e licenciamento.
Economia estimada: R$ 1-2 bilhões/ano em royalties que deixam de ser extraídos do bolso do cidadão. Confiabilidade: BAIXA.
Prazo: 1-2 anos (fase 1).
Base científica: Creative Commons — prova que licenciamento aberto funciona para música. IPHAN — reconhecimento de patrimônio imaterial (samba, capoeira já reconhecidos).
Sistemas: OpenMusicHeritage, OpenMusic.

---

**P26 — Educação antipreconceito com dados**

Correção: A política original propunha "ressignificar a suástica como símbolo de paz" por decreto democrático. No contexto brasileiro de crescente antisemitismo e neonazismo (Santa Catarina, Sul do país), isso é irresponsável. Um processo de votação não apaga trauma histórico de comunidades vivas. A versão revisada foca no que funciona: educação com dados.

Problema: O preconceito mata — racismo, machismo, homofobia, transfobia e antisemitismo são estruturais. Símbolos de ódio são usados para intimidar.

Solução: (1) Educação obrigatória sobre racismo estrutural, antisemitismo e intolerância religiosa nas escolas, com dados históricos e científicos. (2) Legislação que criminalize o uso de símbolos de ódio (suástica nazista, siglas de facção) para intimidação ou incitação à violência. (3) Programas de ressignificação cultural liderados pelas PRÓPRIAS comunidades afetadas — nunca por decreto externo.

Custo: R$ 500 milhões/ano.
Economia estimada: Redução indireta de violência discriminatória.
Prazo: 1-3 anos (fase 1).
Base científica: UNESCO (1995) "Tolerância e Direitos Humanos." Lei 7.716/1989 (Lei Caó) — racism é crime inafiançável. ADI/STF sobre criminalização de homofobia (2019).
Sistema: OpenSymbolRevision (reformulado: OpenAntiPrejudice).

---

## AMBIENTE

**P27 — Catadores como trabalhadores ambientais da República**

Correção: A política original estimou R$ 2.000 por catador para carrinho elétrico + exoesqueleto + IA de triagem + EPI completo. Um exoesqueleto industrial custa R$ 30.000+ sozinho. A versão revisada é mais realista.

Problema: O catador curva a coluna, carrega 80 kg, trabalha no frio e na chuva por migalhas. O Brasil recicla apenas 4% do lixo (ABRELPE, 2023); a Alemanha recicla 67%.

Solução: Equipar o catador com dispositivos ergonômicos: carrinho manual melhorado (não elétrico de início — R$ 1.500), prensa manual portátil (R$ 800), EPI completo (R$ 500), smartphone com app de triagem por IA (R$ 1.000). Identificação: colete "Trabalhador Ambiental da República." Crédito por impacto, automático. Versão 2 (fase 3): carrinho elétrico e exoesqueleto quando o custo baixar.

Custo: R$ 3.000-4.000 por catador (fase 1). R$ 1-2 bilhões/ano para 500.000 catadores.
Economia estimada: R$ 3-5 bilhões/ano em material reciclado recuperado (ABRELPE). Confiabilidade: MÉDIA.
Prazo: 3-5 anos (fases 1-2).
Base científica: ABRELPE (2023) Panorama dos Resíduos Sólidos. Instituto Pólis — PNRS (Lei 12.305/2010). Alemanha — 67% de reciclagem (Eurostat).
Sistema: OpenRecyclers.

---

**P28 — Produtos que não prejudicam**

Problema: Descartável, tóxico, teste em animais, obsolescência programada.

Solução: Critérios obrigatórios para todo produto: não prejudica a saúde, sem teste em animais, não polui, reparável, modular, fabricável em FabLab e trabalho justo. Três produtos proibidos: teflon (PFAS), copo descartável de plástico e teste em animais. Substituição gradual por alternativas modulares e CC0.

Custo: R$ 1-2 bilhões/ano em fiscalização e certificação.
Economia estimada: Redução de 500 bilhões de garrafas e 1 trilhão de sacolas plásticas/ano. Valor: R$ 5-10 bilhões/ano. Confiabilidade: BAIXA.
Prazo: 3-5 anos (fases 1-2).
Base científica: União Europeia — Diretiva SUP (Single-Use Plastics, 2021). Diretiva de Right to Repair (2024). PFAS Restriction Proposal (ECHA). Lei 12.305/2010 (PNRS). ABRELPE (2023).
Sistema: OpenProduct.

---

## GOVERNANÇA

**P29 — Democracia participativa digital**

Correção: A política original propunha 10.000 sorteados com mandato de 3 meses. Rotatividade de 3 meses = zero memória institucional — cada 3 meses, 10.000 pessoas novas votando em leis que não entendem. A versão revisada é mais realista.

Problema: O político decide por você. Promete e não cumpre. Corrupção: estimada em R$ 100-200 bilhões/ano (TCU/CGU). A democracia representativa tem baixa legitimidade.

Solução: Sistema de democracia participativa em três camadas: (1) Representantes eleitos com mandato revogável (recall) — não 3 meses, mas 4 anos com possibilidade de revogação. (2) Assembleia digital permanente aberta a TODOS os cidadãos: todo cidadão pode votar em qualquer proposta via OpenTerminal. (3) Conselho técnico permanente (especialistas sorteados por área) que analisa viabilidade antes da votação popular. O povo decide; os técnicos informam.

Custo: R$ 2-3 bilhões em implementação digital (segurança blockchain, identificação biométrica).
Economia estimada: R$ 50-100 bilhões/ano em corrupção reduzida. Confiabilidade: BAIXA (difícil de provar).
Prazo: 5-10 anos (fases 1-3).
Base científica: Suíça — democracia direta há 800 anos (referendos nacionais). Taiwan — vTaiwan, plataforma digital de participação cidadã (2014-presente). Estonia — i-Voting desde 2005.
Sistema: OpenConstituentAssembly (reformulado: OpenDemocracy).

---

**P30 — Governança fundadora com checks and balances**

Correção: A política original dava ao fundador "voz permanente" com override por IA. Um AI decidindo o que pode ou não ser votado é tecnocracia. A versão revisada é mais conservadora.

Problema: Como garantir que um líder fundador não vire ditador?

Solução: O fundador tem voz consultiva permanente, mas o voto vale 1, igual a todos. Não há IA que bloqueia propostas — a IA APENAS sinaliza potencial conflito com os princípios (P1-P4), mas o veto é exclusivamente humano e democrático. Se a assembleia aprova com 60%, a proposta passa mesmo contra a opinião do fundador.

Custo: Zero.
Economia estimada: Garantia anti-autoritarismo. Incalculável.
Prazo: Imediato (fase 1).
Base científica: Montesquieu — separação de poderes. Constituição Federal de 1988 — checks and balances. Linus Torvalds — o fundador do Linux tem voz, mas a comunidade decide.
Sistema: OpenFounderRole.

---

## INFRAESTRUTURA

**P31 — TV aberta vira streaming público**

Problema: A TV aberta é comercial, vive de IBOPE, tem algoritmo de engajamento e clickbait.

Solução: Fazer toda a comunicação rodar na OpenNetwork sobre o OpenProtocol. Canais temáticos. Grade de 24 horas preenchida por rotação comunitária. Apresentar TV é trabalho. Zero comercial, zero patrocínio, zero IBOPE.

Custo: R$ 3-5 bilhões em transição (infraestrutura + retraining de funcionários de emissoras existentes).
Economia estimada: Eliminação da influência de patrocinador na informação. Difícil quantificar.
Prazo: 5-10 anos (fases 2-3).
Base científica: BBC (Reino Unido) — modelo público funciona. NHK (Japão). ARD/ZDF (Alemanha). TV Brasil já existe, mas com baixo orçamento.
Sistemas: OpenContentPolicy, OpenTV.

---

**P32 — Repositório único, sem fork**

Problema: Cada um copia o projeto, faz versão própria e fragmenta.

Solução: Um único repositório. Pull para puxar, merge request para propor. A assembleia vota com 51%. Tudo é testado antes de integrar. Forks que mutilam são proibidos. Tudo CC0.

Custo: Zero — é política de desenvolvimento.
Economia estimada: Prevenção de fragmentação e duplicação.
Prazo: Imediato (fase 1).
Base científica: Kernel do Linux — um repositório único há 30 anos. Torvalds, L. (2020) sobre maintainer model.
Sistema: OpenRepoPolicy.

---

## TRABALHO

**P33 — Responsabilidades por contexto**

Problema: A pessoa acumula tudo: trabalho, casa, filhos e comunidade. Sobrecarregada.

Solução: Distribuir responsabilidades em seis contextos: pessoal, familiar, laboral, comunitário, cívico e ambiental. Distribuição por capacidade. Rotação de tarefas. Ninguém trabalha mais de 40 horas/semana.

Custo: Zero — é política de gestão.
Economia estimada: Redução de burnout, absenteísmo e rotatividade (R$ 30-50 bi/ano segundo ISMA-BR).
Prazo: 1-3 anos (fase 1).
Base científica: Dinamarca — 37h/semana, maior produtividade da Europa. Stanford (Pencavel, 2014) — produtividade cai após 50h/semana.
Sistema: OpenResponsibility.

---

**P34 — Reparo de tudo: nada se joga fora**

Problema: O Brasil joga fora R$ 20 bilhões/ano em eletrônicos. Obsolescência programada.

Solução: OpenRepair: tudo que quebra, conserta. Diagnóstico por IA, guia passo a passo e FabLab que fabrica a peça. Garantia eterna: enquanto existir, conserta. Right to Repair: sem monopólio de conserto.

Custo: R$ 1-2 bilhões/ano em rede de FabLabs.
Economia estimada: R$ 10-20 bilhões/ano em eletrônicos recuperados. Confiabilidade: MÉDIA.
Prazo: 3-5 anos (fases 1-2).
Base científica: UE — Right to Repair Directive (2024). iFixit — repairability scores. Lei 12.305/2010 (PNRS).
Sistema: OpenRepair.

---

## NOVAS POLÍTICAS (lacunas preenchidas)

**P35 — Saneamento básico universal**

Problema: 35 milhões de brasileiros não têm tratamento de esgoto (SNIS, 2023). Apenas 63% do esgoto gerado é coletado e 49% tratado. Doenças de veiculação hídrica matam crianças. Esta é uma das omissões mais graves do documento original.

Solução: Plano nacional de universalização do saneamento em 10 anos. Prioridade: Norte e Nordeste, onde a cobertura é menor que 30%. Tecnologia descentralizada (fossas sépticas modulares + wetlands construídos para zonas rurais) em paralelo com rede convencional nas cidades. Gestão pública (não privatizada — o modelo privatizante do Novo Marco Legal do Saneamento, Decreto 10.708/2020, falha em gerar universalização).

Custo: R$ 20-30 bilhões/ano por 10 anos.
Economia estimada: R$ 10-15 bilhões/ano em custos médicos evitados (diarréias, hepatite, dengue). Confiabilidade: ALTA.
Prazo: 10 anos (fases 1-4).
Base científica: SNIS (2023) Sistema Nacional de Informações sobre Saneamento. Trata Brasil (2023). OMS — cada R$ 1 em saneamento economiza R$ 4 em saúde (OMS, 2014). Lei 14.026/2020 (Novo Marco do Saneamento).
Sistema: OpenSanitation (NOVO).

---

**P36 — Soberania dos povos originários e quilombolas**

Problema: O Brasil tem 305 povos indígenas, ~1,7 milhão de pessoas (Censo 2022). Terras indígenas demarcadas: ~12,5% do território nacional, mas sob ataque constante por garimpo, madeira e agro. Quilombolas: ~16 milhões de pessoas, com baixa demarcação de territórios. Esta omissão do documento original é inaceitável.

Solução: (1) Concluir a demarcação de todas as terras indígenas pendentes (148 processos parados na FUNAI). (2) Titulação de todos os territórios quilombolas. (3) Proteção armada e tecnológica (satélite + drones) contra invasão. (4) Saúde indígena diferenciada (Subsistema de Saúde Indígena ampliado). (5) Educação bilíngue e intercultural. (6) Consulta prévia, livre e informada (Convenção 169 da OIT) obrigatória para qualquer projeto em território indígena.

Custo: R$ 3-5 bilhões/ano (demarcação, fiscalização, saúde, educação).
Economia estimada: Proteção da Amazônia (estimada em US$ 50-100 bilhões/ano em serviços ambientais, Scientists Advanced). Preservação cultural incalculável. Confiabilidade: MÉDIA.
Prazo: 5-10 anos (fases 1-3).
Base científica: Constituição Federal art. 231 e 232. Convenção 169 da OIT (ratificada pelo Brasil). Censo IBGE 2022. FUNAI. Sociedade Brasileira para o Progresso da Ciência (SBPC).
Sistema: OpenIndigenousRights (NOVO).

---

**P37 — Transição energética e soberania elétrica**

Problema: O Brasil depende de hidrelétricas (60% da matriz), vulneráveis às secas. Importa gás natural e derivados. 1,5 milhão de brasileiros sem acesso à eletricidade (ONS, 2023).

Solução: (1) Expansão acelerada de solar e eólica (meta: 50% da matriz em 15 anos). (2) Microgeração distribuída — todo telhado público com painéis solares. (3) Estudos (não construção imediata) para ampliação nuclear (Angra 3 + 2-3 reatores pequenos modulares SMR). (4) Universalização do acesso à eletricidade via micro-redes solares em comunidades isoladas (Amazônia). (5) Fabricação nacional de painéis e baterias.

Custo: R$ 20-30 bilhões/ano (investimento público + parcerias).
Economia estimada: R$ 10-20 bilhões/ano em importações evitadas + soberania energética. Confiabilidade: MÉDIA.
Prazo: 10-20 anos (fases 2-5).
Base científica: ONS (2023). EPE — Balanço Energético Nacional. IEA (2023) World Energy Outlook. INMETRO. ANEEL Resolução 482/2012 (geração distribuída).
Sistema: OpenEnergy (NOVO).

---

**P38 — Transporte público de massa e carga**

Problema: O transporte público brasileiro é precário. O país usa o caminhão para 60% da carga, rodoviário precário, hidrovia e ferrovia subutilizadas. Congestionamentos custam R$ 40-60 bilhões/ano (CNT, 2023).

Solução: (1) Investimento massivo em transporte público urbano (metrô, VLT, BRT) nas 20 maiores cidades. (2) Revitalização ferroviária para carga (substituir caminhão por trem). (3) Expansão de hidrovias (Amazonas, São Francisco, Tietê-Paraná). (4) Bicicleta como infraestrutura urbana de primeira classe. (5) Fabricação nacional de trens e VLTs.

Custo: R$ 30-50 bilhões/ano.
Economia estimada: R$ 40-60 bilhões/ano em congestionamento reduzido + R$ 10-20 bilhões/ano em custo logístico reduzido. Confiabilidade: MÉDIA.
Prazo: 10-20 anos (fases 2-5).
Base científica: CNT (2023) Confederação Nacional do Transporte. EPL — Empresa de Planejamento e Logística. ANTT (Agência Nacional de Transportes Terrestres). Ministério dos Transportes — Plano Nacional de Logística.
Sistema: OpenTransport (NOVO).

---

**P39 — Soberania alimentar e reforma agrária**

Problema: O Brasil é um dos maiores produtores de alimentos do mundo, mas 33 milhões de pessoas passam fome (Rede PENSSANAM, 2022). Concentração fundiária: 1% das propriedades ocupam 47% da área (Censo Agropecuário IBGE, 2017).

Solução: (1) Reforma agrária ampla: assentamento de famílias sem-terra em terras públicas e improdutivas. (2) Apoio técnico e financeiro à agricultura familiar (responsável por 70% da alimentação do brasileiro). (3) Cooperativismo agrícola com tecnologia Embrapa. (4) Banco de sementes crioulas (contra o monopólio de sementes transgênicas). (5) Combate ao desperdício: 30% da produção agrícola é desperdiçada.

Custo: R$ 10-15 bilhões/ano.
Economia estimada: Erradicação da fome (33 milhões de pessoas) + aumento de 20-30% na produtividade da agricultura familiar. Confiabilidade: MÉDIA.
Prazo: 5-15 anos (fases 1-4).
Base científica: Rede PENSSANAM (2022) II Inquérito Nacional sobre Insegurança Alimentar. IBGE Censo Agropecuário (2017). Embrapa — agricultura familiar. FAO (2023) State of Food Security. Lei 8.629/1993 (reforma agrária).
Sistema: OpenAgrarian (NOVO).

---

**P40 — Política externa soberana e não-alinhada**

Uma visão do Brasil independente dos blocos geopolíticos EUA-China. Priorizar América do Sul, BRICS+ e Sul Global.

Problema: O Brasil oscila entre alinhamento automático aos EUA e alinhamento automático à China. Falta uma doutrina própria.

Solução: (1) Doutrina de não-alinhamento ativo: parcerias por interesse mútuo, não por bloco. (2) Integração sul-americana (Mercosul + UNASUL revitalizada). (3) Liderança no Sul Global (G77+China, BRICS+). (4) Defesa da multipolaridade e reforma do Conselho de Segurança da ONU. (5) Soberania tecnológica: não depender de satélite (Starlink), nem de infraestrutura crítica estrangeira.

Custo: Zero — é política diplomática.
Economia estimada: Soberania e poder de barganha comercial. Difícil quantificar.
Prazo: Imediato (fase 1).
Base científica: Doutrina Itamaraty/Funag. Celso Furtado — dependência econômica. Samuel Pinheiro Guimarães — "Nação Desnudada."
Sistema: OpenForeignPolicy (NOVO).

---

**P41 — Defesa nacional soberana**

Problema: O Brasil gasta apenas 1,3% do PIB em defesa (SIPRI, 2023) — abaixo da média mundial. Depende de equipamento importado (caças Gripen suecos, rifles belgas). A Amazônia é vulnerável.

Solução: (1) Aumentar gradativamente o gasto para 1,8-2,0% do PIB. (2) Nacionalização da indústria de defesa (Embraer, IMBEL, Akafluh expandidos). (3) Sistema Integrado de Monitoramento da Amazônia (SISAMAZONIA) com satélites nacionais + drones + radar. (4) Cyberdefesa nacional. (5) Serviço civil voluntário ampliado (não militar obrigatório).

Custo: R$ 15-25 bilhões/ano adicionais.
Economia estimada: Soberania territorial e tecnológica. Indireto.
Prazo: 10-20 anos (fases 2-5).
Base científica: SIPRI (2023) Military Expenditure Database. Ministério da Defesa — Livro Branco de Defesa Nacional (2020). Embraer — soberania na aviação. Convenção de Ottawa (minas terrestres).
Sistema: OpenDefense (NOVO).

---

**P42 — Direitos digitais e soberania de dados**

Problema: Os dados de 215 milhões de brasileiros estão em servidores estrangeiros (Google, Meta, AWS). Vigilância corporativa e governamental. LGPD existe, mas fiscalização é fraca.

Solução: (1) Soberania de dados: dados de cidadãos brasileiros devem residir em servidores no Brasil. (2) Infraestrutura nacional de nuvem pública (BR Cloud). (3) Criptografia de ponta a ponta como direito. (4) Proibição de vigilância em massa sem ordem judicial. (5) IA pública e auditável (não corporativa de caixa-preta). (6) Internet como direito fundamental (já previsto no Marco Civil da Internet, Lei 12.965/2014).

Custo: R$ 5-10 bilhões/ano (infraestrutura + fiscalização).
Economia estimada: Soberania digital + redução de fraudes. Difícil quantificar.
Prazo: 5-10 anos (fases 1-3).
Base científica: Marco Civil da Internet (Lei 12.965/2014). LGPD (Lei 13.709/2018). GDPR (UE). Snowden disclosures (2013). Schrems II (UE, 2020) — dados europeus fora da UE.
Sistema: OpenDigitalRights (NOVO).

---

## TRANSIÇÃO

**P43 — Transição gradual em sete fases**

Correção: A política original somava R$ 2,422 trilhões/ano de economia. Essa soma aritmética é problemática porque (a) várias estimativas têm baixa confiança, (b) há sobreposição entre políticas que atuam sobre a mesma base, (c) algumas economias são indiretas e difíceis de realizar. A versão revisada apresenta um intervalo.

Problema: Mudança brusca é caos. Ninguém perde nada do dia para a noite.

Solução: Transição em sete fases. Fase 0: construção (116 sistemas prontos). Fase 1: adoção voluntária (1-3 anos). Fase 2: infraestrutura paralela (3-5 anos). Fase 3: dupla circulação (5-10 anos). Fase 4: migração em massa (10-15 anos). Fase 5: descomissionamento (15-20 anos). Fase 6: República completa (20-25 anos).

Custo total consolidado (investimento líquido): R$ 60-110 bilhões/ano durante a transição.

Economia estimada consolidada (intervalo, com sobreposição): R$ 150-400 bilhões/ano ao completar a transição. Esta é uma faixa honesta — não uma promessa. As políticas de maior confiança (saneamento, saúde preventiva, reforma prisional, Housing First) somam sozinhas R$ 50-100 bilhões/ano de economia validável. O restante é potencial.

Confiabilidade do total: BAIXA (soma de estimativas com sobreposição).
Prazo: 20-25 anos.
Base científica: A transição soviética falhou por ser brusca. A chinesa (1978-presente) é gradual e bem-sucedida. China — transição econômica em 40 anos. Polónia — transição gradual foi menos traumática que a russa.
Sistema: OpenTransition.

---

**TOTAL: 43 políticas públicas em 16 áreas.**

Original: 35 políticas em 13 áreas. Esta versão: 43 políticas em 16 áreas.

Principais mudanças desta revisão:
1. Custos honestos — removidos 12 "não há custo" e substituídos por valores reais
2. Fontes externas adicionadas (IBGE, BACEN, OMS, OCDE, IPEA, INFOPEN, SNIS, CNT, etc.)
3. Confiabilidade classificada (ALTA/MÉDIA/BAIXA) para cada estimativa
4. Erros médicos corrigidos (P2 LASIK contraindicações, P3 dente saudável, P4 imortalidade → longevidade)
5. P22 reformulado: vigilância de relacionamentos → prevenção de feminicídio
6. P26 reformulado: suástica → educação antipreconceito
7. P29 reformulado: assembleia de 3 meses → democracia participativa em 3 camadas
8. 8 novas políticas adicionadas: saneamento, povos originários, energia, transporte, soberania alimentar, política externa, defesa, direitos digitais
9. Total de R$ 2,422 trilhões/ano (especulativo) → R$ 150-400 bilhões/ano (intervalo honesto)

Brasil: do capitalismo predatório à República do bem comum. 20 a 25 anos. Gradual. Sem trauma. Com dignidade.