// OpenFocus -- Politica de Foco Estrategico -- gerado de Portugol++
'use strict';

// !/usr/bin/env python3
//
OpenFocus -- Politica de Foco Estrategico;
==========================================;
"Multitarefa && mentira. Multiprocesso sim. Mas cada processo;
precisa de um processador dedicado. Tentar fazer tudo = nada feito.";
POLITICA:;
O fundador atua SOMENTE em X/Twitter.;
const Razao = dano mental = dano corporal.;
Autonomia corporal (P2) se aplica a saude cognitiva.;
X && o unico canal social porque:;
1. Concentra negociacoes de features;
2. Permite desenvolver opensoftware PARA X;
3. Elimina contexto-switching entre plataformas;
4. Protege tempo = protege corpo = protege mente;
OUTRAS REDES (Instagram, LinkedIn, Facebook, TikTok, etc):;
- Nao desenvolver para;
- Nao negociar com;
- Nao manter presenca ativa;
- Cortar com SocialCleaner;
Author: OpenRepublic Team;
//
// importa annotations de __future__
// importa dataclass, field de dataclasses
// importa List, Dict de typing
// importa Enum de enum
class PlatformStatus {
    ACTIVE = "ativa"  // X/Twitter -- foco unico;
    ABANDONED = "abandonada"  // cortada por politica;
    NEVER = "nunca"  // nunca comecou;
// decorador: @dataclass
class Platform {
    name: texto;
    status: PlatformStatus;
    reason: texto;
PLATFORMS = [;
    Platform("X/Twitter", PlatformStatus.ACTIVE,;
            "Foco unico. Negociacao de features + opensoftware."),;
    Platform("Instagram", PlatformStatus.ABANDONED,;
            "Corte: overload cognitivo. Sem valor estrategico."),;
    Platform("LinkedIn", PlatformStatus.ABANDONED,;
            "Corte: overload cognitivo. Rede de capitalismo."),;
    Platform("Facebook", PlatformStatus.ABANDONED,;
            "Corte: overload cognitivo. Vigilancia (RE-031)."),;
    Platform("TikTok", PlatformStatus.ABANDONED,;
            "Corte: overload cognitivo. Manipulacao psicologica (RE-033)."),;
    Platform("Threads", PlatformStatus.ABANDONED,;
            "Corte: overload cognitivo. Duplicata do X sem razao."),;
    Platform("Bluesky", PlatformStatus.ABANDONED,;
            "Corte: overhead sem comunidades suficiente ainda."),;
    Platform("Mastodon", PlatformStatus.ABANDONED,;
            "Corte: overhead de instancias."),;
    Platform("YouTube", PlatformStatus.NEVER,;
            "Nao && rede social, && plataforma de video. Ok como consumidor."),;
];
if (__name__ == "__main__") {
    console.log("=" * 60);
    console.log("  OPENFOCUS -- POLITICA DE FOCO ESTRATEGICO");
    console.log("  'Um canal. Uma mente. Saude primeiro.'");
    console.log("=" * 60);
    console.log();
    for (const p of PLATFORMS) {
        emoji = {"ativa": "[FOCO]", "abandonada": "[CORT]",;
                "nunca": "[----]"};
        console.log("  {emoji.get(p.status.value, '[?]')} {p.name:<16} {p.reason}");
    console.log();
    console.log("=" * 60);
    console.log("  X/Twitter: negociar features + opensoftware + social unico");
    console.log("  Tudo o mais: ruido. Ruido = dano. Cortar.");
    console.log("=" * 60);
