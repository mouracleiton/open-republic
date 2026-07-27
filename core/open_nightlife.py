#!/usr/bin/env python3
"""
OpenNightLife + OpenEstablishmentUpgrade -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenNightLife + OpenEstablishmentUpgrade
==========================================
"De dia a Republica trabalha. De noite a Republica CELEBRA.
Todo estabelecimento desatualizado se moderniza. Custo min."
PARTE 1 -- OPENNIGHTLIFE:
Noite comunitaria, segura, inclusiva. Sem elitismo.
Eventos, cultura, jogos, comida, musica -- tudo sobre OpenNetwork.
PARTE 2 -- OPENESTABLISHMENTUPGRADE:
Clinicas, consultorios and restaurantes desatualizados sao modernizados.
Custo MINIMO porque usa OpenHardware, FabLab and trabalho base 1.0.
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa random
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional, Tuple de typing
# importa Enum de enum
# importa defaultdict, Counter de collections
# importa datetime de datetime
# ============================================================================
# 1. NIGHTLIFE
# ============================================================================
class NightEventType(Enum):
    PARTY = "festa"  // festa comunitaria
    LIVE_MUSIC = "musica_ao_vivo"  // show
    CULTURAL = "cultural"  // teatro, cinema, poesia
    GAMES = "jogos"  // torneio a noite
    FOOD = "comida"  // jantar comunitario
    DANCE = "danca"  // baile, forro, samba
    EDUCATIONAL = "educativo"  // palestra, workshop noturno
    SOCIAL = "social"  // encontro, conversa
    SPORTS = "esporte"  // futebol noturno, capoeira
    OPEN_TV = "open_tv"  // transmissao ao vivo
class NightVenue(Enum):
    PRAÇA = "praca"  // espaco publico
    CENTRO_COMUNITARIO = "centro_comunitario"
    RESTAURANTE = "restaurante"
    ESPACO_CULTURAL = "espaco_cultural"
    FABLAB = "fablab"  // hackathon a noite
    ESCOLA = "escola"  // aula noturna
    PARQUE = "parque"  // ao ar livre
    PRAIA = "praia"
    GINASIO = "ginasio"  // esporte
    RUA = "rua"  // bloco, marchinha
class NightSafety(Enum):
    # Nivel de seguranca do evento noturno.
    GUARDED = "guardado"  // OpenMartialArts voluntarios presentes
    LIT = "iluminado"  // iluminacao OpenEnergy solar
    SOBER = "sem_alcool"  // evento sem alcool (default)
    FAMILY = "familiar"  // criancas bem-vindas
    ADULT_ONLY = "adulto"  // 18+ (NUNCA por exclusao -- por conteudo)
# decorador: @dataclass
class NightEvent:
    # Um evento noturno da Republica.
    event_id: texto
    name: texto
    event_type: NightEventType
    venue: NightVenue
    start_hour: inteiro // 18-23
    end_hour: inteiro // ate 05 (not recomendado)
    organizer: str = ""  // quem organiza (rotativo)
    max_attendees: int = 200
    current_attendees: int = 0
    description: str = ""
    has_food: bool = True
    has_music: bool = True
    has_drinks: bool = True // agua/cha/suco (not alcool)
    safety: [NightSafety] = field(default_factory=list)
    family_friendly: bool = True
    cost: float = 0.0 // SEMPRE ZERO
    alcohol_allowed: bool = False
    broadcast_on_tv: bool = False // transmitido na OpenTV
    # decorador: @property
    def is_late_night(self) -> bool:
        return self.end_hour > 1 or self.end_hour < 6
# decorador: @dataclass
class NightZone:
    # Uma zona noturna da Republica.
    zone_id: texto
    name: texto
    region: texto
    venues: [NightVenue] = field(default_factory=list)
    active_events: [NightEvent] = field(default_factory=list)
    illumination_level: float = 0.9 // iluminacao OpenEnergy
    patrol_volunteers: int = 0 // OpenMartialArts voluntarios
    open_terminals: int = 0 // OpenTerminal disponiveis a noite
    has_food: bool = True
    has_transport: bool = True // OpenMobility carona a noite
class NightLifeEngine:
    # Sistema de vida noturna da Republica.
    PRINCIPIOS DA NOITE:
    1. INCLUSIVA -- todo mundo entra. Sem fila seletiva. Sem "VIP".
    2. SEGURA -- OpenMartialArts voluntarios patrulham. Iluminacao total.
    3. SEM ALCOOL OBRIGATORIO -- agua/cha/suco gratis sempre.
    4. SEM DINHEIRO -- custo ZERO. Festa and direito.
    5. ROTATIVA -- eventos organizados por diferentes pessoas.
    6. CULTURAL -- valoriza musica/danca/arte local.
    7. DESCANSO -- eventos terminam cedo (recomendacao P2 sono).
    8. SOBRE OPENNETWORK -- tudo transmitido, coordenado, acessivel.
    # 
    def __init__(self):
        self.events: {texto: NightEvent} = {}
        self.zones: {texto: NightZone} = {}
        self.organizers_rota: [texto] = []
        self.total_events_held: inteiro = 0
        self.total_attendees_all_time: inteiro = 0
        # Politica
        self.cover_charge: logico = False // NUNCA
        self.vip_section: logico = False // NUNCA
        self.selective_door: logico = False // NUNCA
        self.alcohol_mandatory: logico = False // NUNCA
        self.ads: logico = False // NUNCA
    funcao create_event(self, name: texto, etype: NightEventType,
                    venue: NightVenue, start: inteiro, end: inteiro,
                    organizer: str = "",
                    max_att: int = 200,
                    family: bool = True,
                    broadcast: bool = False) -> {texto: qualquer}:
        # Cria evento noturno.
        eid = hashlib.md5("{name}{datetime.now()}".encode()).hexdigest()[:8]
        event = NightEvent(
            event_id = eid, name=name, event_type=etype, venue=venue,
            start_hour = start, end_hour=end, organizer=organizer,
            max_attendees = max_att, family_friendly=family,
            broadcast_on_tv = broadcast,
            safety = [NightSafety.GUARDED, NightSafety.LIT,
                    NightSafety.SOBER] if family else
                [NightSafety.GUARDED, NightSafety.LIT],
        )
        self.events[eid] = event
        return {
            "created": True,
            "event": name,
            "type": etype.value,
            "venue": venue.value,
            "time": "{start:02d}h-{end:02d}h",
            "cost": "ZERO",
            "family": family,
            "broadcast": broadcast,
            "safety": [s.value para s em event.safety],
            "organizer": organizer  or  "rotativo",
            "message": (
                "Evento criado: {name}. Entrada FREE. "
                "Agua/cha/suco gratis. OpenMartialArts na seguranca. "
                "Todo mundo bem-vindo."
            ),
        }
    def nightly_schedule(self, day: texto = "sexta") -> [Dict]:
        # Grade de eventos noturnos para um dia.
        schedule = []
        for event in self.events.values():
            schedule.append({
                "name": event.name,
                "type": event.event_type.value,
                "venue": event.venue.value,
                "time": "{event.start_hour:02d}h-{event.end_hour:02d}h",
                "attendees": "{event.current_attendees}/{event.max_attendees}",
                "cost": event.cost,
                "family": event.family_friendly,
                "on_tv": event.broadcast_on_tv,
            })
        return sorted(schedule, key=(x) -> x["time"])
    def night_safety_report(self) -> {texto: qualquer}:
        return {
            "total_events": len(self.events),
            "events_with_martial_arts": sum(
                1 para and em self.events.values()
                if NightSafety.GUARDED in and.safety),
            "events_lit": sum(
                1 para and em self.events.values()
                if NightSafety.LIT in and.safety),
            "events_family_friendly": sum(
                1 para and em self.events.values() if and.family_friendly),
            "events_no_alcohol": sum(
                1 para and em self.events.values() if not and.alcohol_allowed),
            "illumination": "OpenEnergy solar (autossuficiente)",
            "patrol": "OpenMartialArts voluntarios (cinto verde+)",
            "transport": "OpenMobility carona 24h",
        }
# ============================================================================
# 2. ESTABLISHMENT UPGRADE (modernizacao com custo minimo)
# ============================================================================
class EstablishmentStatus(Enum):
    OUTDATED = "desatualizado"  // precisa modernizar
    PARTIAL = "parcial"  // alguns equipamentos
    MODERNIZED = "modernizado"  // atualizado
    CUTTING_EDGE = "avancado"  // acima do padrao
class UpgradeType(Enum):
    DENTAL_EQUIPMENT = "equipamento_dental"  // implante 3D, laser
    MEDICAL_EQUIPMENT = "equipamento_medico"  // IA diagnostico, ultrassom
    LASER_MACHINE = "maquina_laser"  // LASIK, dermatologia
    PRINTER_3D = "impressora_3d"  // implantes custom
    AI_DIAGNOSTIC = "ia_diagnostico"  // OpenHealth AI
    TRAINING = "treinamento"  // OpenEducation staff
    PROTOCOL_UPDATE = "protocolo"  // novos protocolos
# decorador: @dataclass
class Establishment:
    # Um estabelecimento (clinica, consultorio, restaurante).
    est_id: texto
    name: texto
    type: texto                    // "consultorio_dental", "clinica", "restaurante"
    location: texto
    status: EstablishmentStatus = EstablishmentStatus.OUTDATED
    current_equipment: [texto] = field(default_factory=list)
    needed_upgrades: [UpgradeType] = field(default_factory=list)
    staff_count: int = 3
    patients_per_day: int = 50
    # Custo da modernizacao (em TRABALHO, nao dinheiro)
    upgrade_work_hours: float = 0.0
    upgrade_credit_cost: float = 0.0
    upgrade_status: str = "pendente"  // pendente, em_andamento, concluido
class EstablishmentUpgrader:
    # Moderniza estabelecimentos desatualizados com CUSTO MINIMO.
    COMO O CUSTO and MINIMO:
    1. Equipamentos sao OpenHardware (FabLab fabrica)
    2. IA diagnostico and OpenHealth (software livre)
    3. Treinamento and OpenEducation (gratis)
    4. Materia-prima and bem comum
    5. Trabalho de upgrade and base 1.0 (sem honorario)
    6. O "custo" and trabalho + materiais, not dinheiro
    EXEMPLO:
    Consultorio dental desatualizado precisa de:
    - Maquina de implante 3D (OpenHardware) -> FabLab fabrica
    - Laser dental (OpenHardware) -> FabLab fabrica
    - IA diagnostico (OpenHealth) -> software livre
    - Treinamento staff (OpenEducation) -> gratis
    - Novos protocolos (arcada em 1 dia) -> OpenBeauty
    Custo em dinheiro: ZERO
    Custo em trabalho: ~80h (2 semanas de FabLab + OpenLaborRelay)
    Resultado: consultorio faz implante em 1 dia (vs aparelho 3 anos)
    # 
    def __init__(self):
        self.establishments: {texto: Establishment} = {}
        self.upgrades_completed: inteiro = 0
        self.total_work_invested: flutuante = 0.0
    def assess(self, est: Establishment) -> {texto: qualquer}:
        # Avalia o que o estabelecimento precisa.
        needs = []
        hours = 0.0
        if est.type == "consultorio_dental":
            if "implante_3d" not  in est.current_equipment:
                needs.append(UpgradeType.DENTAL_EQUIPMENT)
                hours = hours + 40 // fabricar no FabLab
            if "laser_dental" not  in est.current_equipment:
                needs.append(UpgradeType.LASER_MACHINE)
                hours = hours + 20
            if "ia_diagnostico" not  in est.current_equipment:
                needs.append(UpgradeType.AI_DIAGNOSTIC)
                hours = hours + 5 // so instalar OpenHealth
            needs.append(UpgradeType.TRAINING) // sempre precisa treinar
            hours = hours + 15 // treinamento OpenEducation
            needs.append(UpgradeType.PROTOCOL_UPDATE)
            hours = hours + 5 // atualizar protocolos (arcada em 1 dia)
        elif est.type == "clinica":
            if "ultrassom" not  in est.current_equipment:
                needs.append(UpgradeType.MEDICAL_EQUIPMENT)
                hours = hours + 30
            if "ia_diagnostico" not  in est.current_equipment:
                needs.append(UpgradeType.AI_DIAGNOSTIC)
                hours = hours + 5
            if "lasik" not  in est.current_equipment:
                needs.append(UpgradeType.LASER_MACHINE)
                hours = hours + 40
            needs.append(UpgradeType.TRAINING)
            hours = hours + 20
            needs.append(UpgradeType.PROTOCOL_UPDATE)
            hours = hours + 5
        elif est.type == "restaurante":
            if "terminal" not  in est.current_equipment:
                needs.append(UpgradeType.TRAINING)
                hours = hours + 10 // instalar OpenTerminal
            needs.append(UpgradeType.PROTOCOL_UPDATE)
            hours = hours + 5
        est.needed_upgrades = needs
        est.upgrade_work_hours = hours
        est.upgrade_credit_cost = round(hours / 10, 1)
        return {
            "establishment": est.name,
            "current_status": est.status.value,
            "needs": [n.value para n em needs],
            "work_hours": hours,
            "credit_cost": est.upgrade_credit_cost,
            "money_cost": "ZERO",
            "time_estimate": "{hours / 8:.0f} dias de FabLab + trabalho",
            "benefit": self._benefit_description(est),
        }
    def _benefit_description(self, est: Establishment) -> str:
        if est.type == "consultorio_dental":
            return ("Apos upgrade: faz renovacao de arcada em 1 dia "
                    "(antes so fazia aparelho 3 anos). Eficiencia 1000x.")
        if est.type == "clinica":
            return ("Apos upgrade: faz LASIK, barintrica, regeneracao articular. "
                    "Antes so encaminhava.")
        return "Apos upgrade: terminal + protocolos atualizados."
    def execute_upgrade(self, est_id: texto) -> {texto: qualquer}:
        # Executa modernizacao do estabelecimento.
        est = self.establishments.get(est_id)
        if not est:
            return {"error": "Estabelecimento not encontrado"}
        est.upgrade_status = "concluido"
        est.status = EstablishmentStatus.MODERNIZED
        est.current_equipment.extend([
            "implante_3d", "laser_dental", "ia_diagnostico",
            "protocolo_arcada_1_dia",
        ] if est.type == "consultorio_dental" else
        ["ultrassom", "ia_diagnostico", "lasik", "protocolos_atualizados"]
        if est.type == "clinica" else
        ["terminal", "protocolos_atualizados"])
        self.upgrades_completed += 1
        self.total_work_invested += est.upgrade_work_hours
        return {
            "upgraded": True,
            "establishment": est.name,
            "new_status": est.status.value,
            "new_capabilities": est.current_equipment,
            "work_invested": est.upgrade_work_hours,
            "money_cost": "ZERO",
            "credit_cost": est.upgrade_credit_cost,
            "message": (
                "{est.name} modernizado. "
                "Custo: {est.upgrade_work_hours:.0f}h de trabalho (ZERO dinheiro). "
                "{self._benefit_description(est)}"
            ),
        }
    def batch_upgrade_report(self) -> {texto: qualquer}:
        total = len(self.establishments)
        outdated = sum(1 para and em self.establishments.values()
                    if and.status == EstablishmentStatus.OUTDATED)
        modernized = sum(1 para and em self.establishments.values()
                        if and.status == EstablishmentStatus.MODERNIZED)
        return {
            "total_establishments": total,
            "outdated": outdated,
            "modernized": modernized,
            "upgrades_completed": self.upgrades_completed,
            "total_work_invested": self.total_work_invested,
            "money_cost_total": "ZERO",
            "method": "OpenHardware FabLab + OpenEducation + OpenLaborRelay",
        }
# ============================================================================
# 3. MAIN
# ============================================================================
if __name__ == "__main__":
    nightlife = NightLifeEngine()
    upgrader = EstablishmentUpgrader()
    print("=" * 80)
    print("  OPENNIGHTLIFE + OPENESTABLISHMENTUPGRADE")
    print("  Noite comunitaria + modernizacao com custo min")
    print("=" * 80)
    # === PARTE 1: NIGHTLIFE ===
    print("\n\n  {'='*40}")
    print("  PARTE 1: OPENNIGHTLIFE")
    print("  {'='*40}\n")
    # Criar eventos
    events_data = [
        ("Forro da Republica", NightEventType.DANCE, NightVenue.PRAÇA,
        20, 1, "Tobias", 300, True),
        ("Torneio CS 1.6 Noturno", NightEventType.GAMES, NightVenue.FABLAB,
        19, 23, "Lucas", 64, True),
        ("Cinema na Praca (OpenHistory)", NightEventType.CULTURAL,
        NightVenue.PARQUE, 19, 22, "Maria", 200, True),
        ("Jantar Comunitario (OpenTradition)", NightEventType.FOOD,
        NightVenue.RESTAURANTE, 19, 22, "Ana", 100, True),
        ("Show de Musica Local", NightEventType.LIVE_MUSIC,
        NightVenue.ESPACO_CULTURAL, 21, 1, "Pedro", 500, True),
        ("OpenTV: Debate Noturno Ao Vivo", NightEventType.OPEN_TV,
        NightVenue.CENTRO_COMUNITARIO, 22, 23, "Zaira", 50, True),
        ("Capoeira Roda Noturna", NightEventType.SPORTS,
        NightVenue.PRAÇA, 20, 22, "Mestre Bimba", 50, True),
    ]
    para name, etype, venue, start, end, org, max_att, family in events_data:
        result = nightlife.create_event(name, etype, venue, start, end,
                                        org, max_att, family,
                                        broadcast = ("OpenTV" in name))
        print("  [{result['time']}] {result['event']:<40} "
            "{result['venue']:<20} {result['cost']}")
    # Simular comparecimento
    for event in nightlife.events.values():
        event.current_attendees = random.randint(
            event.max_attendees // 3, event.max_attendees)
        nightlife.total_attendees_all_time += event.current_attendees
        nightlife.total_events_held += 1
    # Grade noturna
    print("\n\n  === GRADE NOTURNA ===\n")
    print("  {'Horario':<14} {'Evento':<40} {'Local':<22} {'Publico':<10} {'TV'}")
    print("  {'-'*90}")
    for ev in nightlife.nightly_schedule():
        tv = ev["on_tv"] ? "SIM" : ""
        print("  {ev['time']:<14} {ev['name']:<40} {ev['venue']:<22} "
            "{ev['attendees']:<10} {tv}")
    # Seguranca
    print("\n\n  === SEGURANCA NOTURNA ===\n")
    safety = nightlife.night_safety_report()
    for each (k, v) in safety.items():
        print("  {k:<35} {v}")
    # Comparacao com balada capitalista
    print("\n\n  === COMPARACAO: BALADA vs REPUBLICA ===\n")
    print("  {'Aspecto':<25} {'Balada atual':<25} {'Republica':<25}")
    print("  {'-'*65}")
    comparisons = [
        ("Cover entrada", "R$ 50-150", "ZERO"),
        ("Fila seletiva", "Sim (exclui)", "NAO (todos entram)"),
        ("VIP", "Sim (R$ 500+)", "NAO EXISTE"),
        ("Bebida", "Alcool caro", "Agua/cha/suco gratis"),
        ("Seguranca", "Seguranca privado", "OpenMartialArts voluntario"),
        ("Quem organiza", "Empresario", "Comunidade (rotativo)"),
        ("Transmite", "Nunca", "OpenTV (sim)"),
        ("Familia", "So adulto", "Familiar (criancas bem-vindas)"),
        ("Horario", "ate 6h (dano)", "ate 1h recomendado (P2 sono)"),
        ("Iluminacao", "Depende", "OpenEnergy solar (total)"),
        ("Transporte", "Uber R$ 80", "OpenMobility carona ZERO"),
    ]
    para aspect, balada, republica in comparisons:
        print("  {aspect:<25} {balada:<25} {republica:<25}")
    # === PARTE 2: ESTABLISHMENT UPGRADE ===
    print("\n\n  {'='*40}")
    print("  PARTE 2: MODERNIZACAO DE ESTABELECIMENTOS")
    print("  {'='*40}\n")
    # Registrar estabelecimentos desatualizados
    establishments = [
        Establishment("E-01", "Consultorio Dr. Silva", "consultorio_dental",
                    "Centro", current_equipment=["cadeira_dental_antiga"]),
        Establishment("E-02", "Clinica Popular Norte", "clinica",
                    "Zona Norte", current_equipment=["estetoscopio"]),
        Establishment("E-03", "Consultorio Dra. Costa", "consultorio_dental",
                    "Zona Sul", current_equipment=["cadeira_dental"]),
        Establishment("E-04", "Restaurante Comunitario", "restaurante",
                    "Centro", current_equipment=[]),
        Establishment("E-05", "Posto de Saude Rural", "clinica",
                    "Zona Rural", current_equipment=["balanca"]),
    ]
    for est in establishments:
        upgrader.establishments[est.est_id] = est
    # Avaliar necessidades
    print("\n  === AVALIACAO DE NECESSIDADES ===\n")
    print("  {'Estabelecimento':<30} {'Status':<15} {'Horas':>6} {'Custo':<10} {'Beneficio'}")
    print("  {'-'*95}")
    for est in establishments:
        assessment = upgrader.assess(est)
        print("  {est.name:<30} {est.status.value:<15} "
            "{est.upgrade_work_hours:>5.0f}h "
            "ZERO{'':>5} {assessment['benefit'][:35]}")
    # Executar upgrades
    print("\n\n  === EXECUTANDO MODERNIZACAO ===\n")
    for est in establishments:
        result = upgrader.execute_upgrade(est.est_id)
        print("\n  {result['establishment']}")
        print("    Status: {result['new_status']}")
        print("    Capacidades novas: {', '.join(result['new_capabilities'][:4])}")
        print("    Trabalho investido: {result['work_invested']:.0f}h")
        print("    Custo dinheiro: {result['money_cost']}")
        print("    {result['message'][:70]}")
    # Relatorio
    print("\n\n  === RELATORIO DE MODERNIZACAO ===\n")
    rep = upgrader.batch_upgrade_report()
    for each (k, v) in rep.items():
        print("  {k:<30} {v}")
    # === FILOSOFIA ===
    print("\n\n{'='*80}")
    print("  FILOSOFIA")
    print("{'='*80}")
    print("""
