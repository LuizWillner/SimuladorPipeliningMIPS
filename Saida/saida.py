
def init_html(arq_html):
    arq_html.write('''
        <html lang="pt-br">

        <head>
            <meta charset="windows-1252">
            <title>SAIDA: PIPELINING</title>
        </head>

        <body>
            <header>
                SAIDA: PIPELINING
            </header>
    ''')

    return


def print_banco_regs_html(arq_html, banco_regs):
    arq_html.write('''
        <table id="banco_regs">
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
        <table id="conj_de_instrucoes">
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
        <div id="script_assembly">
    ''')

    for linha in arq_txt:
        arq_html.write(f'''
            <div>{linha}</div>
        ''')

    arq_html.write('''
        </div>
    ''')


def conclude_html(arq_html):
    arq_html.write('''
            <footer>
                Feito por: Luiz Claudio Willner & Marina Piragibe
            </footer>
        </body>
    ''')

    return
