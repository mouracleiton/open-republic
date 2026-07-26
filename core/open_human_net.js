// open_human_net.js
// Transpilacao completa de open_human_net.py para JavaScript
// Comentarios em portugues. Todas as enums, classes, funcoes e cenarios preservados.
// demo() como funcao principal.

const TrustRing = {
    FAMILY: { value: 0, name: 'FAMILY' },
    CAREGIVER: { value: 1, name: 'CAREGIVER' },
    COMMUNITY: { value: 2, name: 'COMMUNITY' },
    PROFESSIONAL: { value: 3, name: 'PROFESSIONAL' },
    EMERGENCY: { value: 4, name: 'EMERGENCY' },
    BYSTANDER: { value: 5, name: 'BYSTANDER' }
};

const AuthorizationLevel = {
    FULL: { value: 'completa', name: 'FULL' },
    HIGH: { value: 'alta', name: 'HIGH' },
    MEDIUM: { value: 'media', name: 'MEDIUM' },
    LOW: { value: 'baixa', name: 'LOW' },
    EMERGENCY_ONLY: { value: 'so_emergencia', name: 'EMERGENCY_ONLY' }
};

const HumanAvailability = {
    AVAILABLE: { value: 'disponivel', name: 'AVAILABLE' },
    MAYBE: { value: 'talvez', name: 'MAYBE' },
    BUSY: { value: 'ocupado', name: 'BUSY' },
    UNREACHABLE: { value: 'inalcancavel', name: 'UNREACHABLE' },
    OFFLINE: { value: 'offline', name: 'OFFLINE' },
    UNKNOWN: { value: 'desconhecido', name: 'UNKNOWN' }
};

const ContactMethod = {
    PHONE_CALL: { value: 'ligacao', name: 'PHONE_CALL' },
    SMS: { value: 'sms', name: 'SMS' },
    WHATSAPP: { value: 'whatsapp', name: 'WHATSAPP' },
    VIDEO_CALL: { value: 'video', name: 'VIDEO_CALL' },
    APP_PUSH: { value: 'notificacao_app', name: 'APP_PUSH' },
    SMARTWATCH: { value: 'smartwatch', name: 'SMARTWATCH' },
    HOME_ASSISTANT: { value: 'assinante_casa', name: 'HOME_ASSISTANT' },
    PHYSICAL_VISIT: { value: 'visita_fisica', name: 'PHYSICAL_VISIT' }
};

const CallStatus = {
    PENDING: { value: 'pendente', name: 'PENDING' },
    RINGING: { value: 'tocando', name: 'RINGING' },
    ANSWERED: { value: 'atendeu', name: 'ANSWERED' },
    CONFIRMED: { value: 'confirmou', name: 'CONFIRMED' },
    DECLINED: { value: 'recusou', name: 'DECLINED' },
    TIMEOUT: { value: 'sem_resposta', name: 'TIMEOUT' },
    FAILED: { value: 'falhou', name: 'FAILED' },
    CANCELLED: { value: 'cancelada', name: 'CANCELLED' }
};

function _haversine_km(lat1, lon1, lat2, lon2) {
    const R = 6371;
    const dlat = (lat2 - lat1) * Math.PI / 180;
    const dlon = (lon2 - lon1) * Math.PI / 180;
    const a = Math.sin(dlat / 2) ** 2 + Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) * Math.sin(dlon / 2) ** 2;
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return R * c;
}

class AuthorizedHuman {
    constructor(human_id, name, phone, ring, authorization, relationship = '', home_location = null,
                preferred_contact = ContactMethod.PHONE_CALL, skills = [], can_make_decisions = false,
                medical_authorization = false, response_timeout_s = 30, max_distance_km = 50.0, available_hours = ['00:00', '23:59']) {
        this.human_id = human_id;
        this.name = name;
        this.phone = phone;
        this.ring = ring;
        this.authorization = authorization;
        this.relationship = relationship;
        this.home_location = home_location;
        this.current_location = null;
        this.last_location_update = 0;
        this.preferred_contact = preferred_contact;
        this.languages = ['pt-BR'];
        this.skills = skills;
        this.available_hours = available_hours;
        this.response_timeout_s = response_timeout_s;
        this.max_distance_km = max_distance_km;
        this.can_make_decisions = can_make_decisions;
        this.medical_authorization = medical_authorization;
        this.photo_url = '';
        this.notes = '';
    }

