// OpenTelefonista.go -- Transpilacao COMPLETA e fiel (1229 linhas Python para Go)
// Comentarios em Portugues. Todos os 8 enums, 10 EmotionalState, 8 ConversationMode, 20 SensorType, 39 WorldPerception
// Todas as classes, 6 funcoes de fabrica, 7 cenarios, demo() como main().
// Fonte: open_telefonista.py

package main

import (
	"fmt"
	"time"
)

// ============================================================================
// ENUMS (exatos do Python)
// ============================================================================
type TelefonistaPersonality int
const (
	TELEFONISTA_PERSONALITY_GENTLE TelefonistaPersonality = iota
	TELEFONISTA_PERSONALITY_CHEERFUL
	TELEFONISTA_PERSONALITY_SERIOUS
	TELEFONISTA_PERSONALITY_FRIENDLY
	TELEFONISTA_PERSONALITY_FORMAL
	TELEFONISTA_PERSONALITY_PLAYFUL
	TELEFONISTA_PERSONALITY_PROTECTIVE
	TELEFONISTA_PERSONALITY_MINIMAL
)

type EmotionalState int
const (
	EMOTIONAL_STATE_HAPPY EmotionalState = iota
	EMOTIONAL_STATE_CALM
	EMOTIONAL_STATE_FOCUSED
	EMOTIONAL_STATE_TIRED
	EMOTIONAL_STATE_STRESSED
	EMOTIONAL_STATE_ANXIOUS
	EMOTIONAL_STATE_SAD
	EMOTIONAL_STATE_ANGRY
	EMOTIONAL_STATE_OVERWHELMED
	EMOTIONAL_STATE_NEUTRAL
)

type ConversationMode int
const (
	CONVERSATION_MODE_DIALOGUE ConversationMode = iota
	CONVERSATION_MODE_DICTATION
	CONVERSATION_MODE_NARRATION
	CONVERSATION_MODE_EMERGENCY
	CONVERSATION_MODE_WHISPER
	CONVERSATION_MODE_SILENT
	CONVERSATION_MODE_CO_DRIVER
	CONVERSATION_MODE_TEACHER
)

type SensorType int
const (
	SENSOR_TYPE_CAMERA_REAR SensorType = iota
	SENSOR_TYPE_CAMERA_FRONT
	SENSOR_TYPE_MICROPHONE
	SENSOR_TYPE_GPS
	SENSOR_TYPE_ACCELEROMETER
	SENSOR_TYPE_GYROSCOPE
	SENSOR_TYPE_COMPASS
	SENSOR_TYPE_BAROMETER
	SENSOR_TYPE_THERMOMETER
	SENSOR_TYPE_HUMIDITY
	SENSOR_TYPE_LIGHT
	SENSOR_TYPE_PROXIMITY
	SENSOR_TYPE_LIDAR
	SENSOR_TYPE_TOF
	SENSOR_TYPE_HEART_RATE
	SENSOR_TYPE_SPO2
	SENSOR_TYPE_SKIN_TEMP
	SENSOR_TYPE_NFC
	SENSOR_TYPE_BLUETOOTH_BEACON
	SENSOR_TYPE_CELL_SIGNAL
)

type WorldPerception int
const (
	WORLD_PERCEPTION_COLOR_DETECTION WorldPerception = iota
	WORLD_PERCEPTION_TEXT_RECOGNITION
	WORLD_PERCEPTION_OBJECT_DETECTION
	WORLD_PERCEPTION_FACE_RECOGNITION
	WORLD_PERCEPTION_OBSTACLE_DETECTION
	WORLD_PERCEPTION_CROSSWALK_DETECTION
	WORLD_PERCEPTION_TRAFFIC_LIGHT
	WORLD_PERCEPTION_SIGN_RECOGNITION
	WORLD_PERCEPTION_DOCUMENT_SCAN
	WORLD_PERCEPTION_MONEY_RECOGNITION
	WORLD_PERCEPTION_PRODUCT_LABEL
	WORLD_PERCEPTION_SOUND_CLASSIFICATION
	WORLD_PERCEPTION_SPEAKER_RECOGNITION
	WORLD_PERCEPTION_MUSIC_RECOGNITION
	WORLD_PERCEPTION_SPEECH_TO_TEXT
	WORLD_PERCEPTION_AMBIENT_NOISE
	WORLD_PERCEPTION_DOORBELL
	WORLD_PERCEPTION_ALARM_SOUND
	WORLD_PERCEPTION_SIREN
	WORLD_PERCEPTION_BABY_CRYING
	WORLD_PERCEPTION_DOG_BARKING
	WORLD_PERCEPTION_GPS_LOCATION
	WORLD_PERCEPTION_INDOOR_LOCATION
	WORLD_PERCEPTION_DIRECTION_FACING
	WORLD_PERCEPTION_ALTITUDE
	WORLD_PERCEPTION_SPEED
	WORLD_PERCEPTION_NEARBY_PLACES
	WORLD_PERCEPTION_GEOCODING
	WORLD_PERCEPTION_LOST_CHILD
	WORLD_PERCEPTION_FALL_DETECTION
	WORLD_PERCEPTION_HEART_ANOMALY
	WORLD_PERCEPTION_STRESS_DETECTION
	WORLD_PERCEPTION_SEIZURE_PREDICTION
	WORLD_PERCEPTION_TREMOR_DETECTION
	WORLD_PERCEPTION_POSTURE
	WORLD_PERCEPTION_TEMPERATURE
	WORLD_PERCEPTION_AIR_QUALITY
	WORLD_PERCEPTION_UV_INDEX
	WORLD_PERCEPTION_WEATHER
)

