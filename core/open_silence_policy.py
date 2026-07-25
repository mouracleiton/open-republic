#!/usr/bin/env python3
"""
OpenSilencePolicy -- Alertas Sonoros de Pressao PROIBIDOS -- gerado de Portugol++
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field

# !/usr/bin/env python3
# 
OpenSilencePolicy -- Alertas Sonoros de Pressao PROIBIDOS
============================================================
"Bip de notificacao as 6h te acordando pra trabalhar.
Ding de mensagem que voce PRECISA responder AGORA.
Alarme de deadline que causa ansiedade.
Tudo isso and PRESSAO SONORA. and PROIBIDO.
O cerebro not and maquina. Descanso and DIREITO.
OpenAbsence garante. OpenSilencePolicy protege o SILENCIO."
O QUE ESTE SISTEMA FAZ:
1. Identifica alertas sonoros que sao PRESSAO (ansiedade/guilt)
2. Desativa TODOS por padrao
3. Substitui por VISUAL discreto (sem som)
4. Permite apenas alertas que o usuario ESCOLHEU receber
5. Honra OpenAbsence (ausencia = ZERO som)
Author: OpenRepublic Team
# 
# importa annotations de __future__
# importa hashlib
# importa dataclass, field de dataclasses
# importa Any, Dict, List, Optional de typing
# importa Enum de enum
# importa datetime de datetime
# ============================================================================
# 1. TIPOS DE ALERTA SONORO
# ============================================================================
class AlertPurpose(Enum):
    # Para que o alerta serve?
    WORK_PRESSURE = "pressao_trabalho"  // forcar a trabalhar mais
    DEADLINE = "deadline_ansiedade"  // prazo逼近 = ansiedade
    NOTIFICATION_BOMBARDMENT = "bombardeio"  // notificacao sem parar
    ENGAGEMENT_TRAP = "armadilha_engajamento"  // viciar em checar
    SOCIAL_PRESSURE = "pressao_social"  // "todos viram sua mensagem"
    GUILT_TRIP = "culpa"  // "voce not respondeu"
    LEGITIMATE = "legitimo"  // alarme que VOCE escolheu
    EMERGENCY = "emergencia"  // emergencia real
    HEALTH_REMINDER = "saude"  // lembrar de tomar agua, mover
class AlertAction(Enum):
    DISABLED = "desativado"  // desligado TOTAL
    VISUAL_ONLY = "so_visual"  // sem som, so sinal visual
    SILENT_BATCH = "silencioso_agrupado"  // junta tudo, mostra 1x/dia
    USER_CHOSEN = "usuario_escolheu"  // usuario optou por receber
    EMERGENCY_ONLY = "so_emergencia"  // so toca se para emergencia real
# ============================================================================
# 2. ALERTA CLASSIFICADO
# ============================================================================
# decorador: @dataclass
class SoundAlert:
    # Um tipo de alerta sonoro classificado.
    alert_id: texto
    name: texto // nome do alerta
    source: texto // de onde vem (app, sistema, etc)
    purpose: AlertPurpose
    description: str = ""
    default_sound: str = ""  // som original
    action: AlertAction = AlertAction.DISABLED
    replacement: str = ""  // o que existe no lugar
    pressure_level: int = 0 // 0-5 (quanto pressiona)
# ============================================================================
# 3. CATÁLOGO DE ALERTAS DE PRESSÃO (TODOS DESATIVADOS)
# ============================================================================
PRESSURE_ALERTS: [SoundAlert] = [
    # === TRABALHO ===
    SoundAlert("AL-W01", "Notificacao de email corporativo as 6h",
            "email_corporativo", AlertPurpose.WORK_PRESSURE,
            "Bip de novo email as 6h da manha. Acorda pessoa pra trabalhar.",
            default_sound = "ding", pressure_level=5,
            replacement = "Email fica na caixa. OpenInbox mostra quando VOCE abrir."),
    SoundAlert("AL-W02", "Slack/Teams message notification",
            "chat_corporativo", AlertPurpose.WORK_PRESSURE,
            "Som de mensagem de trabalho. Pressao pra responder AGORA.",
            default_sound = "knock-brush", pressure_level=5,
            replacement = "Mensagem fica. VOCE ve quando quiser. Sem pressao."),
    SoundAlert("AL-W03", "Deadline alarm (prazo逼近)",
            "gestor_tarefas", AlertPurpose.DEADLINE,
            "Alarme de prazo criando ansiedade. 'FALTA 1 HORA!'",
            default_sound = "alarm-urgent", pressure_level=5,
            replacement = "Prazo visivel no painel. Sem som. Sem panico."),
    SoundAlert("AL-W04", "Boss checking your status",
            "sistema_rh", AlertPurpose.WORK_PRESSURE,
            "Chefe viu que voce esta 'offline'. Pressao pra aparecer online.",
            default_sound = "ping", pressure_level=4,
            replacement = "Status and SEU. Ninguem ve se voce esta online."),
    SoundAlert("AL-W05", "Overtime reminder ('voce pode fazer mais')",
            "sistema_produto", AlertPurpose.WORK_PRESSURE,
            "Lembra de fazer mais horas. Pressao implacavel.",
            default_sound = "chime", pressure_level=4,
            replacement = "ABOLIDO. Max 40h (assembleia votou). Sem pressure."),
    # === ENGAJAMENTO (viciar) ===
    SoundAlert("AL-E01", "Notificacao de like/comentario (Instagram/X)",
            "rede_social", AlertPurpose.ENGAGEMENT_TRAP,
            "Ding de like. Vicia em checar. Dopamina artificial.",
            default_sound = "pop", pressure_level=4,
            replacement = "OpenInbox agrupa. 1 notificacao por dia. Sem ding."),
    SoundAlert("AL-E02", "Badge de mensagem not lida",
            "mensageiro", AlertPurpose.SOCIAL_PRESSURE,
            "Bolinha vermelha + som. 'TEM MENSAGEM!' Pressao social.",
            default_sound = "ba-ding", pressure_level=3,
            replacement = "Sem bolinha. Sem som. VOCE ve quando quiser."),
    SoundAlert("AL-E03", "Streak alarm ('not perca sua sequencia!')",
            "app_habito", AlertPurpose.GUILT_TRIP,
            "Streak de dias consecutivos. Perdeu = culpa. Viciante.",
            default_sound = "flourish", pressure_level=4,
            replacement = "ABOLIDO. Nao existe streak. Nao existe culpa."),
    SoundAlert("AL-E04", "Push notification de promocao",
            "app_compra", AlertPurpose.NOTIFICATION_BOMBARDMENT,
            "PROMOCAO! DESCONTO! COMPRE AGORA! Bombarda o cerebro.",
            default_sound = "cash-register", pressure_level=5,
            replacement = "ABOLIDO. Sem comerciais. Sem push de compra."),
    SoundAlert("AL-E05", "Notification de live/stream comecando",
            "streaming", AlertPurpose.ENGAGEMENT_TRAP,
            "STREAMER FAVORITO TA LIVE! VEM! Pressao FOMO.",
            default_sound = "fanfare", pressure_level=3,
            replacement = "OpenInbox avisa 1x. Sem som. Sem FOMO."),
    # === SOCIAL ===
    SoundAlert("AL-S01", "Mensagem not respondida (lembrete)",
            "mensageiro", AlertPurpose.GUILT_TRIP,
            "Voce not respondeu ha 2 horas. Lembrete sonoro. Culpa.",
            default_sound = "gentle-reminder", pressure_level=4,
            replacement = "ABOLIDO. Voce responde QUANDO PUDER. P2."),
    SoundAlert("AL-S02", "Tag/Mention notification",
            "rede_social", AlertPurpose.SOCIAL_PRESSURE,
            "Alguem te marcou. Pressao pra responder/ver AGORA.",
            default_sound = "ding-dong", pressure_level=3,
            replacement = "OpenInbox mostra. Sem som. VOCE ve quando abrir."),
    SoundAlert("AL-S03", "Read receipt pressure ('entregue, not lido')",
            "mensageiro", AlertPurpose.SOCIAL_PRESSURE,
            "Outro lado ve que voce leu mas not respondeu. Pressao.",
            default_sound = "N/A (visual)", pressure_level=3,
            replacement = "ABOLIDO. Sem recibo de leitura. Privacidade (P2)."),
    # === BOMBARDEIO ===
    SoundAlert("AL-B01", "News push notification (a cada 5 min)",
            "app_noticias", AlertPurpose.NOTIFICATION_BOMBARDMENT,
            "ULTIMA HORA! BREAKING! ALERTA! Bombarda de noticia.",
            default_sound = "news-jingle", pressure_level=5,
            replacement = "OpenTV/OpenInbox mostra. 1 compilado/dia. Sem som."),
    SoundAlert("AL-B02", "App update notification",
            "app_store", AlertPurpose.NOTIFICATION_BOMBARDMENT,
            "ATUALIZE AGORA! 15 apps pedindo update ao mesmo tempo.",
            default_sound = "update-ready", pressure_level=2,
            replacement = "Update automatico silencioso. A noite. Sem som."),
    SoundAlert("AL-B03", "Storage full warning (a cada 5 min)",
            "sistema", AlertPurpose.NOTIFICATION_BOMBARDMENT,
            "ARMazenamento CHEIO! A cada 5 minutos. Insuportavel.",
            default_sound = "warning-beep", pressure_level=3,
            replacement = "Avisa 1x visual. Resolve automatico (OpenRepair)."),
    # === SAUDE (alguns podem ser legitimos se usuario escolheu) ===
    SoundAlert("AL-H01", "Lembrete de agua (a cada hora)",
            "app_saude", AlertPurpose.HEALTH_REMINDER,
            "Beba agua! A cada hora. Benigno mas pode irritar.",
            default_sound = "water-drop", pressure_level=1,
            replacement = "Visual discreto (sem som). Usuario escolhe."),
    SoundAlert("AL-H02", "Lembrete de movimento (a cada 30 min)",
            "app_saude", AlertPurpose.HEALTH_REMINDER,
            "Levante! Mova! A cada 30 min.",
            default_sound = "stretch-bell", pressure_level=1,
            replacement = "Visual discreto. Usuario escolhe. Sem som padrao."),
    # === EMERGENCIA (unica categoria que pode ter som) ===
    SoundAlert("AL-EM01", "Alerta de emergencia real",
            "sistema_republica", AlertPurpose.EMERGENCY,
            "Emergencia REAL (desastre, evacuacao, vida em risco).",
            default_sound = "emergency-siren", pressure_level=0,
            action = AlertAction.EMERGENCY_ONLY,
            replacement = "PERMITIDO. So emergencia REAL."),
    SoundAlert("AL-EM02", "Alarme de incendio",
            "sistema_predio", AlertPurpose.EMERGENCY,
            "Incendio real. Evacuar.",
            default_sound = "fire-alarm", pressure_level=0,
            action = AlertAction.EMERGENCY_ONLY,
            replacement = "PERMITIDO. Emergencia fisica."),
]
# ============================================================================
# 4. MOTOR DE SILENCIO
# ============================================================================
class SilenceEngine:
    # Motor que desativa TODA pressao sonora.
    FILOSOFIA:
    "Para de me encher o saco porra."
    O cerebro not and maquina.
    Notificacao a cada 5 minutos = ansiedade cronica.
    Ding de email as 6h = cortou sono (P2 violado).
    Bolinha vermelha = pressao social constante.
    Streak alarm = culpa artificial.
    A Republica PROTEGE o silencio.
    Silencio and SAUDE MENTAL.
    Silencio and DESCANSO.
    Silencio and DIREITO.
    O QUE FAZ:
    1. DESATIVA todo alerta de pressao por padrao
    2. Substitui por VISUAL discreto (sem som)
    3. Agrupa notificacoes (1 vez/dia, not 50 vezes)
    4. Honra OpenAbsence (ausente = ZERO som)
    5. So permite som se USUARIO ESCOLHEU or EMERGENCIA
    # 
    def __init__(self):
        self.alerts: {texto: SoundAlert} = {a.alert_id: a para a em PRESSURE_ALERTS}
        self.user_choices: Dict[texto, [texto]] = {} // user -> alertas que escolheu ouvir
        self.absent_users: [texto] = [] // usuarios em ausencia (OpenAbsence)
    def disable_all_pressure(self) -> {texto: qualquer}:
        # Desativa TODOS os alertas de pressao.
        disabled = 0
        visual_only = 0
        emergency = 0
        for alert in self.alerts.values():
            if alert.purpose == AlertPurpose.EMERGENCY:
                alert.action = AlertAction.EMERGENCY_ONLY
                emergency = emergency + 1
            elif alert.purpose == AlertPurpose.HEALTH_REMINDER:
                alert.action = AlertAction.VISUAL_ONLY
                visual_only = visual_only + 1
            elif alert.purpose == AlertPurpose.LEGITIMATE:
                alert.action = AlertAction.USER_CHOSEN
                visual_only = visual_only + 1
            else:
                alert.action = AlertAction.DISABLED
                disabled = disabled + 1
        return {
            "total_alertas": len(self.alerts),
            "desativados": disabled,
            "so_visual": visual_only,
            "emergencia_permitido": emergency,
            "som_no_sistema": "ZERO (exceto emergencia real)",
            "message": (
                "DESATIVADO: {disabled} alertas de pressao. "
                "{visual_only} convertidos para visual sem som. "
                "{emergency} emergencias mantidas (unica excecao). "
                "SISTEMA EM SILENCIO. Paz garantida."
            ),
        }
    def user_opt_in(self, user_id: texto, alert_id: texto) -> {texto: qualquer}:
        # Usuario escolhe receber UM alerta especifico.
        alert = self.alerts.get(alert_id)
        if not alert:
            return {"error": "Alerta not encontrado"}
        if user_id not in self.user_choices:
            self.user_choices[user_id] = []
        self.user_choices[user_id].append(alert_id)
        return {
            "user": user_id,
            "alert": alert.name,
            "status": "OPT-IN (usuario escolheu)",
            "message": "Voce ESCOLHEU receber '{alert.name}'. Pode revogar a qualquer momento.",
        }
    def check_alert(self, user_id: texto, alert_id: texto) -> {texto: qualquer}:
        # Verifica se alerta deve tocar para o usuario.
        alert = self.alerts.get(alert_id)
        if not alert:
            return {"action": "BLOQUEAR", "reason": "Alerta not catalogado"}
        # Usuario ausente? ZERO som.
        if user_id in self.absent_users:
            return {
                "user": user_id,
                "alert": alert.name,
                "action": "BLOQUEAR (ausente)",
                "reason": "OpenAbsence: usuario ausente. ZERO som. ZERO pressao.",
                "message": "Bloqueado. {user_id} esta ausente. Silencio absoluto.",
            }
        # Emergencia? Toca.
        if alert.action == AlertAction.EMERGENCY_ONLY:
            return {"action": "TOCAR (emergencia)", "alert": alert.name}
        # Usuario escolheu? Toca.
        if alert_id in self.user_choices.get(user_id, []):
            return {"action": "TOCAR (usuario escolheu)", "alert": alert.name}
        # Desativado?
        if alert.action == AlertAction.DISABLED:
            return {
                "action": "BLOQUEAR (desativado)",
                "alert": alert.name,
                "reason": "Alerta de pressao. DESATIVADO por padrao.",
                "replacement": alert.replacement,
            }
        # Visual only?
        if alert.action == AlertAction.VISUAL_ONLY:
            return {
                "action": "VISUAL (sem som)",
                "alert": alert.name,
                "reason": "Convertido para visual discreto. Sem som.",
            }
        return {"action": "BLOQUEAR", "alert": alert.name}
    funcao what_replaces_sounds(self) retorna List[{texto: texto}]:
        # O que existe no lugar dos alertas sonoros.
        return [
            {"categoria": "Notificacoes de trabalho",
            "antes": "Ding a cada mensagem. Bip de email as 6h.",
            "depois": "OpenInbox agrupa tudo. VOCE abre quando quiser."},
            {"categoria": "Rede social",
            "antes": "Ding de like. Bolinha vermelha. FOMO.",
            "depois": "OpenInbox mostra 1x/dia. Sem ding. Sem bolinha."},
            {"categoria": "Deadline/prazo",
            "antes": "Alarme de prazo. ANSIEDADE.",
            "depois": "Prazo visivel no painel. Sem alarme. Sem panico."},
            {"categoria": "Mensagem not lida",
            "antes": "Recibo de leitura. Pressao social.",
            "depois": "Sem recibo. Voce responde QUANDO puder. P2."},
            {"categoria": "Streak/habito",
            "antes": "Perdeu streak = culpa. Viciante.",
            "depois": "Streak not existe. Nao existe culpa."},
            {"categoria": "Promocao/compra",
            "antes": "PROMOCAO! DESCONTO! COMPRE AGORA!",
            "depois": "ABOLIDO. Sem comercial. Sem push de compra."},
            {"categoria": "News/breaking",
            "antes": "BREAKING! a cada 5 minutos.",
            "depois": "1 compilado/dia. OpenTV/OpenInbox. Sem som."},
            {"categoria": "Update de app",
            "antes": "ATUALIZE AGORA! 15 apps.",
            "depois": "Automatico silencioso. A noite. Voce nem percebe."},
            {"categoria": "Saude (agua/movimento)",
            "antes": "Bip a cada hora.",
            "depois": "Visual discreto. So se VOCE escolher. Sem som padrao."},
        ]
    def stats(self) -> {texto: qualquer}:
        return {
            "total_alertas_catalogados": len(self.alerts),
            "desativados": sum(1 para a em self.alerts.values()
                            if a.action == AlertAction.DISABLED),
            "so_visual": sum(1 para a em self.alerts.values()
                            if a.action == AlertAction.VISUAL_ONLY),
            "emergencia": sum(1 para a em self.alerts.values()
                            if a.action == AlertAction.EMERGENCY_ONLY),
            "usuarios_opt_in": sum(len(v) para v em self.user_choices.values()),
            "usuarios_ausentes_protegidos": len(self.absent_users),
            "som_padrao_sistema": "ZERO",
            "principio": "Silencio and saude mental. Pressao sonora and PROIBIDA.",
        }
# ============================================================================
# 5. MAIN
# ============================================================================
if __name__ == "__main__":
    engine = SilenceEngine()
    print("=" * 80)
    print("  OPENSILENCEPOLICY -- ALERTAS DE PRESSAO DESATIVADOS")
    print("  'Para de me encher o saco porra.'")
    print("=" * 80)
    # === 1. DESATIVAR TUDO ===
    print("\n\n  === 1. DESATIVANDO TODA PRESSAO SONORA ===\n")
    r = engine.disable_all_pressure()
    print("  {r['message']}")
    print("  Som padrao no sistema: {r['som_no_sistema']}")
    # === 2. CATALOGO DE ALERTAS ===
    print("\n\n  === 2. CATALOGO ({len(engine.alerts)} alertas) ===\n")
    current_purpose = None
    for alert in engine.alerts.values():
        if alert.purpose != current_purpose:
            current_purpose = alert.purpose
            icon = alert.purpose != AlertPurpose.EMERGENCY ? "PROIBIDO" : "PERMITIDO"
            print("\n  --- {alert.purpose.value.upper()} [{icon}] ---")
        action_icon = {
            AlertAction.DISABLED: "DESATIVADO",
            AlertAction.VISUAL_ONLY: "VISUAL",
            AlertAction.USER_CHOSEN: "OPT-IN",
            AlertAction.EMERGENCY_ONLY: "EMERG",
        }.get(alert.action, "?")
        print("  [{action_icon:<10}] {alert.name[:45]:<46} pressao:{alert.pressure_level}")
    # === 3. O QUE SUBSTITUI ===
    print("\n\n  === 3. O QUE EXISTE NO LUGAR ===\n")
    replacements = engine.what_replaces_sounds()
    for r in replacements:
        print("\n  {r['categoria'].upper()}:")
        print("    Antes:  {r['antes']}")
        print("    Depois: {r['depois']}")
    # === 4. USUARIO OPT-IN ===
    print("\n\n  === 4. USUARIO PODE OPTAR (se quiser) ===\n")
    opt = engine.user_opt_in("cleiton", "AL-H01")
    print("  {opt['message']}")
    print("  (Pode revogar a qualquer momento. Padrao = desativado.)")
    # === 5. HONRA AUSENCIA ===
    print("\n\n  === 5. HONRA OPENSABSENCE ===\n")
    engine.absent_users.append("cleiton")
    check = engine.check_alert("cleiton", "AL-W01")
    print("  Cleiton (ausente): {check['action']}")
    print("  {check.get('message', check.get('reason', ''))}")
    # === 6. STATS ===
    print("\n\n  === 6. ESTATISTICAS ===\n")
    s = engine.stats()
    for each (k, v) in s.items():
        print("  {k:<35} {v}")
    print("\n{'='*80}")
    print("  OpenSilencePolicy: {s['desativados']} desativados, "
        "{s['so_visual']} visual, {s['emergencia']} emergencia.")
    print("  {s['principio']}")
    print("{'='*80}")