    distance_to(lat, lon) {
        const loc = this.current_location || this.home_location;
        if (!loc) return 9999.0;
        return _haversine_km(loc[0], loc[1], lat, lon);
    }

    is_available_now() {
        const now = new Date();
        const now_h = now.getHours() * 100 + now.getMinutes();
        const start = parseInt(this.available_hours[0].replace(':', ''));
        const end = parseInt(this.available_hours[1].replace(':', ''));
        return start <= now_h && now_h <= end;
    }
}

class CallAttempt {
    constructor(attempt_id, human, method, distance_km, eta_minutes, message_sent) {
        this.attempt_id = attempt_id;
        this.human = human;
        this.method = method;
        this.status = CallStatus.PENDING;
        this.called_at = Date.now() / 1000;
        this.answered_at = null;
        this.timeout_at = null;
        this.message_sent = message_sent;
        this.response_received = '';
        this.distance_km = distance_km;
        this.eta_minutes = eta_minutes;
    }
}

class HumanNet {
    constructor(user_name = '', user_phone = '') {
        this.user_name = user_name;
        this.user_phone = user_phone;
        this.registry = {};
        this.call_history = [];
        this.active_calls = {};
        this.confirmed_helper = null;
        this.current_ring = null;
        this.user_location = null;
        this.user_disabilities = [];
        this.situation_description = '';
        this.auto_call_enabled = true;
        this.consent_given = true;
    }

    register_human(human) {
        this.registry[human.human_id] = human;
        return `${human.name} registrado no anel ${human.ring.name} (${human.authorization.value}).`;
    }

    remove_human(human_id) {
        if (human_id in this.registry) {
            const name = this.registry[human_id].name;
            delete this.registry[human_id];
            return `${name} removido.`;
        }
        return 'Humano nao encontrado.';
    }

    list_humans() {
        const by_ring = {};
        Object.values(this.registry).forEach(h => {
            if (!by_ring[h.ring.name]) by_ring[h.ring.name] = [];
            by_ring[h.ring.name].push(h);
        });
        return by_ring;
    }

    update_user_location(lat, lon) {
        this.user_location = [lat, lon];
    }

    update_human_location(human_id, lat, lon) {
        if (human_id in this.registry) {
            const h = this.registry[human_id];
            h.current_location = [lat, lon];
            h.last_location_update = Date.now() / 1000;
        }
    }

    rank_humans(max_ring = TrustRing.BYSTANDER, required_auth = AuthorizationLevel.LOW) {
        if (!this.user_location) return [];
        const ranked = [];
        const auth_order = [AuthorizationLevel.FULL, AuthorizationLevel.HIGH, AuthorizationLevel.MEDIUM, AuthorizationLevel.LOW, AuthorizationLevel.EMERGENCY_ONLY];
        Object.values(this.registry).forEach(human => {
            if (human.ring.value > max_ring.value) return;
            if (auth_order.indexOf(human.authorization) > auth_order.indexOf(required_auth)) return;
            if (human.ring !== TrustRing.EMERGENCY && !human.is_available_now()) return;
            const dist = human.distance_to(this.user_location[0], this.user_location[1]);
            if (dist > human.max_distance_km && human.ring !== TrustRing.EMERGENCY) return;
            ranked.push([human, dist]);
        });
        ranked.sort((a, b) => a[0].ring.value - b[0].ring.value || a[1] - b[1]);
        return ranked;
    }

