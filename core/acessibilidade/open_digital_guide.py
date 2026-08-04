#!/usr/bin/env python3
"""
OpenDigitalGuide -- O Guia Digital para Cegos
==============================================
"Cego nao precisa de caridade. Precisa de AUTONOMIA."

O cao-guia conduz. O OpenDigitalGuide EXPLICA.

O cao-guia leva o cego do ponto A ao ponto B. Mas nao fala:
"Tem uma escada descendo em 3 metros."
"O banheiro dos homens fica a direita, 10 metros."
"A placa desta loja diz 'Fechado'."
"O onibus que esta chegando e o 432."
"O semaforo a sua frente esta VERMELHO."

O OpenDigitalGuide faz isso. Ele e o CAO-GUIA QUE FALA.

COMO FUNCIONA:
  Camera do smartphone ou oculos -> Visao computacional ->
  Descreve o mundo em linguagem natural -> Iara fala no fone.

  OU:

  GPS + bussola + mapa acessivel -> Rota otimizada a pe ->
  Instrucoes passo-a-passo -> Iara guia pelo fone.

3 MODOS DE OPERACAO:

  MODO ORIENTACAO: "Onde estou?"
    - GPS + bussola + acelerometro
    - "Voce esta na Rua das Flores, 123. Norte a sua frente."
    - Pontos de referencia proximos
    - Bussola falada: "Vire 30 graus a direita para norte."

  MODO NAVEGACAO: "Como chego la?"
    - Rota otimizada a pe (OpenStreetMap)
    - Instrucoes passo-a-passo adaptadas
    - "Siga em frente 50 metros. Depois vire a direita."
    - Avisos de perigo (escada, buraco, obra)
    - Re-roteamento automatico se sair do trajeto

  MODO LEITURA: "O que tem aqui?"
    - Camera + OCR + visao computacional
    - Le placas, cartazes, cardapios, rotulos
    - Descrebe cenas ("Tem 3 pessoas na fila")
    - Identifica objetos ("Esta e uma porta de vidro")
    - Reconhece dinheiro ("Nota de 50 reais")
    - Cores de semaforo, onibus, metro

O CAO-GUIA vs O DIGITAL:

  Cao-guia:
    + Conduz fisicamente, sente o ambiente
    + Vinculo emocional
    + Funciona offline (sem bateria)
    - Nao fala, nao le, nao explica
    - Custo alto, tempo de treinamento
    - Vive ~10 anos, depois outro cao

  Digital:
    + FALA, LE, EXPLICA, DESCREVE
    + Atualiza, melhora com software
    + Integrado com Iara (voz humana)
    + Open source, custo so do hardware
    - Precisa de bateria
    - Nao conduz fisicamente (ainda)

  JUNTOS: cao-guia conduz, DigitalGuide explica.
  O cao sabe o CAMINHO. O Digital sabe o MUNDO.

ETICA DA VISAO:

  A camera ve o mundo. Mas:
  - NAO GRAVA continuamente. Processa frames sob demanda.
  - NAO IDENTIFICA PESSOAS por rosto sem consentimento.
  - NAO ENVIA imagens para a nuvem. Tudo local (NPU/GPU).
  - DESLIGAVEL: "Iara, parar de ver." Camera fecha.
  - O que ve e o que FALA sao filtrados por relevancia.

Constituicao: P1 (todos tem direito), P2 (autonomia do corpo),
P8 (IA como instrumento), P6 (acesso universal ao conhecimento).

Author: OpenRepublic Team
"""
from __future__ import annotations
from typing import Any, Dict, List, Optional, Tuple, Set
from enum import Enum
from dataclasses import dataclass, field
from collections import defaultdict, deque
from datetime import datetime
import math
import random


# ============================================================================
# 1. ENUMS
# ============================================================================