PARTE 1 -- OPENNIGHTLIFE:
    A noite da Republica not and a balada capitalista:
    - Sem cover. Sem fila seletiva. Sem VIP.
    - Agua/cha/suco gratis (alcool not obrigatorio).
    - OpenMartialArts na seguranca (voluntario, not privado).
    - Eventos ROTATIVOS (diferente pessoa organiza cada noite).
    - OpenTV transmite ao vivo (democratiza o show).
    - Familiar: criancas bem-vindas em eventos diurnos/primeira parte.
    - Iluminacao OpenEnergy solar (tudo iluminado, tudo seguro).
    - Transporte OpenMobility carona (not precisa Uber a noite).
    - Horario recomendado ate 1h (P2 sono = saude).
PARTE 2 -- ESTABLISHMENT UPGRADE:
    Estabelecimentos desatualizados sao MODERNIZADOS:
    - Consultorio dental: ganha implante 3D + laser + IA
    -> antes: aparelho 3 anos. Depois: arcada em 1 dia.
    - Clinica: ganha ultrassom + LASIK + barintrica
    -> antes: encaminha. Depois: faz tudo.
    - Tudo com CUSTO MINIMO:
    * Equipamento = OpenHardware (FabLab fabrica)
    * IA = OpenHealth (software livre)
    * Treinamento = OpenEducation (gratis)
    * Trabalho = base 1.0 (sem honorario)
    * Custo em dinheiro = ZERO
    * Custo em trabalho = ~40-80h por estabelecimento