    trigger_emergency_call(situation, user_lat = 0, user_lon = 0, severity = 'critical') {
        if (user_lat !== 0 && user_lon !== 0) this.update_user_location(user_lat, user_lon);
        this.situation_description = situation;
        this.confirmed_helper = null;
        this.active_calls = {};

        if (!this.user_location) {
            return { success: false, error: 'Sem localizacao do usuario. Nao posso chamar ajuda.', fallback: 'Ligar para 190 diretamente.' };
        }

        let max_ring = severity === 'catastrophic' ? TrustRing.EMERGENCY : severity === 'critical' ? TrustRing.PROFESSIONAL : TrustRing.COMMUNITY;
        let required_auth = (severity === 'critical' || severity === 'catastrophic') ? AuthorizationLevel.MEDIUM : AuthorizationLevel.LOW;

        const ranked = this.rank_humans(max_ring, required_auth);
        if (ranked.length === 0) return this._call_emergency_services(situation);

        const results = [];
        for (const [human, distance] of ranked) {
            this.current_ring = human.ring;
            const attempt = this._call_human(human, situation, distance);
            results.push(this._attempt_summary(attempt));
            if (attempt.status === CallStatus.CONFIRMED) {
                this.confirmed_helper = human;
                return {
                    success: true, helper: human.name, phone: human.phone, ring: human.ring.name,
                    distance_km: Math.round(distance * 100) / 100, eta_minutes: attempt.eta_minutes,
                    method: attempt.method.value,
                    message: `${human.name} confirmou! Esta a ${distance.toFixed(1)}km. Chega em ~${Math.round(attempt.eta_minutes)} minutos.`,
                    all_attempts: results
                };
            }
        }
        const emergency_result = this._call_emergency_services(situation);
        return {
            success: false, error: `Nenhum dos ${results.length} humanos disponiveis confirmou.`,
            all_attempts: results, escalated_to_emergency: true, emergency_result
        };
    }

    _call_human(human, situation, distance) {
        const attempt = new CallAttempt(
            `CALL-${human.human_id}-${Math.floor(Date.now() / 1000)}`,
            human, human.preferred_contact, distance, Math.max(1, distance * 3),
            this._build_message(human, situation, distance)
        );
        attempt.status = CallStatus.RINGING;
        this.active_calls[attempt.attempt_id] = attempt;

        const response_chance = {
            [TrustRing.FAMILY.name]: 0.85, [TrustRing.CAREGIVER.name]: 0.70, [TrustRing.COMMUNITY.name]: 0.50,
            [TrustRing.PROFESSIONAL.name]: 0.60, [TrustRing.EMERGENCY.name]: 0.90, [TrustRing.BYSTANDER.name]: 0.30
        };
        const chance = response_chance[human.ring.name] || 0.4;

        if (Math.random() < chance) {
            attempt.status = CallStatus.CONFIRMED;
            attempt.answered_at = Date.now() / 1000;
            attempt.response_received = `${human.name} confirmou que esta indo.`;
        } else {
            attempt.status = CallStatus.TIMEOUT;
            attempt.timeout_at = Date.now() / 1000;
            attempt.response_received = `Sem resposta de ${human.name} em ${human.response_timeout_s}s.`;
        }
        this.call_history.push(attempt);
        return attempt;
    }

    _build_message(human, situation, distance) {
        const disabilities_text = this.user_disabilities.length ? ` Condicao: ${this.user_disabilities.join(', ')}.` : '';
        return `Ola, ${human.name}? Aqui e a Iara, sistema da Republica. ${this.user_name} precisa de ajuda. ` +
            `Situacao: ${situation}. Localizacao aproximada: ${this.user_location[0].toFixed(4)}, ${this.user_location[1].toFixed(4)}. ` +
            `Voce esta a ${distance.toFixed(1)}km.${disabilities_text} Pode ir ate la ou ligar para confirmar que esta bem?`;
    }

    _call_emergency_services(situation) {
        let service, service_type;
        const lower = situation.toLowerCase();
        if (lower.includes('medica') || lower.includes('coracao') || lower.includes('machucad')) {
            service = '192 (SAMU)'; service_type = 'medica';
        } else if (lower.includes('incendio') || lower.includes('fogo')) {
            service = '193 (Bombeiros)'; service_type = 'bombeiros';
        } else {
            service = '190 (Policia)'; service_type = 'policia';
        }
        const msg = `LIGACAO AUTOMATICA para ${service}. Usuario: ${this.user_name}. Localizacao: ${this.user_location}. ` +
            `Situacao: ${situation}. Condicoes: ${this.user_disabilities.length ? this.user_disabilities.join(', ') : 'nenhuma'}. Nenhum contato pessoal respondeu.`;
        return { success: true, service, type: service_type, message: msg, note: 'Emergencia publica acionada. Ajuda a caminho.' };
    }