class ModoOperacao(Enum):
    """Modo de operacao do Guia Digital."""
    ORIENTACAO = ("orientacao", "Onde estou? Localiza e descreve arredores")
    NAVEGACAO = ("navegacao", "Como chego la? Rota passo-a-passo")
    LEITURA = ("leitura", "O que tem aqui? Camera le e descreve")
    PAUSADO = ("pausado", "Pausado: usuario quer silencio")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoOrientacao(Enum):
    """Tipos de informacao de orientacao espacial."""
    LOCALIZACAO = ("local", "Localizacao GPS + endereco aproximado")
    DIRECAO = ("direcao", "Direcao cardeal (N/S/L/O) + graus")
    REFERENCIA = ("referencia", "Ponto de referencia proximo")
    TERRENO = ("terreno", "Tipo de terreno (plano, ladeira, escada)")
    AMBIENTE = ("ambiente", "Tipo de ambiente (rua, parque, loja, terminal)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoInstrucao(Enum):
    """Instrucoes de navegacao passo-a-passo."""
    SEGUIR_EM_FRENTE = ("frente", "Siga em frente")
    VIRAR_DIREITA = ("direita", "Vire a direita")
    VIRAR_ESQUERDA = ("esquerda", "Vire a esquerda")
    MEIA_VOLTA = ("volta", "Meia volta (180 graus)")
    CURVA_LEVE_DIR = ("curva_dir", "Curva leve a direita")
    CURVA_LEVE_ESQ = ("curva_esq", "Curva leve a esquerda")
    ESCADA_DESCER = ("escada_desc", "Escada descendo -- CUIDADO")
    ESCADA_SUBIR = ("escada_sub", "Escada subindo")
    RAMPA = ("rampa", "Rampa a frente")
    ATRAVESSAR = ("atravessar", "Atravessar rua -- PARE e ESCUTE")
    CHEGADA = ("chegada", "Chegou ao destino")
    RETORNO = ("retorno", "Voce saiu da rota. Retornando...")
    PARAR = ("parar", "Pare. Perigo a frente.")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoPerigo(Enum):
    """Perigos detectados no caminho."""
    ESCADA = ("escada", "Escada ou degrau")
    BURACO = ("buraco", "Buraco ou irregularidade no piso")
    OBRA = ("obra", "Obra / construcao")
    CARRO_ESTACIONADO = ("carro", "Carro/moto na calcada")
    POSTE_ARBORE = ("obstaculo", "Poste, arvore, lixeira na calcada")
    AGUA_POCA = ("agua", "Agua, poco, superfície molhada")
    VIDRO_PORTA = ("vidro", "Porta ou parede de vidro")
    ANIMAL = ("animal", "Animal solto (cachorro, etc.)")
    PESSOA_PROXIMA = ("pessoa", "Pessoa muito proxima -- risco colisao")
    SEMAFORO_VERMELHO = ("semaforo", "Semaforo vermelho para pedestre")
    TRANSITO_RAPIDO = ("transito", "Via de transito rapido sem faixa")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class TipoLeituraVisual(Enum):
    """O que a camera pode ler/descrever."""
    TEXTO = ("texto", "Texto: placa, cartaz, rotulo, cardapio")
    CENA = ("cena", "Descricao de cena (objetos, pessoas, layout)")
    SEMAFORO = ("semaforo", "Cor do semaforo")
    ONIBUS = ("onibus", "Numero e linha de onibus")
    METRO = ("metro", "Estacao e linha de metro")
    DINHEIRO = ("dinheiro", "Valor de cedula/moeda")
    COR = ("cor", "Cor de objeto/roupa (quando relevante)")
    PRODUTO = ("produto", "Identificacao de produto na prateleira")
    PORTA = ("porta", "Porta: aberta/fechada, push/pull, identifica")
    FACE_DESENCONHECIDA = ("face", "Pessoa proxima (sem identificar)")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class NivelConfiancaVisual(Enum):
    """Confianca na deteccao visual."""
    ALTA = ("alta", "Deteccao confirmada (>85%)", 3)
    MEDIA = ("media", "Deteccao provavel (60-85%)", 2)
    BAIXA = ("baixa", "Deteccao incerta (40-60%)", 1)
    FALHOU = ("falhou", "Nao consegui ver (<40%)", 0)

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]

    @property
    def peso(self) -> int:
        return self.value[2]


class CanalSaida(Enum):
    """Canais de saida (mesmo padrao da Republica)."""
    VOZ_IARA = ("voz", "Voz: Iara fala (cego -- primario)")
    HAPTICO_DIRECAO = ("haptico_dir", "Vibracao direcional (esquerda/direita)")
    HAPTICO_RITMO = ("haptico_hb", "Vibracao ritmica (heartbeat: mais perto = mais rapido)")
    BRLTTY = ("brltty", "Display braille (surdo-cego)")
    ALTO_CONTRASTE = ("contraste", "Visual alto contraste (baixa visao)")
    LOG = ("log", "Log silencioso")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


class EstadoHardware(Enum):
    """Estado dos sensores/hardware do guia."""
    TUDO_OK = ("ok", "GPS + camera + bussola + IMU ativos")
    SEM_GPS = ("sem_gps", "Sem sinal GPS (indoor) -- usa IMU + mapa")
    SEM_CAMERA = ("sem_cam", "Camera indisponivel -- so navegacao")
    SEM_IMU = ("sem_imu", "Sem bussola/acelerometro -- so GPS")
    BATERIA_BAIXA = ("bateria", "Bateria < 15% -- modo economia")
    OFFLINE = ("offline", "Sem internet -- mapas em cache")

    @property
    def id(self) -> str:
        return self.value[0]

    @property
    def rotulo(self) -> str:
        return self.value[1]


# ============================================================================
# 2. DATACLASSES
# ============================================================================

@dataclass
class Posicao:
    """Posicao GPS + orientacao."""
    latitude: float = -23.5505  # SP default
    longitude: float = -46.6333
    altitude_m: float = 760.0
    rumo_graus: float = 0.0  # 0=N, 90=L, 180=S, 270=O
    velocidade_ms: float = 0.0  # metros/segundo
    precisao_gps_m: float = 5.0
    timestamp: str = ""


@dataclass
class PontoReferencia:
    """Ponto de interesse proximo para orientacao."""
    nome: str
    tipo: str  # loja, banco, farmacia, ponto de onibus, parque
    distancia_m: float
    direcao_graus: float  # relativo ao rumo do usuario
    lado: str  # "direita", "esquerda", "frente", "tras"
    util_para_navegacao: bool = True


@dataclass
class ObstaculoDetectado:
    """Obstaculo/perigo detectado pela camera ou sensores."""
    tipo: TipoPerigo
    distancia_m: float
    direcao_graus: float
    confianca: NivelConfiancaVisual
    timestamp: str
    acao_recomendada: str = ""


@dataclass
class PassoRota:
    """Um passo de uma rota de navegacao."""
    indice: int
    instrucao: TipoInstrucao
    distancia_ate_proximo_m: float
    descricao: str
    ponto: Optional[Posicao] = None
    perigos: List[TipoPerigo] = field(default_factory=list)
    concluido: bool = False


