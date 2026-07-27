# OpenRepublic -- Politica de Poluicao Sonora

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/noise_policy.py`

**Descricao:** =============================================
"Som e vida. Ruido e violencia invisivel."
Na Republica, som nao e commodity de quem paga mais.
Som e bem comum. O ar que vibra nos ouvidos de TODOS
pertence a TODOS.
Este modulo define:
1. O que e som legitimo vs poluicao
2. Limites por zona e horario
3. Quem decide (democracia local)
4. Como medir (qualquer smartphone/terminal burro)
5. Como resolver (comunidade, nao policia)
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenRepublic -- Politica de Poluicao Sonora
=============================================

"Som e vida. Ruido e violencia invisivel."

Na Republica, som nao e commodity de quem paga mais.
Som e bem comum. O ar que vibra nos ouvidos de TODOS
pertence a TODOS.

Este modulo define:
1. O que e som legitimo vs poluicao
2. Limites por zona e horario
3. Quem decide (democracia local)
4. Como medir (qualquer smartphone/terminal burro)
5. Como resolver (comunidade, nao policia)

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa math
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Tuple de typing
// importa Enum de enum
// importa defaultdict de collections


classe SoundZone herda de Enum:
    // Zonas sonoras da Republica.
    SILENCE = "silencio"  // hospitais, bibliotecas, dormitorios
    RESIDENTIAL = "residencial"  // moradia (precisa de sossego)
    COMMUNITY = "comunitario"  // praca, mercado (som moderado)
    ACTIVITY = "atividade"  // fablab, cozinha (som de trabalho)
    CELEBRATION = "celebracao"  // festa, musica (som alto permitido)
    NATURE = "natureza"  // floresta, parque (so som natural)


classe TimeWindow herda de Enum:
    // Janelas de tempo com regras diferentes.
    NIGHT_SILENCE = "silencio_noturno"  // 22h-06h (maxima protecao)
    DAWN = "amanhecer"  // 06h-08h (transicao)
    DAY = "dia"  // 08h-18h (atividade)
    EVENING = "anoitecer"  // 18h-22h (diminuir)


classe NoiseSource herda de Enum:
    // Fontes de ruido.
    MUSIC = "musica"
    CONSTRUCTION = "construcao"
    MACHINERY = "maquinario"
    VEHICLES = "veiculos"
    VOICES = "vozes"
    ANIMALS = "animais"
    CHILDREN = "criancas"  // NUNCA restringir
    NATURE_SOUNDS = "natureza"  // NUNCA restringir
    EMERGENCY = "emergencia"  // sirenas, alarmes (sempre permitido)
    INDUSTRIAL = "industrial"


classe NoiseSeverity herda de Enum:
    NONE = 0
    LOW = 1 // incomodo leve
    MODERATE = 2 // incomodo claro
    HIGH = 3 // dano auditivo com exposicao
    CRITICAL = 4 // dano imediato


// Limites em dB(A) por zona + horario
// Baseado em OMS: >70dB = dano; >55dB em areas residenciais = incomodo
seja NOISE_LIMITS: Dict[(SoundZone, TimeWindow), inteiro] = {
    // dB(A) maximo permitido
    (SoundZone.SILENCE, TimeWindow.NIGHT_SILENCE): 35,
    (SoundZone.SILENCE, TimeWindow.DAWN): 40,
    (SoundZone.SILENCE, TimeWindow.DAY): 45,
    (SoundZone.SILENCE, TimeWindow.EVENING): 40,

    (SoundZone.RESIDENTIAL, TimeWindow.NIGHT_SILENCE): 45,
    (SoundZone.RESIDENTIAL, TimeWindow.DAWN): 50,
    (SoundZone.RESIDENTIAL, TimeWindow.DAY): 60,
    (SoundZone.RESIDENTIAL, TimeWindow.EVENING): 55,

    (SoundZone.COMMUNITY, TimeWindow.NIGHT_SILENCE): 50,
    (SoundZone.COMMUNITY, TimeWindow.DAWN): 55,
    (SoundZone.COMMUNITY, TimeWindow.DAY): 70,
    (SoundZone.COMMUNITY, TimeWindow.EVENING): 65,

    (SoundZone.ACTIVITY, TimeWindow.NIGHT_SILENCE): 55,
    (SoundZone.ACTIVITY, TimeWindow.DAWN): 65,
    (SoundZone.ACTIVITY, TimeWindow.DAY): 80,
    (SoundZone.ACTIVITY, TimeWindow.EVENING): 70,

    (SoundZone.CELEBRATION, TimeWindow.NIGHT_SILENCE): 65,
    (SoundZone.CELEBRATION, TimeWindow.DAWN): 75,
    (SoundZone.CELEBRATION, TimeWindow.DAY): 90,
    (SoundZone.CELEBRATION, TimeWindow.EVENING): 85,

    (SoundZone.NATURE, TimeWindow.NIGHT_SILENCE): 35,
    (SoundZone.NATURE, TimeWindow.DAWN): 40,
    (SoundZone.NATURE, TimeWindow.DAY): 45,
    (SoundZone.NATURE, TimeWindow.EVENING): 40,
}

// Fontes que NUNCA sao restritas
ALWAYS_ALLOWED = {
    NoiseSource.CHILDREN,
    NoiseSource.NATURE_SOUNDS,
    NoiseSource.EMERGENCY,
}


// decorador: @dataclass
classe NoiseEvent:
    // Um evento de ruido detectado.
    event_id: texto
    zone: SoundZone
    time_window: TimeWindow
    measured_db: flutuante
    source: NoiseSource
    seja duration_min: flutuante = 0
    seja location: texto = ""
    seja reporter: texto = ""
    seja timestamp: flutuante = 0
    seja limit_db: inteiro = 0
    seja exceeded_by: flutuante = 0
    seja severity: NoiseSeverity = NoiseSeverity.NONE


classe NoiseMonitor:
    // Sistema de monitoramento de poluicao sonora.

    COMO MEDIR:
    Qualquer smartphone/terminal burro tem microfone.
    App simples mede dB(A) em tempo real.
    Nao precisa de equipamento caro.

    COMO RESOLVER:
    1. Ruido detectado acima do limite -> Jarvis avisa a FONTE
    2. Fonte nao para em 15min -> Jarvis avisa VIZINHANCA
    3. Comunidade resolve (dialogo, nao policia)
    4. Se recorrente (3+ vezes) -> votacao local sobre restricao
    5. Emergencias/criancas/natureza = sempre permitido

    O QUE nao e POLUICAO:
    - Crianca chorando (NUNCA)
    - Pássaros (NUNCA)
    - Musica em zona de celebracao (PERMITIDO)
    - Sirene de emergencia (SEMPRE)
    - Vozes em conversa normal
    // 

    funcao __init__(self):
        self.events: [NoiseEvent] = []
        self.recurring_sources: {texto: inteiro} = defaultdict(inteiro)
        self._counter = 0

    funcao measure(self, db_level: flutuante, zone: SoundZone,
                time_window: TimeWindow,
                source: NoiseSource,
                seja location: texto = "",
                seja duration_min: flutuante = 0) -> NoiseEvent:
        // Registrar medicao de ruido.
        self._counter += 1
        eid = "NOISE-{self._counter:05d}"

        // Crianca, natureza, emergencia = sempre ok
        se source in ALWAYS_ALLOWED entao:
            retorne NoiseEvent(
                event_id = eid, zone=zone, time_window=time_window,
                measured_db = db_level, source=source,
                duration_min = duration_min, location=location,
                severity = NoiseSeverity.NONE, limit_db=999)

        limit = NOISE_LIMITS.get((zone, time_window), 60)
        exceeded = maximo(0, db_level - limit)

        se exceeded == 0 entao:
            severity = NoiseSeverity.NONE
        senao se exceeded <= 5 entao:
            severity = NoiseSeverity.LOW
        senao se exceeded <= 15 entao:
            severity = NoiseSeverity.MODERATE
        senao se exceeded <= 25 entao:
            severity = NoiseSeverity.HIGH
        senao:
            severity = NoiseSeverity.CRITICAL

        event = NoiseEvent(
            event_id = eid, zone=zone, time_window=time_window,
            measured_db = db_level, source=source,
            duration_min = duration_min, location=location,
            limit_db = limit, exceeded_by=exceeded, severity=severity)
        self.events.append(event)

        // Rastrear fontes recorrentes
        se severity.value >= NoiseSeverity.MODERATE.value entao:
            key = "{location}:{source.value}"
            self.recurring_sources[key] += 1

        retorne event

    funcao resolve(self, event: NoiseEvent) -> {texto: qualquer}:
        // Resolver um evento de ruido.
        se event.source in ALWAYS_ALLOWED entao:
            retorne {
                "action": "nenhuma",
                "reason": "{event.source.value} e sempre permitido",
            }

        se event.severity == NoiseSeverity.NONE entao:
            retorne {"action": "nenhuma", "reason": "dentro do limite"}

        se event.severity == NoiseSeverity.LOW entao:
            retorne {"action": "avisar_fonte",
                    "reason": "Ruido de {event.measured_db:.0f}dB "
                             "(limite {event.limit_db}dB). "
                             "Jarvis avisa a fonte. Reduzir em 15min."}

        se event.severity == NoiseSeverity.MODERATE entao:
            retorne {"action": "avisar_vizinhos",
                    "reason": "Excedeu em {event.exceeded_by:.0f}dB. "
                             "Comunidade notificada. Dialogo local."}

        se event.severity == NoiseSeverity.HIGH entao:
            key = "{event.location}:{event.source.value}"
            count = self.recurring_sources.get(key, 0)
            se count >= 3 entao:
                retorne {"action": "votacao_local",
                        "reason": "Ruido recorrente ({count}x). "
                                 "Comunidade vota sobre restricao."}
            retorne {"action": "mediacao_comunitaria",
                    "reason": "Ruido alto (+{event.exceeded_by:.0f}dB). "
                             "Mediador comunitario acionado."}

        // CRITICAL: dano auditivo
        retorne {"action": "intervencao_imediata",
                "reason": "CRITICO: {event.measured_db:.0f}dB. "
                         "Dano auditivo. Parar imediatamente. "
                         "Comunidade + saude acionadas."}

    funcao zone_report(self, zone: SoundZone) -> {texto: qualquer}:
        events = [e para e em self.events if e.zone == zone]
        violations = [e para e em events if e.severity != NoiseSeverity.NONE]
        retorne {
            "zone": zone.value,
            "total_events": tamanho(events),
            "violations": tamanho(violations),
            "worst": maximo((e.measured_db para e em events), default=0),
            "limit_day": NOISE_LIMITS.get((zone, TimeWindow.DAY), "?"),
            "limit_night": NOISE_LIMITS.get((zone, TimeWindow.NIGHT_SILENCE), "?"),
        }


// ============================================================================
// Main
// ============================================================================

se __name__ == "__main__" entao:
    imprima("=" * 75)
    imprima("  OPENREPUBLIC -- POLITICA DE POLUICAO SONORA")
    imprima("  'Som e vida. Ruido e violencia invisivel.'")
    imprima("=" * 75)

    monitor = NoiseMonitor()

    // === Limits Table ===
    imprima("\n\n  === LIMITES DE RUIDO dB(A) ===\n")
    imprima("  {'Zona':<15} {'Noite':>6} {'Amanh.':>7} {'Dia':>6} {'Anoit.':>7}")
    imprima("  {'-'*45}")
    para cada zone em SoundZone:
        night = NOISE_LIMITS.get((zone, TimeWindow.NIGHT_SILENCE), "-")
        dawn = NOISE_LIMITS.get((zone, TimeWindow.DAWN), "-")
        day = NOISE_LIMITS.get((zone, TimeWindow.DAY), "-")
        eve = NOISE_LIMITS.get((zone, TimeWindow.EVENING), "-")
        imprima("  {zone.value:<15} {night:>6} {dawn:>7} {day:>6} {eve:>7}")

    imprima("\n  NUNCA RESTRINGIDOS: criancas, natureza, emergencia")

    // === Simulations ===
    imprima("\n\n  === SIMULACOES ===\n")

    scenarios = [
        ("Musica alta 22h residencial", 75, SoundZone.RESIDENTIAL,
         TimeWindow.NIGHT_SILENCE, NoiseSource.MUSIC, "Casa A"),
        ("Construcao 14h atividade", 82, SoundZone.ACTIVITY,
         TimeWindow.DAY, NoiseSource.CONSTRUCTION, "FabLab"),
        ("Crianca chorando 23h", 70, SoundZone.RESIDENTIAL,
         TimeWindow.NIGHT_SILENCE, NoiseSource.CHILDREN, "Casa B"),
        ("Maquinario 03h", 68, SoundZone.RESIDENTIAL,
         TimeWindow.NIGHT_SILENCE, NoiseSource.MACHINERY, "Oficina"),
        ("Festa 20h celebracao", 88, SoundZone.CELEBRATION,
         TimeWindow.EVENING, NoiseSource.MUSIC, "Praca"),
        ("Passaro 05h", 55, SoundZone.RESIDENTIAL,
         TimeWindow.NIGHT_SILENCE, NoiseSource.NATURE_SOUNDS, "Parque"),
        ("Sirene emergencia 02h", 95, SoundZone.RESIDENTIAL,
         TimeWindow.NIGHT_SILENCE, NoiseSource.EMERGENCY, "Clinica"),
    ]

    para label, db, zone, tw, source, loc in scenarios:
        event = monitor.measure(db, zone, tw, source, loc)
        resolution = monitor.resolve(event)
        flag = event.severity == NoiseSeverity.NONE ? "" : " [{event.severity.name}]"
        imprima("\n  {label}:")
        imprima("    Medido: {event.measured_db:.0f}dB | Limite: {event.limit_db}dB "
              "| Excesso: +{event.exceeded_by:.0f}dB{flag}")
        imprima("    Acao: {resolution['action']}")
        imprima("    {resolution['reason']}")

    // === Zone Report ===
    imprima("\n\n  === RELATORIO POR ZONA ===\n")
    para cada zone em SoundZone:
        rep = monitor.zone_report(zone)
        imprima("  {rep['zone']:<15} eventos={rep['total_events']} "
              "violacoes={rep['violations']} "
              "pior={rep['worst']:.0f}dB "
              "(limite dia={rep['limit_day']} noite={rep['limit_night']})")

    imprima("\n\n{'='*75}")
    imprima("  PRINCIPIOS")
    imprima("{'='*75}")
    imprima("""
  CAPITALISMO OPENREPUBLIC
  ---------------------------------- ----------------------------------
  Quem faz ruido e quem tem dinheiro Ruido e bem comum -- todos decidem
  Multa ($) = punicao de pobre Mediacao comunitaria (nao policia)
  Lei federal uniforme Cada comunidade vota seus limites
  Ruido industrial "normal"           Ruido que fere ouvido = crime
  Crianca chorando = "incomodo"       Crianca NUNCA e poluicao
  Vizinho briga com vizinho Jarvis mede, comunidade resolve
  Denuncia anonima (medo) Transparencia: quem reportou e publico

  LIMITES (baseados em OMS):
    Silencio (hospital/biblio): 35-45 dB
    Residencial: 45-60 dB
    Comunitario: 50-70 dB
    Atividade (FabLab): 55-80 dB
    Celebracao (festa): 65-90 dB
    Natureza: 35-45 dB

    >70 dB = dano auditivo com exposicao prolongada
    >85 dB = dano com 8h
    >120 dB = dor imediata

  COMO RESOLVER (escada de intervencao):
    1. Ruido detectado -> Jarvis avisa a FONTE (15min para reduzir)
    2. Fonte nao para -> Jarvis avisa VIZINHANCA
    3. Dialogo comunitario (mediador, nao policia)
    4. Recorrente (3+x) -> VOTACAO local sobre restricao
    5. Critico (>120dB) -> intervencao imediata + OpenHealth

  O QUE nao e POLUICAO (SEMPRE PERMITIDO):
    Crianca chorando/brincando/risada
    Passaros, vento, chuva, animais
    Sirene de emergencia
    Conversa em volume normal

  "Som e vida. Ruido imposto e violencia invisivel.
   Cada comunidade define seu silencio.
   Cada pessoa tem direito ao sossego.
   Mas criancas sempre podem chorar.
   e passaros sempre podem cantar."
// )

```