    cancel_emergency(reason = 'Usuario esta bem') {
        Object.values(this.active_calls).forEach(a => {
            if (a.status === CallStatus.RINGING || a.status === CallStatus.PENDING) a.status = CallStatus.CANCELLED;
        });
        this.confirmed_helper = null;
        return { cancelled: true, reason, message: `Emergencia cancelada. ${reason}. Todos os contatos foram avisados.` };
    }

    _attempt_summary(attempt) {
        return {
            human: attempt.human.name, ring: attempt.human.ring.name, phone: attempt.human.phone,
            method: attempt.method.value, status: attempt.status.value,
            distance_km: Math.round(attempt.distance_km * 100) / 100,
            eta_minutes: Math.round(attempt.eta_minutes * 10) / 10,
            response: attempt.response_received
        };
    }

    status() {
        const by_ring = this.list_humans();
        const humans_by_ring = {};
        Object.keys(by_ring).forEach(r => humans_by_ring[r] = by_ring[r].length);
        return {
            user_name: this.user_name, total_humans: Object.keys(this.registry).length, humans_by_ring,
            confirmed_helper: this.confirmed_helper ? this.confirmed_helper.name : null,
            current_ring: this.current_ring ? this.current_ring.name : null,
            active_calls: Object.keys(this.active_calls).length, total_calls_made: this.call_history.length,
            auto_call_enabled: this.auto_call_enabled, user_location: this.user_location
        };
    }
}

class ResilienceHumanBridge {
    constructor(human_net) {
        this.net = human_net;
        this.triggered = false;
        this.last_trigger_level = '';
    }
    static DEGRADATION_TRIGGERS = { sobrevivencia: 'critical', emergencia: 'catastrophic', morto: 'catastrophic' };

    check_and_trigger(degradation_level, user_lat = 0, user_lon = 0, situation = '') {
        const severity = ResilienceHumanBridge.DEGRADATION_TRIGGERS[degradation_level];
        if (!severity) {
            if (this.triggered) {
                const result = this.net.cancel_emergency('Sistema recuperado.');
                this.triggered = false;
                this.last_trigger_level = '';
                return result;
            }
            return null;
        }
        if (this.triggered && this.last_trigger_level === degradation_level) return null;
        this.triggered = true;
        this.last_trigger_level = degradation_level;
        if (!situation) situation = `Sistema em nivel ${degradation_level}. Possivel falha multipla.`;
        return this.net.trigger_emergency_call(situation, user_lat, user_lon, severity);
    }
}

function create_default_network(user_name = 'Cleiton') {
    const net = new HumanNet(user_name, '+5511****9999');
    net.user_disabilities = [];
    net.register_human(new AuthorizedHuman('ming', 'MING', '+5511****8888', TrustRing.FAMILY, AuthorizationLevel.FULL,
        'esposa', [-23.5505, -46.6333], ContactMethod.PHONE_CALL, ['primeiros_socorros'], true, true, 20, 30.0));
    net.register_human(new AuthorizedHuman('mae', 'Mae', '+5511****7777', TrustRing.FAMILY, AuthorizationLevel.FULL,
        'mae', [-23.5600, -46.6400], ContactMethod.PHONE_CALL, [], true, true, 30, 50.0));
    net.register_human(new AuthorizedHuman('andre', 'Andre Castro', '+5511****6666', TrustRing.CAREGIVER, AuthorizationLevel.HIGH,
        'parceiro', [-23.5450, -46.6300], ContactMethod.WHATSAPP, ['gestao', 'primeiros_socorros'], false, false, 45, 20.0));
    net.register_human(new AuthorizedHuman('aveone', 'AveOne', '+5511****5555', TrustRing.COMMUNITY, AuthorizationLevel.MEDIUM,
        'equipe infra', [-23.5700, -46.6500], ContactMethod.SMS, ['tecnologia', 'infraestrutura'], false, false, 60, 15.0));
    net.register_human(new AuthorizedHuman('dr_silva', 'Dr. Silva', '+5511****4444', TrustRing.PROFESSIONAL, AuthorizationLevel.HIGH,
        'medico de familia', [-23.5400, -46.6200], ContactMethod.PHONE_CALL, ['medico', 'primeiros_socorros', 'cardiologia'], false, true, 60, 10.0, ['07:00', '19:00']));
    return net;
}

