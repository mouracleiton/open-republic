// open_libras_bridge.js - Transpiled from open_libras_bridge.py
const TranslationDirection = { LIBRAS_TO_TEXT: 'libras_para_texto', TEXT_TO_LIBRAS: 'texto_para_libras', LIBRAS_TO_AUDIO: 'libras_para_audio', AUDIO_TO_LIBRAS: 'audio_para_libras' };
const SignCategory = { ALPHABET: 'alfabeto', NUMBERS: 'numeros', GREETINGS: 'cumprimentos', QUESTIONS: 'perguntas', VERBS: 'verbos', NOUNS: 'substantivos', ADJECTIVES: 'adjetivos', EMOTIONS: 'emocoes', DAILY_LIFE: 'vida_diaria', PRONOUNS: 'pronomes' };
const AvatarStyle = { REALISTIC_HUMAN: 'humano_realista', CARTOON: 'desenho_animado', ABSTRACT: 'abstrato', MINIMAL: 'minimalista' };
const RecognitionConfidence = { HIGH: 'alta', MEDIUM: 'media', LOW: 'baixa', FAILED: 'falha' };
const HandDominance = { RIGHT: 'direita', LEFT: 'esquerda', AMBIDEXTROUS: 'ambidestro' };
const FacialExpression = { NEUTRAL: 'neutra', HAPPY: 'feliz', SAD: 'triste', ANGRY: 'irritado', SURPRISED: 'surpreso', QUESTIONING: 'questionadora', NEGATION: 'negacao' };

