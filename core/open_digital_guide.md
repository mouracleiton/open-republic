# OpenDigitalGuide

> "O cao-guia conduz. O OpenDigitalGuide EXPLICA."

Guia digital para cegos. Responde as 3 perguntas fundamentais:
**Onde estou? / Como chego la? / O que tem aqui?**

## Arquivo
`core/open_digital_guide.py` (~990 linhas)

## Os 3 Modos

| Modo | Pergunta | O que faz |
|------|----------|-----------|
| ORIENTACAO | "Onde estou?" | GPS + bussola + POIs proximos |
| NAVEGACAO | "Como chego la?" | Rota a pe passo-a-passo + deteccao de perigo |
| LEITURA | "O que tem aqui?" | Camera + OCR + visao computacional |

## Comandos por Voz

| Usuario diz... | O que o Guia faz |
|----------------|------------------|
| "Onde estou" | Localiza GPS + descreve arredores |
| "O que tem aqui" | Le cena + texto da camera |
| "Semaforo" | Le cor do semaforo para pedestre |
| "Onibus" | Identifica linha do onibus chegando |
| "Dinheiro" | Identifica valor da nota |
| "Como chego em X" | Calcula rota acessivel |
| "Proximo passo" | Avanca instrucao de navegacao |
| "Repete" | Repete ultima fala |
| "Pare" / "Silencio" | Pausa o guia |

## Arquitetura

```
DigitalGuideEngine (orquestrador)
├── OrientacaoEngine     GPS + POIs + bussola falada
├── NavegacaoEngine      Rotas + deteccao de perigo a frente
└── LeituraVisualEngine  OCR + cena + semaforo + onibus + dinheiro
```

## Enums (7)

- `ModoOperacao` (4): ORIENTACAO, NAVEGACAO, LEITURA, PAUSADO
- `TipoOrientacao` (5): LOCALIZACAO, DIRECAO, REFERENCIA, TERRENO, AMBIENTE
- `TipoInstrucao` (13): SEGUIR_EM_FRENTE, VIRAR_*, ESCADA_*, ATRAVESSAR, CHEGADA, etc.
- `TipoPerigo` (11): ESCADA, BURACO, OBRA, CARRO, POSTE, AGUA, VIDRO, ANIMAL, PESSOA, SEMAFORO, TRANSITO
- `TipoLeituraVisual` (10): TEXTO, CENA, SEMAFORO, ONIBUS, METRO, DINHEIRO, COR, PRODUTO, PORTA, FACE
- `NivelConfiancaVisual` (4): ALTA, MEDIA, BAIXA, FALHOU
- `CanalSaida` (6): VOZ_IARA, HAPTICO_DIRECAO, HAPTICO_RITMO, BRLTTY, ALTO_CONTRASTE, LOG

## Integracao

- **Iara**: voz humana para todas as falas (nunca robotica para conversa)
- **OpenAmbientSoundAI**: o cao ouve, o Guia ve (complementar)
- **OpenDigitalDogGuide**: o DogGuide usa este modulo para visao/navegacao
- **OSM/OSRM**: no mundo real, rotas vem de OpenStreetMap + OSRM API
- **TensorFlow Lite**: no mundo real, visao usa MobileNet/EfficientDet + Tesseract OCR

## Hardware Necessario

| Sensor | Funcao | Alternativa |
|--------|--------|-------------|
| GPS | Localizacao | API Android/Location |
| Camera | Leitura visual | Camera do smartphone |
| Bussola (IMU) | Direcao | Sensor magnetico |
| Acelerometro | Deteccao de passo | Contagem por velocidade |
| Fone estereo | Audio espacial | Fone mono (perde direcionalidade) |

## Custo Estimado (hardware COTS)

- Smartphone Android (ja tem tudo): R$ 0 (usar o que tem)
- Oculos com camera + fone (opcional): R$ 200-800
- Display braille (surdo-cego): R$ 3.000-15.000

## Constituicao

- P1: Todos tem direito a orientacao e mobilidade
- P2: Autonomia do corpo (ir e vir sem depender de terceiros)
- P6: Acesso universal ao conhecimento (ler placas, cardapios)
- P8: IA como instrumento (descreve o mundo, nao decide por voce)

## Etica

- Camera processa frames sob demanda, NAO grava continuamente
- NAO identifica pessoas por rosto sem consentimento
- Tudo offline/local (NPU/GPU do dispositivo)
- Desligavel: "Iara, parar de ver."

## Categoria
PRODUCTIVITY / ACCESSIBILITY