// 6 CENARIOS COMPLETOS
function scenario_blind_lost_battery() {
    console.log('='.repeat(65));
    console.log('CENARIO 1: Cego perdido -- bateria em 1%');
    console.log('='.repeat(65));
    const net = create_default_network('Cleiton');
    net.user_disabilities = ['cegueira_total'];
    net.update_user_location(-23.5510, -46.6340);
    const result = net.trigger_emergency_call('Cego na rua, bateria do smartphone em 1%. Pode perder contato.', -23.5510, -46.6340, 'critical');
    console.log('\nResultado: ' + (result.success ? 'SUCESSO' : 'FALHOU'));
    if (result.success) {
        console.log(`Ajudante: ${result.helper} (anel ${result.ring})`);
        console.log(`Distancia: ${result.distance_km}km | ETA: ${Math.round(result.eta_minutes)}min`);
        console.log(`Metodo: ${result.method}`);
    } else {
        console.log('Erro: ' + (result.error || 'desconhecido'));
        if (result.escalated_to_emergency) console.log('Escalacao: ' + result.emergency_result.service);
    }
    console.log('\nTentativas:');
    (result.all_attempts || []).forEach(a => {
        const icon = a.status === 'confirmou' ? 'OK' : 'X ';
        console.log(`  [${icon}] ${a.human.padEnd(15)} anel=${a.ring.padEnd(12)} dist=${a.distance_km}km status=${a.status}`);
    });
}

function scenario_elderly_fall() {
    console.log('\n' + '='.repeat(65));
    console.log('CENARIO 2: Idosa caiu -- sem resposta em 30s');
    console.log('='.repeat(65));
    const net = new HumanNet('Dona Cecca', '+5511****3333');
    net.user_disabilities = ['idoso', 'osteoporose'];
    net.update_user_location(-23.5520, -46.6350);
    net.register_human(new AuthorizedHuman('filha', 'Maria Filha', '+5511****1111', TrustRing.FAMILY, AuthorizationLevel.FULL,
        'filha', [-23.5480, -46.6310], ContactMethod.PHONE_CALL, ['primeiros_socorros'], true, true, 20));
    net.register_human(new AuthorizedHuman('vizinha', 'Dona Ana', '+5511****2222', TrustRing.CAREGIVER, AuthorizationLevel.HIGH,
        'vizinha', [-23.5515, -46.6345], ContactMethod.PHONE_CALL, ['primeiros_socorros'], false, false, 30, 2.0));
    const result = net.trigger_emergency_call('Idosa caiu. Deteccao de queda pelo smartwatch. Sem resposta ha 30s.', -23.5520, -46.6350, 'catastrophic');
    console.log('\nResultado: ' + (result.success ? 'SUCESSO' : 'FALHOU'));
    if (result.success) {
        console.log(`Quem vai: ${result.helper} (${result.ring})`);
        console.log(`Distancia: ${result.distance_km}km | ETA: ${Math.round(result.eta_minutes)}min`);
    } else console.log('Escalacao: ' + result.escalated_to_emergency);
    console.log('\nTentativas:');
    (result.all_attempts || []).forEach(a => {
        const icon = a.status === 'confirmou' ? 'OK' : 'X ';
        console.log(`  [${icon}] ${a.human.padEnd(15)} anel=${a.ring.padEnd(12)} dist=${a.distance_km}km`);
    });
}

function scenario_seizure() {
    console.log('\n' + '='.repeat(65));
    console.log('CENARIO 3: Crise epileptica iminente');
    console.log('='.repeat(65));
    const net = create_default_network('Pedro');
    net.user_disabilities = ['epilepsia'];
    net.update_user_location(-23.5530, -46.6360);
    const result = net.trigger_emergency_call('Sinais pre-crise epileptica. Smartwatch detectou anomalia cardiaca + temperatura elevada.', 0, 0, 'critical');
    console.log('\nResultado: ' + (result.success ? 'SUCESSO' : 'FALHOU'));
    if (result.success) {
        console.log(`Ajudante: ${result.helper} (anel ${result.ring})`);
        console.log(`Distancia: ${result.distance_km}km | ETA: ${Math.round(result.eta_minutes)}min`);
    }
    console.log('\nTentativas:');
    (result.all_attempts || []).forEach(a => {
        const icon = a.status === 'confirmou' ? 'OK' : 'X ';
        console.log(`  [${icon}] ${a.human.padEnd(15)} dist=${a.distance_km}km status=${a.status}`);
    });
}

