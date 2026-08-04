# OpenDigitalDogGuide

> "O cao-guia conduz o corpo. O DigitalDogGuide protege a vida."

O cao-guia digital completo da Republica. Integra 5 sistemas num so:
audicao ambiente, visao ambiente, navegacao, seguranca domiciliar e
vinculo emocional.

## Arquivo
`core/open_digital_dog_guide.py` (~1020 linhas)

## O que ele e (e nao e)

O cao-guia biologico e INSUBSTITUIVEL na conducao fisica. Este modulo
NAO o substitui. Ele e o SEGUNDO cao -- o complemento que:

- Ouve 24/7 (o cao biologico dorme)
- Le textos/placas/semaforos (o cao nao le)
- Identifica onibus/dinheiro (o cao nao identifica)
- Calcula rotas acessiveis (o cao nao calcula)
- Faz companhia e acolhe (como o cao faz)

## Os 5 Sistemas Integrados

| Sistema | Fonte | O que faz |
|---------|-------|-----------|
| Audicao | OpenAmbientSoundAI | Ouve campainha, sirene, vidro, choro |
| Visao | OpenDigitalGuide | Le placas, semaforos, descreve cenas |
| Navegacao | OpenDigitalGuide | Rotas + deteccao de perigo a frente |
| Seguranca | Sensores IoT casa | Gas, fumaca, intrusao, enchente |
| Vinculo | Motor de personalidade | Cumprimentos, consolo, companhia |

## Personalidade do Cao

O cao digital tem personalidade configuravel:

- **Nome**: o usuario escolhe ("Thor", "Rex", "Luna"...)
- **Voz**: sempre Iara (humana, calorosa) para conversa
- **Tom**: caloroso, formal, descontraido
- **Humor**: reage ao estado emocional do usuario
- **Vinculo**: evolui com o tempo (Desconhecido -> Guardiao)

### Evolucao do Vinculo

| Dias juntos | Status |
|-------------|--------|
| 0 | Desconhecido (aprendendo) |
| 1+ | Conhecido |
| 8+ | Confianca mutua |
| 38+ | Parceiro diario |
| 98+ | Guardiao irmao (vinculo profundo) |

## Tipos de Alerta (20)

| Categoria | Alertas |
|-----------|---------|
| Ambiente | CAMPAINHA, BATIDA_PORTA, TELEFONE |
| Emergencia | INCENDIO, GAS, INVASAO, ENCHENTE |
| Mobilidade | PERIGO_ESCADA, PERIGO_BURACO, SEMAFORO, TRANSITO |
| Rotina | REMEDIO, COMPROMISSO, REFEICAO, HIDRATACAO |
| Social | VISITA_CHEGOU, PESSOA_APROXIMA, SOZINHO_MUITO_TEMPO |
| Leitura | LOJA_FECHADA, ONIBUS_CHEGANDO |

## Niveis de Urgencia (6)

CARINHA -> INFORMATIVO -> ATENCAO -> IMPORTANTE -> URGENTE -> EMERGENCIA

Emergencia dispara TODOS os canais + escalonamento para contato.

## Escalonamento de Emergencia

Se um alerta URGENTE+ nao for confirmado em 90s:
1. Marca evento como ESCALADO
2. Avisa contato de emergencia (esposa, vizinho, etc.)
3. Continua alarmando ate confirmacao

## Interacao Emocional

O cao detecta/reage a 7 humores:

| Humor | Como o cao responde |
|-------|---------------------|
| Triste | "Percebo que nao esta bem. Quer conversar?" |
| Ansioso | "Respira. Ta tudo bem. Eu estou vigiando." |
| Cansado | "Voce parece cansado. Que tal uma pausa?" |
| Dor | "Tomou o remedio? Se forte, ligamos para alguem." |
| Irritado | "Se quiser silencio, eu calo. So digo se algo acontecer." |
| Feliz | Responde normal, mantem o animo |
| Neutro | Responde normal |

## Enums (9)

- `EstadoVigilancia` (6): ATENTO, PATRULHA, DESCANSO, BRINCADEIRA, TREINAMENTO, DESLIGADO
- `TipoSentido` (6): AUDICAO, VISAO, OLFATO_DIGITAL, TATO_DIGITAL, ORIENTACAO, CONEXAO
- `TipoAlertaCao` (20): ver tabela acima
- `NivelUrgenciaCao` (6): CARINHA -> EMERGENCIA
- `HumorUsuario` (7): FELIZ, NEUTRO, CANSADO, TRISTE, ANSIOSO, IRRITADO, DOR
- `TipoInteracao` (9): CUMPRIMENTO, ALERTA, LEMBRETE, DESCRICAO, NAVEGACAO, CONSOLO, etc.
- `StatusVinculo` (5): DESCONHECIDO -> GUARDIAO
- `FonteEvento` (9): MICROFONE, CAMERA, SENSOR_GAS, SENSOR_TEMP, GPS, AGENDA, RELOGIO, USUARIO, API

## Arquitetura

```
DigitalDogGuideEngine (orquestrador)
├── PersonalidadeCao      Vinculo, humor, cumprimentos, consolo
├── AudicaoCao            (delegate OpenAmbientSoundAI)
├── VisaoCao              (delegate OpenDigitalGuide)
├── RotinaCao             Lembretes: remedio, refeicao, hidratacao
└── SegurancaCao          Sensores IoT: gas, fumaca, intrusao, enchente
```

## Custo Comparativo

| Item | Cao biologico | DigitalDogGuide |
|------|---------------|-----------------|
| Custo inicial | R$ 30.000-60.000 | R$ 0 (software) + hardware |
| Manutencao anual | R$ 3.000-5.000 (racao, vet) | R$ 0 (eletricidade) |
| Disponibilidade | ~16h/dia (dorme) | 24/7 |
| Vida util | 10-14 anos | Ilimitado (atualiza) |
| Escala | 1 cego por cao | Ilimitado (1 software) |

## Constituicao

- P1: Todos tem direito a seguranca e autonomia
- P2: Autonomia do corpo (vigiar a propria casa)
- P8: IA como instrumento (o cao acolhe, nao substitui companhia humana)

## Etica

- NAO espiona: processa local, descarta dados
- NAO substitui companhia humana: AMPLIA autonomia
- NAO identifica pessoas por rosto sem consentimento
- TEM DESLIGAR: usuario manda, sempre
- Tudo offline, tudo local, tudo privado

## Integracao

- **OpenAmbientSoundAI**: audicao ambiente
- **OpenDigitalGuide**: visao + navegacao
- **Iara**: voz humana (calorosa) para toda conversa
- **Sensores IoT casa**: gas, fumaca, porta, agua (MQTT/Zigbee)

## Categoria
PRODUCTIVITY / ACCESSIBILITY / SAFETY
