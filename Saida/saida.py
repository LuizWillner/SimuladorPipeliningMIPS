
def init_html(arq_html):
    arq_html.write('''
        <html lang="pt-br">

        <head>
            <meta charset="windows-1252">
            <title>SAIDA: PIPELINING</title>
        </head>

        <body>
            <header>
                <h1>SAIDA: PIPELINING</h1>
            </header>
    ''')

    return


def print_memoria_dados_html(arq_html, memoria_dados):
    arq_html.write('''
        <table class="memoria_dados">
            <tr>
                <th>Index da memoria</th>
                <th>Conteudo armazenado</th>
            </tr>    
    ''')

    for index in memoria_dados.filled_values:
        arq_html.write(f'''
            <tr>
                <th>{index}</th>
                <th>{hex(memoria_dados.filled_values[index])}</th>
            </tr>
        ''')

    arq_html.write('''
        </table>
    ''')
    return


def print_banco_regs_html(arq_html, banco_regs):
    arq_html.write('''
        <table class="banco_regs">
            <tr>
                <th>Numero do registrador</th>
                <th>Nome</th>
                <th>Valor armazenado</th>
            </tr>
    ''')

    for nome_reg in banco_regs:
        reg = banco_regs[nome_reg]

        arq_html.write(f'''
            <tr>
                <th>{reg.id}</th>
                <th>{reg.nome}</th>
                <th>{reg.valor}</th>
            </tr>
        ''')

    arq_html.write('''
        </table>
    ''')

    return


def print_conj_de_instrucoes_html(arq_html, conj_de_instrucoes):
    arq_html.write('''
        <table class="conj_de_instrucoes">
            <tr>
                <th>Nome</th>
                <th>Opcode</th>
                <th>Tipo</th>
                <th>Funct</th>
            </tr>
    ''')

    for nome_inst in conj_de_instrucoes:
        inst = conj_de_instrucoes[nome_inst]

        arq_html.write(f'''
            <tr>
                <th>{inst.nome}</th>
                <th>{inst.opcode}</th>
                <th>{inst.tipo}</th>
                <th>{inst.funct}</th>
            </tr>
        ''')

    arq_html.write('''
        </table>
    ''')

    return


def print_text_file_html(arq_html, arq_txt):
    arq_txt.seek(0)
    arq_html.write('''
        <div class="script_assembly">
    ''')

    for linha in arq_txt:
        arq_html.write(f'''
            <div>{linha}</div>
        ''')

    arq_html.write('''
        </div>
    ''')

    return


def print_pipeline_html(arq_html, fila_pipeline):
    arq_html.write('''
        <table class="pipeline">
            <tr>
                <th>ETAPA 1</th>
                <th>ETAPA 2</th>
                <th>ETAPA 3</th>
                <th>ETAPA 4</th>
                <th>ETAPA 5</th>
            </tr>
    ''')

    arq_html.write('<tr>')
    for linha_inst in fila_pipeline:
        if not linha_inst:
            arq_html.write('''
                <th>
                    NOP
                </th>
            ''')
        else:
            arq_html.write(f'''
                <th>
                    {linha_inst[0].nome}
                </th>
            ''')
    arq_html.write('</tr>')

    arq_html.write('''
        </table">
    ''')

    return


def print_ciclo_html(arq_html, num_ciclo, fila_pipeline, banco_regs, memoria_dados):
    arq_html.write('<div class="ciclo">')
    arq_html.write(f'<h2> CICLO {num_ciclo}</h2>')
    print_pipeline_html(arq_html, fila_pipeline)
    print_banco_regs_html(arq_html, banco_regs)
    print_memoria_dados_html(arq_html, memoria_dados)
    arq_html.write('</div>')


def conclude_html(arq_html):
    arq_html.write('''
            <footer>
                Feito por: Luiz Claudio Willner & Marina Piragibe
            </footer>
        </body>
    ''')

    return
