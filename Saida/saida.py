
def init_html(arq_html):
    arq_html.write('''
        <html lang="pt-br">

        <head>
            <meta charset="windows-1252">
            <link rel="stylesheet" href="style.css">
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
        <div class="memoria_dados">
            <h3>Memoria principal</h3>
    ''')
    arq_html.write('''
            <table>
                <tr>
                    <th>Index da memoria</th>
                    <th>Conteudo armazenado</th>
                </tr>    
    ''')

    for index in memoria_dados.filled_values:
        arq_html.write(f'''
                <tr>
                    <td>{index}</td>
                    <td>{hex(memoria_dados.filled_values[index])}</td>
                </tr>
        ''')

    arq_html.write('''
            </table>
        </div>
    ''')
    return


def print_banco_regs_html(arq_html, banco_regs):
    arq_html.write('''
        <div class="banco_regs">
            <h3>Banco de Registradores</h3>
            <table>
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
                    <td>{reg.id}</td>
                    <td>{reg.nome}</td>
                    <td>{reg.valor}</td>
                </tr>
        ''')

    arq_html.write('''
            </table>
        </div>
    ''')

    return


def print_conj_de_instrucoes_html(arq_html, conj_de_instrucoes):
    arq_html.write('''
        <div class="conj_de_instrucoes">
            <h3>Conjunto de Instrucoes</h3>
            <table>
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
                    <td>{inst.nome}</td>
                    <td>{inst.opcode}</td>
                    <td>{inst.tipo}</td>
                    <td>{inst.funct}</td>
                </tr>
        ''')

    arq_html.write('''
            </table>
        </div>
    ''')

    return


def print_text_file_html(arq_html, arq_txt):
    arq_txt.seek(0)
    arq_html.write('''
    <div class="script_assembly">
        <h3>Script em Assembly .asm</h3>
    ''')

    arq_html.write('<div>')
    for linha in arq_txt:
        arq_html.write(f'''
            <p>{linha}</p>
        ''')
    arq_html.write('</div>')

    arq_html.write('''
    </div>
    ''')

    return


def print_pipeline_html(arq_html, fila_pipeline):
    arq_html.write('''
        <div class="pipeline">
            <table>
                <tr>
                    <th>ETAPA 1</th>
                    <th>ETAPA 2</th>
                    <th>ETAPA 3</th>
                    <th>ETAPA 4</th>
                    <th>ETAPA 5</th>
                </tr>
    ''')

    arq_html.write('<tr>')
    for i in range(len(fila_pipeline)):
        linha_inst = fila_pipeline[i]

        if not linha_inst:
            arq_html.write('''
                    <td>
                        ######### NOP #########
                    </td>
            ''')
        elif i == 0:
            arq_html.write(f'''
                    <td>
                        {linha_inst}
                    </td>
            ''')
        else:
            arq_html.write(f'''
                    <td>
                        {linha_inst[0]}
                    </td>
            ''')
    arq_html.write('</tr>')

    arq_html.write('''
            </table>
        </div>
    ''')

    return


def print_ciclo_html(arq_html, num_ciclo, fila_pipeline, banco_regs, memoria_dados):
    arq_html.write('<div class="ciclo">')
    arq_html.write(f'<h2> CICLO {num_ciclo}</h2>')
    print_pipeline_html(arq_html, fila_pipeline)
    print_banco_regs_html(arq_html, banco_regs)
    print_memoria_dados_html(arq_html, memoria_dados)
    arq_html.write('</div>')
    arq_html.write('<hr>')


def conclude_html(arq_html):
    arq_html.write('''
            <footer>
                Feito por: Luiz Claudio Willner & Marina Piragibe
            </footer>
        </body>
    ''')

    return
