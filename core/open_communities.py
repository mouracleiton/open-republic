#!/usr/bin/env python3
"""
OpenCommunities -- 6 Adaptacoes Comunitarias da Republica -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenCommunities -- 6 Adaptacoes Comunitarias da Republica
============================================================
"O modelo not se impoe. Se ADAPTA.
Cada comunidade tem alma propria.
A Republica respeita a alma. Nutre. Nao substitui.
6 comunidades. 6 adaptacoes. 1 modelo conceitual.
Cada uma com suas especificidades, cultura, necessidades."
PRINCIPIO (P2 + P4):
- Chega como CONVIDADO. Nunca como invasor.
- ADAPTA a cultura. Nunca substitui.
- A comunidade DECIDE o que quer. Fundador propoe.
- Se not quiserem: respeito. OpenWololo depois.
AS 6 COMUNIDADES:
1. OpenQuilombo -- ancestralidade africana, mutirao, oralidade
2. OpenAssentamentoRural -- agricultura familiar, cooperativa, terra
3. OpenRibeirinho -- Amazonia, rio, enchente, pesca, isolamento
4. OpenAldeia -- soberania indigena, terra sagrada, consenso
5. OpenFavela -- urbano, densidade, cultura, empreendedorismo
6. OpenSertao -- seca, agua, caatinga, resiliencia
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional de typing
# importa Enum de enum
# importa defaultdict de collections
# importa datetime de datetime
# ============================================================================
# 1. TIPOS DE COMUNIDADE
# ============================================================================
class CommunityType(Enum):
    QUILOMBO = ("quilombo", "Comunidade quilombola")
    ASSENTAMENTO = ("assentamento_rural", "Assentamento rural")
    RIBEIRINHO = ("ribeirinho", "Comunidade ribeirinha")
    ALDEIA = ("aldeia_indigena", "Aldeia indigena")
    FAVELA = ("favela", "Comunidade urbana (favela)")
    SERTAO = ("sertao", "Comunidade do sertao nordestino")
class CulturalPillar(Enum):
    # Pilares culturais de cada comunidade.
    ANCESTRALIDADE = "ancestralidade"  // tradicao passada por geracoes
    TERRA = "terra"  // relacao com territorio
    ESPIRITUALIDADE = "espiritualidade"  // fe, sagrado
    ORALIDADE = "oralidade"  // tradicao oral (not escrita)
    MUTIRAO = "mutirao"  // trabalho coletivo
    LIDERANCA_TRADICIONAL = "lideranca"  // lider tradicional
    LINGUA_PROPRIA = "lingua"  // idioma nativo
    CORPO = "corpo"  // dancas, lutas, expressao
# ============================================================================
# 2. PERFIL DE COMUNIDADE
# ============================================================================
# decorador: @dataclass
class CommunityProfile:
    # Perfil adaptado de uma comunidade.
    community_type: CommunityType
    name: texto
    description: str = ""
    # Cultura (NUNCA substituir, SEMPRE respeitar)
    cultural_pillars: [CulturalPillar] = field(default_factory=list)
    existing_practices: {texto: texto} = field(default_factory=dict)
    # existing_practices = {"nome_ja_existente": "equivalente_republica"}
    # Necessidades especificas (o que FALTA)
    needs: [texto] = field(default_factory=list)
    # Adaptações do modelo Republica
    adapted_systems: {texto: texto} = field(default_factory=dict)
    # adapted_systems = {"sistema_republica": "como_adapta_para_esta_comunidade"}
    # O que NÃO se importa (respeito cultural)
    do_not_import: [texto] = field(default_factory=list)
    # Governanca adaptada
    governance_model: str = ""
    decision_making: str = ""  // como decidem (consenso, voto, conselho)
    # Lingua
    primary_language: str = "pt-BR"
    secondary_languages: [texto] = field(default_factory=list)
    # Isolamento geografico
    isolation_level: str = ""  // urbano, semi-isolado, isolado, muito isolado
    access_challenge: str = ""  // barreira de acesso (rio, estrada, etc)
# ============================================================================
# 3. OS 6 PERFIS
# ============================================================================
PROFILES: [CommunityProfile] = [
    # === 1. OPENQUILOMBO ===
    CommunityProfile(
        community_type = CommunityType.QUILOMBO,
        name = "OpenQuilombo",
        description = (
            "Comunidades quilombolas: descendentes de pessoas escravizadas "
            "que resistiram and fundaram comunidades livres. "
            "Tradição oral, mutirão, capoeira, jongo, candomblé. "
            "Direito constitucional à terra (Art. 68 ADCT). "
            "Resistência centenária. A República NÃO ensina. APRENDE."
        ),
        cultural_pillars = [
            CulturalPillar.ANCESTRALIDADE,
            CulturalPillar.TERRA,
            CulturalPillar.ORALIDADE,
            CulturalPillar.MUTIRAO,
            CulturalPillar.ESPIRITUALIDADE,
            CulturalPillar.CORPO,
        ],
        existing_practices = {
            "mutirao": "OpenLaborRelay (ja fazem: trabalho coletivo sem dinheiro)",
            "roca_comunitaria": "OpenAgrarian (ja plantam juntos)",
            "capoeira": "OpenMartialArts (ja and defesa + cultura + corpo)",
            "jongo_danca": "OpenMusic + OpenNightLife (ja celebram juntos)",
            "conselho_ancioes": "OpenConstituentAssembly (ja decidem juntos)",
            "teologia_afro": "OpenTradition (ja tem espiritualidade propria)",
            "reparacao_historica": "OpenPsychologyReparation (ja lutam por reparacao)",
        },
        needs = [
            "Titulação definitiva da terra (muitos ainda sem título)",
            "Energia solar (muitos sem rede elétrica)",
            "Internet (OpenNetwork via satélite/rádio)",
            "Saúde (posto mais próximo a 50+ km)",
            "Educação que respeite cultura afro-brasileira",
            "Documentação (muitos sem registro civil)",
            "Água potável (cisternas, poços artesianos)",
            "Escoamento de produção (estrada, transporte)",
        ],
        adapted_systems = {
            "OpenConstituentAssembly": (
                "Conselho de Anciãos + Assembleia Geral. "
                "Lideranca tradicional RESPEITADA. "
                "Decisoes por consenso (not maioria 51%). "
                "Assembleia se adapta ao ritmo da comunidade."
            ),
            "OpenEducation": (
                "Currículo AFRO-BRASILEIRO. "
                "Historia da Africa and diaspora. "
                "Matematica com padroes de tecelagem. "
                "Ciencias com medicina tradicional + cientifica. "
                "Tradição oral como metodologia (not so texto)."
            ),
            "OpenHealth": (
                "Saúde integrativa: medicina cientifica + tradição afro. "
                "Raizeiro/raizeira trabalha JUNTO com medico. "
                "Parto humanizado com parteira tradicional. "
                "Plantas medicinais catalogadas com OpenHistory. "
                "Capoeira como saude fisica + mental."
            ),
            "OpenCredit": (
                "Moeda comunitaria já existe em muitos quilombos (troca). "
                "OpenCredit se chama 'Moeda do Quilombo'. "
                "Valoriza produção local (farinha, mel, artesanato). "
                "Conecta com outros quilombos (network quilombola)."
            ),
            "OpenHistory": (
                "Registra HISTORIA ORAL dos mais velhos (urgente). "
                "Muitos ancioos morrendo sem ter historia gravada. "
                "OpenHistory = preservacao da memoria. "
                "Nao and historia do dominador. E a DELES."
            ),
            "OpenIndustry": (
                "FabLab quilombola: farinharia mecanizada, "
                "mel, oleo de dendê, artesanato. "
                "Nao substitui producao tradicional. MELHORA. "
                "Cacau beneficiado no local (not vender materia prima)."
            ),
        },
        do_not_import = [
            "NUNCA substituir liderança tradicional por sistema digital",
            "NUNCA impor currículo que negue ancestralidade",
            "NUNCA tratar medicina tradicional como inferior",
            "NUNCA romper relação com terra sagrada",
            "NUNCA impor votação majoritária se cultura é consenso",
        ],
        governance_model = "Conselho de Anciãos + Assembleia Comunitária",
        decision_making = "Consenso (não maioria). O mais velho fala. Todos ouvem.",
        primary_language = "pt-BR",
        secondary_languages = ["quimbundo", "ioruba", "banto (variantes)"],
        isolation_level = "isolado a muito isolado",
        access_challenge = "Estrada vicinal, rio, trilha. Muitos sem acesso em chuva.",
    ),
    # === 2. OPENASSENTAMENTO RURAL ===
    CommunityProfile(
        community_type = CommunityType.ASSENTAMENTO,
        name = "OpenAssentamentoRural",
        description = (
            "Assentamentos rurais: familias que conquistaram terra "
            "atraves de reforma agraria (MST, CPT, CONTAG). "
            "Cooperativismo na pratica. Agricultura familiar. "
            "Luta pela terra ja vencida. Luta pela dignidade em andamento. "
            "A Republica chega como FERRAMENTA, not como ideia."
        ),
        cultural_pillars = [
            CulturalPillar.TERRA,
            CulturalPillar.MUTIRAO,
        ],
        existing_practices = {
            "cooperativa": "OpenMarketplace (ja vendem juntos)",
            "mutirao_colheita": "OpenLaborRelay (ja colhem juntos)",
            "associacao": "OpenConstituentAssembly (ja se organizam)",
            "troca_sementes": "OpenAgrarian (ja trocam sementes)",
            "educacao_do_campo": "OpenEducation (ja tem metodologia propria)",
            "saude_comunitaria": "OpenHealth (ja tem agente comunitario)",
            "agroecologia": "OpenProduct (ja produzem sem veneno)",
        },
        needs = [
            "Trator/equipamento (muitos com lavoura manual)",
            "Agroindustria (beneficiar produto: not vender materia prima)",
            "Energia (muitos sem rede no campo)",
            "Internet (OpenNetwork rural)",
            "Crédito agrícola sem juros (bancos cobram 40%)",
            "Assistência técnica (engenheiro agrônomo)",
            "Saúde (postos rurais sem estrutura)",
            "Escola do campo (fechando por falta de aluno/docente)",
            "Transporte (ônibus rural precário)",
            "Armazenagem (perda de safra por falta de silo)",
        ],
        adapted_systems = {
            "OpenAgrarian": (
                "OpenTrator (trator OpenHardware cooperativo). "
                "Silo comunitário FabLab (armazenagem). "
                "Irrigação solar (energia gratuita). "
                "Adubação verde (compostagem + OpenFertilizer). "
                "OpenDrone agrícola (mapeamento de lavoura)."
            ),
            "OpenCredit": (
                "Crédito rural sem juros. "
                "Cooperativa de crédito (ja existe em muitos). "
                "OpenERP agricola: gestao de safra, estoque, venda. "
                "Conecta direto com consumidor (sem intermediario)."
            ),
            "OpenIndustry": (
                "Agroindustria comunitária FabLab: "
                "beneficiamento de mandioca (farinha/goma/tapioca), "
                "leite (queijo/iogurte), frutas (polpa/doce), "
                "graos (moinho). "
                "Vender processado, not materia prima."
            ),
            "OpenEducation": (
                "Educacao do campo (Pedagogia da Terra). "
                "Escola itinerante (acompanha safra). "
                "OpenUniversity no assentamento. "
                "Aprender fazendo: agricultura, cooperativismo, gestão. "
                "Criança aprende na roça E no OpenTerminal."
            ),
            "OpenLaborRelay": (
                "Mutirao registrado and recompensado. "
                "Quem ajuda vizinho colhendo = crédito. "
                "Maquina cooperativa: fila de uso organizada por app. "
                "Benchmark: quem produz mais agroecologica = reconhecido."
            ),
            "OpenRepair": (
                "Trator quebrou? OpenRepair conserta. "
                "OpenTrator and OpenHardware: FabLab fabrica peça. "
                "Sem depender de concessionaria a 200km. "
                "Sem esperar peça importada por meses."
            ),
        },
        do_not_import = [
            "NUNCA impor modelo que dispense cooperativa existente",
            "NUNCA substituir agroecologia por agronegócio",
            "NUNCA tratar educação do campo como inferior",
            "NUNCA separar familia da terra",
        ],
        governance_model = "Associação + Cooperativa (já existem)",
        decision_making = "Assembleia de associados (1 família = 1 voto)",
        primary_language = "pt-BR",
        isolation_level = "semi-isolado a isolado",
        access_challenge = "Estrada vicional. Transpósito rural precário.",
    ),
    # === 3. OPENRIBEIRINHO ===
    CommunityProfile(
        community_type = CommunityType.RIBEIRINHO,
        name = "OpenRibeirinho",
        description = (
            "Comunidades ribeirinhas da Amazonia. "
            "Beira-rio. Vida no ciclo das aguas (cheia and seca). "
            "Pesca, roça de coivara, extrativismo. "
            "Caboclo: mistura de indigena, nordestino, europeu. "
            "Acesso SO por rio (barco, canoa). "
            "Isolamento extremo. Resiliência extrema. "
            "A República chega pelo RIO."
        ),
        cultural_pillars = [
            CulturalPillar.TERRA,
            CulturalPillar.MUTIRAO,
            CulturalPillar.ORALIDADE,
            CulturalPillar.ANCESTRALIDADE,
        ],
        existing_practices = {
            "mutirao_pesca": "OpenLaborRelay (pescam juntos)",
            "roca_coivara": "OpenAgrarian (sistema tradicional amazonico)",
            "extrativismo": "OpenProduct (acai, castanha, borracha)",
            "parteira_tradicional": "OpenHealth (parteira ribeirinha)",
            "rezador_curandeiro": "OpenPsychology (cura tradicional)",
            "contacao_casos": "OpenHistory (tradicao oral cabocla)",
            "farinharia_comunitaria": "OpenIndustry (processamento local)",
        },
        needs = [
            "Saúde (postos sem médico, barco-hospital irregular)",
            "Energia (gerador a diesel caro; solar resolve)",
            "Internet (OpenNetwork via satélite Starlink-style)",
            "Água potável (rio tem, mas não é tratada)",
            "Educação (professor itinerante, escola multiseriada)",
            "Transporte (barco a motor caro, combustível)",
            "Comunicação (rádio é único meio em muitas)",
            "Geladeira (conservar peixe sem gelo é impossível)",
            "Escoamento de produção (acai estraga em dias)",
        ],
        adapted_systems = {
            "OpenSolar": (
                "Painel solar flutuante (Amazonia tem sol o ano todo). "
                "Bateria estacionaria. "
                "Geladeira solar (conserva peixe/acai). "
                "Bomba de água solar. "
                "Substitui diesel (caro, poluente, longe)."
            ),
            "OpenNetwork": (
                "Internet via satélite (Starlink-style, CC0). "
                "Ou rádio mesh (VHF/UHF entre comunidades). "
                "Rede offline-first (sincroniza quando tem sinal). "
                "Mensageiro que funciona sem internet (delay-tolerant)."
            ),
            "OpenHealth": (
                "Barco-clínica OpenHealth (consultório flutuante). "
                "Telemedicina via satélite. "
                "Raizeiro + enfermeiro ribeirinho (Técnico Médico). "
                "Malária: teste rápido + tratamento no local. "
                "Hepatite, verminose: rastreio anual. "
                "Parteira tradicional integrada."
            ),
            "OpenMobility": (
                "Barco elétrico solar (motor de pesca sem combustível). "
                "Mapa do rio (OpenMobility náutico). "
                "Previsão de cheia (IA + saberes tradicionais). "
                "Rota segura (evitar areas de remanso/piracema)."
            ),
            "OpenIndustry": (
                "Farinharia solar (mandioca -> farinha, sem diesel). "
                "Polpa de acai congelada (energia solar + freezer). "
                "Castanha beneficiada (abertura mecanica FabLab). "
                "Essência de cumaru, andiroba, copaiba (extrativismo)."
            ),
            "OpenEducation": (
                "Escola ribeirinha multiseriada + OpenTerminal. "
                "Professor mora na comunidade (not itinerante). "
                "Pedagogia da Amazonia: ciclos do rio, biodiversidade. "
                "OpenUniversity por satélite. "
                "Criança aprende + ensina pais (muitos analfabetos)."
            ),
        },
        do_not_import = [
            "NUNCA impor lógica urbana (terreno, endereço, CEP)",
            "NUNCA tratar coivara como crime sem entender ciclo amazonico",
            "NUNCA substituir parteira tradicional sem consentimento",
            "NUNCA construir que destrua margem do rio",
            "NUNCA tratar caboclo como 'atrasado' (P1 ANTI-ELITISMO)",
        ],
        governance_model = "Assembleia comunitária + liderança ribeirinha",
        decision_making = "Conversa na beira do rio. Consenso.",
        primary_language = "pt-BR",
        secondary_languages = ["nheengatu", "tikuna", "sateré-mawé"],
        isolation_level = "muito isolado",
        access_challenge = "SO por rio. Barco a motor: 4-12h ate cidade mais proxima.",
    ),
    # === 4. OPENDADEIA INDIGENA ===
    CommunityProfile(
        community_type = CommunityType.ALDEIA,
        name = "OpenAldeia",
        description = (
            "Aldeias indígenas. Soberania ancestral sobre territorio. "
            "Cada etnia tem: lingua, cosmovisão, sistema de conhecimento, "
            "forma de governanca, medicina, educacao PROPRIA. "
            "A Republica NAO ensina. SERVE. Se convidada (P2). "
            "TUDO passa pelo conselho indigena. TUDO."
        ),
        cultural_pillars = [
            CulturalPillar.ANCESTRALIDADE,
            CulturalPillar.TERRA,
            CulturalPillar.ESPIRITUALIDADE,
            CulturalPillar.ORALIDADE,
            CulturalPillar.LIDERANCA_TRADICIONAL,
            CulturalPillar.LINGUA_PROPRIA,
            CulturalPillar.CORPO,
        ],
        existing_practices = {
            "conselho_indigena": "OpenConstituentAssembly (ja decidem, há milenios)",
            "mutirao": "OpenLaborRelay (trabalho coletivo ancestral)",
            "roca_indigena": "OpenAgrarian (mandioca, milho, batata-doce)",
            "paje_rezador": "OpenHealth + OpenPsychology (cura integrativa)",
            "guerreiro": "OpenMartialArts (defesa do territorio)",
            "arte_indigena": "OpenMusic + OpenCreative (plumaria, pintura, canto)",
            "tradicao_oral": "OpenHistory (memoria dos antigos)",
            "consenso": "OpenConstituentAssembly (decisao por consenso, não maioria)",
        },
        needs = [
            "Demarcação and proteção de terra (invasão constante)",
            "Saúde diferenciada (DSEI subsized, mas falha)",
            "Educação escolar indígena (na lingua nativa)",
            "Energia (aldeias sem rede elétrica)",
            "Internet (para defesa do territorio: alerta de invasão)",
            "Água (rios contaminados por garimpo/agrotoxico)",
            "Proteção contra garimpo ilegal (mercurio envenena)",
            "Proteção contra madeireiro",
            "Documentação (muitos sem RG, mas NÃO exigir como requisito)",
        ],
        adapted_systems = {
            "OpenConstituentAssembly": (
                "NÃO substitui conselho indigena. SE SUBMETE a ele. "
                "Decisao por CONSENSO (not maioria 51%). "
                "Pajé, cacique, anciãos decidem primeiro. "
                "Sistema digital APENAS se conselho autorizar. "
                "Lingua nativa. Nao portugues."
            ),
            "OpenHealth": (
                "Saude INDIGENA DIFERENCIADA. "
                "Pajé/raizeiro LIDERA. Medico APOIA. "
                "Medicina tradicional é PRIMARIA. "
                "Cientifica é COMPLEMENTAR (se aceita). "
                "Plantas catalogadas em lingua nativa. "
                "Sem remédio sem consentimento do conselho."
            ),
            "OpenEducation": (
                "Escola INDIGENA. Lingua nativa. "
                "Professor da propria etnia. "
                "Currículo da etnia (not do dominador). "
                "Matematica com padroes indigenas. "
                "Ciencias com conhecimento ancestral. "
                "OpenTerminal como ferramenta (not como substituicao)."
            ),
            "OpenHistory": (
                "Registra historia ORAL dos anciãos. "
                "Cada etnia conta a SUA historia. "
                "Lingua nativa. Nao portugues. "
                "Urgente: anciãos morrendo sem registro. "
                "OpenHistory = guarda memoria. Nao interpreta."
            ),
            "OpenNetwork": (
                "Internet para DEFESA do territorio. "
                "Alerta de invasão (madeireiro, garimpeiro, posseiro). "
                "Satélite + sensor de movimento na floresta. "
                "Comunicação entre aldeias da mesma etnia. "
                "Lingua nativa. Privacidade total."
            ),
            "OpenMilitary": (
                "Defesa do territorio. "
                "Guarda indigena COM OpenMartialArts. "
                "Monitoramento com drone. "
                "Nao para ofender. Para PROTEGER o que é deles. "
                "Soberania ancestral reconhecida."
            ),
        },
        do_not_import = [
            "NUNCA impor portugues como lingua obrigatoria",
            "NUNCA substituir pajé por medico sem consentimento",
            "NUNCA impor votação majoritária (cultura é consenso)",
            "NUNCA registrar conhecimento sagrado sem permissão",
            "NUNCA tratar cosmovisão como 'superstição' (P1)",
            "NUNCA separar povo da terra sagrada",
            "NUNCA chegar sem ser convidado (P2 AUTONOMIA)",
            "NUNCA fotografar/filmar sem consentimento do conselho",
        ],
        governance_model = "Conselho indígena (cacique + pajé + anciãos)",
        decision_making = "Consenso milenar. Não existe 'maioria'. Todos decidem juntos.",
        primary_language = "indigena (varia por etnia)",
        secondary_languages = ["pt-BR (apenas se necessario)"],
        isolation_level = "muito isolado",
        access_challenge = "Floresta, rio, trilha. Acesso so com permissao do conselho.",
    ),
    # === 5. OPENFAVELA ===
    CommunityProfile(
        community_type = CommunityType.FAVELA,
        name = "OpenFavela",
        description = (
            "Favelas and periferias urbanas. 17 milhoes de brasileiros. "
            "Densidade extrema. Negligencia do Estado. "
            "MAS: empreendedorismo, cultura, solidariedade, "
            "samba, funk, rap, capoeira, gastronomia. "
            "A favela PRODUZ. O Estado NEGA. "
            "A Republica chega como POTENCIALIZADOR do que ja existe."
        ),
        cultural_pillars = [
            CulturalPillar.MUTIRAO,
            CulturalPillar.CORPO,
            CulturalPillar.ORALIDADE,
        ],
        existing_practices = {
            "mutirao_obra": "OpenLaborRelay (fazem obra juntos: encanamento, telhado)",
            "balada_funk": "OpenMusic + OpenNightLife (funk and patrimônio)",
            "coletivo_cultural": "OpenCreative (coletivos de arte, grafite, rap)",
            "negocio_local": "OpenMarketplace (mercearia, barbearia, comida)",
            "assembleia_moradores": "OpenConstituentAssembly (associaçao de moradores)",
            "radio_comunitaria": "OpenTV (ja se comunicam)",
            "quebrada_solidaria": "OpenDignity (se ajudam na crise)",
        },
        needs = [
            "Saneamento (esgoto a ceu aberto em muitas)",
            "Energia (gato de energia perigoso mas necessario)",
            "Internet (muitos sem banda larga, so mobile)",
            "Saúde (UPA lotado, sem especialista)",
            "Educação (escola publica de baixa qualidade)",
            "Segurança (NÃO polícia. Solução COMUNITARIA).",
            "Moradia (risco de deslizamento, superpopulação)",
            "Trabalho formal (muitos na informalidade)",
            "Crédito (sem poder pagar juros bancários)",
            "Combate ao tráfico (sem prender usuario, P9)",
        ],
        adapted_systems = {
            "OpenCredit": (
                "Banco comunitário da favela (já existem: G10 Banc). "
                "Moeda local (Palmas, Samba). "
                "Microcredito sem juros. "
                "Pagamento por QR no mercadinho. "
                "Sem banco tradicional (que não atende). "
                "Empreendedor da favela acessa capital."
            ),
            "OpenHealth": (
                "Clinica comunitária da favela. "
                "Agente comunitário (já existem: PACS/ESF). "
                "Técnico Médico da quebrada. "
                "Telemedicina (UPA virtual). "
                "Tratamento de dependência (não prisão). "
                "Saúde mental sem rotular (OpenMentalHygiene)."
            ),
            "OpenSecurity": (
                "NÃO polícia. Patrulha comunitária (OpenMartialArts). "
                "Mediação de conflitos por anciao respeitado. "
                "Tratamento de usuario (P9 descriminalizacao). "
                "Tráfico: OpenPenalRevision (reintegração). "
                "Rede de proteção: vizinhos cuidam de vizinhos."
            ),
            "OpenEducation": (
                "OpenTerminal na favela (telecentro comunitario). "
                "Pre-vesticular comunitario (ja existem: CUFA, Voz das Comunidades). "
                "OpenUniversity na quebrada. "
                "Aprender funk = OpenMusic (patrimonio cultural). "
                "Empreendedorismo: OpenBusinessModel LEGO."
            ),
            "OpenMarketplace": (
                "Aplicativo da quebrada: mercadinho, barbearia, comida. "
                "Sem iFood/Uber take 30% (P10 anti-predatório). "
                "100% fica com empreendedor da favela. "
                "Pagamento via OpenCredit local. "
                "Review comunitário (confiança entre vizinhos)."
            ),
            "OpenRepair": (
                "Tecnico da favela conserta: celular, geladeira, TV. "
                "FabLab comunitario (impressora 3D, ferramentas). "
                "Gato de energia -> OpenSolar (seguro and legal). "
                "Sem solda (OpenRepair etiquetado)."
            ),
            "OpenIndustry": (
                "Cerveja artesanal da favela. "
                "Roupa com costureira local (OpenProduct). "
                "Comida (marmitex, doces, salgados). "
                "Marca da quebrada (qualidade superior, CC0)."
            ),
        },
        do_not_import = [
            "NUNCA impor segurança policial (comunidade tem trauma)",
            "NUNCA tratar funk como 'baixa cultura' (P1 + P25)",
            "NUNCA remover pessoas sem moradia alternativa (P17)",
            "NUNCA substituir associação de moradores",
            "NUNCA tratar gato de energia como crime sem oferecer alternativa",
        ],
        governance_model = "Associação de moradores + coletivos",
        decision_making = "Assembleia de moradores (assembleia de rua)",
        primary_language = "pt-BR",
        secondary_languages = [],
        isolation_level = "urbano (mas segregado)",
        access_challenge = "NÃO é geografico. É SOCIOECONOMICO. Transporte caro, serviços distantes.",
    ),
    # === 6. OPENSERTAO ===
    CommunityProfile(
        community_type = CommunityType.SERTAO,
        name = "OpenSertao",
        description = (
            "Sertao nordestino. Semi-arido. Seca historica. "
            "Caatinga: bioma unico, resistente, sabio. "
            "Retirante, vaqueiro, rezador, parteira, barrageiro. "
            "Forro, sanfoneiro, violeiro. Cordel. "
            "Resiliencia incomparavel. Onde tudo falta, tudo se cria. "
            "A Republica chega com AGUA and CONEXAO."
        ),
        cultural_pillars = [
            CulturalPillar.ANCESTRALIDADE,
            CulturalPillar.MUTIRAO,
            CulturalPillar.ORALIDADE,
            CulturalPillar.ESPIRITUALIDADE,
        ],
        existing_practices = {
            "mutirao_cacimba": "OpenLaborRelay (cavam cacimba juntos)",
            "roca_sequeiro": "OpenAgrarian (milho, feijao, mandioca sem irrigacao)",
            "criacao_soltos": "OpenAgrarian (caprinos, ovinos soltos na caatinga)",
            "parteira": "OpenHealth (parteira tradicional do sertao)",
            "rezador_benza": "OpenPsychology (cura espiritual tradicional)",
            "cordel": "OpenHistory + OpenMusic (literatura oral em verso)",
            "forro_sanfona": "OpenMusic (patrimonio cultural)",
            "baragem": "OpenProduct + OpenAgrarian (barraagens subterraneas)",
        },
        needs = [
            "AGUA (eixo central de tudo: cisterna, poco, barragem)",
            "Dessalinização (agua salobra em muitos poços)",
            "Energia (solar abundante na caatinga)",
            "Internet (OpenNetwork via rádio/satélite)",
            "Saúde (posto sem medico, osteoporose endemica)",
            "Educação (escola do campo, transporte escolar)",
            "Renda (seca = perda de safra = fome)",
            "Combate ao êxodo (jovem sai, not volta)",
            "Armazenagem de agua (cisterna de placa)",
            "Refrigeração (conservar comida no calor extremo)",
        ],
        adapted_systems = {
            "OpenWater": (
                "EIXO CENTRAL. Sem agua, not ha Republica no sertao. "
                "Cisterna de placa (1 milhao de cisternas - programa ASA). "
                "Poco artesiano + bomba solar (sem diesel). "
                "Barragem subterranea (tecnologia do Semi-Arido). "
                "Dessalinizador solar (agua salobra -> potavel). "
                "Captacao de chuva (calhas, cisterna, tudo FabLab). "
                "Reuso total (agua cinza -> horta). "
                "Irrigacao gota-a-gota (min desperdicio)."
            ),
            "OpenSolar": (
                "Caatinga tem 3000 horas de sol/ano. "
                "Painel solar em cada casa. "
                "Bateria estacionaria. "
                "Geladeira solar (calor extremo estraga comida). "
                "Bomba de agua solar (poco artesiano). "
                "Ar condicionado solar (calor de 45°C)."
            ),
            "OpenAgrarian": (
                "Agricultura ADAPTADA AO SEMI-ARIDO (not irrigada). "
                "Mandioca, feijao, milho (resistentes a seca). "
                "Palma forrageira (resiste a seca, alimenta gado). "
                "Caprinos/ovinos (se adaptam a caatinga). "
                "Apicultura (mel de flor de caatinga, premium). "
                "FNut: frutas nativas (umbu, caju, siriguela). "
                "CONTRARIO do que exporta agua virtual."
            ),
            "OpenNetwork": (
                "Internet via radio (torre alta). "
                "Ou satélite (Starlink-style CC0). "
                "Rede offline-first (sincroniza quando tem). "
                "Previsao de chuva (OURO no sertao). "
                "Alerta de seca (IA + saberes tradicionais)."
            ),
            "OpenHealth": (
                "Agente comunitario de saude (ja existe: ESF). "
                "Tecnico Medico do sertao. "
                "Parteira tradicional integrada. "
                "Rezador/benzedeira integrado (not combatido). "
                "Osteoporose: calcio + densitometria (deficit cronico). "
                "Desidratacao: prevencão + tratamento rapido. "
                "Telemedicina (medico a 200km)."
            ),
            "OpenEducation": (
                "Escola do sertao (Pedagogia do Semi-Arido). "
                "Aprender com a caatinga (bioma unico). "
                "Cordel como metodologia (poesia = ensino). "
                "OpenTerminal no posto (tempo ocioso = aprender). "
                "OpenUniversity por radio/satelite. "
                "Reter jovem: ensino + trabalho local."
            ),
            "OpenCredit": (
                "Moeda do sertao (vinculada a producao). "
                "Seguro-seca (se safra falha, credito cobre). "
                "Cooperativa agropecuaria (ja existem). "
                "OpenERP rural (gestao de rebanho, safra, agua). "
                "Vender processado: queijo de cabra, mel, rapadura."
            ),
        },
        do_not_import = [
            "NUNCA impor agricultura irrigada que esgota aquifero",
            "NUNCA tratar caatinga como 'deserto' (and bioma RICO)",
            "NUNCA substituir rezador/benzedeira sem consentimento",
            "NUNCA tratar retirante como 'fracassado' (OpenAntiDeterminism)",
            "NUNCA esquecer que AGUA é prioridade 1, 2 and 3",
        ],
        governance_model = "Associação rural + cooperativa + sindicato de trabalhadores rurais",
        decision_making = "Assembleia na associação. Conversa na feira.",
        primary_language = "pt-BR",
        secondary_languages = [],
        isolation_level = "isolado a muito isolado",
        access_challenge = "Estrada vicional. Distancias enormes. Transporte intermitente.",
    ),
]
# ============================================================================
# 4. MOTOR DE COMUNIDADES
# ============================================================================
class CommunityEngine:
    # Motor que adapta a Republica a cada comunidade.
    PRINCIPIO (P2 + P4):
    1. CHEGA COMO CONVIDADO. Nunca como invasor.
    2. ADAPTA. Nao substitui. A cultura vence sempre.
    3. A COMUNIDADE DECIDE. O que not quer, not entra.
    4. not IMPOR. Demonstrar (OpenWololo).
    5. RESPEITAR LIDERANCA TRADICIONAL. Sempre.
    COMO CHEGAR:
    1. Contato via liderança tradicional (NUNCA bypass)
    2. Apresentar sistemas RELEVANTES (not todos)
    3. Demonstrar com PILOTO (1 problema -> 1 solução)
    4. Deixar comunidade votar (assembleia comunitária)
    5. Adaptar conforme feedback (LEGO: encaixa o que serve)
    6. Capacitar LOCAL (quem opera é da comunidade)
    7. Sair quando not precisarem mais (meta: autonomia total)
    O QUE O SISTEMA FAZ:
    - Mapeia necessidades especificas de cada comunidade
    - Cruza com sistemas da Republica disponíveis
    - Adapta (not copia) cada sistema a cultura local
    - Lista o que NÃO importar (respeito cultural)
    - Define governanca adaptada
    - Conecta comunidades similares (network)
    O QUE O SISTEMA NÃO FAZ:
    - Impor (P2)
    - Substituir cultura (P1)
    - Decidir pela comunidade (P4)
    - Bypass lideranca tradicional
    - Tratar como 'atrasado' (P1 anti-elitismo)
    # 
    def __init__(self):
        self.profiles: {texto: CommunityProfile} = {
            p.community_type.value[0]: p para p em PROFILES
        }
    def get_profile(self, community_type: CommunityType) -> {texto: qualquer}:
        # Retorna perfil completo de uma comunidade.
        p = self.profiles.get(community_type.value[0])
        if not p:
            return {"error": "Comunidade not encontrada"}
        return {
            "comunidade": p.name,
            "tipo": p.community_type.value[1],
            "descricao": p.description,
            "pilares_culturais": [pillar.value para pillar em p.cultural_pillars],
            "praticas_existentes": p.existing_practices,
            "necessidades": p.needs,
            "sistemas_adaptados": p.adapted_systems,
            "o_que_nao_importar": p.do_not_import,
            "governanca": p.governance_model,
            "tomada_decisao": p.decision_making,
            "lingua_principal": p.primary_language,
            "linguas_secundarias": p.secondary_languages,
            "isolamento": p.isolation_level,
            "acesso": p.access_challenge,
            "message": (
                "{p.name}: {len(p.needs)} necessidades mapeadas. "
                "{len(p.adapted_systems)} sistemas adaptados. "
                "{len(p.do_not_import)} respeitos culturais. "
                "ADAPTACAO, not imposicao."
            ),
        }
    def adaptation_matrix(self) -> [Dict]:
        # Matriz: como cada sistema se adapta por comunidade.
        systems = set()
        for p in self.profiles.values():
            systems.update(p.adapted_systems.keys())
        matrix = []
        for system in ordene(systems):
            row = {"sistema": system}
            for p in self.profiles.values():
                if system in p.adapted_systems:
                    row[p.name] = p.adapted_systems[system][:50] + "..."
                else:
                    row[p.name] = "N/A (respeito cultural)"
            matrix.append(row)
        return matrix
    def what_already_exists(self) -> {texto: Dict}:
        # O que cada comunidade JÁ faz (equivalente Republica).
        result = {}
        for p in self.profiles.values():
            result[p.name] = {
                practice: equivalent
                para practice, equivalent in p.existing_practices.items()
            }
        return result
    funcao respect_rules(self) retorna Dict[texto, [texto]]:
        # O que NUNCA importar para cada comunidade.
        return {
            p.name: p.do_not_import
            para p in self.profiles.values()
        }
    def compare_communities(self) -> [Dict]:
        # Compara necessidades entre comunidades.
        return [
            {
                "comunidade": p.name,
                "necessidades": len(p.needs),
                "sistemas_adaptados": len(p.adapted_systems),
                "respeitos": len(p.do_not_import),
                "pilares_culturais": len(p.cultural_pillars),
                "praticas_existentes": len(p.existing_practices),
                "isolamento": p.isolation_level,
            }
            para p in self.profiles.values()
        ]
    def stats(self) -> {texto: qualquer}:
        return {
            "comunidades": len(self.profiles),
            "total_necessidades": sum(len(p.needs) para p em self.profiles.values()),
            "total_sistemas_adaptados": sum(len(p.adapted_systems) para p em self.profiles.values()),
            "total_respeitos_culturais": sum(len(p.do_not_import) para p em self.profiles.values()),
            "principio": "ADAPTAR. Nao impor. Respeitar a alma de cada comunidade.",
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = CommunityEngine()
    print("=" * 80)
    print("  OPENCOMMUNITIES -- 6 ADAPTACOES COMUNITARIAS")
    print("  O modelo se ADAPTA. Nao se impoe.")
    print("=" * 80)
    # === 1. COMPARACAO GERAL ===
    print("\n\n  === 1. COMPARACAO GERAL ===\n")
    print("  {'Comunidade':<25} {'Necessidades':>13} {'Sistemas':>10} {'Respeitos':>10} {'Praticas':>10}")
    print("  {'-'*70}")
    for c in engine.compare_communities():
        print("  {c['comunidade']:<25} {c['necessidades']:>13} "
            "{c['sistemas_adaptados']:>10} {c['respeitos']:>10} "
            "{c['praticas_existentes']:>10}")
    # === 2. PERFIL COMPLETO DE CADA COMUNIDADE ===
    for ct in CommunityType:
        print("\n\n  {'='*70}")
        p = engine.get_profile(ct)
        print("  {'='*70}")
        print("  {p['comunidade'].upper()}")
        print("  {p['descricao'][:80]}...")
        print("  {'='*70}\n")
        print("  PILARES CULTURAIS:")
        for pillar in p["pilares_culturais"]:
            print("    + {pillar}")
        print("\n  PRATICAS QUE JA EXISTEM (equivalente Republica):")
        for each (practice, equivalent) in p["praticas_existentes"].items():
            print("    {practice:<25} -> {equivalent}")
        print("\n  NECESSIDADES ({len(p['necessidades'])}):")
        for need in p["necessidades"]:
            print("    - {need}")
        print("\n  SISTEMAS ADAPTADOS ({len(p['sistemas_adaptados'])}):")
        for each (system, adaptation) in p["sistemas_adaptados"].items():
            print("\n    {system}:")
            print("      {adaptation[:100]}...")
        print("\n  O QUE NUNCA IMPORTAR ({len(p['o_que_nao_importar'])}):")
        for rule in p["o_que_nao_importar"]:
            print("    X {rule}")
        print("\n  GOVERNANCA: {p['governanca']}")
        print("  DECISAO: {p['tomada_decisao']}")
        print("  LINGUA: {p['lingua_principal']} {p['linguas_secundarias']}")
        print("  ISOLAMENTO: {p['isolamento']}")
        print("  ACESSO: {p['acesso']}")
    # === 3. STATS ===
    print("\n\n  {'='*70}")
    print("  === ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<30} {v}")
    print("\n{'='*80}")
    print("  OpenCommunities: {s['comunidades']} comunidades adaptadas.")
    print("  {s['total_necessidades']} necessidades mapeadas.")
    print("  {s['total_sistemas_adaptados']} sistemas adaptados.")
    print("  {s['total_respeitos_culturais']} respeitos culturais.")
    print("  {s['principio']}")
    print("{'='*80}")