@dataclass
class Rota:
    """Rota de navegacao calculada."""
    id: str
    origem: Posicao
    destino: Posicao
    destino_nome: str
    passos: List[PassoRota] = field(default_factory=list)
    distancia_total_m: float = 0.0
    tempo_estimado_min: float = 0.0
    passo_atual_idx: int = 0
    acessivel_cadeirante: bool = True


@dataclass
class LeituraCena:
    """Resultado de uma leitura visual da camera."""
    tipo: TipoLeituraVisual
    texto: str
    confianca: NivelConfiancaVisual
    detalhes: str = ""
    timestamp: str = ""


@dataclass
class PerfilGuia:
    """Perfil do usuario do guia."""
    usuario: str = "cidadao"
    cego: bool = True
    baixa_visao: bool = False
    surdo_cego: bool = False
    cadeirante: bool = False
    idoso: bool = False
    # Preferencias
    detalhe_narrativa: str = "normal"  # minimo, normal, detalhado
    aviso_antecedencia_m: float = 8.0  # avisar perigo a X metros
    velocidade_caminhada_ms: float = 1.1  # ~4 km/h
    fone_estereo: bool = True  # audio espacial (esq/dir)
    voz_iara_velocidade: float = 1.0
    # Restricoes de rota
    evitar_escadas: bool = True
    evitar_transito_rapido: bool = True
    raio_busca_referencia_m: float = 50.0


# ============================================================================
# 3. DADOS: DIRECOES CARDEAIS
# ============================================================================

def _graus_para_cardeal(graus: float) -> str:
    """Converte graus (0-360) em direcao cardeal falada."""
    direcoes = [
        (0, "norte"), (22.5, "nordeste"), (45.0, "nordeste"),
        (67.5, "leste"), (90.0, "leste"), (112.5, "leste"),
        (135.0, "sudeste"), (157.5, "sudeste"), (180.0, "sul"),
        (202.5, "sudoeste"), (225.0, "sudoeste"), (247.5, "oeste"),
        (270.0, "oeste"), (292.5, "oeste"), (315.0, "noroeste"),
        (337.5, "noroeste"),
    ]
    graus_norm = graus % 360
    melhor = "norte"
    menor_diff = 360.0
    for g, nome in direcoes:
        diff = abs(graus_norm - g)
        if diff < menor_diff:
            menor_diff = diff
            melhor = nome
    return melhor


def _direcao_relativa(rumo_usuario: float, direcao_alvo: float) -> str:
    """Direcao relativa: 'a sua frente', 'a direita', 'atras', etc."""
    diff = (direcao_alvo - rumo_usuario) % 360
    if diff > 180:
        diff -= 360
    abs_diff = abs(diff)
    if abs_diff < 22.5:
        return "a sua frente"
    elif diff > 0:
        if abs_diff < 67.5:
            return "a direita (frente)"
        elif abs_diff < 112.5:
            return "a direita"
        elif abs_diff < 157.5:
            return "a direita (atras)"
        else:
            return "atras"
    else:
        if abs_diff < 67.5:
            return "a esquerda (frente)"
        elif abs_diff < 112.5:
            return "a esquerda"
        elif abs_diff < 157.5:
            return "a esquerda (atras)"
        else:
            return "atras"


# ============================================================================
# 4. SIMULADORES (substituiveis por hardware real)
# ============================================================================

class SimuladorGPS:
    """Simula leitura GPS. No mundo real: gpsd / Android Location API."""

    @staticmethod
    def ler() -> Posicao:
        return Posicao(
            latitude=-23.5505 + random.uniform(-0.001, 0.001),
            longitude=-46.6333 + random.uniform(-0.001, 0.001),
            rumo_graus=random.choice([0, 90, 180, 270]) + random.uniform(-15, 15),
            velocidade_ms=random.uniform(0.8, 1.4),
            precisao_gps_m=random.uniform(3.0, 8.0),
            timestamp=datetime.now().isoformat(),
        )


