# Treinamento Avancado 01 -- Pipelines de Processamento de Dados

**Nivel:** Avancado
**Topico:** Analise de Dados com Portugol++
**Duracao estimada:** 50 min

**Objetivo:** Construir pipelines ETL (Extract, Transform, Load) em PP.

---

```portugol++

// TREINAMENTO AVANCADO -- Licao 01: Pipelines ETL
// ============================================================
// Um pipeline e uma sequencia de transformacoes.
// Dados crus entram de um lado, insights saido do outro.

// ============================================================
// CLASSE PIPELINE -- representa uma cadeia de transformacoes
// ============================================================

classe Pipeline:
    nome: texto
    etapas: [texto] = []
    dados_entrada: [Dict] = []
    dados_saida: [Dict] = []

    funcao executar(self) -> [Dict]:
        imprima("Pipeline '" + self.nome + "' iniciado -- " + texto(tamanho(self.dados_entrada)) + " registros")
        self.dados_saida = self.dados_entrada
        para cada (i, etapa) em enumere(self.etapas):
            imprima("  Etapa " + texto(i + 1) + ": " + etapa)
            self.dados_saida = self._aplicar_etapa(etapa, self.dados_saida)
            imprima("    -> " + texto(tamanho(self.dados_saida)) + " registros apos etapa")
        imprima("Pipeline concluido: " + texto(tamanho(self.dados_saida)) + " registros finais")
        retorne self.dados_saida

    funcao _aplicar_etapa(self, etapa: texto, dados: [Dict]) -> [Dict]:
        se etapa == "limpar_nulos" entao:
            retorne self._limpar_nulos(dados)
        se etapa == "normalizar" entao:
            retorne self._normalizar(dados)
        se etapa == "remover_outliers" entao:
            retorne self._remover_outliers(dados)
        retorne dados

    funcao _limpar_nulos(self, dados: [Dict]) -> [Dict]:
        seja limpos: [Dict] = []
        para cada r em dados:
            se r["valor"] != nulo e r["valor"] > 0 entao:
                limpos.adicione(r)
        retorne limpos

    funcao _normalizar(self, dados: [Dict]) -> [Dict]:
        // Min-Max normalization: (x - min) / (max - min)
        seja minimo: flutuante = 999999.0
        seja maximo: flutuante = 0.0
        para cada r em dados:
            se r["valor"] < minimo entao:
                minimo = r["valor"]
            se r["valor"] > maximo entao:
                maximo = r["valor"]

        para cada r em dados:
            r["valor_norm"] = (r["valor"] - minimo) / (maximo - minimo)
        retorne dados

    funcao _remover_outliers(self, dados: [Dict]) -> [Dict]:
        // Remove valores acima de 3x a media
        seja soma: flutuante = 0.0
        para cada r em dados:
            soma = soma + r["valor"]
        seja media = soma / tamanho(dados)
        seja limite = media * 3.0

        seja limpos: [Dict] = []
        para cada r em dados:
            se r["valor"] <= limite entao:
                limpos.adicione(r)
        retorne limpos


// ============================================================
// EXECUTANDO O PIPELINE
// ============================================================

seja dados_crus = [
    {"id": 1, "produto": "A", "valor": 100.0},
    {"id": 2, "produto": "B", "valor": 200.0},
    {"id": 3, "produto": "C", "valor": 0.0},
    {"id": 4, "produto": "D", "valor": 5000.0},
    {"id": 5, "produto": "E", "valor": 150.0},
    {"id": 6, "produto": "F", "valor": 300.0},
    {"id": 7, "produto": "G", "valor": 50.0},
]

seja pipe = Pipeline()
pipe.nome = "Limpeza de Dados"
pipe.etapas = ["limpar_nulos", "remover_outliers", "normalizar"]
pipe.dados_entrada = dados_crus

seja resultado = pipe.executar()

imprima("\n--- RESULTADO FINAL ---")
para cada r em resultado:
    imprima("  " + r["produto"] + ": original=" + texto(r["valor"]) + " normalizado=" + texto(r["valor_norm"]))

// EXERCICIO: adicione etapas "agrupar_por_categoria" e
// "calcular_estatisticas" ao pipeline.
```
