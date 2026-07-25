# OpenLegoCode -- Programacao Modular em Formato LEGO

**Linguagem:** Portugol++ (PPM)

**Arquivo original:** `core/open_lego_code.py`

**Descricao:** =====================================================
"Escrever codigo e coisa do passado.
 Programar e ENCAIXAR pecas.
 Cada bloco faz UMA coisa.
 Blocos se conectam como LEGO.
 O programa e a CADEIA de blocos encaixados.
 Se uma peca quebra, troca. O resto funciona.
 Se uma peca melhora, todos que a usam melhoram.
 Ninguem escreve monolito. Todo mundo encaixa."
CONCEITO:
  Em vez de:
    def calcular_imposto(renda):
        if renda > 5000:
            return renda * 0.27
        return renda * 0.15
  Voce encaixa:
    [INPUT: renda] -> [CONDITIONAL] -> [MULTIPLY: 0.27] -> [OUTPUT]
                                  -> [MULTIPLY: 0.15] -> [OUTPUT]
  Cada bloco e REUSAVEL.
  Cada bloco e TESTAVEL isoladamente.
  Cada bloco pode ser TROCADO sem quebrar o resto.
  Cada bloco tem ENTRADA e SAIDA (conectores LEGO).
  IA pode GERAR blocos.
  Cidadaos podem MONTAR sem saber programar.
  Tudo visual. Tudo modular. Tudo LEGO.
Author: OpenRepublic Team

---