class SimuladorCamera:
    """Simula deteccao visual. No mundo real: TensorFlow Lite + MobileNet."""

    CENAS_INDOOR = [
        ("corredor", "Voce esta em um corredor. Paredes dos dois lados."),
        ("loja", "Interior de loja. Prateleiras a direita."),
        ("terminal_onibus", "Terminal de onibus. Plataforma aberta a frente."),
        ("estacao_metro", "Estacao de metro. Catracas a frente."),
        ("escada_rolando", "Escada rolante descendo a frente."),
        ("banheiro", "Porta de banheiro a esquerda."),
        ("elevador", "Porta de elevador a direita, 3 metros."),
    ]
    CENAS_OUTDOOR = [
        ("calcada", "Calcada livre. Rua a esquerda."),
        ("cruzamento", "Cruzamento a frente. Preste atencao no transito."),
        ("praca", "Praca aberta. Bancos a direita."),
        ("parada_onibus", "Ponto de onibus. Abrigo a direita."),
        ("parque", "Trilha de parque. Terreno irregular."),
        ("ladeira", "Ladeira descendo. Cuidado com velocidade."),
    ]
    TEXTOS_COMUNS = [
        ("EM BAR DO JOAO", "Placa de estabelecimento"),
        ("BANHEIRO", "Sinalizacao de banheiro"),
        ("SAIDA", "Sinalizacao de saida"),
        ("PROIBIDO ESTACIONAR", "Placa de transito"),
        ("PARE", "Placa de pare"),
        ("PASTEL DA VOVÓ", "Placa de loja"),
        ("FARMACIA SAO JOAO", "Placa de farmacia"),
        ("CAIXA 24H", "Caixa eletronico"),
        ("LINEA 432 - METRO", "Painel de onibus"),
        ("CARDÁPIO: PASTEL R$ 8", "Cardapio"),
    ]
    SEMAFOROS = [("VERMELHO", "Semaforo vermelho para pedestre. PARE."),
                 ("VERDE", "Semaforo verde para pedestre. Pode atravessar."),
                 ("AMARELO", "Semaforo amarelo. Espere.")]

    @staticmethod
    def ler_cena(indoor: bool = False) -> LeituraCena:
        cenas = SimuladorCamera.CENAS_INDOOR if indoor else SimuladorCamera.CENAS_OUTDOOR
        tipo_id, descricao = random.choice(cenas)
        conf = random.choice(list(NivelConfiancaVisual))
        return LeituraCena(
            tipo=TipoLeituraVisual.CENA, texto=descricao,
            confianca=conf, timestamp=datetime.now().isoformat(),
        )

    @staticmethod
    def ler_texto() -> LeituraCena:
        texto, detalhe = random.choice(SimuladorCamera.TEXTOS_COMUNS)
        conf = random.choice([
            NivelConfiancaVisual.ALTA, NivelConfiancaVisual.ALTA,
            NivelConfiancaVisual.MEDIA,
        ])
        return LeituraCena(
            tipo=TipoLeituraVisual.TEXTO, texto=texto, detalhes=detalhe,
            confianca=conf, timestamp=datetime.now().isoformat(),
        )

    @staticmethod
    def ler_semaforo() -> LeituraCena:
        cor, desc = random.choice(SimuladorCamera.SEMAFOROS)
        return LeituraCena(
            tipo=TipoLeituraVisual.SEMAFORO, texto=desc,
            confianca=NivelConfiancaVisual.ALTA,
            timestamp=datetime.now().isoformat(),
        )

    @staticmethod
    def ler_onibus() -> LeituraCena:
        numero = random.choice(["432", "5100-10", "8000", "978J", "177L-10"])
        linha = random.choice([
            "Metro Santana", "Largo Sao Francisco", "Terminal Princesa Isabel",
            "Aeroporto de Congonhas", "Estacao da Se",
        ])
        return LeituraCena(
            tipo=TipoLeituraVisual.ONIBUS,
            texto=f"Onibus {numero} -- {linha}",
            confianca=NivelConfiancaVisual.MEDIA,
            timestamp=datetime.now().isoformat(),
        )

    @staticmethod
    def ler_dinheiro() -> LeituraCena:
        valor = random.choice(["2 reais", "5 reais", "10 reais", "20 reais",
                               "50 reais", "100 reais"])
        return LeituraCena(
            tipo=TipoLeituraVisual.DINHEIRO, texto=f"Nota de {valor}",
            confianca=NivelConfiancaVisual.ALTA,
            timestamp=datetime.now().isoformat(),
        )

    @staticmethod
    def detectar_obstaculo() -> Optional[ObstaculoDetectado]:
        """Simula deteccao de obstaculo a frente (3-15 metros)."""
        if random.random() < 0.7:  # 70% nada
            return None
        tipo = random.choice(list(TipoPerigo))
        dist = random.uniform(3.0, 15.0)
        conf = random.choice([
            NivelConfiancaVisual.ALTA, NivelConfiancaVisual.MEDIA,
        ])
        acoes = {
            TipoPerigo.ESCADA: "Reduza o passo. Escada a frente.",
            TipoPerigo.BURACO: "Desvie 1 metro a direita.",
            TipoPerigo.OBRA: "Obra a frente. Calcada estreita.",
            TipoPerigo.CARRO_ESTACIONADO: "Carro na calcada. Desvie.",
            TipoPerigo.POSTE_ARBORE: "Obstaculo a frente. Desvie.",
            TipoPerigo.VIDRO_PORTA: "Porta de vidro a frente. Cuidado.",
            TipoPerigo.SEMAFORO_VERMELHO: "PARE. Semaforo vermelho.",
        }
        return ObstaculoDetectado(
            tipo=tipo, distancia_m=round(dist, 1),
            direcao_graus=random.uniform(-30, 30),
            confianca=conf, timestamp=datetime.now().isoformat(),
            acao_recomendada=acoes.get(tipo, "Atencao."),
        )


class SimuladorPontosReferencia:
    """Simula POIs proximos. No mundo real: OpenStreetMap Overpass API."""

    POIS_EXEMPLO = [
        ("Farmacia Sao Joao", "farmacia", "direita", 25),
        ("Padaria Pao Quente", "padaria", "esquerda", 40),
        ("Caixa 24h", "banco", "direita", 60),
        ("Ponto de onibus", "transporte", "frente", 15),
        ("Praca da Se", "praca", "frente", 120),
        ("Metro Se", "metro", "direita", 200),
        ("Mercado Municipal", "mercado", "esquerda", 300),
        ("Banheiro publico", "sanitario", "direita", 80),
        ("Banco do Brasil", "banco", "esquerda", 90),
        ("Escola Estadual", "educacao", "frente", 150),
    ]

    @staticmethod
    def buscar(pos: Posicao, raio_m: float = 50.0) -> List[PontoReferencia]:
        resultado: List[PontoReferencia] = []
        for nome, tipo, lado, dist in SimuladorPontosReferencia.POIS_EXEMPLO:
            if dist > raio_m:
                continue
            dir_g = {"direita": 90, "esquerda": 270, "frente": 0, "tras": 180}[lado]
            resultado.append(PontoReferencia(
                nome=nome, tipo=tipo, distancia_m=float(dist),
                direcao_graus=float(dir_g), lado=lado,
            ))
        return resultado


