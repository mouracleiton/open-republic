# Treinamento Avancado 04 -- Series Temporais e Previsao

**Nivel:** Avancado
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 50 min

**Objetivo:** Analisar serie temporal, calcular medias moveis e tendencias.

---

```portugol++

// TREINAMENTO AVANCADO -- Licao 04: Series Temporais
// ============================================================
// Series temporais sao dados coletados ao longo do tempo.
// Aplicacoes: vendas mensais, acessos diarios, cotacoes.

// ============================================================
// 1. CLASSE SERIE TEMPORAL
// ============================================================

classe SerieTemporal:
    valores: [flutuante] = []
    rotulos: [texto] = []

    funcao adicionar_ponto(self, rotulo: texto, valor: flutuante) -> vazio:
        self.valores.adicione(valor)
        self.rotulos.adicione(rotulo)

    funcao media_movel(self, janela: inteiro) -> [flutuante]:
        // Media movel simples de N periodos
        seja resultado: [flutuante] = []
        sea n = tamanho(self.valores)
        para cada i em intervalo(n):
            se i < janela - 1 entao:
                resultado.adicione(0.0)
            senao:
                seja soma: flutuante = 0.0
                para cada j em intervalo(janela):
                    soma = soma + self.valores[i - j]
                resultado.adicione(soma / janela)
        retorne resultado

    funcao taxa_crescimento(self) -> [flutuante]:
        // Variacao percentual mes a mes
        seja resultado: [flutuante] = [0.0]
        para cada i em intervalo(1, tamanho(self.valores)):
            se self.valores[i - 1] > 0 entao:
                seja taxa = ((self.valores[i] - self.valores[i - 1]) / self.valores[i - 1]) * 100.0
                resultado.adicione(taxa)
            senao:
                resultado.adicione(0.0)
        retorne resultado

    funcao tendencia(self) -> texto:
        // Determina se a serie esta crescendo ou decrescendo
        seja taxa = self.taxa_crescimento()
        seja soma_taxas: flutuante = 0.0
        para cada t em taxa:
            soma_taxas = soma_taxas + t
        seja media_taxa = soma_taxas / tamanho(taxa)

        se media_taxa > 5.0 entao:
            retorne "CRESCIMENTO FORTE"
        senao se media_taxa > 0.0 entao:
            retorne "CRESCIMENTO MODERADO"
        senao se media_taxa > -5.0 entao:
            retorne "DECLINIO MODERADO"
        senao:
            retorne "DECLINIO FORTE"

    funcao projetar(self, periodos: inteiro) -> [flutuante]:
        // Projeta valores futuros baseado na taxa media de crescimento
        seja taxa = self.taxa_crescimento()
        seja soma: flutuante = 0.0
        para cada t em taxa:
            soma = soma + t
        seja taxa_media = soma / tamanho(taxa) / 100.0

        seja ultimo = self.valores[tamanho(self.valores) - 1]
        seja projecao: [flutuante] = []
        para cada i em intervalo(periodos):
            ultimo = ultimo * (1.0 + taxa_media)
            projecao.adicione(ultimo)
        retorne projecao


// ============================================================
// 2. APLICACAO: ANALISE DE VENDAS MENSAIS
// ============================================================

seja serie = SerieTemporal()

// Vendas de 12 meses
serie.adicionar_ponto("Jan", 12000.0)
serie.adicionar_ponto("Fev", 15000.0)
serie.adicionar_ponto("Mar", 13000.0)
serie.adicionar_ponto("Abr", 18000.0)
serie.adicionar_ponto("Mai", 22000.0)
serie.adicionar_ponto("Jun", 20000.0)
serie.adicionar_ponto("Jul", 25000.0)
serie.adicionar_ponto("Ago", 28000.0)
serie.adicionar_ponto("Set", 26000.0)
serie.adicionar_ponto("Out", 32000.0)
serie.adicionar_ponto("Nov", 38000.0)
serie.adicionar_ponto("Dez", 42000.0)

imprima("=== ANALISE DE SERIE TEMPORAL ===")
imprima("Periodos: " + texto(tamanho(serie.valores)))

// Tendencia
imprima("Tendencia: " + serie.tendencia())

// Media movel 3 meses
imprima("\n--- MEDIA MOVEL (3 meses) ---")
seja mm3 = serie.media_movel(3)
para cada (i, valor) em enumere(mm3):
    se i >= 2 entao:
        imprima("  " + serie.rotulos[i] + ": " + texto(valor))

// Taxa de crescimento
imprima("\n--- TAXA DE CRESCIMENTO MENSAL ---")
seja taxas = serie.taxa_crescimento()
para cada (i, taxa) em enumere(taxas):
    se i > 0 entao:
        imprima("  " + serie.rotulos[i] + ": " + texto(taxa) + "%")

// Projecao proximos 3 meses
imprima("\n--- PROJECAO (3 meses) ---")
seja projecao = serie.projetar(3)
seja meses_futuros = ["Jan+1", "Fev+1", "Mar+1"]
para cada (i, valor) em enumere(projecao):
    imprima("  " + meses_futuros[i] + ": R$ " + texto(valor))

// EXERCICIO: adicione deteccao de sazonalidade comparando
// meses equivalentes e calculando o indice sazonal.
```
