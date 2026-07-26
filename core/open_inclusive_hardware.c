/* OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel
================================================================
"O hardware certo transforma uma deficiencia em uma capacidade.
O cego tem o smartphone como olhos. O surdo tem o smartwatch como ouvidos.
O tetraplegico tem o eye-tracker como maos. O autista tem o fone como escudo.

A IDE nao escolhe o hardware. O HARDWARE DO USUARIO escolhe a IDE.
Se a pessoa tem um smartphone Android de R$300, a IDE funciona.
Se a pessoa tem um SmartWatch, a IDE funciona.
Se a pessoa tem um eye-tracker de R$15.000, a IDE funciona.
Se a pessoa NAO TEM NADA, a IDE funciona no terminal publico (OpenTerminal).

ZERO barreira de hardware. ZERO custo de entrada. MAXIMA adaptacao.

Integrado com:
- OpenInclusiveIDE (IDE se adapta ao hardware disponivel)
- OpenTerminal (todo terminal publico roda a IDE)
- OpenAbsence (hardware respeita pausas)
- OpenBodilyAutonomy (usuario controla seu dispositivo)
- OpenSilencePolicy (dispositivos respeitam o silencio)

HARDWARE MAPEADO (6 CATEGORIAS, 40+ DISPOSITIVOS):

1. MASSA (smartphone, tablet, smartwatch, notebook, desktop)
   - Disponivel em qualquer lugar, barato, ubiquo
   
2. ASSISTIVO VISUAL (leitor de tela, display braille, lupa eletronica)
   - Para cegos e baixa visao
   
3. ASSISTIVO MOTOR (eye-tracker, switch, teclado especial, BCI)
   - Para deficiencias motoras severas
   
4. ASSISTIVO AUDITIVO (implante coclear, aparelho auditivo, loop)
   - Para surdos e baixa audicao
   
5. ASSISTIVO COGNITIVO (fone ANC, luz inteligente, weighted blanket)
   - Para autismo, TDAH, epilepsia
   
6. TERMINAL PUBLICO (TV, kiosk, terminal burro, computador comunitario)
   - Para quem nao tem hardware proprio

PRINCIPIO CHAVE: O hardware NAO define o desenvolvedor.
O desenvolvedor define o hardware. A IDE se adapta.

Author: OpenRepublic Team (Cleiton Cofundador + MING Cofundadora -- 50/50)
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

// ============================================================================
// 1. CATEGORIAS DE HARDWARE
// ============================================================================

typedef enum {
    MASS = 0,
    ASSISTIVE_VISUAL,
    ASSISTIVE_MOTOR,
    ASSISTIVE_AUDITORY,
    ASSISTIVE_COGNITIVE,
    TERMINAL_PUBLIC,
    WEARABLE,
    BRAIN
} HardwareCategory;

typedef enum {
    FREE = 0,
    VERY_LOW,
    LOW,
    MEDIUM,
    HIGH,
    VERY_HIGH,
    SUBSIDIZED
} HardwareCost;

typedef enum {
    UBIQUITOUS = 0,
    COMMON,
    SPECIALIZED,
    MEDICAL,
    RARE,
    EXPERIMENTAL
} HardwareAvailability;

typedef enum {
    BLUETOOTH = 0,
    USB,
    WIFI,
    NFC,
    CLOUD,
    AUDIO_JACK,
    PROPRIETARY,
    WIRELESS,
    HDMI
} ConnectionType;

// ============================================================================
// 2. PERFIL DE HARDWARE
// ============================================================================

typedef struct {
    char device_id[16];
    char name[128];
    HardwareCategory category;
    HardwareCost cost;
    HardwareAvailability availability;
    ConnectionType connections[8];
    int num_connections;
    char platforms[8][32];
    int num_platforms;
    char disabilities_served[16][32];
    int num_disabilities;
    char input_capabilities[16][32];
    int num_inputs;
    char output_capabilities[16][32];
    int num_outputs;
    float battery_hours;
    bool offline_capable;
    char languages_supported[4][16];
    int num_languages;
    char description[512];
} HardwareDevice;

// ============================================================================
// 3. CATALOGO DE HARDWARE (44 DISPOSITIVOS)
// ============================================================================

HardwareDevice HARDWARE_CATALOG[44];
int HARDWARE_CATALOG_SIZE = 44;

// Funcoes para popular o catalogo (simulacao de inicializacao)
void init_hardware_catalog() {
    // HW-001
    strcpy(HARDWARE_CATALOG[0].device_id, "HW-001");
    strcpy(HARDWARE_CATALOG[0].name, "Smartphone Android (qualquer)");
    HARDWARE_CATALOG[0].category = MASS;
    HARDWARE_CATALOG[0].cost = LOW;
    HARDWARE_CATALOG[0].availability = UBIQUITOUS;
    HARDWARE_CATALOG[0].connections[0] = BLUETOOTH; HARDWARE_CATALOG[0].connections[1] = USB; HARDWARE_CATALOG[0].connections[2] = WIFI; HARDWARE_CATALOG[0].connections[3] = NFC; HARDWARE_CATALOG[0].connections[4] = AUDIO_JACK;
    HARDWARE_CATALOG[0].num_connections = 5;
    strcpy(HARDWARE_CATALOG[0].platforms[0], "Android"); HARDWARE_CATALOG[0].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[0].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[0].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[0].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[0].disabilities_served[3], "cognitiva"); strcpy(HARDWARE_CATALOG[0].disabilities_served[4], "espectro_autista"); strcpy(HARDWARE_CATALOG[0].disabilities_served[5], "desenvolvimento"); strcpy(HARDWARE_CATALOG[0].disabilities_served[6], "multipla"); strcpy(HARDWARE_CATALOG[0].disabilities_served[7], "temporaria");
    HARDWARE_CATALOG[0].num_disabilities = 8;
    strcpy(HARDWARE_CATALOG[0].input_capabilities[0], "touch"); strcpy(HARDWARE_CATALOG[0].input_capabilities[1], "voice"); strcpy(HARDWARE_CATALOG[0].input_capabilities[2], "camera"); strcpy(HARDWARE_CATALOG[0].input_capabilities[3], "microphone"); strcpy(HARDWARE_CATALOG[0].input_capabilities[4], "bluetooth_keyboard"); strcpy(HARDWARE_CATALOG[0].input_capabilities[5], "nfc"); strcpy(HARDWARE_CATALOG[0].input_capabilities[6], "accelerometer"); strcpy(HARDWARE_CATALOG[0].input_capabilities[7], "gyroscope");
    HARDWARE_CATALOG[0].num_inputs = 8;
    strcpy(HARDWARE_CATALOG[0].output_capabilities[0], "screen"); strcpy(HARDWARE_CATALOG[0].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[0].output_capabilities[2], "vibration"); strcpy(HARDWARE_CATALOG[0].output_capabilities[3], "flash_led"); strcpy(HARDWARE_CATALOG[0].output_capabilities[4], "screen_reader");
    HARDWARE_CATALOG[0].num_outputs = 5;
    HARDWARE_CATALOG[0].battery_hours = 12.0f;
    HARDWARE_CATALOG[0].offline_capable = true;
    strcpy(HARDWARE_CATALOG[0].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[0].num_languages = 1;
    strcpy(HARDWARE_CATALOG[0].description, "O dispositivo mais inclusivo do planeta. TalkBack, Voice Access, Switch Access nativos.");

    // HW-002
    strcpy(HARDWARE_CATALOG[1].device_id, "HW-002");
    strcpy(HARDWARE_CATALOG[1].name, "iPhone (qualquer)");
    HARDWARE_CATALOG[1].category = MASS;
    HARDWARE_CATALOG[1].cost = MEDIUM;
    HARDWARE_CATALOG[1].availability = UBIQUITOUS;
    HARDWARE_CATALOG[1].connections[0] = BLUETOOTH; HARDWARE_CATALOG[1].connections[1] = USB; HARDWARE_CATALOG[1].connections[2] = WIFI; HARDWARE_CATALOG[1].connections[3] = NFC;
    HARDWARE_CATALOG[1].num_connections = 4;
    strcpy(HARDWARE_CATALOG[1].platforms[0], "iOS"); HARDWARE_CATALOG[1].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[1].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[1].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[1].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[1].disabilities_served[3], "cognitiva"); strcpy(HARDWARE_CATALOG[1].disabilities_served[4], "espectro_autista"); strcpy(HARDWARE_CATALOG[1].disabilities_served[5], "desenvolvimento"); strcpy(HARDWARE_CATALOG[1].disabilities_served[6], "multipla"); strcpy(HARDWARE_CATALOG[1].disabilities_served[7], "temporaria");
    HARDWARE_CATALOG[1].num_disabilities = 8;
    strcpy(HARDWARE_CATALOG[1].input_capabilities[0], "touch"); strcpy(HARDWARE_CATALOG[1].input_capabilities[1], "voice"); strcpy(HARDWARE_CATALOG[1].input_capabilities[2], "face_id"); strcpy(HARDWARE_CATALOG[1].input_capabilities[3], "camera"); strcpy(HARDWARE_CATALOG[1].input_capabilities[4], "microphone"); strcpy(HARDWARE_CATALOG[1].input_capabilities[5], "bluetooth_keyboard"); strcpy(HARDWARE_CATALOG[1].input_capabilities[6], "lidar");
    HARDWARE_CATALOG[1].num_inputs = 7;
    strcpy(HARDWARE_CATALOG[1].output_capabilities[0], "screen"); strcpy(HARDWARE_CATALOG[1].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[1].output_capabilities[2], "vibration"); strcpy(HARDWARE_CATALOG[1].output_capabilities[3], "taptic_engine"); strcpy(HARDWARE_CATALOG[1].output_capabilities[4], "voiceover"); strcpy(HARDWARE_CATALOG[1].output_capabilities[5], "flash_led");
    HARDWARE_CATALOG[1].num_outputs = 6;
    HARDWARE_CATALOG[1].battery_hours = 15.0f;
    HARDWARE_CATALOG[1].offline_capable = true;
    strcpy(HARDWARE_CATALOG[1].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[1].num_languages = 1;
    strcpy(HARDWARE_CATALOG[1].description, "VoiceOver, Switch Control, Voice Control, Sound Detection nativos. Lidar para deteccao de obstaculos.");

    // HW-003
    strcpy(HARDWARE_CATALOG[2].device_id, "HW-003");
    strcpy(HARDWARE_CATALOG[2].name, "Smartphone basico (teclado fisico)");
    HARDWARE_CATALOG[2].category = MASS;
    HARDWARE_CATALOG[2].cost = VERY_LOW;
    HARDWARE_CATALOG[2].availability = COMMON;
    HARDWARE_CATALOG[2].connections[0] = AUDIO_JACK; HARDWARE_CATALOG[2].connections[1] = BLUETOOTH;
    HARDWARE_CATALOG[2].num_connections = 2;
    strcpy(HARDWARE_CATALOG[2].platforms[0], "KaiOS"); strcpy(HARDWARE_CATALOG[2].platforms[1], "Feature Phone"); HARDWARE_CATALOG[2].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[2].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[2].disabilities_served[1], "motora"); strcpy(HARDWARE_CATALOG[2].disabilities_served[2], "temporaria");
    HARDWARE_CATALOG[2].num_disabilities = 3;
    strcpy(HARDWARE_CATALOG[2].input_capabilities[0], "keypad"); strcpy(HARDWARE_CATALOG[2].input_capabilities[1], "voice"); strcpy(HARDWARE_CATALOG[2].input_capabilities[2], "microphone");
    HARDWARE_CATALOG[2].num_inputs = 3;
    strcpy(HARDWARE_CATALOG[2].output_capabilities[0], "screen_small"); strcpy(HARDWARE_CATALOG[2].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[2].output_capabilities[2], "vibration"); strcpy(HARDWARE_CATALOG[2].output_capabilities[3], "tts_basic");
    HARDWARE_CATALOG[2].num_outputs = 4;
    HARDWARE_CATALOG[2].battery_hours = 72.0f;
    HARDWARE_CATALOG[2].offline_capable = true;
    strcpy(HARDWARE_CATALOG[2].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[2].num_languages = 1;
    strcpy(HARDWARE_CATALOG[2].description, "Telefone botoeiro com TTS. Para quem nao tem smartphone ou prefere teclado fisico.");

    // HW-004
    strcpy(HARDWARE_CATALOG[3].device_id, "HW-004");
    strcpy(HARDWARE_CATALOG[3].name, "Tablet Android");
    HARDWARE_CATALOG[3].category = MASS;
    HARDWARE_CATALOG[3].cost = MEDIUM;
    HARDWARE_CATALOG[3].availability = UBIQUITOUS;
    HARDWARE_CATALOG[3].connections[0] = BLUETOOTH; HARDWARE_CATALOG[3].connections[1] = USB; HARDWARE_CATALOG[3].connections[2] = WIFI;
    HARDWARE_CATALOG[3].num_connections = 3;
    strcpy(HARDWARE_CATALOG[3].platforms[0], "Android"); HARDWARE_CATALOG[3].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[3].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[3].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[3].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[3].disabilities_served[3], "cognitiva"); strcpy(HARDWARE_CATALOG[3].disabilities_served[4], "espectro_autista"); strcpy(HARDWARE_CATALOG[3].disabilities_served[5], "desenvolvimento");
    HARDWARE_CATALOG[3].num_disabilities = 6;
    strcpy(HARDWARE_CATALOG[3].input_capabilities[0], "touch"); strcpy(HARDWARE_CATALOG[3].input_capabilities[1], "voice"); strcpy(HARDWARE_CATALOG[3].input_capabilities[2], "camera"); strcpy(HARDWARE_CATALOG[3].input_capabilities[3], "microphone"); strcpy(HARDWARE_CATALOG[3].input_capabilities[4], "stylus"); strcpy(HARDWARE_CATALOG[3].input_capabilities[5], "bluetooth_keyboard");
    HARDWARE_CATALOG[3].num_inputs = 6;
    strcpy(HARDWARE_CATALOG[3].output_capabilities[0], "screen_large"); strcpy(HARDWARE_CATALOG[3].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[3].output_capabilities[2], "vibration");
    HARDWARE_CATALOG[3].num_outputs = 3;
    HARDWARE_CATALOG[3].battery_hours = 10.0f;
    HARDWARE_CATALOG[3].offline_capable = true;
    strcpy(HARDWARE_CATALOG[3].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[3].num_languages = 1;
    strcpy(HARDWARE_CATALOG[3].description, "Tela maior = mais area para botoes grandes, blocos visuais, zoom.");

    // HW-005
    strcpy(HARDWARE_CATALOG[4].device_id, "HW-005");
    strcpy(HARDWARE_CATALOG[4].name, "iPad");
    HARDWARE_CATALOG[4].category = MASS;
    HARDWARE_CATALOG[4].cost = MEDIUM;
    HARDWARE_CATALOG[4].availability = UBIQUITOUS;
    HARDWARE_CATALOG[4].connections[0] = BLUETOOTH; HARDWARE_CATALOG[4].connections[1] = USB; HARDWARE_CATALOG[4].connections[2] = WIFI;
    HARDWARE_CATALOG[4].num_connections = 3;
    strcpy(HARDWARE_CATALOG[4].platforms[0], "iPadOS"); HARDWARE_CATALOG[4].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[4].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[4].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[4].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[4].disabilities_served[3], "cognitiva"); strcpy(HARDWARE_CATALOG[4].disabilities_served[4], "espectro_autista"); strcpy(HARDWARE_CATALOG[4].disabilities_served[5], "desenvolvimento");
    HARDWARE_CATALOG[4].num_disabilities = 6;
    strcpy(HARDWARE_CATALOG[4].input_capabilities[0], "touch"); strcpy(HARDWARE_CATALOG[4].input_capabilities[1], "voice"); strcpy(HARDWARE_CATALOG[4].input_capabilities[2], "face_id"); strcpy(HARDWARE_CATALOG[4].input_capabilities[3], "camera"); strcpy(HARDWARE_CATALOG[4].input_capabilities[4], "microphone"); strcpy(HARDWARE_CATALOG[4].input_capabilities[5], "stylus_pencil"); strcpy(HARDWARE_CATALOG[4].input_capabilities[6], "lidar");
    HARDWARE_CATALOG[4].num_inputs = 7;
    strcpy(HARDWARE_CATALOG[4].output_capabilities[0], "screen_large"); strcpy(HARDWARE_CATALOG[4].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[4].output_capabilities[2], "taptic_engine"); strcpy(HARDWARE_CATALOG[4].output_capabilities[3], "voiceover");
    HARDWARE_CATALOG[4].num_outputs = 4;
    HARDWARE_CATALOG[4].battery_hours = 10.0f;
    HARDWARE_CATALOG[4].offline_capable = true;
    strcpy(HARDWARE_CATALOG[4].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[4].num_languages = 1;
    strcpy(HARDWARE_CATALOG[4].description, "Apple Pencil para deteccao de tremores. AssistiveTouch. Full Keyboard Control.");

    // HW-006
    strcpy(HARDWARE_CATALOG[5].device_id, "HW-006");
    strcpy(HARDWARE_CATALOG[5].name, "Smartwatch Android (WearOS)");
    HARDWARE_CATALOG[5].category = WEARABLE;
    HARDWARE_CATALOG[5].cost = MEDIUM;
    HARDWARE_CATALOG[5].availability = COMMON;
    HARDWARE_CATALOG[5].connections[0] = BLUETOOTH; HARDWARE_CATALOG[5].connections[1] = WIFI;
    HARDWARE_CATALOG[5].num_connections = 2;
    strcpy(HARDWARE_CATALOG[5].platforms[0], "WearOS"); HARDWARE_CATALOG[5].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[5].disabilities_served[0], "auditiva"); strcpy(HARDWARE_CATALOG[5].disabilities_served[1], "motora"); strcpy(HARDWARE_CATALOG[5].disabilities_served[2], "cognitiva"); strcpy(HARDWARE_CATALOG[5].disabilities_served[3], "temporaria");
    HARDWARE_CATALOG[5].num_disabilities = 4;
    strcpy(HARDWARE_CATALOG[5].input_capabilities[0], "touch_small"); strcpy(HARDWARE_CATALOG[5].input_capabilities[1], "voice"); strcpy(HARDWARE_CATALOG[5].input_capabilities[2], "microphone"); strcpy(HARDWARE_CATALOG[5].input_capabilities[3], "accelerometer"); strcpy(HARDWARE_CATALOG[5].input_capabilities[4], "heart_rate"); strcpy(HARDWARE_CATALOG[5].input_capabilities[5], "gestures"); strcpy(HARDWARE_CATALOG[5].input_capabilities[6], "crown");
    HARDWARE_CATALOG[5].num_inputs = 7;
    strcpy(HARDWARE_CATALOG[5].output_capabilities[0], "screen_tiny"); strcpy(HARDWARE_CATALOG[5].output_capabilities[1], "vibration"); strcpy(HARDWARE_CATALOG[5].output_capabilities[2], "speaker_tiny"); strcpy(HARDWARE_CATALOG[5].output_capabilities[3], "haptic");
    HARDWARE_CATALOG[5].num_outputs = 4;
    HARDWARE_CATALOG[5].battery_hours = 24.0f;
    HARDWARE_CATALOG[5].offline_capable = true;
    strcpy(HARDWARE_CATALOG[5].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[5].num_languages = 1;
    strcpy(HARDWARE_CATALOG[5].description, "Vibracao no pulso para alertas (surdez). Monitor de batimento (epilepsia/ansiedade). Coroa para navegacao (motor).");

    // HW-007
    strcpy(HARDWARE_CATALOG[6].device_id, "HW-007");
    strcpy(HARDWARE_CATALOG[6].name, "Apple Watch");
    HARDWARE_CATALOG[6].category = WEARABLE;
    HARDWARE_CATALOG[6].cost = MEDIUM;
    HARDWARE_CATALOG[6].availability = COMMON;
    HARDWARE_CATALOG[6].connections[0] = BLUETOOTH; HARDWARE_CATALOG[6].connections[1] = WIFI;
    HARDWARE_CATALOG[6].num_connections = 2;
    strcpy(HARDWARE_CATALOG[6].platforms[0], "watchOS"); HARDWARE_CATALOG[6].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[6].disabilities_served[0], "auditiva"); strcpy(HARDWARE_CATALOG[6].disabilities_served[1], "motora"); strcpy(HARDWARE_CATALOG[6].disabilities_served[2], "cognitiva"); strcpy(HARDWARE_CATALOG[6].disabilities_served[3], "temporaria"); strcpy(HARDWARE_CATALOG[6].disabilities_served[4], "neurologica");
    HARDWARE_CATALOG[6].num_disabilities = 5;
    strcpy(HARDWARE_CATALOG[6].input_capabilities[0], "touch_small"); strcpy(HARDWARE_CATALOG[6].input_capabilities[1], "voice"); strcpy(HARDWARE_CATALOG[6].input_capabilities[2], "microphone"); strcpy(HARDWARE_CATALOG[6].input_capabilities[3], "crown_digital"); strcpy(HARDWARE_CATALOG[6].input_capabilities[4], "accelerometer"); strcpy(HARDWARE_CATALOG[6].input_capabilities[5], "heart_rate"); strcpy(HARDWARE_CATALOG[6].input_capabilities[6], "ecg"); strcpy(HARDWARE_CATALOG[6].input_capabilities[7], "fall_detection"); strcpy(HARDWARE_CATALOG[6].input_capabilities[8], "gestures"); strcpy(HARDWARE_CATALOG[6].input_capabilities[9], "sip_pinch");
    HARDWARE_CATALOG[6].num_inputs = 10;
    strcpy(HARDWARE_CATALOG[6].output_capabilities[0], "screen_tiny"); strcpy(HARDWARE_CATALOG[6].output_capabilities[1], "taptic_engine"); strcpy(HARDWARE_CATALOG[6].output_capabilities[2], "speaker_tiny"); strcpy(HARDWARE_CATALOG[6].output_capabilities[3], "haptic");
    HARDWARE_CATALOG[6].num_outputs = 4;
    HARDWARE_CATALOG[6].battery_hours = 18.0f;
    HARDWARE_CATALOG[6].offline_capable = true;
    strcpy(HARDWARE_CATALOG[6].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[6].num_languages = 1;
    strcpy(HARDWARE_CATALOG[6].description, "Fall Detection (queda). ECG (coracao). Taptic Engine para surdos. AssistiveTouch (pinca/sorvo para tetraplegia). Noise app (autismo).");

    // HW-008
    strcpy(HARDWARE_CATALOG[7].device_id, "HW-008");
    strcpy(HARDWARE_CATALOG[7].name, "Smartwatch basico / Pulseira fitness");
    HARDWARE_CATALOG[7].category = WEARABLE;
    HARDWARE_CATALOG[7].cost = LOW;
    HARDWARE_CATALOG[7].availability = UBIQUITOUS;
    HARDWARE_CATALOG[7].connections[0] = BLUETOOTH;
    HARDWARE_CATALOG[7].num_connections = 1;
    strcpy(HARDWARE_CATALOG[7].platforms[0], "Proprietary"); HARDWARE_CATALOG[7].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[7].disabilities_served[0], "auditiva"); strcpy(HARDWARE_CATALOG[7].disabilities_served[1], "temporaria");
    HARDWARE_CATALOG[7].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[7].input_capabilities[0], "touch_tiny"); strcpy(HARDWARE_CATALOG[7].input_capabilities[1], "accelerometer"); strcpy(HARDWARE_CATALOG[7].input_capabilities[2], "heart_rate");
    HARDWARE_CATALOG[7].num_inputs = 3;
    strcpy(HARDWARE_CATALOG[7].output_capabilities[0], "screen_tiny"); strcpy(HARDWARE_CATALOG[7].output_capabilities[1], "vibration");
    HARDWARE_CATALOG[7].num_outputs = 2;
    HARDWARE_CATALOG[7].battery_hours = 168.0f;
    HARDWARE_CATALOG[7].offline_capable = true;
    strcpy(HARDWARE_CATALOG[7].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[7].num_languages = 1;
    strcpy(HARDWARE_CATALOG[7].description, "R$80-200. Vibracao para notificacoes (surdez). Monitor basico de sono/atividade.");

    // HW-009
    strcpy(HARDWARE_CATALOG[8].device_id, "HW-009");
    strcpy(HARDWARE_CATALOG[8].name, "Anel Smart (Smart Ring)");
    HARDWARE_CATALOG[8].category = WEARABLE;
    HARDWARE_CATALOG[8].cost = MEDIUM;
    HARDWARE_CATALOG[8].availability = SPECIALIZED;
    HARDWARE_CATALOG[8].connections[0] = BLUETOOTH;
    HARDWARE_CATALOG[8].num_connections = 1;
    strcpy(HARDWARE_CATALOG[8].platforms[0], "Proprietary"); HARDWARE_CATALOG[8].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[8].disabilities_served[0], "auditiva"); strcpy(HARDWARE_CATALOG[8].disabilities_served[1], "neurologica");
    HARDWARE_CATALOG[8].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[8].input_capabilities[0], "accelerometer"); strcpy(HARDWARE_CATALOG[8].input_capabilities[1], "heart_rate"); strcpy(HARDWARE_CATALOG[8].input_capabilities[2], "temperature"); strcpy(HARDWARE_CATALOG[8].input_capabilities[3], "spO2");
    HARDWARE_CATALOG[8].num_inputs = 4;
    strcpy(HARDWARE_CATALOG[8].output_capabilities[0], "vibration_tiny"); strcpy(HARDWARE_CATALOG[8].output_capabilities[1], "led");
    HARDWARE_CATALOG[8].num_outputs = 2;
    HARDWARE_CATALOG[8].battery_hours = 168.0f;
    HARDWARE_CATALOG[8].offline_capable = true;
    strcpy(HARDWARE_CATALOG[8].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[8].num_languages = 1;
    strcpy(HARDWARE_CATALOG[8].description, "Discreto. Monitor de sono, temperatura, SpO2. Para autismo: biofeedback discreto.");

    // HW-010
    strcpy(HARDWARE_CATALOG[9].device_id, "HW-010");
    strcpy(HARDWARE_CATALOG[9].name, "Oculos Inteligentes (Smart Glasses)");
    HARDWARE_CATALOG[9].category = WEARABLE;
    HARDWARE_CATALOG[9].cost = HIGH;
    HARDWARE_CATALOG[9].availability = SPECIALIZED;
    HARDWARE_CATALOG[9].connections[0] = BLUETOOTH; HARDWARE_CATALOG[9].connections[1] = WIFI;
    HARDWARE_CATALOG[9].num_connections = 2;
    strcpy(HARDWARE_CATALOG[9].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[9].platforms[1], "Proprietary"); HARDWARE_CATALOG[9].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[9].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[9].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[9].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[9].disabilities_served[3], "neurologica");
    HARDWARE_CATALOG[9].num_disabilities = 4;
    strcpy(HARDWARE_CATALOG[9].input_capabilities[0], "voice"); strcpy(HARDWARE_CATALOG[9].input_capabilities[1], "camera"); strcpy(HARDWARE_CATALOG[9].input_capabilities[2], "microphone"); strcpy(HARDWARE_CATALOG[9].input_capabilities[3], "bone_conduction_audio"); strcpy(HARDWARE_CATALOG[9].input_capabilities[4], "head_tracking"); strcpy(HARDWARE_CATALOG[9].input_capabilities[5], "eye_tracking_basic");
    HARDWARE_CATALOG[9].num_inputs = 6;
    strcpy(HARDWARE_CATALOG[9].output_capabilities[0], "hud_overlay"); strcpy(HARDWARE_CATALOG[9].output_capabilities[1], "bone_conduction_speaker"); strcpy(HARDWARE_CATALOG[9].output_capabilities[2], "vibration");
    HARDWARE_CATALOG[9].num_outputs = 3;
    HARDWARE_CATALOG[9].battery_hours = 6.0f;
    HARDWARE_CATALOG[9].offline_capable = true;
    strcpy(HARDWARE_CATALOG[9].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[9].num_languages = 1;
    strcpy(HARDWARE_CATALOG[9].description, "Legendas em tempo real no campo de visao (surdez). Navegacao por setas (cegueira). Heads-up display.");

    // HW-011
    strcpy(HARDWARE_CATALOG[10].device_id, "HW-011");
    strcpy(HARDWARE_CATALOG[10].name, "Notebook / Laptop");
    HARDWARE_CATALOG[10].category = MASS;
    HARDWARE_CATALOG[10].cost = MEDIUM;
    HARDWARE_CATALOG[10].availability = UBIQUITOUS;
    HARDWARE_CATALOG[10].connections[0] = BLUETOOTH; HARDWARE_CATALOG[10].connections[1] = USB; HARDWARE_CATALOG[10].connections[2] = WIFI; HARDWARE_CATALOG[10].connections[3] = AUDIO_JACK;
    HARDWARE_CATALOG[10].num_connections = 4;
    strcpy(HARDWARE_CATALOG[10].platforms[0], "Linux"); strcpy(HARDWARE_CATALOG[10].platforms[1], "Windows"); strcpy(HARDWARE_CATALOG[10].platforms[2], "macOS"); HARDWARE_CATALOG[10].num_platforms = 3;
    strcpy(HARDWARE_CATALOG[10].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[10].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[10].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[10].disabilities_served[3], "cognitiva"); strcpy(HARDWARE_CATALOG[10].disabilities_served[4], "espectro_autista"); strcpy(HARDWARE_CATALOG[10].disabilities_served[5], "neurologica"); strcpy(HARDWARE_CATALOG[10].disabilities_served[6], "multipla"); strcpy(HARDWARE_CATALOG[10].disabilities_served[7], "temporaria");
    HARDWARE_CATALOG[10].num_disabilities = 8;
    strcpy(HARDWARE_CATALOG[10].input_capabilities[0], "keyboard"); strcpy(HARDWARE_CATALOG[10].input_capabilities[1], "trackpad"); strcpy(HARDWARE_CATALOG[10].input_capabilities[2], "microphone"); strcpy(HARDWARE_CATALOG[10].input_capabilities[3], "camera"); strcpy(HARDWARE_CATALOG[10].input_capabilities[4], "bluetooth_devices");
    HARDWARE_CATALOG[10].num_inputs = 5;
    strcpy(HARDWARE_CATALOG[10].output_capabilities[0], "screen"); strcpy(HARDWARE_CATALOG[10].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[10].output_capabilities[2], "vibration_rare");
    HARDWARE_CATALOG[10].num_outputs = 3;
    HARDWARE_CATALOG[10].battery_hours = 8.0f;
    HARDWARE_CATALOG[10].offline_capable = true;
    strcpy(HARDWARE_CATALOG[10].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[10].num_languages = 1;
    strcpy(HARDWARE_CATALOG[10].description, "Plataforma de desenvolvimento completa. Screen readers, IDEs, eye-tracking via USB.");

    // HW-012
    strcpy(HARDWARE_CATALOG[11].device_id, "HW-012");
    strcpy(HARDWARE_CATALOG[11].name, "Desktop / PC");
    HARDWARE_CATALOG[11].category = MASS;
    HARDWARE_CATALOG[11].cost = MEDIUM;
    HARDWARE_CATALOG[11].availability = COMMON;
    HARDWARE_CATALOG[11].connections[0] = BLUETOOTH; HARDWARE_CATALOG[11].connections[1] = USB; HARDWARE_CATALOG[11].connections[2] = WIFI; HARDWARE_CATALOG[11].connections[3] = AUDIO_JACK;
    HARDWARE_CATALOG[11].num_connections = 4;
    strcpy(HARDWARE_CATALOG[11].platforms[0], "Linux"); strcpy(HARDWARE_CATALOG[11].platforms[1], "Windows"); HARDWARE_CATALOG[11].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[11].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[11].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[11].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[11].disabilities_served[3], "cognitiva"); strcpy(HARDWARE_CATALOG[11].disabilities_served[4], "espectro_autista"); strcpy(HARDWARE_CATALOG[11].disabilities_served[5], "neurologica"); strcpy(HARDWARE_CATALOG[11].disabilities_served[6], "multipla");
    HARDWARE_CATALOG[11].num_disabilities = 7;
    strcpy(HARDWARE_CATALOG[11].input_capabilities[0], "keyboard"); strcpy(HARDWARE_CATALOG[11].input_capabilities[1], "mouse"); strcpy(HARDWARE_CATALOG[11].input_capabilities[2], "microphone"); strcpy(HARDWARE_CATALOG[11].input_capabilities[3], "camera"); strcpy(HARDWARE_CATALOG[11].input_capabilities[4], "usb_devices"); strcpy(HARDWARE_CATALOG[11].input_capabilities[5], "pcie_cards");
    HARDWARE_CATALOG[11].num_inputs = 6;
    strcpy(HARDWARE_CATALOG[11].output_capabilities[0], "screen_large"); strcpy(HARDWARE_CATALOG[11].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[11].output_capabilities[2], "multi_monitor");
    HARDWARE_CATALOG[11].num_outputs = 3;
    HARDWARE_CATALOG[11].battery_hours = 0.0f;
    HARDWARE_CATALOG[11].offline_capable = true;
    strcpy(HARDWARE_CATALOG[11].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[11].num_languages = 1;
    strcpy(HARDWARE_CATALOG[11].description, "Maximo de conectividade. Multi-tela, GPUs para IA, todo tipo de periferico.");

    // HW-013
    strcpy(HARDWARE_CATALOG[12].device_id, "HW-013");
    strcpy(HARDWARE_CATALOG[12].name, "Display Braille (linha braille)");
    HARDWARE_CATALOG[12].category = ASSISTIVE_VISUAL;
    HARDWARE_CATALOG[12].cost = HIGH;
    HARDWARE_CATALOG[12].availability = SPECIALIZED;
    HARDWARE_CATALOG[12].connections[0] = BLUETOOTH; HARDWARE_CATALOG[12].connections[1] = USB;
    HARDWARE_CATALOG[12].num_connections = 2;
    strcpy(HARDWARE_CATALOG[12].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[12].platforms[1], "iOS"); strcpy(HARDWARE_CATALOG[12].platforms[2], "Linux"); strcpy(HARDWARE_CATALOG[12].platforms[3], "Windows"); strcpy(HARDWARE_CATALOG[12].platforms[4], "macOS"); HARDWARE_CATALOG[12].num_platforms = 5;
    strcpy(HARDWARE_CATALOG[12].disabilities_served[0], "visual");
    HARDWARE_CATALOG[12].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[12].input_capabilities[0], "braille_keys"); strcpy(HARDWARE_CATALOG[12].input_capabilities[1], "routing_buttons"); strcpy(HARDWARE_CATALOG[12].input_capabilities[2], "navigation");
    HARDWARE_CATALOG[12].num_inputs = 3;
    strcpy(HARDWARE_CATALOG[12].output_capabilities[0], "braille_cells_40"); strcpy(HARDWARE_CATALOG[12].output_capabilities[1], "braille_cells_80");
    HARDWARE_CATALOG[12].num_outputs = 2;
    HARDWARE_CATALOG[12].battery_hours = 20.0f;
    HARDWARE_CATALOG[12].offline_capable = true;
    strcpy(HARDWARE_CATALOG[12].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[12].num_languages = 1;
    strcpy(HARDWARE_CATALOG[12].description, "40-80 celulas braille. Celulas piezoeletricas que sobem e descem. Cego le codigo tateando.");

    // HW-013b
    strcpy(HARDWARE_CATALOG[13].device_id, "HW-013b");
    strcpy(HARDWARE_CATALOG[13].name, "Display Braille portatil (14-20 celulas)");
    HARDWARE_CATALOG[13].category = ASSISTIVE_VISUAL;
    HARDWARE_CATALOG[13].cost = MEDIUM;
    HARDWARE_CATALOG[13].availability = SPECIALIZED;
    HARDWARE_CATALOG[13].connections[0] = BLUETOOTH; HARDWARE_CATALOG[13].connections[1] = USB;
    HARDWARE_CATALOG[13].num_connections = 2;
    strcpy(HARDWARE_CATALOG[13].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[13].platforms[1], "iOS"); HARDWARE_CATALOG[13].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[13].disabilities_served[0], "visual");
    HARDWARE_CATALOG[13].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[13].input_capabilities[0], "braille_keys");
    HARDWARE_CATALOG[13].num_inputs = 1;
    strcpy(HARDWARE_CATALOG[13].output_capabilities[0], "braille_cells_14");
    HARDWARE_CATALOG[13].num_outputs = 1;
    HARDWARE_CATALOG[13].battery_hours = 20.0f;
    HARDWARE_CATALOG[13].offline_capable = true;
    strcpy(HARDWARE_CATALOG[13].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[13].num_languages = 1;
    strcpy(HARDWARE_CATALOG[13].description, "Versao portatil menor. Cabe no bolso. Conecta no smartphone.");

    // HW-014
    strcpy(HARDWARE_CATALOG[14].device_id, "HW-014");
    strcpy(HARDWARE_CATALOG[14].name, "Leitor de tela software (NVDA, Orca, VoiceOver, TalkBack)");
    HARDWARE_CATALOG[14].category = ASSISTIVE_VISUAL;
    HARDWARE_CATALOG[14].cost = FREE;
    HARDWARE_CATALOG[14].availability = UBIQUITOUS;
    HARDWARE_CATALOG[14].num_connections = 0;
    strcpy(HARDWARE_CATALOG[14].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[14].platforms[1], "iOS"); strcpy(HARDWARE_CATALOG[14].platforms[2], "Linux"); strcpy(HARDWARE_CATALOG[14].platforms[3], "Windows"); strcpy(HARDWARE_CATALOG[14].platforms[4], "macOS"); HARDWARE_CATALOG[14].num_platforms = 5;
    strcpy(HARDWARE_CATALOG[14].disabilities_served[0], "visual");
    HARDWARE_CATALOG[14].num_disabilities = 1;
    HARDWARE_CATALOG[14].num_inputs = 0;
    strcpy(HARDWARE_CATALOG[14].output_capabilities[0], "tts"); strcpy(HARDWARE_CATALOG[14].output_capabilities[1], "braille_output"); strcpy(HARDWARE_CATALOG[14].output_capabilities[2], "audio_cues");
    HARDWARE_CATALOG[14].num_outputs = 3;
    HARDWARE_CATALOG[14].battery_hours = 0.0f;
    HARDWARE_CATALOG[14].offline_capable = true;
    strcpy(HARDWARE_CATALOG[14].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[14].num_languages = 1;
    strcpy(HARDWARE_CATALOG[14].description, "NVDA (gratis, Windows). Orca (Linux). VoiceOver (Apple). TalkBack (Android). Converte tela em voz/braille.");

    // HW-015
    strcpy(HARDWARE_CATALOG[15].device_id, "HW-015");
    strcpy(HARDWARE_CATALOG[15].name, "Lupa eletronica / CCTV");
    HARDWARE_CATALOG[15].category = ASSISTIVE_VISUAL;
    HARDWARE_CATALOG[15].cost = MEDIUM;
    HARDWARE_CATALOG[15].availability = SPECIALIZED;
    HARDWARE_CATALOG[15].connections[0] = HDMI;
    HARDWARE_CATALOG[15].num_connections = 1;
    strcpy(HARDWARE_CATALOG[15].platforms[0], "Standalone"); HARDWARE_CATALOG[15].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[15].disabilities_served[0], "visual");
    HARDWARE_CATALOG[15].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[15].input_capabilities[0], "camera_zoom");
    HARDWARE_CATALOG[15].num_inputs = 1;
    strcpy(HARDWARE_CATALOG[15].output_capabilities[0], "screen_zoomed");
    HARDWARE_CATALOG[15].num_outputs = 1;
    HARDWARE_CATALOG[15].battery_hours = 4.0f;
    HARDWARE_CATALOG[15].offline_capable = true;
    strcpy(HARDWARE_CATALOG[15].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[15].num_languages = 1;
    strcpy(HARDWARE_CATALOG[15].description, "Camera que amplia texto/papel para tela. Para baixa visao.");

    // HW-016
    strcpy(HARDWARE_CATALOG[16].device_id, "HW-016");
    strcpy(HARDWARE_CATALOG[16].name, "Eye Tracker (Tobii, EyeX)");
    HARDWARE_CATALOG[16].category = ASSISTIVE_MOTOR;
    HARDWARE_CATALOG[16].cost = HIGH;
    HARDWARE_CATALOG[16].availability = SPECIALIZED;
    HARDWARE_CATALOG[16].connections[0] = USB; HARDWARE_CATALOG[16].connections[1] = WIFI;
    HARDWARE_CATALOG[16].num_connections = 2;
    strcpy(HARDWARE_CATALOG[16].platforms[0], "Windows"); strcpy(HARDWARE_CATALOG[16].platforms[1], "Linux"); HARDWARE_CATALOG[16].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[16].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[16].disabilities_served[1], "multipla");
    HARDWARE_CATALOG[16].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[16].input_capabilities[0], "eye_gaze"); strcpy(HARDWARE_CATALOG[16].input_capabilities[1], "dwell_selection"); strcpy(HARDWARE_CATALOG[16].input_capabilities[2], "blink");
    HARDWARE_CATALOG[16].num_inputs = 3;
    HARDWARE_CATALOG[16].num_outputs = 0;
    HARDWARE_CATALOG[16].battery_hours = 0.0f;
    HARDWARE_CATALOG[16].offline_capable = true;
    strcpy(HARDWARE_CATALOG[16].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[16].num_languages = 1;
    strcpy(HARDWARE_CATALOG[16].description, "Camera infravermelha rastreia olhos. Tetraplegia, ELA, paralisia cerebral. Custo: R$2.000-8.000.");

    // HW-017
    strcpy(HARDWARE_CATALOG[17].device_id, "HW-017");
    strcpy(HARDWARE_CATALOG[17].name, "Eye Tracker portatil (smartphone)");
    HARDWARE_CATALOG[17].category = ASSISTIVE_MOTOR;
    HARDWARE_CATALOG[17].cost = MEDIUM;
    HARDWARE_CATALOG[17].availability = SPECIALIZED;
    HARDWARE_CATALOG[17].num_connections = 0;
    strcpy(HARDWARE_CATALOG[17].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[17].platforms[1], "iOS"); HARDWARE_CATALOG[17].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[17].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[17].disabilities_served[1], "multipla");
    HARDWARE_CATALOG[17].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[17].input_capabilities[0], "eye_gaze_front_camera");
    HARDWARE_CATALOG[17].num_inputs = 1;
    HARDWARE_CATALOG[17].num_outputs = 0;
    HARDWARE_CATALOG[17].battery_hours = 6.0f;
    HARDWARE_CATALOG[17].offline_capable = true;
    strcpy(HARDWARE_CATALOG[17].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[17].num_languages = 1;
    strcpy(HARDWARE_CATALOG[17].description, "Usa camera frontal do smartphone para rastrear olhos. Precisao menor mas gratuito com app.");

    // HW-018
    strcpy(HARDWARE_CATALOG[18].device_id, "HW-018");
    strcpy(HARDWARE_CATALOG[18].name, "Switch / Botao adaptativo");
    HARDWARE_CATALOG[18].category = ASSISTIVE_MOTOR;
    HARDWARE_CATALOG[18].cost = VERY_LOW;
    HARDWARE_CATALOG[18].availability = COMMON;
    HARDWARE_CATALOG[18].connections[0] = BLUETOOTH; HARDWARE_CATALOG[18].connections[1] = AUDIO_JACK; HARDWARE_CATALOG[18].connections[2] = USB;
    HARDWARE_CATALOG[18].num_connections = 3;
    strcpy(HARDWARE_CATALOG[18].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[18].platforms[1], "iOS"); strcpy(HARDWARE_CATALOG[18].platforms[2], "Windows"); strcpy(HARDWARE_CATALOG[18].platforms[3], "Linux"); strcpy(HARDWARE_CATALOG[18].platforms[4], "macOS"); HARDWARE_CATALOG[18].num_platforms = 5;
    strcpy(HARDWARE_CATALOG[18].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[18].disabilities_served[1], "multipla"); strcpy(HARDWARE_CATALOG[18].disabilities_served[2], "desenvolvimento");
    HARDWARE_CATALOG[18].num_disabilities = 3;
    strcpy(HARDWARE_CATALOG[18].input_capabilities[0], "single_switch"); strcpy(HARDWARE_CATALOG[18].input_capabilities[1], "dual_switch");
    HARDWARE_CATALOG[18].num_inputs = 2;
    HARDWARE_CATALOG[18].num_outputs = 0;
    HARDWARE_CATALOG[18].battery_hours = 0.0f;
    HARDWARE_CATALOG[18].offline_capable = true;
    strcpy(HARDWARE_CATALOG[18].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[18].num_languages = 1;
    strcpy(HARDWARE_CATALOG[18].description, "Um ou dois botoes grandes. Scan automatico passa opcoes, usuario aciona para selecionar. DIY possivel por R$20.");

    // HW-019
    strcpy(HARDWARE_CATALOG[19].device_id, "HW-019");
    strcpy(HARDWARE_CATALOG[19].name, "Teclado adaptativo grande");
    HARDWARE_CATALOG[19].category = ASSISTIVE_MOTOR;
    HARDWARE_CATALOG[19].cost = LOW;
    HARDWARE_CATALOG[19].availability = SPECIALIZED;
    HARDWARE_CATALOG[19].connections[0] = BLUETOOTH; HARDWARE_CATALOG[19].connections[1] = USB;
    HARDWARE_CATALOG[19].num_connections = 2;
    strcpy(HARDWARE_CATALOG[19].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[19].platforms[1], "iOS"); strcpy(HARDWARE_CATALOG[19].platforms[2], "Windows"); strcpy(HARDWARE_CATALOG[19].platforms[3], "Linux"); strcpy(HARDWARE_CATALOG[19].platforms[4], "macOS"); HARDWARE_CATALOG[19].num_platforms = 5;
    strcpy(HARDWARE_CATALOG[19].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[19].disabilities_served[1], "cognitiva"); strcpy(HARDWARE_CATALOG[19].disabilities_served[2], "desenvolvimento");
    HARDWARE_CATALOG[19].num_disabilities = 3;
    strcpy(HARDWARE_CATALOG[19].input_capabilities[0], "large_keys"); strcpy(HARDWARE_CATALOG[19].input_capabilities[1], "color_coded");
    HARDWARE_CATALOG[19].num_inputs = 2;
    HARDWARE_CATALOG[19].num_outputs = 0;
    HARDWARE_CATALOG[19].battery_hours = 0.0f;
    HARDWARE_CATALOG[19].offline_capable = true;
    strcpy(HARDWARE_CATALOG[19].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[19].num_languages = 1;
    strcpy(HARDWARE_CATALOG[19].description, "Teclas 3x maiores, coloridas, com guard de mao. Para tremores, baixa destreza, Down.");

    // HW-020
    strcpy(HARDWARE_CATALOG[20].device_id, "HW-020");
    strcpy(HARDWARE_CATALOG[20].name, "Teclado de cabeca / boca");
    HARDWARE_CATALOG[20].category = ASSISTIVE_MOTOR;
    HARDWARE_CATALOG[20].cost = LOW;
    HARDWARE_CATALOG[20].availability = SPECIALIZED;
    HARDWARE_CATALOG[20].connections[0] = USB; HARDWARE_CATALOG[20].connections[1] = BLUETOOTH;
    HARDWARE_CATALOG[20].num_connections = 2;
    strcpy(HARDWARE_CATALOG[20].platforms[0], "Windows"); strcpy(HARDWARE_CATALOG[20].platforms[1], "Linux"); strcpy(HARDWARE_CATALOG[20].platforms[2], "Android"); HARDWARE_CATALOG[20].num_platforms = 3;
    strcpy(HARDWARE_CATALOG[20].disabilities_served[0], "motora");
    HARDWARE_CATALOG[20].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[20].input_capabilities[0], "head_stick"); strcpy(HARDWARE_CATALOG[20].input_capabilities[1], "mouth_stick"); strcpy(HARDWARE_CATALOG[20].input_capabilities[2], "sip_puff");
    HARDWARE_CATALOG[20].num_inputs = 3;
    HARDWARE_CATALOG[20].num_outputs = 0;
    HARDWARE_CATALOG[20].battery_hours = 0.0f;
    HARDWARE_CATALOG[20].offline_capable = true;
    strcpy(HARDWARE_CATALOG[20].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[20].num_languages = 1;
    strcpy(HARDWARE_CATALOG[20].description, "Ponteiro de cabeca ou bocal para digitar em teclado na tela. Sip-and-puff = sopro/succao.");

    // HW-021
    strcpy(HARDWARE_CATALOG[21].device_id, "HW-021");
    strcpy(HARDWARE_CATALOG[21].name, "Trackball adaptativo");
    HARDWARE_CATALOG[21].category = ASSISTIVE_MOTOR;
    HARDWARE_CATALOG[21].cost = LOW;
    HARDWARE_CATALOG[21].availability = COMMON;
    HARDWARE_CATALOG[21].connections[0] = BLUETOOTH; HARDWARE_CATALOG[21].connections[1] = USB;
    HARDWARE_CATALOG[21].num_connections = 2;
    strcpy(HARDWARE_CATALOG[21].platforms[0], "Windows"); strcpy(HARDWARE_CATALOG[21].platforms[1], "Linux"); strcpy(HARDWARE_CATALOG[21].platforms[2], "macOS"); strcpy(HARDWARE_CATALOG[21].platforms[3], "Android"); HARDWARE_CATALOG[21].num_platforms = 4;
    strcpy(HARDWARE_CATALOG[21].disabilities_served[0], "motora");
    HARDWARE_CATALOG[21].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[21].input_capabilities[0], "trackball"); strcpy(HARDWARE_CATALOG[21].input_capabilities[1], "large_ball");
    HARDWARE_CATALOG[21].num_inputs = 2;
    HARDWARE_CATALOG[21].num_outputs = 0;
    HARDWARE_CATALOG[21].battery_hours = 0.0f;
    HARDWARE_CATALOG[21].offline_capable = true;
    strcpy(HARDWARE_CATALOG[21].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[21].num_languages = 1;
    strcpy(HARDWARE_CATALOG[21].description, "Bola grande movida com palma/queixo/dorso do pe. Estavel para tremores (Parkinson).");

    // HW-022
    strcpy(HARDWARE_CATALOG[22].device_id, "HW-022");
    strcpy(HARDWARE_CATALOG[22].name, "Pedal de pe (Foot Pedal)");
    HARDWARE_CATALOG[22].category = ASSISTIVE_MOTOR;
    HARDWARE_CATALOG[22].cost = VERY_LOW;
    HARDWARE_CATALOG[22].availability = COMMON;
    HARDWARE_CATALOG[22].connections[0] = USB; HARDWARE_CATALOG[22].connections[1] = BLUETOOTH;
    HARDWARE_CATALOG[22].num_connections = 2;
    strcpy(HARDWARE_CATALOG[22].platforms[0], "Windows"); strcpy(HARDWARE_CATALOG[22].platforms[1], "Linux"); strcpy(HARDWARE_CATALOG[22].platforms[2], "macOS"); HARDWARE_CATALOG[22].num_platforms = 3;
    strcpy(HARDWARE_CATALOG[22].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[22].disabilities_served[1], "temporaria");
    HARDWARE_CATALOG[22].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[22].input_capabilities[0], "foot_press_left"); strcpy(HARDWARE_CATALOG[22].input_capabilities[1], "foot_press_right"); strcpy(HARDWARE_CATALOG[22].input_capabilities[2], "foot_press_center");
    HARDWARE_CATALOG[22].num_inputs = 3;
    HARDWARE_CATALOG[22].num_outputs = 0;
    HARDWARE_CATALOG[22].battery_hours = 0.0f;
    HARDWARE_CATALOG[22].offline_capable = true;
    strcpy(HARDWARE_CATALOG[22].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[22].num_languages = 1;
    strcpy(HARDWARE_CATALOG[22].description, "Para quem tem uso dos pes mas nao das maos. 3 pedais = 3 botoes. R$50-150.");

    // HW-023
    strcpy(HARDWARE_CATALOG[23].device_id, "HW-023");
    strcpy(HARDWARE_CATALOG[23].name, "EMG / MIODOELETRICO (braco bio-feedback)");
    HARDWARE_CATALOG[23].category = ASSISTIVE_MOTOR;
    HARDWARE_CATALOG[23].cost = MEDIUM;
    HARDWARE_CATALOG[23].availability = EXPERIMENTAL;
    HARDWARE_CATALOG[23].connections[0] = BLUETOOTH; HARDWARE_CATALOG[23].connections[1] = USB;
    HARDWARE_CATALOG[23].num_connections = 2;
    strcpy(HARDWARE_CATALOG[23].platforms[0], "Windows"); strcpy(HARDWARE_CATALOG[23].platforms[1], "Linux"); strcpy(HARDWARE_CATALOG[23].platforms[2], "Android"); HARDWARE_CATALOG[23].num_platforms = 3;
    strcpy(HARDWARE_CATALOG[23].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[23].disabilities_served[1], "multipla");
    HARDWARE_CATALOG[23].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[23].input_capabilities[0], "emg_signal"); strcpy(HARDWARE_CATALOG[23].input_capabilities[1], "muscle_activation");
    HARDWARE_CATALOG[23].num_inputs = 2;
    HARDWARE_CATALOG[23].num_outputs = 0;
    HARDWARE_CATALOG[23].battery_hours = 8.0f;
    HARDWARE_CATALOG[23].offline_capable = true;
    strcpy(HARDWARE_CATALOG[23].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[23].num_languages = 1;
    strcpy(HARDWARE_CATALOG[23].description, "Sensores no musculo. Detecta contracao muscular residual. Para amputados, paralisia parcial.");

    // HW-024
    strcpy(HARDWARE_CATALOG[24].device_id, "HW-024");
    strcpy(HARDWARE_CATALOG[24].name, "BCI Invasivo (Neuralink/Synchron)");
    HARDWARE_CATALOG[24].category = BRAIN;
    HARDWARE_CATALOG[24].cost = VERY_HIGH;
    HARDWARE_CATALOG[24].availability = EXPERIMENTAL;
    HARDWARE_CATALOG[24].connections[0] = WIFI; HARDWARE_CATALOG[24].connections[1] = BLUETOOTH;
    HARDWARE_CATALOG[24].num_connections = 2;
    strcpy(HARDWARE_CATALOG[24].platforms[0], "Windows"); strcpy(HARDWARE_CATALOG[24].platforms[1], "Linux"); HARDWARE_CATALOG[24].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[24].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[24].disabilities_served[1], "multipla");
    HARDWARE_CATALOG[24].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[24].input_capabilities[0], "neural_spikes"); strcpy(HARDWARE_CATALOG[24].input_capabilities[1], "motor_intention");
    HARDWARE_CATALOG[24].num_inputs = 2;
    HARDWARE_CATALOG[24].num_outputs = 0;
    HARDWARE_CATALOG[24].battery_hours = 0.0f;
    HARDWARE_CATALOG[24].offline_capable = true;
    strcpy(HARDWARE_CATALOG[24].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[24].num_languages = 1;
    strcpy(HARDWARE_CATALOG[24].description, "Eletrodos no cerebro. Tetraplegia profunda. Ainda em ensaios clinicos.");

    // HW-025
    strcpy(HARDWARE_CATALOG[25].device_id, "HW-025");
    strcpy(HARDWARE_CATALOG[25].name, "BCI Nao-Invasivo (EEG headset)");
    HARDWARE_CATALOG[25].category = BRAIN;
    HARDWARE_CATALOG[25].cost = MEDIUM;
    HARDWARE_CATALOG[25].availability = SPECIALIZED;
    HARDWARE_CATALOG[25].connections[0] = BLUETOOTH; HARDWARE_CATALOG[25].connections[1] = USB;
    HARDWARE_CATALOG[25].num_connections = 2;
    strcpy(HARDWARE_CATALOG[25].platforms[0], "Windows"); strcpy(HARDWARE_CATALOG[25].platforms[1], "Linux"); strcpy(HARDWARE_CATALOG[25].platforms[2], "Android"); HARDWARE_CATALOG[25].num_platforms = 3;
    strcpy(HARDWARE_CATALOG[25].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[25].disabilities_served[1], "multipla");
    HARDWARE_CATALOG[25].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[25].input_capabilities[0], "eeg_waves"); strcpy(HARDWARE_CATALOG[25].input_capabilities[1], "concentration_level"); strcpy(HARDWARE_CATALOG[25].input_capabilities[2], "blink_detect");
    HARDWARE_CATALOG[25].num_inputs = 3;
    strcpy(HARDWARE_CATALOG[25].output_capabilities[0], "neurofeedback_display");
    HARDWARE_CATALOG[25].num_outputs = 1;
    HARDWARE_CATALOG[25].battery_hours = 6.0f;
    HARDWARE_CATALOG[25].offline_capable = true;
    strcpy(HARDWARE_CATALOG[25].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[25].num_languages = 1;
    strcpy(HARDWARE_CATALOG[25].description, "Capacete com eletrodos. Le ondas cerebrais. Precisao baixa mas nao invasivo. R$500-3000.");

    // HC-026
    strcpy(HARDWARE_CATALOG[26].device_id, "HC-026");
    strcpy(HARDWARE_CATALOG[26].name, "Aparelho Auditivo (digital)");
    HARDWARE_CATALOG[26].category = ASSISTIVE_AUDITORY;
    HARDWARE_CATALOG[26].cost = MEDIUM;
    HARDWARE_CATALOG[26].availability = MEDICAL;
    HARDWARE_CATALOG[26].connections[0] = BLUETOOTH;
    HARDWARE_CATALOG[26].num_connections = 1;
    strcpy(HARDWARE_CATALOG[26].platforms[0], "Standalone"); HARDWARE_CATALOG[26].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[26].disabilities_served[0], "auditiva");
    HARDWARE_CATALOG[26].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[26].input_capabilities[0], "bluetooth_audio_in");
    HARDWARE_CATALOG[26].num_inputs = 1;
    strcpy(HARDWARE_CATALOG[26].output_capabilities[0], "audio_amplified"); strcpy(HARDWARE_CATALOG[26].output_capabilities[1], "audio_filtered");
    HARDWARE_CATALOG[26].num_outputs = 2;
    HARDWARE_CATALOG[26].battery_hours = 96.0f;
    HARDWARE_CATALOG[26].offline_capable = true;
    strcpy(HARDWARE_CATALOG[26].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[26].num_languages = 1;
    strcpy(HARDWARE_CATALOG[26].description, "Amplifica e filtra som. Bluetooth direto do smartphone. Programa SUS cobre.");

    // HC-027
    strcpy(HARDWARE_CATALOG[27].device_id, "HC-027");
    strcpy(HARDWARE_CATALOG[27].name, "Implante Coclear");
    HARDWARE_CATALOG[27].category = ASSISTIVE_AUDITORY;
    HARDWARE_CATALOG[27].cost = VERY_HIGH;
    HARDWARE_CATALOG[27].availability = MEDICAL;
    HARDWARE_CATALOG[27].connections[0] = BLUETOOTH;
    HARDWARE_CATALOG[27].num_connections = 1;
    strcpy(HARDWARE_CATALOG[27].platforms[0], "Standalone"); HARDWARE_CATALOG[27].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[27].disabilities_served[0], "auditiva");
    HARDWARE_CATALOG[27].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[27].input_capabilities[0], "bluetooth_audio_in");
    HARDWARE_CATALOG[27].num_inputs = 1;
    strcpy(HARDWARE_CATALOG[27].output_capabilities[0], "electrical_stimulation");
    HARDWARE_CATALOG[27].num_outputs = 1;
    HARDWARE_CATALOG[27].battery_hours = 24.0f;
    HARDWARE_CATALOG[27].offline_capable = true;
    strcpy(HARDWARE_CATALOG[27].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[27].num_languages = 1;
    strcpy(HARDWARE_CATALOG[27].description, "Cirurgico. Eletrodos na coclea. Para surdez profunda. SUS cobre em alguns estados.");

    // HC-028
    strcpy(HARDWARE_CATALOG[28].device_id, "HC-028");
    strcpy(HARDWARE_CATALOG[28].name, "Loop Magnetico / Sistema FM");
    HARDWARE_CATALOG[28].category = ASSISTIVE_AUDITORY;
    HARDWARE_CATALOG[28].cost = LOW;
    HARDWARE_CATALOG[28].availability = SPECIALIZED;
    HARDWARE_CATALOG[28].connections[0] = AUDIO_JACK; HARDWARE_CATALOG[28].connections[1] = BLUETOOTH;
    HARDWARE_CATALOG[28].num_connections = 2;
    strcpy(HARDWARE_CATALOG[28].platforms[0], "Standalone"); HARDWARE_CATALOG[28].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[28].disabilities_served[0], "auditiva");
    HARDWARE_CATALOG[28].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[28].input_capabilities[0], "audio_in");
    HARDWARE_CATALOG[28].num_inputs = 1;
    strcpy(HARDWARE_CATALOG[28].output_capabilities[0], "magnetic_loop");
    HARDWARE_CATALOG[28].num_outputs = 1;
    HARDWARE_CATALOG[28].battery_hours = 0.0f;
    HARDWARE_CATALOG[28].offline_capable = true;
    strcpy(HARDWARE_CATALOG[28].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[28].num_languages = 1;
    strcpy(HARDWARE_CATALOG[28].description, "Cabo de loop magnetico no pescoco. Transmite audio direto pro aparelho auditivo. Elimina ruido ambiente.");

    // HC-029
    strcpy(HARDWARE_CATALOG[29].device_id, "HC-029");
    strcpy(HARDWARE_CATALOG[29].name, "Fone ANC (Active Noise Cancelling)");
    HARDWARE_CATALOG[29].category = ASSISTIVE_COGNITIVE;
    HARDWARE_CATALOG[29].cost = LOW;
    HARDWARE_CATALOG[29].availability = UBIQUITOUS;
    HARDWARE_CATALOG[29].connections[0] = BLUETOOTH; HARDWARE_CATALOG[29].connections[1] = AUDIO_JACK;
    HARDWARE_CATALOG[29].num_connections = 2;
    strcpy(HARDWARE_CATALOG[29].platforms[0], "Standalone"); HARDWARE_CATALOG[29].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[29].disabilities_served[0], "espectro_autista"); strcpy(HARDWARE_CATALOG[29].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[29].disabilities_served[2], "cognitiva");
    HARDWARE_CATALOG[29].num_disabilities = 3;
    strcpy(HARDWARE_CATALOG[29].input_capabilities[0], "anc_microphone");
    HARDWARE_CATALOG[29].num_inputs = 1;
    strcpy(HARDWARE_CATALOG[29].output_capabilities[0], "audio_anc"); strcpy(HARDWARE_CATALOG[29].output_capabilities[1], "audio_filtered");
    HARDWARE_CATALOG[29].num_outputs = 2;
    HARDWARE_CATALOG[29].battery_hours = 30.0f;
    HARDWARE_CATALOG[29].offline_capable = true;
    strcpy(HARDWARE_CATALOG[29].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[29].num_languages = 1;
    strcpy(HARDWARE_CATALOG[29].description, "Cancela ruido ambiente. ESCUDO SENSORIAL para autista/TDAH em ambiente ruidoso. R$100-500.");

    // HC-030
    strcpy(HARDWARE_CATALOG[30].device_id, "HC-030");
    strcpy(HARDWARE_CATALOG[30].name, "Fone com microfone direcional");
    HARDWARE_CATALOG[30].category = ASSISTIVE_COGNITIVE;
    HARDWARE_CATALOG[30].cost = LOW;
    HARDWARE_CATALOG[30].availability = COMMON;
    HARDWARE_CATALOG[30].connections[0] = BLUETOOTH; HARDWARE_CATALOG[30].connections[1] = AUDIO_JACK;
    HARDWARE_CATALOG[30].num_connections = 2;
    strcpy(HARDWARE_CATALOG[30].platforms[0], "Standalone"); HARDWARE_CATALOG[30].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[30].disabilities_served[0], "auditiva"); strcpy(HARDWARE_CATALOG[30].disabilities_served[1], "espectro_autista");
    HARDWARE_CATALOG[30].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[30].input_capabilities[0], "directional_microphone");
    HARDWARE_CATALOG[30].num_inputs = 1;
    strcpy(HARDWARE_CATALOG[30].output_capabilities[0], "audio_directed");
    HARDWARE_CATALOG[30].num_outputs = 1;
    HARDWARE_CATALOG[30].battery_hours = 20.0f;
    HARDWARE_CATALOG[30].offline_capable = true;
    strcpy(HARDWARE_CATALOG[30].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[30].num_languages = 1;
    strcpy(HARDWARE_CATALOG[30].description, "Captura som da frente, cancela resto. Para APD (Processamento Auditivo) e autismo.");

    // HC-031
    strcpy(HARDWARE_CATALOG[31].device_id, "HC-031");
    strcpy(HARDWARE_CATALOG[31].name, "Luz Inteligente (Smart Bulb)");
    HARDWARE_CATALOG[31].category = ASSISTIVE_COGNITIVE;
    HARDWARE_CATALOG[31].cost = LOW;
    HARDWARE_CATALOG[31].availability = UBIQUITOUS;
    HARDWARE_CATALOG[31].connections[0] = WIFI; HARDWARE_CATALOG[31].connections[1] = BLUETOOTH;
    HARDWARE_CATALOG[31].num_connections = 2;
    strcpy(HARDWARE_CATALOG[31].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[31].platforms[1], "iOS"); HARDWARE_CATALOG[31].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[31].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[31].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[31].disabilities_served[2], "espectro_autista"); strcpy(HARDWARE_CATALOG[31].disabilities_served[3], "neurologica");
    HARDWARE_CATALOG[31].num_disabilities = 4;
    HARDWARE_CATALOG[31].num_inputs = 0;
    strcpy(HARDWARE_CATALOG[31].output_capabilities[0], "color_light"); strcpy(HARDWARE_CATALOG[31].output_capabilities[1], "brightness_control"); strcpy(HARDWARE_CATALOG[31].output_capabilities[2], "temperature_color"); strcpy(HARDWARE_CATALOG[31].output_capabilities[3], "no_flicker");
    HARDWARE_CATALOG[31].num_outputs = 4;
    HARDWARE_CATALOG[31].battery_hours = 0.0f;
    HARDWARE_CATALOG[31].offline_capable = true;
    strcpy(HARDWARE_CATALOG[31].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[31].num_languages = 1;
    strcpy(HARDWARE_CATALOG[31].description, "Notificacao visual por cor (surdez). Luz quente para acalmar (autismo/epilepsia). Sem flicker.");

    // HC-032
    strcpy(HARDWARE_CATALOG[32].device_id, "HC-032");
    strcpy(HARDWARE_CATALOG[32].name, "Weighted Blanket (Manta Ponderada)");
    HARDWARE_CATALOG[32].category = ASSISTIVE_COGNITIVE;
    HARDWARE_CATALOG[32].cost = VERY_LOW;
    HARDWARE_CATALOG[32].availability = COMMON;
    HARDWARE_CATALOG[32].num_connections = 0;
    strcpy(HARDWARE_CATALOG[32].platforms[0], "Physical"); HARDWARE_CATALOG[32].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[32].disabilities_served[0], "espectro_autista"); strcpy(HARDWARE_CATALOG[32].disabilities_served[1], "cognitiva"); strcpy(HARDWARE_CATALOG[32].disabilities_served[2], "neurologica");
    HARDWARE_CATALOG[32].num_disabilities = 3;
    HARDWARE_CATALOG[32].num_inputs = 0;
    strcpy(HARDWARE_CATALOG[32].output_capabilities[0], "deep_pressure_stimulation");
    HARDWARE_CATALOG[32].num_outputs = 1;
    HARDWARE_CATALOG[32].battery_hours = 0.0f;
    HARDWARE_CATALOG[32].offline_capable = true;
    strcpy(HARDWARE_CATALOG[32].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[32].num_languages = 1;
    strcpy(HARDWARE_CATALOG[32].description, "Pressao profunda calmante. Reduz ansiedade (autismo/TDAH). Melhora sono. R$100-300.");

    // HC-033
    strcpy(HARDWARE_CATALOG[33].device_id, "HC-033");
    strcpy(HARDWARE_CATALOG[33].name, "Bracelete Anti-Ansiedade / Vibratorio");
    HARDWARE_CATALOG[33].category = WEARABLE;
    HARDWARE_CATALOG[33].cost = VERY_LOW;
    HARDWARE_CATALOG[33].availability = COMMON;
    HARDWARE_CATALOG[33].connections[0] = BLUETOOTH;
    HARDWARE_CATALOG[33].num_connections = 1;
    strcpy(HARDWARE_CATALOG[33].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[33].platforms[1], "iOS"); HARDWARE_CATALOG[33].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[33].disabilities_served[0], "espectro_autista"); strcpy(HARDWARE_CATALOG[33].disabilities_served[1], "cognitiva"); strcpy(HARDWARE_CATALOG[33].disabilities_served[2], "neurologica");
    HARDWARE_CATALOG[33].num_disabilities = 3;
    strcpy(HARDWARE_CATALOG[33].input_capabilities[0], "heart_rate"); strcpy(HARDWARE_CATALOG[33].input_capabilities[1], "skin_conductance");
    HARDWARE_CATALOG[33].num_inputs = 2;
    strcpy(HARDWARE_CATALOG[33].output_capabilities[0], "vibration_patterns"); strcpy(HARDWARE_CATALOG[33].output_capabilities[1], "temperature_cooling");
    HARDWARE_CATALOG[33].num_outputs = 2;
    HARDWARE_CATALOG[33].battery_hours = 72.0f;
    HARDWARE_CATALOG[33].offline_capable = true;
    strcpy(HARDWARE_CATALOG[33].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[33].num_languages = 1;
    strcpy(HARDWARE_CATALOG[33].description, "Vibracao para acalmar (biofeedback). Detecta crise de ansiedade por batimento. R$80-200.");

    // HW-034
    strcpy(HARDWARE_CATALOG[34].device_id, "HW-034");
    strcpy(HARDWARE_CATALOG[34].name, "TV Smart (qualquer)");
    HARDWARE_CATALOG[34].category = TERMINAL_PUBLIC;
    HARDWARE_CATALOG[34].cost = MEDIUM;
    HARDWARE_CATALOG[34].availability = UBIQUITOUS;
    HARDWARE_CATALOG[34].connections[0] = WIFI; HARDWARE_CATALOG[34].connections[1] = HDMI; HARDWARE_CATALOG[34].connections[2] = BLUETOOTH;
    HARDWARE_CATALOG[34].num_connections = 3;
    strcpy(HARDWARE_CATALOG[34].platforms[0], "Android TV"); strcpy(HARDWARE_CATALOG[34].platforms[1], "Tizen"); strcpy(HARDWARE_CATALOG[34].platforms[2], "webOS"); HARDWARE_CATALOG[34].num_platforms = 3;
    strcpy(HARDWARE_CATALOG[34].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[34].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[34].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[34].disabilities_served[3], "cognitiva"); strcpy(HARDWARE_CATALOG[34].disabilities_served[4], "espectro_autista"); strcpy(HARDWARE_CATALOG[34].disabilities_served[5], "desenvolvimento"); strcpy(HARDWARE_CATALOG[34].disabilities_served[6], "temporaria");
    HARDWARE_CATALOG[34].num_disabilities = 7;
    strcpy(HARDWARE_CATALOG[34].input_capabilities[0], "remote"); strcpy(HARDWARE_CATALOG[34].input_capabilities[1], "voice"); strcpy(HARDWARE_CATALOG[34].input_capabilities[2], "bluetooth_keyboard"); strcpy(HARDWARE_CATALOG[34].input_capabilities[3], "camera_optional");
    HARDWARE_CATALOG[34].num_inputs = 4;
    strcpy(HARDWARE_CATALOG[34].output_capabilities[0], "screen_huge"); strcpy(HARDWARE_CATALOG[34].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[34].output_capabilities[2], "hdmi_out");
    HARDWARE_CATALOG[34].num_outputs = 3;
    HARDWARE_CATALOG[34].battery_hours = 0.0f;
    HARDWARE_CATALOG[34].offline_capable = true;
    strcpy(HARDWARE_CATALOG[34].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[34].num_languages = 1;
    strcpy(HARDWARE_CATALOG[34].description, "Todo estabelecimento tem uma TV. OpenTerminal transforma TV ociosa em terminal da Republica.");

    // HW-035
    strcpy(HARDWARE_CATALOG[35].device_id, "HW-035");
    strcpy(HARDWARE_CATALOG[35].name, "Kiosk / Terminal Publico");
    HARDWARE_CATALOG[35].category = TERMINAL_PUBLIC;
    HARDWARE_CATALOG[35].cost = MEDIUM;
    HARDWARE_CATALOG[35].availability = SPECIALIZED;
    HARDWARE_CATALOG[35].connections[0] = WIFI; HARDWARE_CATALOG[35].connections[1] = USB;
    HARDWARE_CATALOG[35].num_connections = 2;
    strcpy(HARDWARE_CATALOG[35].platforms[0], "Linux"); strcpy(HARDWARE_CATALOG[35].platforms[1], "Windows"); HARDWARE_CATALOG[35].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[35].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[35].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[35].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[35].disabilities_served[3], "cognitiva"); strcpy(HARDWARE_CATALOG[35].disabilities_served[4], "multipla");
    HARDWARE_CATALOG[35].num_disabilities = 5;
    strcpy(HARDWARE_CATALOG[35].input_capabilities[0], "touch"); strcpy(HARDWARE_CATALOG[35].input_capabilities[1], "keypad"); strcpy(HARDWARE_CATALOG[35].input_capabilities[2], "nfc"); strcpy(HARDWARE_CATALOG[35].input_capabilities[3], "camera");
    HARDWARE_CATALOG[35].num_inputs = 4;
    strcpy(HARDWARE_CATALOG[35].output_capabilities[0], "screen_large"); strcpy(HARDWARE_CATALOG[35].output_capabilities[1], "speaker");
    HARDWARE_CATALOG[35].num_outputs = 2;
    HARDWARE_CATALOG[35].battery_hours = 0.0f;
    HARDWARE_CATALOG[35].offline_capable = true;
    strcpy(HARDWARE_CATALOG[35].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[35].num_languages = 1;
    strcpy(HARDWARE_CATALOG[35].description, "Terminal em praca, hospital, escola. wheelchair-height. Audio jack para fone.");

    // HW-036
    strcpy(HARDWARE_CATALOG[36].device_id, "HW-036");
    strcpy(HARDWARE_CATALOG[36].name, "Terminal Burro (Raspberry Pi + tela)");
    HARDWARE_CATALOG[36].category = TERMINAL_PUBLIC;
    HARDWARE_CATALOG[36].cost = VERY_LOW;
    HARDWARE_CATALOG[36].availability = SPECIALIZED;
    HARDWARE_CATALOG[36].connections[0] = WIFI; HARDWARE_CATALOG[36].connections[1] = USB; HARDWARE_CATALOG[36].connections[2] = AUDIO_JACK; HARDWARE_CATALOG[36].connections[3] = HDMI;
    HARDWARE_CATALOG[36].num_connections = 4;
    strcpy(HARDWARE_CATALOG[36].platforms[0], "Linux"); HARDWARE_CATALOG[36].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[36].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[36].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[36].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[36].disabilities_served[3], "cognitiva");
    HARDWARE_CATALOG[36].num_disabilities = 4;
    strcpy(HARDWARE_CATALOG[36].input_capabilities[0], "keyboard"); strcpy(HARDWARE_CATALOG[36].input_capabilities[1], "usb_switch"); strcpy(HARDWARE_CATALOG[36].input_capabilities[2], "usb_eye_tracker"); strcpy(HARDWARE_CATALOG[36].input_capabilities[3], "bluetooth");
    HARDWARE_CATALOG[36].num_inputs = 4;
    strcpy(HARDWARE_CATALOG[36].output_capabilities[0], "screen"); strcpy(HARDWARE_CATALOG[36].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[36].output_capabilities[2], "audio_jack");
    HARDWARE_CATALOG[36].num_outputs = 3;
    HARDWARE_CATALOG[36].battery_hours = 0.0f;
    HARDWARE_CATALOG[36].offline_capable = true;
    strcpy(HARDWARE_CATALOG[36].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[36].num_languages = 1;
    strcpy(HARDWARE_CATALOG[36].description, "Raspberry Pi R$150 + tela R$100 = terminal completo. OpenKit da Republica.");

    // HW-037
    strcpy(HARDWARE_CATALOG[37].device_id, "HW-037");
    strcpy(HARDWARE_CATALOG[37].name, "Computador Comunitario (biblioteca, escola)");
    HARDWARE_CATALOG[37].category = TERMINAL_PUBLIC;
    HARDWARE_CATALOG[37].cost = FREE;
    HARDWARE_CATALOG[37].availability = COMMON;
    HARDWARE_CATALOG[37].connections[0] = WIFI; HARDWARE_CATALOG[37].connections[1] = USB; HARDWARE_CATALOG[37].connections[2] = AUDIO_JACK;
    HARDWARE_CATALOG[37].num_connections = 3;
    strcpy(HARDWARE_CATALOG[37].platforms[0], "Linux"); strcpy(HARDWARE_CATALOG[37].platforms[1], "Windows"); HARDWARE_CATALOG[37].num_platforms = 2;
    strcpy(HARDWARE_CATALOG[37].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[37].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[37].disabilities_served[2], "motora"); strcpy(HARDWARE_CATALOG[37].disabilities_served[3], "cognitiva"); strcpy(HARDWARE_CATALOG[37].disabilities_served[4], "multipla"); strcpy(HARDWARE_CATALOG[37].disabilities_served[5], "temporaria");
    HARDWARE_CATALOG[37].num_disabilities = 6;
    strcpy(HARDWARE_CATALOG[37].input_capabilities[0], "keyboard"); strcpy(HARDWARE_CATALOG[37].input_capabilities[1], "mouse"); strcpy(HARDWARE_CATALOG[37].input_capabilities[2], "microphone"); strcpy(HARDWARE_CATALOG[37].input_capabilities[3], "usb_devices");
    HARDWARE_CATALOG[37].num_inputs = 4;
    strcpy(HARDWARE_CATALOG[37].output_capabilities[0], "screen"); strcpy(HARDWARE_CATALOG[37].output_capabilities[1], "speaker"); strcpy(HARDWARE_CATALOG[37].output_capabilities[2], "audio_jack");
    HARDWARE_CATALOG[37].num_outputs = 3;
    HARDWARE_CATALOG[37].battery_hours = 0.0f;
    HARDWARE_CATALOG[37].offline_capable = true;
    strcpy(HARDWARE_CATALOG[37].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[37].num_languages = 1;
    strcpy(HARDWARE_CATALOG[37].description, "Zero custo. Disponivel em bibliotecas publicas, telecentros, escola publica.");

    // HW-038
    strcpy(HARDWARE_CATALOG[38].device_id, "HW-038");
    strcpy(HARDWARE_CATALOG[38].name, "Microfone (dedicado)");
    HARDWARE_CATALOG[38].category = MASS;
    HARDWARE_CATALOG[38].cost = VERY_LOW;
    HARDWARE_CATALOG[38].availability = UBIQUITOUS;
    HARDWARE_CATALOG[38].connections[0] = USB; HARDWARE_CATALOG[38].connections[1] = AUDIO_JACK; HARDWARE_CATALOG[38].connections[2] = BLUETOOTH;
    HARDWARE_CATALOG[38].num_connections = 3;
    strcpy(HARDWARE_CATALOG[38].platforms[0], "Linux"); strcpy(HARDWARE_CATALOG[38].platforms[1], "Windows"); strcpy(HARDWARE_CATALOG[38].platforms[2], "macOS"); strcpy(HARDWARE_CATALOG[38].platforms[3], "Android"); strcpy(HARDWARE_CATALOG[38].platforms[4], "iOS"); HARDWARE_CATALOG[38].num_platforms = 5;
    strcpy(HARDWARE_CATALOG[38].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[38].disabilities_served[1], "comunicacao");
    HARDWARE_CATALOG[38].num_disabilities = 2;
    strcpy(HARDWARE_CATALOG[38].input_capabilities[0], "voice_high_quality"); strcpy(HARDWARE_CATALOG[38].input_capabilities[1], "noise_cancellation");
    HARDWARE_CATALOG[38].num_inputs = 2;
    HARDWARE_CATALOG[38].num_outputs = 0;
    HARDWARE_CATALOG[38].battery_hours = 0.0f;
    HARDWARE_CATALOG[38].offline_capable = true;
    strcpy(HARDWARE_CATALOG[38].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[38].num_languages = 1;
    strcpy(HARDWARE_CATALOG[38].description, "Para dictacao de codigo por voz. Microfone de lapela R$30 = suficiente.");

    // HW-039
    strcpy(HARDWARE_CATALOG[39].device_id, "HW-039");
    strcpy(HARDWARE_CATALOG[39].name, "Camera Web (webcam)");
    HARDWARE_CATALOG[39].category = MASS;
    HARDWARE_CATALOG[39].cost = VERY_LOW;
    HARDWARE_CATALOG[39].availability = UBIQUITOUS;
    HARDWARE_CATALOG[39].connections[0] = USB; HARDWARE_CATALOG[39].connections[1] = WIFI;
    HARDWARE_CATALOG[39].num_connections = 2;
    strcpy(HARDWARE_CATALOG[39].platforms[0], "Linux"); strcpy(HARDWARE_CATALOG[39].platforms[1], "Windows"); strcpy(HARDWARE_CATALOG[39].platforms[2], "macOS"); strcpy(HARDWARE_CATALOG[39].platforms[3], "Android"); strcpy(HARDWARE_CATALOG[39].platforms[4], "iOS"); HARDWARE_CATALOG[39].num_platforms = 5;
    strcpy(HARDWARE_CATALOG[39].disabilities_served[0], "motora"); strcpy(HARDWARE_CATALOG[39].disabilities_served[1], "comunicacao"); strcpy(HARDWARE_CATALOG[39].disabilities_served[2], "auditiva");
    HARDWARE_CATALOG[39].num_disabilities = 3;
    strcpy(HARDWARE_CATALOG[39].input_capabilities[0], "hand_tracking"); strcpy(HARDWARE_CATALOG[39].input_capabilities[1], "face_tracking"); strcpy(HARDWARE_CATALOG[39].input_capabilities[2], "eye_tracking_basic"); strcpy(HARDWARE_CATALOG[39].input_capabilities[3], "gesture"); strcpy(HARDWARE_CATALOG[39].input_capabilities[4], "sign_language_capture");
    HARDWARE_CATALOG[39].num_inputs = 5;
    HARDWARE_CATALOG[39].num_outputs = 0;
    HARDWARE_CATALOG[39].battery_hours = 0.0f;
    HARDWARE_CATALOG[39].offline_capable = true;
    strcpy(HARDWARE_CATALOG[39].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[39].num_languages = 1;
    strcpy(HARDWARE_CATALOG[39].description, "Gestos de mao, tracking facial, captura de Libras. Webcam R$50 = suficiente.");

    // HW-040
    strcpy(HARDWARE_CATALOG[40].device_id, "HW-040");
    strcpy(HARDWARE_CATALOG[40].name, "Teclado Braille (Perkins / eletronico)");
    HARDWARE_CATALOG[40].category = ASSISTIVE_VISUAL;
    HARDWARE_CATALOG[40].cost = MEDIUM;
    HARDWARE_CATALOG[40].availability = SPECIALIZED;
    HARDWARE_CATALOG[40].connections[0] = BLUETOOTH; HARDWARE_CATALOG[40].connections[1] = USB;
    HARDWARE_CATALOG[40].num_connections = 2;
    strcpy(HARDWARE_CATALOG[40].platforms[0], "Android"); strcpy(HARDWARE_CATALOG[40].platforms[1], "iOS"); strcpy(HARDWARE_CATALOG[40].platforms[2], "Windows"); strcpy(HARDWARE_CATALOG[40].platforms[3], "Linux"); strcpy(HARDWARE_CATALOG[40].platforms[4], "macOS"); HARDWARE_CATALOG[40].num_platforms = 5;
    strcpy(HARDWARE_CATALOG[40].disabilities_served[0], "visual");
    HARDWARE_CATALOG[40].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[40].input_capabilities[0], "braille_input_6_keys"); strcpy(HARDWARE_CATALOG[40].input_capabilities[1], "braille_input_8_keys"); strcpy(HARDWARE_CATALOG[40].input_capabilities[2], "space"); strcpy(HARDWARE_CATALOG[40].input_capabilities[3], "navigation");
    HARDWARE_CATALOG[40].num_inputs = 4;
    HARDWARE_CATALOG[40].num_outputs = 0;
    HARDWARE_CATALOG[40].battery_hours = 20.0f;
    HARDWARE_CATALOG[40].offline_capable = true;
    strcpy(HARDWARE_CATALOG[40].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[40].num_languages = 1;
    strcpy(HARDWARE_CATALOG[40].description, "6-8 teclas para digitar em Braille. Conecta no smartphone. Cego digita codigo direto.");

    // HW-041
    strcpy(HARDWARE_CATALOG[41].device_id, "HW-041");
    strcpy(HARDWARE_CATALOG[41].name, "Ponteiro Laser / Caneta Virtual");
    HARDWARE_CATALOG[41].category = ASSISTIVE_MOTOR;
    HARDWARE_CATALOG[41].cost = LOW;
    HARDWARE_CATALOG[41].availability = SPECIALIZED;
    HARDWARE_CATALOG[41].connections[0] = BLUETOOTH;
    HARDWARE_CATALOG[41].num_connections = 1;
    strcpy(HARDWARE_CATALOG[41].platforms[0], "Windows"); strcpy(HARDWARE_CATALOG[41].platforms[1], "Linux"); strcpy(HARDWARE_CATALOG[41].platforms[2], "Android"); HARDWARE_CATALOG[41].num_platforms = 3;
    strcpy(HARDWARE_CATALOG[41].disabilities_served[0], "motora");
    HARDWARE_CATALOG[41].num_disabilities = 1;
    strcpy(HARDWARE_CATALOG[41].input_capabilities[0], "laser_point"); strcpy(HARDWARE_CATALOG[41].input_capabilities[1], "gesture");
    HARDWARE_CATALOG[41].num_inputs = 2;
    HARDWARE_CATALOG[41].num_outputs = 0;
    HARDWARE_CATALOG[41].battery_hours = 8.0f;
    HARDWARE_CATALOG[41].offline_capable = true;
    strcpy(HARDWARE_CATALOG[41].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[41].num_languages = 1;
    strcpy(HARDWARE_CATALOG[41].description, "Aponta laser na tela de longe. Para quem nao alcanca a tela ou tem tremor.");

    // HW-042
    strcpy(HARDWARE_CATALOG[42].device_id, "HW-042");
    strcpy(HARDWARE_CATALOG[42].name, "Haptic Vest / Colete Tátil");
    HARDWARE_CATALOG[42].category = WEARABLE;
    HARDWARE_CATALOG[42].cost = HIGH;
    HARDWARE_CATALOG[42].availability = EXPERIMENTAL;
    HARDWARE_CATALOG[42].connections[0] = BLUETOOTH; HARDWARE_CATALOG[42].connections[1] = WIFI;
    HARDWARE_CATALOG[42].num_connections = 2;
    strcpy(HARDWARE_CATALOG[42].platforms[0], "Windows"); strcpy(HARDWARE_CATALOG[42].platforms[1], "Linux"); strcpy(HARDWARE_CATALOG[42].platforms[2], "Android"); HARDWARE_CATALOG[42].num_platforms = 3;
    strcpy(HARDWARE_CATALOG[42].disabilities_served[0], "visual"); strcpy(HARDWARE_CATALOG[42].disabilities_served[1], "auditiva"); strcpy(HARDWARE_CATALOG[42].disabilities_served[2], "motora");
    HARDWARE_CATALOG[42].num_disabilities = 3;
    HARDWARE_CATALOG[42].num_inputs = 0;
    strcpy(HARDWARE_CATALOG[42].output_capabilities[0], "haptic_array"); strcpy(HARDWARE_CATALOG[42].output_capabilities[1], "vibration_patterns_complex");
    HARDWARE_CATALOG[42].num_outputs = 2;
    HARDWARE_CATALOG[42].battery_hours = 4.0f;
    HARDWARE_CATALOG[42].offline_capable = true;
    strcpy(HARDWARE_CATALOG[42].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[42].num_languages = 1;
    strcpy(HARDWARE_CATALOG[42].description, "Vibracoes no corpo representam informacao. Surdo sente musica. Cego sente ambiente.");

    // HW-043
    strcpy(HARDWARE_CATALOG[43].device_id, "HW-043");
    strcpy(HARDWARE_CATALOG[43].name, "Fone de Ouvido Comum");
    HARDWARE_CATALOG[43].category = MASS;
    HARDWARE_CATALOG[43].cost = VERY_LOW;
    HARDWARE_CATALOG[43].availability = UBIQUITOUS;
    HARDWARE_CATALOG[43].connections[0] = AUDIO_JACK; HARDWARE_CATALOG[43].connections[1] = BLUETOOTH;
    HARDWARE_CATALOG[43].num_connections = 2;
    strcpy(HARDWARE_CATALOG[43].platforms[0], "Standalone"); HARDWARE_CATALOG[43].num_platforms = 1;
    strcpy(HARDWARE_CATALOG[43].disabilities_served[0], "auditiva"); strcpy(HARDWARE_CATALOG[43].disabilities_served[1], "espectro_autista"); strcpy(HARDWARE_CATALOG[43].disabilities_served[2], "cognitiva");
    HARDWARE_CATALOG[43].num_disabilities = 3;
    strcpy(HARDWARE_CATALOG[43].input_capabilities[0], "microphone_optional");
    HARDWARE_CATALOG[43].num_inputs = 1;
    strcpy(HARDWARE_CATALOG[43].output_capabilities[0], "audio"); strcpy(HARDWARE_CATALOG[43].output_capabilities[1], "audio_isolated");
    HARDWARE_CATALOG[43].num_outputs = 2;
    HARDWARE_CATALOG[43].battery_hours = 0.0f;
    HARDWARE_CATALOG[43].offline_capable = true;
    strcpy(HARDWARE_CATALOG[43].languages_supported[0], "pt-BR"); HARDWARE_CATALOG[43].num_languages = 1;
    strcpy(HARDWARE_CATALOG[43].description, "Fone comum R$15. Para TTS (cego), isolamento (autista), audio direto (surdo com aparelho).");
}

// ============================================================================
// 4. MOTOR DE COMPATIBILIDADE
// ============================================================================

// (Implementacoes resumidas para demonstracao - funcoes completas necessitariam mais codigo para buscas)
// find_by_disability, find_by_cost, etc. seriam implementadas aqui com loops sobre o catalogo

// ============================================================================
// 5. DEMONSTRACAO (main)
// ============================================================================

int main() {
    init_hardware_catalog();
    printf("==================================================================\n");
    printf("OpenInclusiveHardware -- Integracao com TODO Hardware Acessivel\n");
    printf("==================================================================\n");
    printf("\nCatalogo: %d dispositivos mapeados\n", HARDWARE_CATALOG_SIZE);
    // Demonstra contagem por categoria (exemplo)
    printf("\nTODO hardware. TODA deficiencia. ZERO barreira.\n");
    return 0;
}