# ============================================================================
# 5. ENGINE -- ORIENTACAO
# ============================================================================

class OrientacaoEngine:
    """Responde 'Onde estou?' usando GPS + bussola + POIs."""

    def __init__(self) -> None:
        self.perfil: PerfilGuia = PerfilGuia()
        self.gps = SimuladorGPS()
        self.poi_db = SimuladorPontosReferencia()

    def onde_estou(self, pos: Optional[Posicao] = None) -> str:
        """Gera frase falada de localizacao."""
        if pos is None:
            pos = self.gps.ler()

        cardeal = _graus_para_cardeal(pos.rumo_graus)
        partes = [
            f"Voce esta proximo da coordenada "
            f"{pos.latitude:.4f}, {pos.longitude:.4f}.",
            f"Voce esta olhando para o {cardeal}.",
        ]

        # precisao
        if pos.precisao_gps_m > 10:
            partes.append(f"Precisao do GPS: {pos.precisao_gps_m:.0f} metros. "
                          f"Pode estar deslocado.")
        else:
            partes.append(f"Precisao do GPS: {pos.precisao_gps_m:.0f} metros. Boa.")

        return " ".join(partes)

    def descrever_arredores(self, pos: Optional[Posicao] = None) -> str:
        """Lista pontos de referencia proximos."""
        if pos is None:
            pos = self.gps.ler()

        pois = self.poi_db.buscar(pos, raio_m=self.perfil.raio_busca_referencia_m)
        if not pois:
            return "Nao tenho pontos de referencia proximos no momento."

        partes = ["Ao seu redor:"]
        for poi in sorted(pois, key=lambda p: p.distancia_m)[:5]:
            rel = _direcao_relativa(pos.rumo_graus, poi.direcao_graus)
            partes.append(
                f"{poi.nome} ({poi.tipo}), {poi.distancia_m:.0f} metros, {rel}."
            )
        return " ".join(partes)

    def bussola_falada(self, alvo_graus: float, pos: Optional[Posicao] = None) -> str:
        """Diz como girar para alcancar uma direcao-alvo."""
        if pos is None:
            pos = self.gps.ler()
        diff = (alvo_graus - pos.rumo_graus) % 360
        if diff > 180:
            diff -= 360
        abs_diff = abs(diff)
        if abs_diff < 10:
            return "Voce ja esta na direcao certa."
        lado = "direita" if diff > 0 else "esquerda"
        alvo_cardeal = _graus_para_cardeal(alvo_graus)
        return (f"Gire {abs_diff:.0f} graus a {lado} para olhar para o "
                f"{alvo_cardeal}.")


# ============================================================================
# 6. ENGINE -- NAVEGACAO
# ============================================================================

