# =========================== IMPORTS ============================

# ==================== CONSTANTS & GLOBALS =======================

# ======================== FUNCTIONS =============================

def processar_instrucao_R(comando, banco_regs):
    # TODO: Executar instrução do tipo R
    if comando[0] == 'ADD':
        nome_rd = comando[1].lower()
        rd = banco_regs[nome_rd]
        rd.print_register()

        nome_rs = comando[2].lower()
        rs = banco_regs[nome_rs]
        rs.print_register()

        nome_rt = comando[3].lower()
        rt = banco_regs[nome_rt]
        rt.print_register()
    return


def processar_instrucao_I():
    # TODO: Executar instrução do tipo I
    return


def processar_instrucao_J():
    # TODO: Executar instrução do tipo J
    return


def executar(script_em_lista, banco_regs, memoria_dados, conj_de_instrucoes, flags_no_arq):
    pipelining_etapas = [None, None, None, None, None]

    print('############# SCRIPT #############')
    for linha in script_em_lista:
        print(linha)
    print()

    print('######## BANCO DE REGISTRADORES ########')
    for reg in banco_regs:
        banco_regs[reg].print_register()
    print()

    print('########## FLAGS NO ARQ ##########')
    print(flags_no_arq)
    print()

    for linha in script_em_lista:
        # Descobrir em qual indexação da lista está o comando
        i = 0
        if ':' in linha[i]:
            i += 1

        nome_comando = linha[i]
        instrucao = conj_de_instrucoes[nome_comando]

        if instrucao.tipo == 'R':
            # TODO: Executar instrução do tipo R
            processar_instrucao_R(linha[i:], banco_regs)
        elif instrucao.tipo == 'I':
            # TODO: Executar instrução do tipo I
            processar_instrucao_I()
        else:  # instrucao.tipo == 'J'
            # TODO: Executar instrução do tipo J
            processar_instrucao_J()

    return