```portugol++

// !/usr/bin/env python3
// 
OpenLegoCode -- Programacao Modular em Formato LEGO
=====================================================

"Escrever codigo e coisa do passado.
 Programar e ENCAIXAR pecas.
 Cada bloco faz UMA coisa.
 Blocos se conectam como LEGO.
 O programa e a CADEIA de blocos encaixados.

 Se uma peca quebra, troca. O resto funciona.
 Se uma peca melhora, todos que a usam melhoram.
 Ninguem escreve monolito. Todo mundo encaixa."

CONCEITO:
  Em vez de:
    funcao calcular_imposto(renda):
        se renda > 5000 entao:
            retorne renda * 0.27
        retorne renda * 0.15

  Voce encaixa:
    [INPUT: renda] -> [CONDITIONAL] -> [MULTIPLY: 0.27] -> [OUTPUT]
                                  -> [MULTIPLY: 0.15] -> [OUTPUT]

  Cada bloco e REUSAVEL.
  Cada bloco e TESTAVEL isoladamente.
  Cada bloco pode ser TROCADO sem quebrar o resto.
  Cada bloco tem ENTRADA e SAIDA (conectores LEGO).

  IA pode GERAR blocos.
  Cidadaos podem MONTAR sem saber programar.
  Tudo visual. Tudo modular. Tudo LEGO.

Author: OpenRepublic Team
// 

// importa annotations de __future__

// importa hashlib
// importa json
// importa dataclass, field de dataclasses
// importa Any, Dict, List, Optional, Callable, Union de typing
// importa Enum de enum
// importa defaultdict de collections
// importa datetime de datetime


// ============================================================================
// 1. TIPOS DE CONECTORES (encaixes LEGO)
// ============================================================================

classe LegoPin herda de Enum:
    // Tipos de pinos (conectores) de entrada e saida.

    Cada pino tem um TIPO. So encaixa com pino do mesmo tipo.
    Como LEGO: pino 2x1 so encaixa em buraco 2x1.
    // 
    // Dados
    NUMBER = "numero"
    STRING = "texto"
    BOOLEAN = "sim_nao"
    LIST = "lista"
    DICT = "dicionario"
    ANY = "qualquer"  // encaixa em tudo

    // Especiais
    PERSON = "pessoa"
    CREDIT = "credito"
    EVENT = "evento"
    FILE = "arquivo"
    IMAGE = "imagem"
    AUDIO = "audio"
    OBJECT_3D = "objeto_3d"
    DIAGNOSIS = "diagnostico"
    TASK = "tarefa"
    VOTE = "voto"


// ============================================================================
// 2. BLOCO DE CODIGO LEGO
// ============================================================================

// decorador: @dataclass
classe LegoInput:
    // Entrada de um bloco (buraco onde outro bloco encaixa).
    name: texto
    pin_type: LegoPin
    seja required: logico = verdadeiro
    seja default: qualquer = nulo
    seja description: texto = ""


// decorador: @dataclass
classe LegoOutput:
    // Saida de um bloco (pino que encaixa em outro).
    name: texto
    pin_type: LegoPin
    seja description: texto = ""


// decorador: @dataclass
classe LegoBlock:
    // Um bloco de codigo LEGO.

    Cada bloco:
    - Tem ENTRADAS (buracos)
    - Tem SAIDAS (pinos)
    - Faz UMA coisa bem definida
    - Pode ser TESTADO isoladamente
    - Pode ser REUSADO em qualquer cadeia
    - Tem versao e autor
    // 
    block_id: texto
    name: texto
    category: texto // matematica, logica, texto, ia, saude, etc
    seja description: texto = ""

    // Conectores
    seja inputs: [LegoInput] = field(default_factory=list)
    seja outputs: [LegoOutput] = field(default_factory=list)

    // Execucao (funcao real ou descricao para IA gerar)
    seja logic: texto = ""  // descricao do que faz (IA implementa)
    seja code_rust: texto = ""  // codigo Rust gerado (producao)

    // Metadata
    seja author: texto = ""
    seja version: texto = "1.0.0"
    seja tested: logico = falso
    seja uses: inteiro = 0 // quantas cadeias usam este bloco
    seja color: texto = "blue"  // cor visual do bloco (categoria)

    funcao can_connect(self, other: "LegoBlock",
                    seja my_output_idx: inteiro = 0,
                    seja their_input_idx: inteiro = 0) -> logico:
        // Verifica se meu pino de saida encaixa na entrada do outro.
        se my_output_idx >= tamanho(self.outputs) entao:
            retorne falso
        se their_input_idx >= tamanho(other.inputs) entao:
            retorne falso

        my_out = self.outputs[my_output_idx]
        their_in = other.inputs[their_input_idx]

        // ANY encaixa em tudo
        se my_out.pin_type == LegoPin.ANY ou their_in.pin_type == LegoPin.ANY entao:
            retorne verdadeiro
        retorne my_out.pin_type == their_in.pin_type


// ============================================================================
// 3. CADEIA DE BLOCOS (programa LEGO)
// ============================================================================

// decorador: @dataclass
classe LegoConnection:
    // Conexao entre dois blocos.
    from_block: texto // ID do bloco de origem
    from_output: inteiro // indice da saida
    to_block: texto // ID do bloco de destino
    to_input: inteiro // indice da entrada
    seja valid: logico = verdadeiro


// decorador: @dataclass
classe LegoProgram:
    // Um programa montado com blocos LEGO.

    O programa e um GRAFO de blocos conectados.
    Cada bloco produz dados que alimentam o proximo.

    Exemplo de programa (calcular credito de trabalho):
      [INPUT: horas] -> [MULTIPLY: impacto_factor] -> [ADD: base] -> [OUTPUT: credito]
    // 
    program_id: texto
    name: texto
    seja description: texto = ""
    seja blocks: {texto: LegoBlock} = field(default_factory=dict)
    seja connections: [LegoConnection] = field(default_factory=list)
    seja created_by: texto = ""
    seja created_date: texto = ""

    // decorador: @property
    funcao block_count(self) -> inteiro:
        retorne tamanho(self.blocks)

    // decorador: @property
    funcao connection_count(self) -> inteiro:
        retorne tamanho(self.connections)

    // decorador: @property
    funcao is_valid(self) -> logico:
        // Verifica se TODAS as conexoes sao compativeis.
        retorne all(c.valid para c em self.connections)

    // decorador: @property
    funcao all_inputs_connected(self) -> logico:
        // Verifica se TODAS as entradas obrigatórias estao conectadas.
        connected_inputs = set()
        para cada conn em self.connections:
            connected_inputs.add("{conn.to_block}:{conn.to_input}")

        para cada (bid, block) em self.blocks.items():
            para cada (i, inp) em enumere(block.inputs):
                se inp.required  e  "{bid}:{i}" nao  in connected_inputs entao:
                    retorne falso
        retorne verdadeiro


// ============================================================================
// 4. CATALOGO DE BLOCOS PADRAO (biblioteca LEGO)
// ============================================================================

funcao build_block_library() -> {texto: LegoBlock}:
    // Constroi biblioteca de blocos LEGO padrao.

    blocks = {}

    // === ENTRADA / SAIDA ===
    blocks["IN-NUM"] = LegoBlock(
        "IN-NUM", "Entrada: Numero", "entrada",
        "Fornece um numero para a cadeia.",
        inputs = [],
        outputs = [LegoOutput("valor", LegoPin.NUMBER)],
        logic = "Retorna um numero fornecido pelo usuario.",
        color = "green",
    )
    blocks["IN-STR"] = LegoBlock(
        "IN-STR", "Entrada: Texto", "entrada",
        "Fornece um texto para a cadeia.",
        inputs = [],
        outputs = [LegoOutput("valor", LegoPin.STRING)],
        logic = "Retorna um texto fornecido pelo usuario.",
        color = "green",
    )
    blocks["OUT"] = LegoBlock(
        "OUT", "Saida", "saida",
        "Resultado final da cadeia.",
        inputs = [LegoInput("resultado", LegoPin.ANY)],
        outputs = [],
        logic = "Retorna o resultado final.",
        color = "red",
    )

    // === MATEMATICA ===
    blocks["MATH-ADD"] = LegoBlock(
        "MATH-ADD", "Somar", "matematica",
        "Soma dois numeros.",
        inputs = [LegoInput("a", LegoPin.NUMBER), LegoInput("b", LegoPin.NUMBER)],
        outputs = [LegoOutput("soma", LegoPin.NUMBER)],
        logic = "return a + b",
        code_rust = "fn add(a: f64, b: f64) -> f64 { a + b }",
        color = "blue",
    )
    blocks["MATH-MUL"] = LegoBlock(
        "MATH-MUL", "Multiplicar", "matematica",
        "Multiplica dois numeros.",
        inputs = [LegoInput("a", LegoPin.NUMBER), LegoInput("b", LegoPin.NUMBER)],
        outputs = [LegoOutput("produto", LegoPin.NUMBER)],
        logic = "return a * b",
        code_rust = "fn mul(a: f64, b: f64) -> f64 { a * b }",
        color = "blue",
    )
    blocks["MATH-SUB"] = LegoBlock(
        "MATH-SUB", "Subtrair", "matematica",
        "Subtrai b de a.",
        inputs = [LegoInput("a", LegoPin.NUMBER), LegoInput("b", LegoPin.NUMBER)],
        outputs = [LegoOutput("diferenca", LegoPin.NUMBER)],
        logic = "return a - b",
        color = "blue",
    )
    blocks["MATH-DIV"] = LegoBlock(
        "MATH-DIV", "Dividir", "matematica",
        "Divide a por b.",
        inputs = [LegoInput("a", LegoPin.NUMBER), LegoInput("b", LegoPin.NUMBER)],
        outputs = [LegoOutput("quociente", LegoPin.NUMBER)],
        logic = "return a / b if b != 0 else 0",
        color = "blue",
    )
    blocks["MATH-MAX"] = LegoBlock(
        "MATH-MAX", "Maximo", "matematica",
        "Retorna o maior de dois numeros.",
        inputs = [LegoInput("a", LegoPin.NUMBER), LegoInput("b", LegoPin.NUMBER)],
        outputs = [LegoOutput("maximo", LegoPin.NUMBER)],
        logic = "return max(a, b)",
        color = "blue",
    )
    blocks["MATH-MIN"] = LegoBlock(
        "MATH-MIN", "Minimo", "matematica",
        inputs = [LegoInput("a", LegoPin.NUMBER), LegoInput("b", LegoPin.NUMBER)],
        outputs = [LegoOutput("minimo", LegoPin.NUMBER)],
        logic = "return min(a, b)",
        color = "blue",
    )
    blocks["MATH-CLAMP"] = LegoBlock(
        "MATH-CLAMP", "Limitar (Clamp)", "matematica",
        "Limita valor entre min e max.",
        inputs = [LegoInput("valor", LegoPin.NUMBER),
                LegoInput("min", LegoPin.NUMBER),
                LegoInput("max", LegoPin.NUMBER)],
        outputs = [LegoOutput("limitado", LegoPin.NUMBER)],
        logic = "return max(min_val, min(max_val, valor))",
        color = "blue",
    )

    // === LOGICA ===
    blocks["LOGIC-IF"] = LegoBlock(
        "LOGIC-IF", "Se...Entao...Senao", "logica",
        "Condicional. Se condicao = verdadeiro, usa A. Senao, usa B.",
        inputs = [LegoInput("condicao", LegoPin.BOOLEAN),
                LegoInput("se_verdadeiro", LegoPin.ANY),
                LegoInput("se_falso", LegoPin.ANY)],
        outputs = [LegoOutput("resultado", LegoPin.ANY)],
        logic = "return a if cond else b",
        color = "yellow",
    )
    blocks["LOGIC-GT"] = LegoBlock(
        "LOGIC-GT", "Maior Que", "logica",
        inputs = [LegoInput("a", LegoPin.NUMBER), LegoInput("b", LegoPin.NUMBER)],
        outputs = [LegoOutput("resultado", LegoPin.BOOLEAN)],
        logic = "return a > b",
        color = "yellow",
    )
    blocks["LOGIC-LT"] = LegoBlock(
        "LOGIC-LT", "Menor Que", "logica",
        inputs = [LegoInput("a", LegoPin.NUMBER), LegoInput("b", LegoPin.NUMBER)],
        outputs = [LegoOutput("resultado", LegoPin.BOOLEAN)],
        logic = "return a < b",
        color = "yellow",
    )
    blocks["LOGIC-EQ"] = LegoBlock(
        "LOGIC-EQ", "Igual", "logica",
        inputs = [LegoInput("a", LegoPin.ANY), LegoInput("b", LegoPin.ANY)],
        outputs = [LegoOutput("resultado", LegoPin.BOOLEAN)],
        logic = "return a == b",
        color = "yellow",
    )
    blocks["LOGIC-AND"] = LegoBlock(
        "LOGIC-AND", "E (AND)", "logica",
        inputs = [LegoInput("a", LegoPin.BOOLEAN), LegoInput("b", LegoPin.BOOLEAN)],
        outputs = [LegoOutput("resultado", LegoPin.BOOLEAN)],
        logic = "return a and b",
        color = "yellow",
    )
    blocks["LOGIC-OR"] = LegoBlock(
        "LOGIC-OR", "Ou (OR)", "logica",
        inputs = [LegoInput("a", LegoPin.BOOLEAN), LegoInput("b", LegoPin.BOOLEAN)],
        outputs = [LegoOutput("resultado", LegoPin.BOOLEAN)],
        logic = "return a or b",
        color = "yellow",
    )

    // === TEXTO ===
    blocks["STR-CONCAT"] = LegoBlock(
        "STR-CONCAT", "Juntar Textos", "texto",
        inputs = [LegoInput("a", LegoPin.STRING), LegoInput("b", LegoPin.STRING)],
        outputs = [LegoOutput("resultado", LegoPin.STRING)],
        logic = "return a + b",
        color = "purple",
    )
    blocks["STR-UPPER"] = LegoBlock(
        "STR-UPPER", "MAIUSCULAS", "texto",
        inputs = [LegoInput("texto", LegoPin.STRING)],
        outputs = [LegoOutput("resultado", LegoPin.STRING)],
        logic = "return texto.upper()",
        color = "purple",
    )
    blocks["STR-LEN"] = LegoBlock(
        "STR-LEN", "Tamanho do Texto", "texto",
        inputs = [LegoInput("texto", LegoPin.STRING)],
        outputs = [LegoOutput("tamanho", LegoPin.NUMBER)],
        logic = "return len(texto)",
        color = "purple",
    )

    // === REPUBLICA (blocos especificos) ===
    blocks["REP-CREDIT"] = LegoBlock(
        "REP-CREDIT", "Calcular Credito de Trabalho", "republica",
        "Calcula credito baseado em horas e impacto (OpenLaborPolicy).",
        inputs = [LegoInput("horas", LegoPin.NUMBER),
                LegoInput("pessoas_afetadas", LegoPin.NUMBER)],
        outputs = [LegoOutput("credito", LegoPin.CREDIT)],
        logic = (
            "impacto = horas * (1 + log10(pessoas_afetadas) * ripple)"
            "credito = clamp(impacto / 100, min=5, max=100)"
        ),
        color = "orange",
        author = "OpenRepublic",
    )
    blocks["REP-VOTE"] = LegoBlock(
        "REP-VOTE", "Registrar Voto", "republica",
        "Registra voto na assembleia (OpenDemocracy).",
        inputs = [LegoInput("cidadao", LegoPin.PERSON),
                LegoInput("proposta", LegoPin.STRING),
                LegoInput("voto", LegoPin.BOOLEAN)],
        outputs = [LegoOutput("registro", LegoPin.VOTE)],
        logic = "assembleia.registrar(cidadao, proposta, voto)",
        color = "orange",
    )
    blocks["REP-DIAG"] = LegoBlock(
        "REP-DIAG", "Diagnostico OpenHealth", "republica",
        "IA diagnostica baseado em sintomas (OpenHealth).",
        inputs = [LegoInput("sintomas", LegoPin.STRING)],
        outputs = [LegoOutput("diagnostico", LegoPin.DIAGNOSIS)],
        logic = "openhealth.ai_diagnose(sintomas)",
        color = "orange",
    )
    blocks["REP-TASK"] = LegoBlock(
        "REP-TASK", "Criar Tarefa", "republica",
        "Cria tarefa no OpenLaborRelay.",
        inputs = [LegoInput("titulo", LegoPin.STRING),
                LegoInput("horas_estimadas", LegoPin.NUMBER)],
        outputs = [LegoOutput("tarefa", LegoPin.TASK)],
        logic = "laborrelay.create(titulo, horas)",
        color = "orange",
    )
    blocks["REP-FACTCHECK"] = LegoBlock(
        "REP-FACTCHECK", "Fact-Check (OpenSymbolRevision)", "republica",
        "Verifica frase preconceituosa e corrige.",
        inputs = [LegoInput("frase", LegoPin.STRING)],
        outputs = [LegoOutput("correcao", LegoPin.STRING),
                 LegoOutput("e_preconceito", LegoPin.BOOLEAN)],
        logic = "symbol_revision.fact_check(frase)",
        color = "orange",
    )

    // === IA ===
    blocks["IA-GENERATE"] = LegoBlock(
        "IA-GENERATE", "IA: Gerar Codigo", "ia",
        "IA gera codigo a partir de descricao em linguagem natural.",
        inputs = [LegoInput("descricao", LegoPin.STRING)],
        outputs = [LegoOutput("codigo", LegoPin.STRING)],
        logic = "ia.generate_code(descricao)",
        color = "cyan",
    )
    blocks["IA-TRANSLATE"] = LegoBlock(
        "IA-TRANSLATE", "IA: Traduzir", "ia",
        inputs = [LegoInput("texto", LegoPin.STRING),
                LegoInput("idioma", LegoPin.STRING)],
        outputs = [LegoOutput("traducao", LegoPin.STRING)],
        logic = "ia.translate(texto, idioma)",
        color = "cyan",
    )
    blocks["IA-SUMMARY"] = LegoBlock(
        "IA-SUMMARY", "IA: Resumir", "ia",
        inputs = [LegoInput("texto", LegoPin.STRING)],
        outputs = [LegoOutput("resumo", LegoPin.STRING)],
        logic = "ia.summarize(texto)",
        color = "cyan",
    )

    retorne blocks


// ============================================================================
// 5. MOTOR DE PROGRAMACAO LEGO
// ============================================================================

classe LegoCodeEngine:
    // Motor que gerencia programacao em formato LEGO.

    COMO FUNCIONA:
    1. Cidadao MONTA programa encaixando blocos
    2. Sistema VERIFICA se conexoes sao compativeis
    3. Sistema EXECUTA a cadeia (passa dados entre blocos)
    4. Sistema GERA codigo Rust otimizado (producao)
    5. Sistema VERSIONA cada bloco (troca sem quebrar)

    QUEM PODE PROGRAMAR:
    - TODO cidadao (sem saber programar)
    - IA gera blocos novos a partir de descricao
    - Blocos sao REUSAVEIS por toda Republica
    - Visual: arrastar e soltar (como Scratch/Blockly)

    VANTAGENS:
    - Sem erro de sintaxe (blocos so encaixam se compativeis)
    - Sem monolito (cada bloco e testavel isoladamente)
    - Sem dependencia oculta (conexoes sao explicitas)
    - Sem "works on my machine" (bloco e auto-contido)
    - IA pode GERAR, OTIMIZAR e TROCAR blocos
    // 

    funcao __init__(self):
        self.library: {texto: LegoBlock} = build_block_library()
        self.programs: {texto: LegoProgram} = {}

    funcao list_blocks(self, category: texto = None) -> [Dict]:
        blocks = self.library.values()
        se category entao:
            blocks = [b para b em blocks if b.category == category]
        retorne [
            {"id": b.block_id, "name": b.name, "category": b.category,
             "inputs": tamanho(b.inputs), "outputs": tamanho(b.outputs),
             "color": b.color, "uses": b.uses}
            para b em blocks
        ]

    funcao list_categories(self) -> {texto: inteiro}:
        retorne dict(Counter(b.category para b em self.library.values()))

    funcao create_program(self, name: texto,
                       seja description: texto = "",
                       seja created_by: texto = "") -> texto:
        // Cria programa vazio (cidadao vai montar).
        pid = hashlib.md5("{name}{datetime.now()}".encode()).hexdigest()[:8]
        prog = LegoProgram(
            program_id = pid, name=name, description=description,
            created_by = created_by,
            created_date = datetime.now().isoformat(),
        )
        self.programs[pid] = prog
        retorne pid

    funcao add_block(self, program_id: texto, block_id: texto,
                  seja instance_name: texto = "") -> {texto: qualquer}:
        // Adiciona bloco ao programa.
        prog = self.programs.get(program_id)
        se nao prog entao:
            retorne {"error": "Programa nao encontrado"}
        block = self.library.get(block_id)
        se nao block entao:
            retorne {"error": "Bloco nao encontrado na biblioteca"}

        inst_id = instance_name  ou  "{block_id}-{len(prog.blocks)}"
        prog.blocks[inst_id] = block
        block.uses += 1

        retorne {
            "added": verdadeiro,
            "instance": inst_id,
            "block": block.name,
            "inputs": [{"name": i.name, "type": i.pin_type.value,
                        "required": i.required} para i em block.inputs],
            "outputs": [{"name": o.name, "type": o.pin_type.value}
                        para o em block.outputs],
        }

    funcao connect(self, program_id: texto,
                from_instance: texto, from_output: inteiro,
                to_instance: texto, to_input: inteiro) -> {texto: qualquer}:
        // Conecta saida de um bloco na entrada de outro (LEGO snap).
        prog = self.programs.get(program_id)
        se nao prog entao:
            retorne {"error": "Programa nao encontrado"}

        from_block = prog.blocks.get(from_instance)
        to_block = prog.blocks.get(to_instance)
        se nao from_block ou nao to_block entao:
            retorne {"error": "Bloco nao encontrado no programa"}

        // Verificar compatibilidade de pinos
        compatible = from_block.can_connect(to_block, from_output, to_input)
        se nao compatible entao:
            out_type = from_block.outputs[from_output].pin_type.value
            in_type = to_block.inputs[to_input].pin_type.value
            retorne {
                "error": "Pinos incompativeis",
                "from_output_type": out_type,
                "to_input_type": in_type,
                "message": "Saida {out_type} nao encaixa em entrada {in_type}. "
                           "LEGO: so encaixa se o tipo for igual (ou ANY).",
            }

        conn = LegoConnection(
            from_block = from_instance, from_output=from_output,
            to_block = to_instance, to_input=to_input,
            valid = verdadeiro,
        )
        prog.connections.append(conn)

        retorne {
            "connected": verdadeiro,
            "from": "{from_instance}.{from_block.outputs[from_output].name}",
            "to": "{to_instance}.{to_block.inputs[to_input].name}",
            "type": from_block.outputs[from_output].pin_type.value,
            "message": "Blocos encaixados. Pinos compativeis.",
        }

    funcao validate_program(self, program_id: texto) -> {texto: qualquer}:
        // Valida programa completo.
        prog = self.programs.get(program_id)
        se nao prog entao:
            retorne {"error": "nao encontrado"}

        issues = []
        se nao prog.is_valid entao:
            issues.append("Conexoes invalidas")
        se nao prog.all_inputs_connected entao:
            issues.append("Entradas obrigatorias desconectadas")

        // Verificar ciclos
        se self._has_cycle(prog) entao:
            issues.append("Ciclo detectado (loop infinito)")

        retorne {
            "program": prog.name,
            "blocks": prog.block_count,
            "connections": prog.connection_count,
            "valid": tamanho(issues) == 0,
            "issues": issues,
            "ready": tamanho(issues) == 0,
        }

    funcao _has_cycle(self, prog: LegoProgram) -> logico:
        // Detecta ciclo no grafo de blocos.
        graph = defaultdict(list)
        para cada conn em prog.connections:
            graph[conn.from_block].append(conn.to_block)

        visited = set()
        stack = set()

        funcao visit(node):
            se node in stack entao:
                retorne verdadeiro
            se node in visited entao:
                retorne falso
            visited.add(node)
            stack.add(node)
            para cada neighbor em graph[node]:
                se visit(neighbor) entao:
                    retorne verdadeiro
            stack.discard(node)
            retorne falso

        retorne any(visit(n) para n em list(prog.blocks.keys()))

    funcao execute(self, program_id: texto,
                seja initial_values: {texto: qualquer} = nulo) -> {texto: qualquer}:
        // Executa programa LEGO (simula passagem de dados).
        prog = self.programs.get(program_id)
        se nao prog entao:
            retorne {"error": "nao encontrado"}

        validation = self.validate_program(program_id)
        se nao  validation["valid"] entao:
            retorne {"error": "Programa invalido", "issues": validation["issues"]}

        // Topological sort
        order = self._topo_sort(prog)

        // Executar cada bloco em ordem
        results = {}
        values = initial_values ou {}

        para cada inst_id em order:
            block = prog.blocks[inst_id]
            block_results = self._execute_block(block, inst_id, prog, values)
            results[inst_id] = block_results
            values.update(block_results)

        retorne {
            "program": prog.name,
            "executed": verdadeiro,
            "blocks_executed": tamanho(order),
            "results": results,
            "final_output": results.get(
                next((c.to_block para c em prog.connections
                      if c.to_block.startswith("OUT")), "OUT-0"), {}),
        }

    funcao _execute_block(self, block: LegoBlock, inst_id: texto,
                       prog: LegoProgram,
                       all_values: Dict) -> {texto: qualquer}:
        // Executa um bloco e retorna seus outputs.
        // Para demo: simular execucao baseada na logica
        retorne {
            block.outputs ? "{inst_id}.{block.outputs[0].name}" : inst_id:
                "[{block.name} executado]"
        }

    funcao _topo_sort(self, prog: LegoProgram) -> [texto]:
        // Ordenacao topologica dos blocos.
        graph = defaultdict(list)
        in_degree = defaultdict(inteiro)

        para cada inst_id em prog.blocks:
            in_degree[inst_id] = 0

        para cada conn em prog.connections:
            graph[conn.from_block].append(conn.to_block)
            in_degree[conn.to_block] += 1

        queue = [n para n em prog.blocks if in_degree[n] == 0]
        order = []

        enquanto queue faca:
            node = queue.pop(0)
            order.append(node)
            para cada neighbor em graph[node]:
                in_degree[neighbor] -= 1
                se in_degree[neighbor] == 0 entao:
                    queue.append(neighbor)

        retorne order

    funcao generate_rust(self, program_id: texto) -> {texto: qualquer}:
        // Gera codigo Rust a partir do programa LEGO.
        prog = self.programs.get(program_id)
        se nao prog entao:
            retorne {"error": "nao encontrado"}

        order = self._topo_sort(prog)

        lines = ["// Codigo gerado automaticamente por OpenLegoCode"]
        lines.append("// Programa: {prog.name}")
        lines.append("// Blocos: {prog.block_count}")
        lines.append("")
        lines.append("fn main() {")
        para cada inst_id em order:
            block = prog.blocks[inst_id]
            se block.code_rust entao:
                lines.append("    // {inst_id}: {block.name}")
                lines.append("    // {block.code_rust}")
            senao:
                lines.append("    // {inst_id}: {block.name} ({block.logic})")
        lines.append("}")

        retorne {
            "program": prog.name,
            "language": "Rust",
            "lines": tamanho(lines),
            "code": "\n".join(lines),
            "blocks_converted": tamanho(order),
        }

    funcao ai_generate_block(self, description: texto) -> {texto: qualquer}:
        // IA gera bloco novo a partir de descricao em linguagem natural.
        block_id = "AI-{hashlib.md5(description[:20].encode()).hexdigest()[:6]}"

        // IA decide tipo de pino baseado na descricao
        desc_lower = description.lower()
        se any(w in desc_lower para w em ["numero", "calcular", "somar", "media"]) entao:
            pin_out = LegoPin.NUMBER
        senao se any(w in desc_lower para w em ["texto", "frase", "string"]) entao:
            pin_out = LegoPin.STRING
        senao se any(w in desc_lower para w em ["sim/nao", "verdadeiro", "condicao"]) entao:
            pin_out = LegoPin.BOOLEAN
        senao se any(w in desc_lower para w em ["credito", "pagar"]) entao:
            pin_out = LegoPin.CREDIT
        senao se any(w in desc_lower para w em ["pessoa", "cidadao", "paciente"]) entao:
            pin_out = LegoPin.PERSON
        senao:
            pin_out = LegoPin.ANY

        new_block = LegoBlock(
            block_id = block_id,
            name = "IA: {description[:30]}",
            category = "ia_gerado",
            description = "Bloco gerado por IA. Descricao: {description}",
            inputs = [LegoInput("entrada", LegoPin.ANY)],
            outputs = [LegoOutput("resultado", pin_out)],
            logic = description,
            author = "IA-OpenLegoCode",
            tested = falso,
            color = "cyan",
        )
        self.library[block_id] = new_block

        retorne {
            "generated": verdadeiro,
            "block_id": block_id,
            "name": new_block.name,
            "output_type": pin_out.value,
            "logic": description,
            "message": (
                "IA gerou bloco '{block_id}' a partir de: '{description}'. "
                "Pode ser usado em qualquer programa LEGO. "
                "Reusavel por toda Republica."
            ),
        }

    funcao stats(self) -> {texto: qualquer}:
        retorne {
            "total_blocos_biblioteca": tamanho(self.library),
            "total_programas": tamanho(self.programs),
            "categorias": self.list_categories(),
            "blocos_ia": soma(1 para b em self.library.values()
                             if b.category == "ia_gerado"),
            "total_usos": soma(b.uses para b em self.library.values()),
        }


// importa Counter de collections


// ============================================================================
// 6. MAIN
// ============================================================================

se __name__ == "__main__" entao:
    engine = LegoCodeEngine()

    imprima("=" * 80)
    imprima("  OPENLEGOCODE -- PROGRAMACAO MODULAR EM FORMATO LEGO")
    imprima("  Escrever codigo e coisa do passado. Programa-se ENCAIXANDO.")
    imprima("=" * 80)

    // === 1. BIBLIOTECA DE BLOCOS ===
    imprima("\n\n  === 1. BIBLIOTECA DE BLOCOS ({len(engine.library)}) ===\n")
    cats = engine.list_categories()
    para cada (cat, count) em ordene(cats.items(), key=(x) -> -x[1]):
        blocks_in_cat = [b para b em engine.library.values() if b.category == cat]
        imprima("\n  {cat.upper()} ({count} blocos):")
        para cada b em blocks_in_cat:
            in_types = ", ".join("{i.name}:{i.pin_type.value}" para i em b.inputs)
            out_types = ", ".join("{o.name}:{o.pin_type.value}" para o em b.outputs)
            imprima("    [{b.block_id}] {b.name}")
            imprima("      Entradas: ({in_types or 'nenhuma'})")
            imprima("      Saidas: ({out_types or 'nenhuma'})")

    // === 2. MONTAR PROGRAMA: CALCULAR CREDITO ===
    imprima("\n\n  === 2. MONTANDO PROGRAMA: 'Calcular Credito de Trabalho' ===\n")
    pid = engine.create_program("Calcular Credito", "Calcula credito de trabalho")

    // Adicionar blocos
    engine.add_block(pid, "IN-NUM", "horas_input")
    engine.add_block(pid, "IN-NUM", "pessoas_input")
    engine.add_block(pid, "REP-CREDIT", "calc_credito")
    engine.add_block(pid, "OUT", "resultado")

    imprima("  Blocos adicionados: {engine.programs[pid].block_count}")

    // Conectar blocos (LEGO snap)
    imprima("\n  Conectando blocos:")
    connections = [
        ("horas_input", 0, "calc_credito", 0),       // horas -> credito.horas
        ("pessoas_input", 0, "calc_credito", 1),      // pessoas -> credito.pessoas
        ("calc_credito", 0, "resultado", 0),           // credito -> saida
    ]
    para from_inst, from_out, to_inst, to_in in connections:
        r = engine.connect(pid, from_inst, from_out, to_inst, to_in)
        status = r.get("connected") ? "OK" : "FALHOU"
        imprima("  [{status}] {r.get('from', '?')} -> {r.get('to', '?')}")

    // Validar
    imprima("\n  Validacao:")
    val = engine.validate_program(pid)
    imprima("  Valido: {'SIM' if val['valid'] else 'NAO'}")
    imprima("  Blocos: {val['blocks']}, Conexoes: {val['connections']}")
    se val["issues"] entao:
        imprima("  Issues: {val['issues']}")

    // === 3. MONTAR PROGRAMA: FACT-CHECK DE PRECONCEITO ===
    imprima("\n\n  === 3. MONTANDO: 'Fact-Check de Preconceito' ===\n")
    pid2 = engine.create_program("Fact-Check Preconceito",
                                 "Verifica frase e corrige")

    engine.add_block(pid2, "IN-STR", "frase_input")
    engine.add_block(pid2, "REP-FACTCHECK", "verificar")
    engine.add_block(pid2, "OUT", "correcao_output")

    engine.connect(pid2, "frase_input", 0, "verificar", 0)
    engine.connect(pid2, "verificar", 0, "correcao_output", 0)

    val2 = engine.validate_program(pid2)
    imprima("  Valido: {'SIM' if val2['valid'] else 'NAO'}")
    imprima("  Blocos: {val2['blocks']}, Conexoes: {val2['connections']}")

    // === 4. IA GERA BLOCO NOVO ===
    imprima("\n\n  === 4. IA GERA BLOCO NOVO ===\n")
    ai_blocks = [
        "Calcular imposto de renda progressivo",
        "Verificar se paciente precisa de vacina",
        "Traduzir musica para outro idioma mantendo ritmo",
        "Calcular rota otima de carona solidaria",
    ]
    para cada desc em ai_blocks:
        r = engine.ai_generate_block(desc)
        imprima("  [{r['block_id']}] {r['name']}")
        imprima("    Logica: {r['logic'][:60]}...")
        imprima("    Saida: {r['output_type']}")

    // === 5. PINOS INCOMPATIVEIS (erro LEGO) ===
    imprima("\n\n  === 5. ERRO: PINOS INCOMPATIVEIS (LEGO nao encaixa) ===\n")
    pid3 = engine.create_program("Teste Erro", "Testa pino incompativel")
    engine.add_block(pid3, "IN-STR", "texto_in")
    engine.add_block(pid3, "MATH-ADD", "soma")
    // Tentar conectar STRING em NUMBER -> ERRO
    r = engine.connect(pid3, "texto_in", 0, "soma", 0)
    imprima("  Tentativa: texto -> soma")
    imprima("  Resultado: {r.get('error', 'conectado')}")
    imprima("  Mensagem: {r.get('message', '')}")
    imprima("\n  LEGO: pino texto NAO encaixa em buraco numero.")
    imprima("  Sistema IMPEDE erro de tipo antes de executar.")

    // === 6. GERAR CODIGO RUST ===
    imprima("\n\n  === 6. GERAR CODIGO RUST DO PROGRAMA ===\n")
    rust = engine.generate_rust(pid)
    imprima("  Programa: {rust['program']}")
    imprima("  Linguagem: {rust['language']}")
    imprima("  Linhas: {rust['lines']}")
    para cada line em rust["code"].split("\n")[:10]:
        imprima("  {line}")

    // === 7. STATS ===
    imprima("\n\n  === 7. ESTATISTICAS ===\n")
    s = engine.stats()
    para cada (k, v) em s.items():
        se isinstance(v, dict) entao:
            imprima("  {k}:")
            para cada (sk, sv) em v.items():
                imprima("    {sk:<20} {sv}")
        senao:
            imprima("  {k:<30} {v}")

    // === FILOSOFIA ===
    imprima("\n\n{'='*80}")
    imprima("  FILOSOFIA: PROGRAMACAO EM LEGO")
    imprima("{'='*80}")
    imprima("""
  ESCREVER CODIGO e COISA DO PASSADO:
    Antes: escrever 500 linhas de codigo.
    Um erro de sintaxe e tudo para.
    Uma mudanca quebra tudo.
    So programador entende.

    Agora: ENCAIXAR BLOCOS LEGO.
    Cada bloco faz UMA coisa.
    Blocos so encaixam se compativeis (sem erro de tipo).
    Uma mudanca troca UM bloco (resto funciona).
    TODO cidadao pode programar (visual, nao textual).

  COMO FUNCIONA:
    1. Cidadao ABRE o OpenLegoCode Studio (visual)
    2. ARRASTA blocos da biblioteca
    3. ENCAIXA saida de um na entrada de outro
    4. Sistema VERIFICA compatibilidade (pino = tipo)
    5. SISTEMA VALIDA (todas entradas conectadas, sem ciclo)
    6. EXECUTA (passa dados entre blocos)
    7. GERA Rust (para producao)

  BIBLIOTECA DE BLOCOS (reusavel):
    ENTRADA: numero, texto
    MATEMATICA: somar, multiplicar, subtrair, dividir, clamp, maximo, minimo
    LOGICA: if/else, maior que, igual, AND, OR
    TEXTO: concatenar, maiusculas, tamanho
    REPUBLICA: credito, voto, diagnostico, tarefa, fact-check
    IA: gerar codigo, traduzir, resumir
    IA_GERADO: blocos que a IA cria sob demanda

  PINOS TIPIZADOS (LEGO so encaixa se compativel):
    numero -> so encaixa em numero (ou ANY)
    texto -> so encaixa em texto (ou ANY)
    sim_nao -> so encaixa em sim_nao (ou ANY)
    pessoa -> so encaixa em pessoa (ou ANY)
    credito -> so encaixa em credito (ou ANY)
    ANY -> encaixa em tudo

  IA GERA BLOCOS:
    "Calcula imposto progressivo" -> IA cria bloco
    "Verifica se paciente precisa vacina" -> IA cria bloco
    Bloco criado entra na biblioteca. Todos podem usar.
    Bloco e REUSAVEL por toda Republica.

  VANTAGENS:
    - Sem erro de sintaxe (bloco so encaixa se compativel)
    - Sem monolito (cada bloco testavel isoladamente)
    - Sem dependencia oculta (conexoes explicitas)
    - IA pode gerar, otimizar e trocar blocos
    - Cidadao programa sem saber programar
    - Tudo visual, modular, reusavel

  OPENLEGOCODE STUDIO:
    Interface visual (arrastar e soltar).
    Funciona no OpenTerminal, OpenTVStick, smartphone.
    OpenLite renderiza a interface.
    FabLab nao precisa -- e software puro.

  PRINCIPIOS:
    P1: Todo cidadao pode programar. Sem elitismo de codigo.
    P2: Bloco e autonomo. Declara o que faz (entradas/saidas).
    seja P3: Criar bloco reusavel = trabalho de alto impacto.
    P4: Biblioteca e bem comum (CC0). Todos usam. Todos contribuem.
// )
    imprima("{'='*80}")
    imprima("  OpenLegoCode: {s['total_blocos_biblioteca']} blocos na biblioteca, "
          "{s['total_programas']} programas montados.")
    imprima("  Escrever codigo e coisa do passado. Encaixa pecas.")
    imprima("{'='*80}")

```