function scenario_resilience_integration() {
    console.log('\n' + '='.repeat(65));
    console.log('CENARIO 4: Integracao Resilience -> HumanNet');
    console.log('='.repeat(65));
    const net = create_default_network('Cleiton');
    net.update_user_location(-23.5510, -46.6340);
    const bridge = new ResilienceHumanBridge(net);
    console.log('\n[Nivel: completo]');
    let r = bridge.check_and_trigger('completo', -23.5510, -46.6340, '');
    console.log('  Resultado: ' + (r === null ? 'Sem acao' : JSON.stringify(r)));
    console.log('\n[Nivel: degradado_1]');
    r = bridge.check_and_trigger('degradado_1', -23.5510, -46.6340, '');
    console.log('  Resultado: ' + (r === null ? 'Sem acao -- sistema funcional' : JSON.stringify(r)));
    console.log('\n[Nivel: sobrevivencia] -> DISPARA HUMANOS');
    r = bridge.check_and_trigger('sobrevivencia', -23.5510, -46.6340, 'Bateria critica + GPS perdido. Usuario vulneravel.');
    if (r) {
        if (r.success) {
            console.log(`  AJUDANTE: ${r.helper} a ${r.distance_km}km`);
            console.log(`  ETA: ${Math.round(r.eta_minutes || 0)} min`);
        } else console.log('  Escalado para emergencia publica');
    } else console.log('  Nao disparou');
    console.log('\n[Nivel: completo novamente] -> CANCELA');
    r = bridge.check_and_trigger('completo', 0, 0, '');
    if (r) console.log('  ' + (r.message || 'Cancelado'));
}

function scenario_ring_escalation() {
    console.log('\n' + '='.repeat(65));
    console.log('CENARIO 5: Escalacao de aneis (ninguem atende)');
    console.log('='.repeat(65));
    const net = new HumanNet('Teste', '+5511****0000');
    net.update_user_location(-23.5500, -46.6300);
    net.register_human(new AuthorizedHuman('h1', 'Familiar 1', '+55111', TrustRing.FAMILY, AuthorizationLevel.FULL,
        'irmao', [-23.5490, -46.6290], ContactMethod.PHONE_CALL, [], false, false, 10));
    net.register_human(new AuthorizedHuman('h2', 'Cuidador 1', '+5512', TrustRing.CAREGIVER, AuthorizationLevel.HIGH,
        'cuidador', [-23.5480, -46.6280], ContactMethod.PHONE_CALL, [], false, false, 10));
    net.register_human(new AuthorizedHuman('h3', 'Comunidade 1', '+5513', TrustRing.COMMUNITY, AuthorizationLevel.MEDIUM,
        'vizinho Republica', [-23.5470, -46.6270], ContactMethod.PHONE_CALL, [], false, false, 10));
    const result = net.trigger_emergency_call('Usuario incapacitado. Necessita assistencia fisica imediata.', 0, 0, 'catastrophic');
    if (result.success) console.log('\nAlguem atendeu: ' + result.helper);
    else {
        console.log('\nNinguem atendeu nos aneis pessoais.');
        if (result.escalated_to_emergency) console.log('Escalacao para emergencia publica: ' + result.emergency_result.service);
    }
    console.log('\nTentativas (' + (result.all_attempts || []).length + '):');
    (result.all_attempts || []).forEach(a => {
        const icon = a.status === 'confirmou' ? 'OK' : 'X ';
        console.log(`  [${icon}] anel=${a.ring.padEnd(12)} ${a.human.padEnd(15)} dist=${a.distance_km}km`);
    });
}