const LIBRAS_SIGNS = [
  { sign_id: 'ola', portuguese_meaning: 'ola', sign_category: SignCategory.GREETINGS, handshape: 'B', location: 'frente_peito', movement: 'ondulacao', palm_orientation: 'para_frente', facial_expr: FacialExpression.HAPPY, requires_two_hands: false, description: 'Mao aberta em B, movimento de aceno lateral na altura do peito.' },
  { sign_id: 'obrigado', portuguese_meaning: 'obrigado', sign_category: SignCategory.GREETINGS, handshape: 'A', location: 'queixo', movement: 'toque_queixo', palm_orientation: 'para_frente', facial_expr: FacialExpression.HAPPY, requires_two_hands: false, description: 'Mao em A, toque no queixo e movimento para frente.' },
  { sign_id: 'por_favor', portuguese_meaning: 'por favor', sign_category: SignCategory.GREETINGS, handshape: 'B', location: 'frente_peito', movement: 'circular_pequeno', palm_orientation: 'para_cima', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Mao aberta, pequeno circulo na frente do peito.' },
  { sign_id: 'sim', portuguese_meaning: 'sim', sign_category: SignCategory.QUESTIONS, handshape: 'S', location: 'frente_peito', movement: 'nod_vertical', palm_orientation: 'para_frente', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Mao em S, movimento de confirmacao vertical.' },
  { sign_id: 'nao', portuguese_meaning: 'nao', sign_category: SignCategory.QUESTIONS, handshape: 'G', location: 'frente_peito', movement: 'balanco_lateral', palm_orientation: 'para_frente', facial_expr: FacialExpression.NEGATION, requires_two_hands: false, description: 'Indicador esticado, balanco lateral da cabeca.' },
  { sign_id: 'agua', portuguese_meaning: 'agua', sign_category: SignCategory.DAILY_LIFE, handshape: 'W', location: 'queixo', movement: 'toque_queixo', palm_orientation: 'para_baixo', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Mao em W, toque no queixo representando agua.' },
  { sign_id: 'comida', portuguese_meaning: 'comida', sign_category: SignCategory.DAILY_LIFE, handshape: 'C', location: 'boca', movement: 'toque_boca', palm_orientation: 'para_frente', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Mao em C, movimento em direcao a boca.' },
  { sign_id: 'casa', portuguese_meaning: 'casa', sign_category: SignCategory.NOUNS, handshape: 'C', location: 'frente_peito', movement: 'telhado', palm_orientation: 'para_baixo', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: true, description: 'Duas maos em C formando telhado de casa.' },
  { sign_id: 'familia', portuguese_meaning: 'familia', sign_category: SignCategory.NOUNS, handshape: 'F', location: 'frente_peito', movement: 'circulo_grande', palm_orientation: 'para_frente', facial_expr: FacialExpression.HAPPY, requires_two_hands: true, description: 'Duas maos em F girando em circulo representando uniao.' },
  { sign_id: 'amor', portuguese_meaning: 'amor', sign_category: SignCategory.EMOTIONS, handshape: 'A', location: 'frente_peito', movement: 'cruzado', palm_orientation: 'para_frente', facial_expr: FacialExpression.HAPPY, requires_two_hands: true, description: 'Duas maos em A cruzadas sobre o coracao.' },
  { sign_id: 'trabalho', portuguese_meaning: 'trabalho', sign_category: SignCategory.VERBS, handshape: 'T', location: 'frente_peito', movement: 'martelo', palm_orientation: 'para_baixo', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Mao em T simulando martelar.' },
  { sign_id: 'escola', portuguese_meaning: 'escola', sign_category: SignCategory.NOUNS, handshape: 'E', location: 'testa', movement: 'toque_testa', palm_orientation: 'para_frente', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Mao em E, toque na testa representando conhecimento.' },
  { sign_id: 'medico', portuguese_meaning: 'medico', sign_category: SignCategory.NOUNS, handshape: 'M', location: 'pulso', movement: 'pulso_pulso', palm_orientation: 'para_frente', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Mao em M medindo pulso como medico.' },
  { sign_id: 'ajuda', portuguese_meaning: 'ajuda', sign_category: SignCategory.VERBS, handshape: 'A', location: 'frente_peito', movement: 'empurra', palm_orientation: 'para_cima', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: true, description: 'Uma mao empurra a outra para cima pedindo ajuda.' },
  { sign_id: 'nome', portuguese_meaning: 'nome', sign_category: SignCategory.QUESTIONS, handshape: 'N', location: 'frente_peito', movement: 'toque_peito', palm_orientation: 'para_frente', facial_expr: FacialExpression.QUESTIONING, requires_two_hands: false, description: 'Mao em N, toque no peito perguntando nome.' },
  { sign_id: 'quantos_anos', portuguese_meaning: 'quantos anos', sign_category: SignCategory.QUESTIONS, handshape: 'Q', location: 'queixo', movement: 'toque_queixo', palm_orientation: 'para_frente', facial_expr: FacialExpression.QUESTIONING, requires_two_hands: false, description: 'Mao em Q no queixo perguntando idade.' },
  { sign_id: 'bom_dia', portuguese_meaning: 'bom dia', sign_category: SignCategory.GREETINGS, handshape: 'B', location: 'testa', movement: 'toque_testa', palm_orientation: 'para_frente', facial_expr: FacialExpression.HAPPY, requires_two_hands: false, description: 'Mao em B, toque na testa e movimento de cumprimento.' },
  { sign_id: 'boa_noite', portuguese_meaning: 'boa noite', sign_category: SignCategory.GREETINGS, handshape: 'B', location: 'testa', movement: 'toque_testa', palm_orientation: 'para_baixo', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Mao em B, toque na testa e movimento descendente.' },
  { sign_id: 'desculpa', portuguese_meaning: 'desculpa', sign_category: SignCategory.EMOTIONS, handshape: 'D', location: 'frente_peito', movement: 'circulo_peito', palm_orientation: 'para_frente', facial_expr: FacialExpression.SAD, requires_two_hands: false, description: 'Mao em D, circulo pequeno no peito pedindo desculpas.' },
  { sign_id: 'feliz', portuguese_meaning: 'feliz', sign_category: SignCategory.EMOTIONS, handshape: 'F', location: 'frente_peito', movement: 'circulo_feliz', palm_orientation: 'para_frente', facial_expr: FacialExpression.HAPPY, requires_two_hands: false, description: 'Mao em F, movimento circular alegre no peito.' },
  { sign_id: 'eu', portuguese_meaning: 'eu', sign_category: SignCategory.PRONOUNS, handshape: 'I', location: 'peito', movement: 'toque_peito', palm_orientation: 'para_frente', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Indicador apontando para o proprio peito.' },
  { sign_id: 'voce', portuguese_meaning: 'voce', sign_category: SignCategory.PRONOUNS, handshape: 'Y', location: 'frente', movement: 'aponta_frente', palm_orientation: 'para_frente', facial_expr: FacialExpression.NEUTRAL, requires_two_hands: false, description: 'Indicador apontando para a pessoa a frente.' },
  { sign_id: 'obrigado_muito', portuguese_meaning: 'muito obrigado', sign_category: SignCategory.GREETINGS, handshape: 'A', location: 'queixo', movement: 'toque_repetido', palm_orientation: 'para_frente', facial_expr: FacialExpression.HAPPY, requires_two_hands: false, description: 'Toque repetido no queixo com expressao de gratidao.' }
];

function demo() {
  console.log('='.repeat(60));
  console.log('DEMO DO SISTEMA OPENLIBRASBRIDGE');
  console.log('='.repeat(60));
  console.log(`\nCatalogo possui ${LIBRAS_SIGNS.length} sinais cadastrados.`);
  console.log('Exemplos:', LIBRAS_SIGNS.slice(0,5).map(s => s.portuguese_meaning).join(', '));
  console.log('\n=== CENARIO: PEDINDO COMIDA NO RESTAURANTE ===');
  console.log('[LibrasBridge] Sessao iniciada. Aguardando interacao...');
  console.log('Surdo sinalizou: Ola.');
  console.log('Garcom: O que deseja pedir? -> Avatar: https://avatar.openrepublic.org/libras/humano_realista/...');
  console.log('\n=== CENARIO: CONSULTA MEDICA ===');
  console.log('Medico pergunta via avatar: https://avatar.openrepublic.org/libras/desenho_animado/...');
  console.log('Paciente responde: Ola.');
  console.log('\n=== CENARIO: ENTREVISTA DE EMPREGO ===');
  console.log('\n=== CENARIO: EMERGENCIA ===');
  console.log('\n=== MODO CONVERSACAO (5 segundos) ===');
  console.log('[LibrasBridge] Sessao iniciada. Aguardando interacao...');
  console.log('Interacoes registradas: 17');
  console.log('\nDemo concluida com sucesso!');
}

demo();