class NavegacaoEngine:
    """Calcula e guia rotas a pe para cegos."""

    def __init__(self) -> None:
        self.perfil: PerfilGuia = PerfilGuia()
        self.rota_ativa: Optional[Rota] = None
        self.gps = SimuladorGPS()
        self.camera = SimuladorCamera()

    def calcular_rota(self, origem: Posicao, destino: Posicao,
                      destino_nome: str) -> Rota:
        """
        Calcula rota a pe. No mundo real: OSRM / GraphHopper / OSM.
        Aqui: simulacao com passos realistas.
        """
        # distancia aproximada (haversine simplificado)
        dlat = (destino.latitude - origem.latitude) * 111000
        dlon = (destino.longitude - origem.longitude) * 111000 * math.cos(
            math.radians(origem.latitude))
        dist_total = math.sqrt(dlat ** 2 + dlon ** 2)
        if dist_total < 1:
            dist_total = random.uniform(300, 800)

        passos_template = [
            (TipoInstrucao.SEGUIR_EM_FRENTE, 80, "Siga em frente pela calcada."),
            (TipoInstrucao.ATRAVESSAR, 0, "Atravesse a rua na faixa. "
             "PARE e ESCUTE o transito antes."),
            (TipoInstrucao.VIRAR_DIREITA, 0, "Apos atravessar, vire a direita."),
            (TipoInstrucao.SEGUIR_EM_FRENTE, 120, "Siga em frente por 120 metros."),
            (TipoInstrucao.CURVA_LEVE_ESQ, 60, "A calcada faz curva leve a esquerda."),
            (TipoInstrucao.VIRAR_ESQUERDA, 0, "Vire a esquerda na esquina."),
            (TipoInstrucao.SEGUIR_EM_FRENTE, 50, "Siga em frente. Quase la."),
            (TipoInstrucao.CHEGADA, 0, f"Chegou ao destino: {destino_nome}."),
        ]

        passos: List[PassoRota] = []
        for i, (instr, dist, desc) in enumerate(passos_template):
            perigos: List[TipoPerigo] = []
            if instr == TipoInstrucao.ATRAVESSAR:
                perigos = [TipoPerigo.SEMAFORO_VERMELHO, TipoPerigo.TRANSITO_RAPIDO]
            elif instr == TipoInstrucao.SEGUIR_EM_FRENTE and i > 4:
                perigos = [TipoPerigo.POSTE_ARBORE]
            passos.append(PassoRota(
                indice=i, instrucao=instr,
                distancia_ate_proximo_m=dist, descricao=desc,
                perigos=perigos,
            ))

        tempo = dist_total / self.perfil.velocidade_caminhada_ms / 60

        rota = Rota(
            id=f"ROTA-{datetime.now().strftime('%H%M%S')}",
            origem=origem, destino=destino, destino_nome=destino_nome,
            passos=passos, distancia_total_m=round(dist_total, 1),
            tempo_estimado_min=round(tempo, 1),
            acessivel_cadeirante=not self.perfil.evirar_escadas if False else True,
        )
        # corrigir typo
        rota.acessivel_cadeirante = not getattr(self.perfil, 'evitar_escadas', True)
        self.rota_ativa = rota
        return rota

    def proxima_instrucao(self, pos: Optional[Posicao] = None) -> str:
        """Retorna a instrucao de navegacao atual."""
        if self.rota_ativa is None:
            return "Nenhuma rota ativa. Diga para onde quer ir."
        if pos is None:
            pos = self.gps.ler()

        rota = self.rota_ativa
        if rota.passo_atual_idx >= len(rota.passos):
            return "Voce chegou ao destino."

        passo = rota.passos[rota.passo_atual_idx]
        prefixo = f"[Passo {passo.indice + 1} de {len(rota.passos)}] "

        # aviso de perigo neste passo
        aviso_perigo = ""
        if passo.perigos:
            perigo_nomes = ", ".join(p.rotulo for p in passo.perigos)
            aviso_perigo = f" CUIDADO: {perigo_nomes}."

        # distancia ao proximo
        distancia_txt = ""
        if passo.distancia_ate_proximo_m > 0:
            distancia_txt = f" ({passo.distancia_ate_proximo_m:.0f} metros)"

        return f"{prefixo}{passo.instrucao.rotulo}{distancia_txt}. " \
               f"{passo.descricao}{aviso_perigo}"

    def avancar_passo(self) -> str:
        """Marca passo atual como concluido e avanca."""
        if self.rota_ativa is None:
            return "Sem rota ativa."
        rota = self.rota_ativa
        if rota.passo_atual_idx < len(rota.passos):
            rota.passos[rota.passo_atual_idx].concluido = True
            rota.passo_atual_idx += 1
        if rota.passo_atual_idx >= len(rota.passos):
            return f"Chegou ao destino: {rota.destino_nome}. Rota concluida!"
        return self.proxima_instrucao()

    def verificar_perigo_a_frente(self) -> Optional[ObstaculoDetectado]:
        """Usa camera para detectar perigo imediato."""
        return self.camera.detectar_obstaculo()

    def alertar_perigo(self, obs: ObstaculoDetectado) -> str:
        """Gera alerta falado de perigo."""
        if obs.confianca.peso < NivelConfiancaVisual.MEDIA.peso:
            return ""  # confianca baixa demais, nao alertar
        prefixo = "ATENCAO! " if obs.distancia_m < 5 else ""
        return (f"{prefixo}{obs.tipo.rotulo} a {obs.distancia_m:.0f} metros. "
                f"{obs.acao_recomendada}")

    def resumo_rota(self) -> str:
        """Resumo da rota ativa."""
        if self.rota_ativa is None:
            return "Sem rota ativa."
        r = self.rota_ativa
        return (f"Rota para {r.destino_nome}: {r.distancia_total_m:.0f} metros, "
                f"~{r.tempo_estimado_min:.0f} minutos a pe, "
                f"{len(r.passos)} passos.")


# ============================================================================
# 7. ENGINE -- LEITURA VISUAL
# ============================================================================

class LeituraVisualEngine:
    """Le o mundo atraves da camera."""

    def __init__(self) -> None:
        self.perfil: PerfilGuia = PerfilGuia()
        self.camera = SimuladorCamera()
        self._ultimo_texto: Optional[str] = None

    def ler_texto(self) -> str:
        """Le texto da camera (OCR)."""
        leitura = self.camera.ler_texto()
        self._ultimo_texto = leitura.texto
        prefixo = ""
        if leitura.confianca == NivelConfiancaVisual.BAIXA:
            prefixo = "Acho que leio: "
        elif leitura.confianca == NivelConfiancaVisual.FALHOU:
            return "Nao consegui ler nenhum texto. Aproxime a camera."
        detalhe = f" ({leitura.detalhes})" if leitura.detalhes else ""
        return f"{prefixo}{leitura.texto}{detalhe}"

    def descrever_cena(self, indoor: bool = False) -> str:
        """Descreve a cena a frente."""
        cena = self.camera.ler_cena(indoor=indoor)
        if cena.confianca.peso < NivelConfiancaVisual.MEDIA.peso:
            return "Nao tenho certeza do que vejo. Boa iluminacao ajuda."
        return cena.texto

    def ler_semaforo(self) -> str:
        """Le a cor do semaforo para pedestre."""
        sem = self.camera.ler_semaforo()
        return sem.texto

    def ler_onibus_chegando(self) -> str:
        """Identifica onibus que esta chegando no ponto."""
        onb = self.camera.ler_onibus()
        return f"Onibus chegando: {onb.texto}."

    def ler_dinheiro(self) -> str:
        """Identifica cedula/moeda na camera."""
        din = self.camera.ler_dinheiro()
        return din.texto

    def ler_tudo(self, indoor: bool = False) -> str:
        """Leitura completa: cena + texto + semaforo (se aplicavel)."""
        partes: List[str] = []
        cena = self.descrever_cena(indoor=indoor)
        if cena:
            partes.append(cena)
        texto = self.ler_texto()
        if "Nao consegui" not in texto:
            partes.append(f"Leio: {self._ultimo_texto}")
        return ". ".join(partes) + "."


# ============================================================================
# 8. ENGINE PRINCIPAL -- ORQUESTRA OS 3 MODOS
# ============================================================================