function scenario_child_lost() {
    console.log('\n' + '='.repeat(65));
    console.log('CENARIO 6: Crianca perdida no shopping');
    console.log('='.repeat(65));
    const net = new HumanNet('Sophia (8 anos)', '+5511****0000');
    net.update_user_location(-23.5610, -46.6560);
    net.register_human(new AuthorizedHuman('pai', 'Cleiton (Pai)', '+5511****9999', TrustRing.FAMILY, AuthorizationLevel.FULL,
        'pai', [-23.5505, -46.6333], ContactMethod.PHONE_CALL, [], false, false, 15, 20.0));
    net.register_human(new AuthorizedHuman('mae', 'MING (Mae)', '+5511****8888', TrustRing.FAMILY, AuthorizationLevel.FULL,
        'mae', [-23.5505, -46.6333], ContactMethod.PHONE_CALL, [], false, false, 15, 20.0));
    const result = net.trigger_emergency_call('Crianca de 8 anos separada dos pais no shopping. Sistema da Republica detectou saida de zona segura.', 0, 0, 'critical');
    if (result.success) {
        console.log('\n' + result.helper + ' confirmou! Esta a caminho.');
        console.log(`Distancia: ${result.distance_km}km | ETA: ${Math.round(result.eta_minutes)}min`);
    } else console.log('\nEscalado para emergencia.');
}

function demo() {
    console.log('='.repeat(70));
    console.log('OpenHumanNet -- Chamar o Humano Autorizado Mais Proximo');
    console.log('='.repeat(70));
    const net = create_default_network('Cleiton');
    net.update_user_location(-23.5505, -46.6333);
    console.log('\nUsuario: ' + net.user_name);
    console.log('Localizacao: ' + net.user_location);
    console.log('Humanos registrados: ' + Object.keys(net.registry).length);
    const humans_by_ring = net.list_humans();
    console.log('\nRede por aneis:');
    Object.values(TrustRing).forEach(ring => {
        const humans = humans_by_ring[ring.name] || [];
        console.log(`  Anel ${ring.value} (${ring.name}): ${humans.length} humano(s)`);
        humans.forEach(h => {
            const dist = h.distance_to(-23.5505, -46.6333);
            console.log(`    - ${h.name.padEnd(15)} (${h.relationship.padEnd(15)}) auth=${h.authorization.value.padEnd(15)} dist=${dist.toFixed(1)}km`);
        });
    });
    scenario_blind_lost_battery();
    scenario_elderly_fall();
    scenario_seizure();
    scenario_resilience_integration();
    scenario_ring_escalation();
    scenario_child_lost();
    console.log('\n' + '='.repeat(70));
    console.log('COBERTURA DO SISTEMA');
    console.log('='.repeat(70));
    console.log('\n  Aneis de confianca: ' + Object.keys(TrustRing).length);
    Object.values(TrustRing).forEach(r => console.log(`    Anel ${r.value}: ${r.name}`));
    console.log('\n  Niveis de autorizacao: ' + Object.keys(AuthorizationLevel).length);
    Object.values(AuthorizationLevel).forEach(a => console.log(`    ${a.value}`));
    console.log('\n  Metodos de contato: ' + Object.keys(ContactMethod).length);
    Object.values(ContactMethod).forEach(c => console.log(`    ${c.value}`));
    console.log('\n  Estados de chamada: ' + Object.keys(CallStatus).length);
    console.log('\n  FLUXO DE PRIORIDADE:');
    console.log('    1. Sistema detecta falha (OpenResilience: SURVIVAL/EMERGENCY)');
    console.log('    2. Pegar localizacao do usuario (GPS/ultima/triangulacao)');
    console.log('    3. Ranquear humanos: anel -> distancia -> disponibilidade');
    console.log('    4. Chamar Anel 0 (Familia) primeiro');
    console.log('    5. Se familia nao atende -> Anel 1 (Cuidador)');
    console.log('    6. Se cuidador nao atende -> Anel 2 (Comunidade)');
    console.log('    7. Se comunidade nao atende -> Anel 3 (Profissional)');
    console.log('    8. Se profissional nao atende -> Anel 4 (190/192/193)');
    console.log('    9. PARAR quando humano CONFIRMA que vai ajudar');
    console.log('   10. Se ninguem -> Anel 5 (estranho proximo via appel)');
    console.log('\n' + '='.repeat(70));
    console.log('A tecnologia NAO substitui o humano.');
    console.log('A tecnologia CONECTA o humano CERTO no momento CERTO.');
    console.log('\nTODO hardware falha. TODO software cai.');
    console.log('O HUMANO e o sistema final. Ele nunca falha.');
}

if (require.main === module) {
    demo();
}

module.exports = { TrustRing, AuthorizationLevel, ContactMethod, CallStatus, AuthorizedHuman, HumanNet, ResilienceHumanBridge, create_default_network, demo };