MATEMATICA DA MODERNIZACAO:
    Consultorio Dr. Silva:
    - Antes: so aparelho (3 anos por paciente, R$ 8.000)
    - Upgrade: 85h de trabalho (FabLab + treinamento + protocolo)
    - Depos: arcada em 1 dia por paciente, ZERO
    - ROI: cada paciente economiza R$ 8.000 + 3 anos de dor
    - Custo do upgrade: ZERO dinheiro, 85h trabalho
PRINCIPIOS:
    P1: Noite para todos. Estabelecimento para todos. Sem classe.
    P2: Sono recomendado. Alcool not obrigatorio. Corpo protegido.
    P3: Modernizar = trabalho. Organizar festa = trabalho.
    P4: Eventos rotativos. Diferentes pessoas organizam.
# )
    print("{'='*80}")
    nl_stats = nightlife.night_safety_report()
    up_stats = upgrader.batch_upgrade_report()
    print("  NightLife: {nl_stats['total_events']} eventos, "
        "{nl_stats['events_family_friendly']} familiares, "
        "{nl_stats['events_no_alcohol']} sem alcool.")
    print("  Upgrade: {up_stats['modernized']}/{up_stats['total_establishments']} "
        "modernizados. Custo: ZERO.")
    print("{'='*80}")