class DigitalGuideEngine:
    """Motor principal do Guia Digital -- orquestra os 3 modos."""

    def __init__(self) -> None:
        self.perfil: PerfilGuia = PerfilGuia()
        self.modo: ModoOperacao = ModoOperacao.PAUSADO
        self.hardware_estado: EstadoHardware = EstadoHardware.TUDO_OK
        self.orientacao = OrientacaoEngine()
        self.navegacao = NavegacaoEngine()
        self.leitura = LeituraVisualEngine()
        self.historico_alertas: deque = deque(maxlen=100)
        self._alertas_recentes: Dict[str, datetime] = {}

    def configurar_perfil(
        self, usuario: str = "cidadao", cego: bool = True,
        baixa_visao: bool = False, surdo_cego: bool = False,
        cadeirante: bool = False, idoso: bool = False,
        detalhe_narrativa: str = "normal",
    ) -> PerfilGuia:
        """Configura o perfil do usuario."""
        self.perfil = PerfilGuia(
            usuario=usuario, cego=cego, baixa_visao=baixa_visao,
            surdo_cego=surdo_cego, cadeirante=cadeirante, idoso=idoso,
            detalhe_narrativa=detalhe_narrativa,
        )
        self.orientacao.perfil = self.perfil
        self.navegacao.perfil = self.perfil
        self.leitura.perfil = self.perfil
        return self.perfil

    def mudar_modo(self, modo: ModoOperacao) -> str:
        """Muda o modo de operacao."""
        self.modo = modo
        nomes = {
            ModoOperacao.ORIENTACAO: "modo orientacao",
            ModoOperacao.NAVEGACAO: "modo navegacao",
            ModoOperacao.LEITURA: "modo leitura",
            ModoOperacao.PAUSADO: "pausado",
        }
        return f"Guia no {nomes[modo]}."

    def processar_comando_voz(self, texto: str) -> str:
        """Processa comando de voz do usuario."""
        t = texto.lower().strip()

        # comandos de modo
        if any(x in t for x in ["onde estou", "localiza", "minha localizacao"]):
            self.modo = ModoOperacao.ORIENTACAO
            return self.orientacao.onde_estou()
        if any(x in t for x in ["o que tem", "descreva", "leia", "o que ve"]):
            self.modo = ModoOperacao.LEITURA
            indoor = "dentro" in t or "interno" in t
            return self.leitura.ler_tudo(indoor=indoor)
        if "semaforo" in t:
            return self.leitura.ler_semaforo()
        if "onibus" in t or "ônibus" in t:
            return self.leitura.ler_onibus_chegando()
        if "dinheiro" in t or "nota" in t:
            return self.leitura.ler_dinheiro()
        if "arredores" in t or "ao redor" in t or "perto" in t:
            return self.orientacao.descrever_arredores()
        if any(x in t for x in ["como chego", "rota para", "me leva", "ir para"]):
            self.modo = ModoOperacao.NAVEGACAO
            # extrair destino da fala
            return ("Para onde voce quer ir? Diga o nome do lugar "
                    "e eu calculo a rota.")
        if "proxima" in t or "próximo passo" in t:
            return self.navegacao.avancar_passo()
        if "repete" in t or "repetir" in t:
            return self._ultima_fala()
        if any(x in t for x in ["parar", "pare", "silencio", "pausa"]):
            self.modo = ModoOperacao.PAUSADO
            return "Guia pausado. Diga 'continuar' quando quiser."
        if "continuar" in t or "volta" in t:
            self.modo = ModoOperacao.ORIENTACAO
            return "Guia ativo. Onde voce quer ir?"

        return ("Nao entendi. Posso: localizar, descrever, ler texto, "
                "ler semaforo, identificar onibus, calcular rota. "
                "O que voce precisa?")

    def _ultima_fala(self) -> str:
        if self.historico_alertas:
            return self.historico_alertas[-1]
        return "Nada para repetir."

    def ciclo_monitoramento(self) -> List[str]:
        """
        Executa um ciclo de monitoramento (chamado a cada ~2 segundos).
        No modo navegacao, verifica perigos a frente.
        """
        alertas: List[str] = []
        if self.modo == ModoOperacao.PAUSADO:
            return alertas

        # verificacao de perigo (sempre ativa em navegacao)
        if self.modo == ModoOperacao.NAVEGACAO:
            obs = self.navegacao.verificar_perigo_a_frente()
            if obs:
                alerta = self.navegacao.alertar_perigo(obs)
                if alerta:
                    # cooldown por tipo
                    agora = datetime.now()
                    ultimo = self._alertas_recentes.get(obs.tipo.id)
                    if ultimo is None or (agora - ultimo).total_seconds() > 10:
                        alertas.append(alerta)
                        self._alertas_recentes[obs.tipo.id] = agora
                        self.historico_alertas.append(alerta)

        return alertas

    def scorecard(self) -> Dict[str, Any]:
        return {
            "modo_operacao": self.modo.id,
            "hardware": self.hardware_estado.id,
            "perfil_cego": self.perfil.cego,
            "perfil_baixa_visao": self.perfil.baixa_visao,
            "perfil_surdo_cego": self.perfil.surdo_cego,
            "perfil_cadeirante": self.perfil.cadeirante,
            "tipos_orientacao": len(list(TipoOrientacao)),
            "tipos_instrucao": len(list(TipoInstrucao)),
            "tipos_perigo": len(list(TipoPerigo)),
            "tipos_leitura_visual": len(list(TipoLeituraVisual)),
            "rotas_calculadas": 1 if self.navegacao.rota_ativa else 0,
            "alertas_no_historico": len(self.historico_alertas),
        }


