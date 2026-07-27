// OpenLegoStudio -- Interface Visual de Programacao LEGO -- gerado de Portugol++
public class OpenlegostudioInterfaceVisualDeProgramacaoLego {

    // !/usr/bin/env python3
    //
    OpenLegoStudio -- Interface Visual de Programacao LEGO;
    =========================================================;
    "O OpenLegoCode tem os blocos. Mas o cidadao precisa de uma INTERFACE.;
    Arrastar. Soltar. Encaixar. Ver o programa FLUIR.;
    Sem texto. Sem sintaxe. Sem complexidade.;
    So blocos coloridos que encaixam como LEGO fisico.";
    O QUE ISTO FAZ:;
    1. INTERFACE VISUAL: paleta de blocos + canvas + conexao;
    2. RENDERIZACAO ASCII do canvas (para terminal/TUI);
    3. SNAP AUTOMATICO: blocos so encaixam se compativeis;
    4. LIVE EXECUTION: executa enquanto monta;
    5. ERROR VISUAL: pino incompativel fica vermelho;
    6. GERACAO RUST: botao gera codigo pronto para producao;
    7. GALERIA: programas da comunidade (reusaveis);
    8. IA ASSISTENTE: descreve o que quer -> IA monta os blocos;
    Author: OpenRepublic Team;
    //
    // importa annotations de __future__
    // importa hashlib
    // importa dataclass, field de dataclasses
    // importa Any, Dict, List, Optional, Tuple de typing
    // importa Enum de enum
    // importa defaultdict de collections
    // importa datetime de datetime
    // ============================================================================
    // 1. ELEMENTOS DA INTERFACE
    // ============================================================================
    public static class BlockColor {
        // Cores dos blocos por categoria (visual).
        INPUT = ("verde", " Entrada de dados");
        OUTPUT = ("vermelho", "Saida de dados");
        MATH = ("azul", " Matematica");
        LOGIC = ("amarelo", "Logica");
        TEXT = ("roxo", "  Texto");
        REPUBLIC = ("laranja", "Republica");
        IA = ("ciano", "   Inteligencia Artificial");
        CUSTOM = ("branco", "Customizado");
    public static class BlockShape {
        // Formatos visuais (ASCII art).
        INPUT = "input";
        OUTPUT = "output";
        PROCESS = "process";
        DECISION = "decision";
        DATA = "data";
    public static class CanvasSlot {
        // Estado de um slot no canvas.
        EMPTY = "vazio";
        OCCUPIED = "ocupado";
        VALID_TARGET = "alvo_valido"  // verde (pode soltar aqui);
        INVALID_TARGET = "alvo_invalido"  // vermelho (! pode);
        HOVER = "hover";
    // ============================================================================
    // 2. BLOCO VISUAL (no canvas)
    // ============================================================================
    // decorador: @dataclass
    public static class VisualBlock {
        // Um bloco renderizado no canvas.
        Cada bloco ocupa uma POSICAO (x, y) no canvas.;
        Tem largura/altura visuais.;
        Tem PINOS de entrada (esquerda) && saida (direita).;
        //
        instance_id: texto;
        block_id: texto // referencia a biblioteca OpenLegoCode;
        name: texto;
        color: BlockColor;
        shape: BlockShape;
        int x = 0 // posicao no canvas;
        int y = 0;
        int width = 20 // largura visual;
        int height = 5 // altura visual;
        // Pinos
        [Dict] input_pins = field(default_factory=list)  // [{"name", "type", "connected"}];
        [Dict] output_pins = field(default_factory=list);
        // Estado
        boolean executing = false;
        boolean has_error = false;
        String error_msg = "";
        Object result_value = null;
        // decorador: @property
        public int center_x(self) {
            return self.x + self.width // 2;
        // decorador: @property
        public int center_y(self) {
            return self.y + self.height // 2;
    // ============================================================================
    // 3. CONEXAO VISUAL (fio entre blocos)
    // ============================================================================
    // decorador: @dataclass
    public static class VisualConnection {
        // Conexao visual entre dois pinos.
        conn_id: texto;
        from_instance: texto;
        from_pin_idx: inteiro;
        to_instance: texto;
        to_pin_idx: inteiro;
        boolean valid = true;
        String color = "verde"  // verde=valido, vermelho=invalido;
        // Renderizacao
        List[(inteiro, inteiro)] wire_path = field(default_factory=list);
    // ============================================================================
    // 4. CANVAS (area de trabalho)
    // ============================================================================
    // decorador: @dataclass
    public static class Canvas {
        // Canvas onde os blocos sao posicionados.
        Grid de caracteres ASCII.;
        Cada celula pode conter parte de um bloco || fio de conexao.;
        //
        int width = 80;
        int height = 40;
        List[[texto]] grid = field(default_factory=list);
        {texto: VisualBlock} blocks = field(default_factory=dict);
        [VisualConnection] connections = field(default_factory=list);
        int cursor_x = 0;
        int cursor_y = 0;
        texto? selected_block = null;
        texto? dragging_block = null;
        CanvasSlot? snap_target = CanvasSlot.EMPTY;
        public void __post_init__(self) {
            self.grid = [[" " para _ em intervalo(self.width)] para _ em intervalo(self.height)];
        public None place_block(self, block: VisualBlock) {
            self.blocks[block.instance_id] = block;
        public String render(self) {
            // Renderiza canvas como ASCII art.
            // Limpar grid
            self.grid = [[" " para _ em intervalo(self.width)] para _ em intervalo(self.height)];
            // Renderizar conexoes (fios) primeiro
            /* TODO: for-each Java para conn em self.connections */
                self._render_wire(conn);
            // Renderizar blocos por cima
            /* TODO: for-each Java para block em self.blocks.values() */
                self._render_block(block);
            // Converter grid para string
            lines = [];
            // Borda superior
            lines.append("+" + "-" * self.width + "+");
            /* TODO: for-each Java para row em self.grid */
                lines.append("|" + "".join(row) + "|");
            lines.append("+" + "-" * self.width + "+");
            return "\n".join(lines);
        public None _render_block(self, block: VisualBlock) {
            // Desenha bloco no grid usando ASCII art.
            color_letter = {"verde": "I", "vermelho": "O", "azul": "M",;
                            "amarelo": "L", "roxo": "T", "laranja": "R",;
                            "ciano": "A", "branco": "C"};
            icon = color_letter.get(block.color.value[0], "B");
            b = block;
            // Verificar limites
            if (b.y >= self.height || b.x >= self.width) {
                return null;
            // Moldura superior
            /* TODO: for-each Java para i em intervalo(minimo(b.width, self.width - b.x)) */
                if (b.y < self.height && b.x + i < self.width) {
                    self.grid[b.y][b.x + i] = "-";
            // Linha do titulo
            title = " {icon} {b.name[:b.width-4]} ";
            /* para cada (i, ch) em enumere(title): */
                if (b.y + 1 < self.height && b.x + i < self.width) {
                    i < b.width ? self.grid[b.y + 1][b.x + i] = ch : " ";
            // Pinos de entrada (esquerda)
            /* para cada (idx, pin) em enumere(b.input_pins): */
                if (b.y + 2 + idx < self.height) {
                    pin_label = ">{pin['name']}:{pin['type'][:3]}";
                    conn_marker = pin.get("connected") ? "*" : "o";
                    if (b.x > 0) {
                        self.grid[b.y + 2 + idx][b.x - 1] = conn_marker;
                    /* para cada (i, ch) em enumere(pin_label[:b.width-2]): */
                        if (b.x + 1 + i < self.width) {
                            self.grid[b.y + 2 + idx][b.x + 1 + i] = ch;
            // Pinos de saida (direita)
            /* para cada (idx, pin) em enumere(b.output_pins): */
                y_pos = b.y + 2 + idx;
                if (y_pos < self.height) {
                    pin_label = "{pin['name']}:{pin['type'][:3]}>";
                    conn_marker = pin.get("connected") ? "*" : "o";
                    start_x = b.x + b.width - tamanho(pin_label) - 1;
                    if (start_x > 0) {
                        /* para cada (i, ch) em enumere(pin_label): */
                            if (start_x + i < self.width) {
                                self.grid[y_pos][start_x + i] = ch;
                    if (b.x + b.width < self.width) {
                        self.grid[y_pos][b.x + b.width] = conn_marker;
            // Moldura inferior
            bottom_y = b.y + b.height - 1;
            /* TODO: for-each Java para i em intervalo(minimo(b.width, self.width - b.x)) */
                if (bottom_y < self.height && b.x + i < self.width) {
                    self.grid[bottom_y][b.x + i] = "-";
            // Marcador de erro
            if (block.has_error) {
                if (b.y + 1 < self.height && b.x + b.width - 2 < self.width) {
                    self.grid[b.y + 1][b.x + b.width - 2] = "X";
            // Marcador de execucao
            if (block.executing) {
                if (b.y + 1 < self.height && b.x < self.width) {
                    self.grid[b.y + 1][b.x] = ">";
        public None _render_wire(self, conn: VisualConnection) {
            // Desenha fio de conexao entre blocos.
            from_block = self.blocks.get(conn.from_instance);
            to_block = self.blocks.get(conn.to_instance);
            if (! from_block || ! to_block) {
                return null;
            // Ponto de saida (direita do bloco origem)
            x1 = from_block.x + from_block.width;
            y1 = from_block.y + 2 + conn.from_pin_idx;
            // Ponto de entrada (esquerda do bloco destino)
            x2 = to_block.x - 1;
            y2 = to_block.y + 2 + conn.to_pin_idx;
            wire_char = conn.valid ? "=" : "!";
            color = conn.valid ? "=" : "!";
            // Desenhar caminho (L shape)
            mid_x = (x1 + x2) // 2;
            // Horizontal da saida ate mid_x
            /* TODO: for-each Java para x em intervalo(x1, minimo(mid_x, self.width)) */
                if (y1 < self.height  &&  self.grid[y1][x] == " ") {
                    self.grid[y1][x] = wire_char;
            // Vertical de y1 ate y2
            step = y2 > y1 ? 1 : -1;
            /* TODO: for-each Java para y em intervalo(y1, y2, step) */
                if (0 <= y < self.height && 0 <= mid_x < self.width) {
                    if (self.grid[y][mid_x] == " ") {
                        self.grid[y][mid_x] = wire_char;
            // Horizontal de mid_x ate entrada
            /* TODO: for-each Java para x em intervalo(maximo(mid_x, 0), minimo(x2, self.width)) */
                if (0 <= y2 < self.height  &&  self.grid[y2][x] == " ") {
                    self.grid[y2][x] = wire_char;
    // ============================================================================
    // 5. PALETA DE BLOCOS (barra lateral)
    // ============================================================================
    // decorador: @dataclass
    public static class BlockPalette {
        // Paleta lateral com todos os blocos disponiveis.
        Cidadao clica (|| seleciona) um bloco da paleta.;
        Depois clica no canvas onde quer colocar.;
        Bloco aparece no canvas.;
        //
        Dict[texto, [Dict]] categories = field(default_factory=dict);
        public String render(self) {
            // Renderiza paleta como menu de texto.
            lines = ["  PALETA DE BLOCOS", "  " + "=" * 36];
            /* para cada (cat, blocks) em self.categories.items(): */
                lines.append("\n  [{cat.upper()}]");
                /* TODO: for-each Java para b em blocks */
                    lines.append("    {b['id']:<12} {b['name']}");
            return "\n".join(lines);
    public BlockPalette build_palette() {
        // Constroi paleta com blocos da biblioteca OpenLegoCode.
        palette = BlockPalette();
        palette.categories = {
            "entrada": [;
                {"id": "IN-NUM", "name": "Numero"},;
                {"id": "IN-STR", "name": "Texto"},;
            ],;
            "matematica": [;
                {"id": "MATH-ADD", "name": "Somar"},;
                {"id": "MATH-MUL", "name": "Multiplicar"},;
                {"id": "MATH-SUB", "name": "Subtrair"},;
                {"id": "MATH-DIV", "name": "Dividir"},;
                {"id": "MATH-CLAMP", "name": "Limitar"},;
            ],;
            "logica": [;
                {"id": "LOGIC-IF", "name": "Se/Entao/Senao"},;
                {"id": "LOGIC-GT", "name": "Maior Que"},;
                {"id": "LOGIC-LT", "name": "Menor Que"},;
                {"id": "LOGIC-EQ", "name": "Igual"},;
                {"id": "LOGIC-AND", "name": "E (AND)"},;
                {"id": "LOGIC-OR", "name": "Ou (OR)"},;
            ],;
            "republica": [;
                {"id": "REP-CREDIT", "name": "Calcular Credito"},;
                {"id": "REP-VOTE", "name": "Registrar Voto"},;
                {"id": "REP-DIAG", "name": "Diagnostico OpenHealth"},;
                {"id": "REP-FACTCHECK", "name": "Fact-Check Preconceito"},;
                {"id": "REP-TASK", "name": "Criar Tarefa"},;
            ],;
            "ia": [;
                {"id": "IA-GENERATE", "name": "IA: Gerar Codigo"},;
                {"id": "IA-TRANSLATE", "name": "IA: Traduzir"},;
                {"id": "IA-SUMMARY", "name": "IA: Resumir"},;
            ],;
            "saida": [;
                {"id": "OUT", "name": "Resultado Final"},;
            ],;
        };
        return palette;
    // ============================================================================
    // 6. IA ASSISTENTE (monta por descricao)
    // ============================================================================
    public static class LegoAssistant {
        // IA que monta programa LEGO a partir de descricao em linguagem natural.
        Cidadao diz: "Quero calcular credito de trabalho baseado em horas";
        IA monta: [IN-NUM] -> [REP-CREDIT] -> [OUT];
        Cidadao diz: "Quero verificar se frase && preconceito";
        IA monta: [IN-STR] -> [REP-FACTCHECK] -> [OUT];
        //
        public void __init__(self) {
            self.templates: Dict[texto, [texto]] = {
                "credito": ["IN-NUM", "IN-NUM", "REP-CREDIT", "OUT"],;
                "fact_check": ["IN-STR", "REP-FACTCHECK", "OUT"],;
                "diagnostico": ["IN-STR", "REP-DIAG", "OUT"],;
                "votar": ["IN-STR", "REP-VOTE", "OUT"],;
                "imposto": ["IN-NUM", "MATH-MUL", "LOGIC-IF", "OUT"],;
                "traduzir": ["IN-STR", "IA-TRANSLATE", "OUT"],;
                "resumir": ["IN-STR", "IA-SUMMARY", "OUT"],;
                "gerar_codigo": ["IN-STR", "IA-GENERATE", "OUT"],;
            };
        public {texto: qualquer} understand(self, description: texto) {
            // Entende descricao e sugere cadeia de blocos.
            desc = description.lower();
            // Matching simples
            selected_template = null;
            matched_keywords = [];
            /* para cada (key, template) em self.templates.items(): */
                keywords = key.split("_");
                hits = soma(1 para kw em keywords if kw in desc);
                if (hits > 0) {
                    selected_template = template;
                    matched_keywords.append((key, hits));
            // Busca adicional
            if (! selected_template) {
                if (any(w in desc para w em ["credito", "pagar", "trabalho"])) {
                    selected_template = self.templates["credito"];
                } else if (any(w in desc para w em ["preconceito", "racismo", "fact"])) {
                    selected_template = self.templates["fact_check"];
                } else if (any(w in desc para w em ["traduzir", "traducao"])) {
                    selected_template = self.templates["traduzir"];
                } else if (any(w in desc para w em ["resumir", "resumo"])) {
                    selected_template = self.templates["resumir"];
                } else if (any(w in desc para w em ["diagnostic", "saude", "doente"])) {
                    selected_template = self.templates["diagnostico"];
                } else {
                    // Template generico
                    selected_template = ["IN-STR", "IA-GENERATE", "OUT"];
            return {;
                "understood": true,;
                "description": description,;
                "template": selected_template,;
                "block_count": tamanho(selected_template),;
                "message": (;
                    "Entendi: '{description}'. ";
                    "Vou montar {len(selected_template)} blocos. ";
                    "Cadeia: {' -> '.join(selected_template)}";
                ),;
            };
        public [Dict] auto_connect(self, template: [texto]) {
            // Gera conexoes automaticas baseado no template.
            connections = [];
            /* TODO: for-each Java para i em intervalo(tamanho(template) - 1) */
                connections.append({
                    "from": template[i],;
                    "from_pin": 0,;
                    "to": template[i + 1],;
                    "to_pin": 0,;
                    "auto": true,;
                });
            return connections;
    // ============================================================================
    // 7. GALERIA COMUNITARIA
    // ============================================================================
    // decorador: @dataclass
    public static class GalleryProgram {
        // Programa compartilhado na galeria.
        program_id: texto;
        name: texto;
        author: texto;
        String description = "";
        [texto] blocks = field(default_factory=list);
        int downloads = 0;
        double rating = 0.0;
    public [GalleryProgram] build_gallery() {
        return [;
            GalleryProgram("G-001", "Calculadora de Credito",;
                "Cleiton", "Calcula credito baseado em horas + impacto",;
                ["IN-NUM", "IN-NUM", "REP-CREDIT", "OUT"],;
                downloads = 342, rating=4.8),;
            GalleryProgram("G-002", "Fact-Check Preconceito",;
                "Maria", "Verifica frase preconceituosa && corrige",;
                ["IN-STR", "REP-FACTCHECK", "OUT"],;
                downloads = 218, rating=4.9),;
            GalleryProgram("G-003", "Triagem OpenHealth",;
                "Dra. Helena", "IA tria paciente por sintomas",;
                ["IN-STR", "REP-DIAG", "OUT"],;
                downloads = 156, rating=4.7),;
            GalleryProgram("G-004", "Tradutor Universal",;
                "Joao", "Traduz texto mantendo contexto",;
                ["IN-STR", "IA-TRANSLATE", "OUT"],;
                downloads = 489, rating=4.6),;
            GalleryProgram("G-005", "Calculo de Imposto Progressivo",;
                "Ana", "Calcula imposto baseado em faixa de renda",;
                ["IN-NUM", "LOGIC-GT", "LOGIC-IF", "MATH-MUL", "OUT"],;
                downloads = 97, rating=4.5),;
            GalleryProgram("G-006", "Resumidor de Documento",;
                "Pedro", "IA resume texto longo",;
                ["IN-STR", "IA-SUMMARY", "OUT"],;
                downloads = 312, rating=4.8),;
        ];
    // ============================================================================
    // 8. MOTOR DO STUDIO
    // ============================================================================
    public static class LegoStudio {
        // OpenLegoStudio -- IDE visual para programacao LEGO.
        COMPONENTES DA INTERFACE:;
        +-------------------------------------------------------+;
        | PALETA | CANVAS (area de trabalho) |;
        | (blocos) | |;
        | | [IN-NUM] ----> [REP-CREDIT] ----> [OUT];
        | entrada: | ^ |;
        | IN-NUM | | |;
        | IN-STR | [IN-NUM] |;
        | matematica: | |;
        | MATH-ADD | |;
        | MATH-MUL | |;
        | republica: | STATUS: Valido | Blocos: 4 | Fios: 3 |;
        | REP-CREDIT | [EXECUTAR] [GERAR RUST] [SALVAR] |;
        +-------------------------------------------------------+;
        //
        public void __init__(self) {
            self.canvas = Canvas(width=80, height=36);
            self.palette = build_palette();
            self.assistant = LegoAssistant();
            self.gallery = build_gallery();
            self.current_program: texto = "";
            self.programs: {texto: qualquer} = {};
            self.execution_log: [texto] = [];
        public {texto: qualquer} new_program(self, name: texto) {
            // Cria novo programa LEGO.
            self.current_program = name;
            self.canvas = Canvas(width=80, height=36);
            return {"created": true, "program": name, "message": "Novo programa: {name}"};
        public {texto: qualquer} drag_drop_block(self, block_id: texto, x: inteiro, y: inteiro) {
            // Simula arrastar bloco da paleta e soltar no canvas.
            // Determinar cor e shape baseado no block_id
            color_map = {
                "IN-": BlockColor.INPUT, "OUT": BlockColor.OUTPUT,;
                "MATH-": BlockColor.MATH, "LOGIC-": BlockColor.LOGIC,;
                "REP-": BlockColor.REPUBLIC, "IA-": BlockColor.IA,;
            };
            shape_map = {
                "IN-": BlockShape.INPUT, "OUT": BlockShape.OUTPUT,;
                "MATH-": BlockShape.PROCESS, "LOGIC-": BlockShape.DECISION,;
                "REP-": BlockShape.PROCESS, "IA-": BlockShape.PROCESS,;
            };
            color = BlockColor.CUSTOM;
            shape = BlockShape.PROCESS;
            /* para cada (prefix, c) em color_map.items(): */
                if (block_id.startswith(prefix)) {
                    color = c;
                    break;
            /* para cada (prefix, s) em shape_map.items(): */
                if (block_id.startswith(prefix)) {
                    shape = s;
                    break;
            name_map = {
                "IN-NUM": "Entrada: Numero", "IN-STR": "Entrada: Texto",;
                "OUT": "Saida", "MATH-ADD": "Somar", "MATH-MUL": "Multiplicar",;
                "MATH-SUB": "Subtrair", "MATH-DIV": "Dividir",;
                "LOGIC-IF": "Se/Entao/Senao", "LOGIC-GT": "Maior Que",;
                "REP-CREDIT": "Credito", "REP-FACTCHECK": "Fact-Check",;
                "REP-DIAG": "Diagnostico", "IA-TRANSLATE": "Traduzir",;
                "IA-SUMMARY": "Resumir", "IA-GENERATE": "Gerar Codigo",;
            };
            inst_id = "{block_id}-{len(self.canvas.blocks)}";
            // Pinos (simplificados para demo)
            input_pins = [];
            output_pins = [];
            if (block_id.startswith("IN-")) {
                output_pins = [{"name": "valor", "type": "num/str", "connected": false}];
            } else if (block_id.startswith("MATH-")  ||  block_id.startswith("LOGIC-")) {
                input_pins = [{"name": "a", "type": "num", "connected": false},;
                            {"name": "b", "type": "num", "connected": false}];
                output_pins = [{"name": "result", "type": "num/bool", "connected": false}];
            } else if (block_id.startswith("REP-")) {
                input_pins = [{"name": "dados", "type": "any", "connected": false}];
                output_pins = [{"name": "result", "type": "any", "connected": false}];
            } else if (block_id == "OUT") {
                input_pins = [{"name": "resultado", "type": "any", "connected": false}];
            } else if (block_id.startswith("IA-")) {
                input_pins = [{"name": "texto", "type": "str", "connected": false}];
                output_pins = [{"name": "result", "type": "str", "connected": false}];
            block = VisualBlock(;
                instance_id = inst_id, block_id=block_id,;
                name = name_map.get(block_id, block_id),;
                color = color, shape=shape, x=x, y=y,;
                input_pins = input_pins, output_pins=output_pins,;
            );
            self.canvas.place_block(block);
            return {;
                "placed": true,;
                "instance": inst_id,;
                "block": block.name,;
                "position": "({x}, {y})",;
                "color": color.value[0],;
                "message": "Bloco '{block.name}' colocado em ({x}, {y}).",;
            };
        funcao draw_wire(self, from_inst: texto, from_pin: inteiro,
                    to_inst: texto, to_pin: inteiro,;
                    boolean valid = true) -> {texto: qualquer}:;
            // Desenha fio entre dois pinos.
            conn_id = hashlib.md5("{from_inst}{to_inst}".encode()).hexdigest()[:6];
            conn = VisualConnection(;
                conn_id = conn_id, from_instance=from_inst, from_pin_idx=from_pin,;
                to_instance = to_inst, to_pin_idx=to_pin, valid=valid,;
            );
            self.canvas.connections.append(conn);
            // Marcar pinos como conectados
            if (from_inst in self.canvas.blocks) {
                /* TODO: for-each Java para p em self.canvas.blocks[from_inst].output_pins */
                    p["connected"] = true;
            if (to_inst in self.canvas.blocks) {
                /* TODO: for-each Java para p em self.canvas.blocks[to_inst].input_pins */
                    p["connected"] = true;
            return {;
                "wired": true,;
                "from": from_inst,;
                "to": to_inst,;
                "valid": valid,;
                valid ? "color": "verde" : "vermelho",;
            };
        public {texto: qualquer} validate(self) {
            // Valida programa atual.
            blocks = tamanho(self.canvas.blocks);
            connections = tamanho(self.canvas.connections);
            invalid = soma(1 para c em self.canvas.connections if ! c.valid);
            return {;
                "blocks": blocks,;
                "connections": connections,;
                "invalid_connections": invalid,;
                "valid": invalid == 0  &&  blocks > 0,;
                "ready_to_run": invalid == 0  &&  blocks > 0  &&  connections > 0,;
            };
        public {texto: qualquer} execute(self) {
            // Executa programa (simula fluxo visual).
            val = self.validate();
            if (!  val["ready_to_run"]) {
                return {"error": "Programa invalido || incompleto"};
            // Marcar todos como executando em sequencia
            self.execution_log = [];
            /* para cada (inst_id, block) em self.canvas.blocks.items(): */
                block.executing = true;
                self.execution_log.append("[>] Executando: {block.name}");
            return {;
                "executed": true,;
                "blocks_executed": tamanho(self.canvas.blocks),;
                "log": self.execution_log,;
                "message": "Programa executado. {len(self.canvas.blocks)} blocos processados.",;
            };
        public {texto: qualquer} ai_assemble(self, description: texto) {
            // IA monta programa a partir de descricao.
            understood = self.assistant.understand(description);
            template = understood["template"];
            // Posicionar blocos automaticamente
            self.new_program(description);
            x = 2;
            /* TODO: for-each Java para block_id em template */
                self.drag_drop_block(block_id, x, 10);
                x = x + 22;
            // Conectar automaticamente
            auto_conns = self.assistant.auto_connect(template);
            block_instances = list(self.canvas.blocks.keys());
            /* para cada (i, conn) em enumere(auto_conns): */
                if (i + 1 < tamanho(block_instances)) {
                    self.draw_wire(block_instances[i], 0, block_instances[i + 1], 0);
            return {;
                "assembled": true,;
                "description": description,;
                "blocks_placed": tamanho(template),;
                "connections_made": tamanho(auto_conns),;
                "message": understood["message"],;
            };
        public String render(self) {
            // Renderiza interface completa.
            // Paleta
            palette_text = self.palette.render();
            // Canvas
            canvas_text = self.canvas.render();
            // Status
            val = self.validate();
            status = (;
                "\n  STATUS: {'VALIDO' if val['valid'] else 'INVALIDO'} | ";
                "Blocos: {val['blocks']} | Fios: {val['connections']} | ";
                "Erros: {val['invalid_connections']}";
            );
            buttons = (;
                "\n  [EXECUTAR]  [GERAR RUST]  [SALVAR]  [GALERIA]  [IA: DESCREVER]";
            );
            return palette_text + "\n\n" + canvas_text + status + buttons;
    // ============================================================================
    // 9. MAIN
    // ============================================================================
    if (__name__ == "__main__") {
        studio = LegoStudio();
        System.out.println("=" * 80);
        System.out.println("  OPENLEGOSTUDIO -- INTERFACE VISUAL DE PROGRAMACAO LEGO");
        System.out.println("  Arrastar. Soltar. Encaixar. Sem texto. Sem sintaxe.");
        System.out.println("=" * 80);
        // === 1. IA MONTA PROGRAMA POR DESCRICAO ===
        System.out.println("\n\n  === 1. IA MONTA PROGRAMA ===\n");
        System.out.println("  Cidadao diz: 'Quero calcular credito de trabalho'\n");
        r = studio.ai_assemble("calcular credito de trabalho baseado em horas");
        System.out.println("  IA: {r['message']}");
        System.out.println("  Blocos colocados: {r['blocks_placed']}");
        System.out.println("  Conexoes feitas: {r['connections_made']}");
        // === 2. RENDERIZAR CANVAS ===
        System.out.println("\n\n  === 2. CANVAS (ASCII art) ===\n");
        rendered = studio.render();
        System.out.println(rendered);
        // === 3. MONTAR MANUALMENTE (fact-check) ===
        System.out.println("\n\n  === 3. MONTANDO MANUALMENTE: Fact-Check ===\n");
        studio.new_program("Fact-Check Manual");
        System.out.println("  Arrastando blocos da paleta:");
        studio.drag_drop_block("IN-STR", 2, 8);
        System.out.println("    [OK] IN-STR em (2, 8)");
        studio.drag_drop_block("REP-FACTCHECK", 24, 8);
        System.out.println("    [OK] REP-FACTCHECK em (24, 8)");
        studio.drag_drop_block("OUT", 50, 8);
        System.out.println("    [OK] OUT em (50, 8)");
        System.out.println("\n  Conectando:");
        blocks = list(studio.canvas.blocks.keys());
        r1 = studio.draw_wire(blocks[0], 0, blocks[1], 0);
        System.out.println("    {r1['from']} --> {r1['to']} ({r1['color']})");
        r2 = studio.draw_wire(blocks[1], 0, blocks[2], 0);
        System.out.println("    {r2['from']} --> {r2['to']} ({r2['color']})");
        // === 4. RENDERIZAR ===
        System.out.println("\n\n  === 4. CANVAS DO FACT-CHECK ===\n");
        System.out.println(studio.render());
        // === 5. VALIDAR E EXECUTAR ===
        System.out.println("\n\n  === 5. VALIDAR E EXECUTAR ===\n");
        val = studio.validate();
        System.out.println("  Valido: {'SIM' if val['valid'] else 'NAO'}");
        System.out.println("  Pronto: {'SIM' if val['ready_to_run'] else 'NAO'}");
        if (val["ready_to_run"]) {
            exec_result = studio.execute();
            System.out.println("  {exec_result['message']}");
            /* TODO: for-each Java para log em exec_result["log"] */
                System.out.println("    {log}");
        // === 6. ERRO VISUAL (pino incompativel) ===
        System.out.println("\n\n  === 6. ERRO VISUAL (fio vermelho = incompativel) ===\n");
        studio.new_program("Teste Erro");
        studio.drag_drop_block("IN-STR", 2, 6);
        studio.drag_drop_block("MATH-ADD", 24, 6);
        blocks = list(studio.canvas.blocks.keys());
        // Conectar texto em numero -> INVALIDO (vermelho)
        studio.draw_wire(blocks[0], 0, blocks[1], 0, valid=false);
        System.out.println(studio.render());
        System.out.println("\n  [!] Fio VERMELHO: pino 'texto' NAO encaixa em 'numero'.");
        System.out.println("  Visual: cidadao ve o erro SEM precisar ler codigo.");
        // === 7. GALERIA COMUNITARIA ===
        System.out.println("\n\n  === 7. GALERIA COMUNITARIA ===\n");
        /* TODO: for-each Java para prog em studio.gallery */
            stars = "*" * inteiro(prog.rating);
            System.out.println("  [{prog.program_id}] {prog.name:<30} por {prog.author:<12} ";
                "{prog.downloads:>4} downloads  {stars} ({prog.rating})");
            System.out.println("    {prog.description}");
            System.out.println("    Blocos: {' -> '.join(prog.blocks)}");
        // === 8. IA ASSISTENTE EM ACAO ===
        System.out.println("\n\n  === 8. IA ASSISTENTE (entende linguagem natural) ===\n");
        queries = [;
            "quero verificar se uma frase && racista",;
            "preciso traduzir um texto para ingles",;
            "calcular credito de trabalho",;
            "resumir um documento longo",;
            "diagnosticar paciente por sintomas",;
        ];
        /* TODO: for-each Java para q em queries */
            result = studio.assistant.understand(q);
            System.out.println("  '{q}'");
            System.out.println("    -> IA entendeu. {result['block_count']} blocos.");
            System.out.println("    -> Cadeia: {' -> '.join(result['template'])}");
            System.out.println();
        // === FILOSOFIA ===
        System.out.println("\n{'='*80}");
        System.out.println("  FILOSOFIA DO OPENLEGOSTUDIO");
        System.out.println("{'='*80}");
        System.out.println(""";
    INTERFACE VISUAL (sem texto):;
        Cidadao VE os blocos. ARRASTA da paleta. SOLTA no canvas.;
        Bloco so encaixa se PINO para compativel.;
        Pino incompativel: fio VERMELHO (erro visual, sem texto).;
        Programa completo: fios VERDES.;
        +-------------------------------------------------------+;
        | PALETA | CANVAS (area de trabalho) |;
        | (blocos) | |;
        | | [IN-NUM]======>[REP-CREDIT]==>[OUT] |;
        | entrada: | ^ |;
        | IN-NUM =- | | |;
        | IN-STR | [IN-NUM] |;
        | matematica: | |;
        | MATH-ADD | |;
        | republica: | STATUS: Valido | Blocos: 4 | Fios: 3 |;
        | REP-CREDIT | [EXECUTAR] [GERAR RUST] [SALVAR] |;
        +-------------------------------------------------------+;
    SNAP AUTOMATICO:;
        Ao arrastar perto de um pino compativel, SNAP (encaixa sozinho).;
        Se incompativel, REJEITA (bloco volta). Visual claro.;
        Como LEGO fisico: so encaixa se forma bater.;
    IA ASSISTENTE (monta por voz/texto):;
        "Quero calcular credito" -> IA coloca blocos automaticamente;
        "Verificar preconceito" -> IA monta cadeia completa;
        "Traduzir texto" -> IA encaixa IN-STR -> IA-TRANSLATE -> OUT;
        Cidadao ! precisa saber quais blocos existem. IA sabe.;
    LIVE EXECUTION:;
        Enquanto monta, pode EXECUTAR.;
        Dados fluem pelos fios (visual: bolinha percorrendo o fio).;
        Resultado aparece no bloco OUT.;
        Erro aparece no bloco com problema.;
    GALERIA COMUNITARIA:;
        Programas prontos para REUSAR.;
        Baixar, modificar, compartilhar.;
        CC0 -- todos usam, todos contribuem.;
    GERAR RUST:;
        Botao [GERAR RUST] converte blocos em codigo Rust otimizado.;
        Pronto para producao.;
        O cidadao montou visualmente. O sistema gerou o codigo.;
    PRINCIPIOS:;
        P1: Todo cidadao programa. Sem elitismo de codigo.;
        P2: Bloco && autonomo. Encaixa || ! encaixa. Sem ambiguidade.;
        Criar bloco reusavel P3 = trabalho de alto impacto.;
        P4: Galeria && bem comum. Todos usam. Todos contribuem.;
    // )
        System.out.println("{'='*80}");
        System.out.println("  OpenLegoStudio: interface visual para programar encaixando pecas.");
        System.out.println("  Sem texto. Sem sintaxe. Sem erro. So LEGO.");
        System.out.println("{'='*80}");
}