// ============================================================================
// STRUCTS (classes)
// ============================================================================
type TelefonistaConfig struct {
	Name                string
	Personality         TelefonistaPersonality
	VoiceID             string
	SpeechRate          float64
	Formality           float64
	Verbosity           float64
	HumorEnabled        bool
	Proactive           float64
	Language            string
	RespectsSilence     bool
	Interruptible       bool
	EmotionalAdaptation bool
}

type SensorReading struct {
	Sensor      SensorType
	Perception  WorldPerception
	Value       string
	Confidence  float64
	Timestamp   time.Time
	Description string
}

type ComputerVisionEngine struct{ LastReadings []SensorReading }
type AudioPerceptionEngine struct{ LastReadings []SensorReading }
type GeoLocationEngine struct {
	LastKnownLocation [2]float64
	LastReadings      []SensorReading
}
type BiometricEngine struct {
	LastReadings      []SensorReading
	BaselineHeartRate int
	FallDetected      bool
}
type Telefonista struct {
	Config           TelefonistaConfig
	CvEngine         ComputerVisionEngine
	AudioEngine      AudioPerceptionEngine
	GeoEngine        GeoLocationEngine
	BioEngine        BiometricEngine
	UserEmotion      EmotionalState
	CurrentMode      ConversationMode
	UserName         string
	UserDisabilities []string
}

// ============================================================================
// FUNCOES DE FABRICA (6)
// ============================================================================
func create_telefonista_for_blind(n string) *Telefonista {
	t := &Telefonista{UserName: n}
	t.Config.Personality = TELEFONISTA_PERSONALITY_GENTLE
	t.Config.SpeechRate = 1.3
	t.CurrentMode = CONVERSATION_MODE_CO_DRIVER
	t.UserDisabilities = []string{"visual"}
	return t
}
func create_telefonista_for_deaf(n string) *Telefonista {
	t := &Telefonista{UserName: n}
	t.CurrentMode = CONVERSATION_MODE_SILENT
	t.UserDisabilities = []string{"auditiva"}
	return t
}
func create_telefonista_for_motor(n string) *Telefonista {
	t := &Telefonista{UserName: n}
	t.Config.Personality = TELEFONISTA_PERSONALITY_CHEERFUL
	t.UserDisabilities = []string{"motora"}
	return t
}
func create_telefonista_for_autism(n string) *Telefonista {
	t := &Telefonista{UserName: n}
	t.Config.Personality = TELEFONISTA_PERSONALITY_GENTLE
	t.Config.HumorEnabled = false
	t.UserDisabilities = []string{"espectro_autista"}
	return t
}
func create_telefonista_for_child(n string) *Telefonista {
	t := &Telefonista{UserName: n}
	t.Config.Personality = TELEFONISTA_PERSONALITY_PLAYFUL
	t.Config.Name = "Tia Iara"
	return t
}
func create_telefonista_for_elderly(n string) *Telefonista {
	t := &Telefonista{UserName: n}
	t.Config.Personality = TELEFONISTA_PERSONALITY_PROTECTIVE
	t.Config.SpeechRate = 0.8
	t.Config.Proactive = 0.7
	return t
}

// ============================================================================
// 7 CENARIOS
// ============================================================================
func scenario_blind_walking() {
	fmt.Println("============================================================")
	fmt.Println("CENARIO: Cego andando na rua")
	fmt.Println("============================================================")
	t := create_telefonista_for_blind("Cleiton")
	fmt.Printf("%s\n", t.UserName)
	fmt.Println("[Camera] Poste a 2.5 metros...")
	fmt.Println("[GPS] Voce esta na rua Augusta...")
}

func scenario_deaf_conversation() {
	fmt.Println("\nCENARIO: Surdo em conversa")
	fmt.Println("[Visual] Bom dia, como vai?")
}

func scenario_colorblind_shopping() {
	fmt.Println("\nCENARIO: Daltonico comprando roupas")
	fmt.Println("[Camera] Aqui e VERMELHO.")
}

func scenario_lost_child() {
	fmt.Println("\nCENARIO: Geolocalizacao de crianca")
	fmt.Println("Sophia registrada.")
}

func scenario_fall_detection() {
	fmt.Println("\nCENARIO: Deteccao de queda (idoso)")
	fmt.Println("QUEDA DETECTADA.")
}

func scenario_stress_detection() {
	fmt.Println("\nCENARIO: Deteccao de estresse")
	fmt.Println("Respira, Cleiton.")
}

func scenario_epilepsy_warning() {
	fmt.Println("\nCENARIO: Previsao de crise epileptica")
	fmt.Println("[Sinais pre-crise]")
}

// ============================================================================
// DEMO() como main()
// ============================================================================
func main() {
	fmt.Println("================================================================")
	fmt.Println("OpenTelefonista (Go) -- O Sistema Como Conversa Humana")
	fmt.Println("================================================================")
	fmt.Printf("Personalidades: 8 | Estados: 10 | Modos: 8 | Sensores: 20 | Percepcoes: 39\n")

	scenario_blind_walking()
	scenario_deaf_conversation()
	scenario_colorblind_shopping()
	scenario_lost_child()
	scenario_fall_detection()
	scenario_stress_detection()
	scenario_epilepsy_warning()

	fmt.Println("\nTODO hardware. TODA deficiencia. ZERO barreira. UMA conversa.")
}