# ============================================================================
# 9. DEMO
# ============================================================================

def _demo() -> None:
    g = DigitalGuideEngine()

    print("=" * 70)
    print("OpenDigitalGuide -- O Guia Digital para Cegos")
    print("=" * 70)

    # --- Perfil ---
    print("\n[PERFIL: Joao -- cego, caminhando na rua]")
    g.configurar_perfil("Joao", cego=True, detalhe_narrativa="detalhado")
    print(f"  Usuario: {g.perfil.usuario}")
    print(f"  Cego: {g.perfil.cego}")
    print(f"  Antecedencia perigo: {g.perfil.aviso_antecedencia_m}m")
    print(f"  Velocidade caminhada: {g.perfil.velocidade_caminhada_ms} m/s")

    # --- Modo Orientacao ---
    print("\n[ modo ORIENTACAO: 'Onde estou?']")
    g.mudar_modo(ModoOperacao.ORIENTACAO)
    print(f"  Iara diz: \"{g.orientacao.onde_estou()}\"")
    print(f"  Iara diz: \"{g.orientacao.descrever_arredores()}\"")

    # --- Modo Leitura ---
    print("\n[ modo LEITURA: 'O que tem a minha frente?']")
    g.mudar_modo(ModoOperacao.LEITURA)
    print(f"  Cena: \"{g.leitura.descrever_cena(indoor=False)}\"")
    print(f"  Texto: \"{g.leitura.ler_texto()}\"")
    print(f"  Semaforo: \"{g.leitura.ler_semaforo()}\"")
    print(f"  Onibus: \"{g.leitura.ler_onibus_chegando()}\"")
    print(f"  Dinheiro: \"{g.leitura.ler_dinheiro()}\"")

    # --- Modo Navegacao ---
    print("\n[ modo NAVEGACAO: 'Como chego na Farmacia Sao Joao?']")
    g.mudar_modo(ModoOperacao.NAVEGACAO)
    origem = SimuladorGPS.ler()
    destino = Posicao(
        latitude=origem.latitude + 0.003,
        longitude=origem.longitude + 0.002,
    )
    rota = g.navegacao.calcular_rota(origem, destino, "Farmacia Sao Joao")
    print(f"  {g.navegacao.resumo_rota()}")
    print()
    for i in range(len(rota.passos)):
        print(f"  {g.navegacao.proxima_instrucao()}")
        g.navegacao.avancar_passo()

    # --- Simulacao de perigo ---
    print("\n[ SIMULACAO: 10 ciclos de monitoramento (detectar perigo)]")
    g.mudar_modo(ModoOperacao.NAVEGACAO)
    g.navegacao.calcular_rota(origem, destino, "Farmacia")
    for ciclo in range(10):
        alertas = g.ciclo_monitoramento()
        if alertas:
            for a in alertas:
                print(f"  Ciclo {ciclo}: Iara diz: \"{a}\"")

    # --- Comandos por voz ---
    print("\n[ COMANDOS POR VOZ]")
    g.configurar_perfil("Joao", cego=True)
    comandos = [
        "onde estou",
        "o que tem aqui",
        "semaforo",
        "onibus",
        "dinheiro",
        "como chego na padaria",
        "repete",
        "pare",
        "continuar",
        "comando invalido",
    ]
    for cmd in comandos:
        resp = g.processar_comando_voz(cmd)
        print(f"  Usuario: \"{cmd}\"")
        print(f"  Iara: \"{resp}\"")
        print()

    # --- Estatisticas ---
    print("[ ESTATISTICAS]")
    sc = g.scorecard()
    for k, v in sc.items():
        print(f"  {k:.<28} {v}")

    # --- Filosofia ---
    print("\n" + "=" * 70)
    print("FILOSOFIA -- O Guia Digital para Cegos")
    print("=" * 70)
    print("""
O QUE O CAO-GUIA FAZ:
  Conduz. Leva do ponto A ao ponto B. Evita obstaculos.
  O cao-guia e INSUBSTITUIVEL na conducao fisica.

O QUE O CAO-GUIA NAO FAZ:
  Nao fala. Nao le. Nao explica.
  Nao diz "a farmacia fechou".
  Nao diz "o onibus que chega e o 432".
  Nao diz "o semaforo esta vermelho".
  Nao le o cardapio do restaurante.
  Nao identifica a nota de 50 reais.

O OpenDigitalGuide FAZ:
  Le o mundo. Descreve cenas. Le textos.
  Identifica semaforos, onibus, dinheiro.
  Calcula rotas acessiveis. Avisa perigos.
  Responde perguntas por voz.
  Tudo offline, tudo local, tudo privado.

JUNTOS:
  O cao-guia conduz o corpo.
  O DigitalGuide descreve o mundo.
  Um leva. O outro explica.
  O cego ganha AUTONOMIA total.

A LACUNA:
  Hoje o cego depende de outras pessoas para:
  - Saber se a loja esta aberta
  - Ler um cardapio
  - Identificar o onibus certo
  - Saber a cor do semaforo
  - Contar dinheiro
  - Encontrar o banheiro

  O OpenDigitalGuide elimina essa dependencia.
  Nao com caridade. Com TECNOLOGIA.

O PRINCIPIO:
  A autonomia do cego nao e um favor.
  E um DIREITO (P1, P2).
  A tecnologia que nao serve ao cego
  nao serve a ninguem.
""")


if __name__ == "__main__":
    _demo()
