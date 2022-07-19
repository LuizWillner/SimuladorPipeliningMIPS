# =========================== IMPORTS ============================

# ==================== CONSTANTS & GLOBALS =======================

# ======================== FUNCTIONS =============================

def processar_instrucao_R():
    # TODO: Executar instrução do tipo R
    return


def processar_instrucao_I():
    # TODO: Executar instrução do tipo I
    return


def processar_instrucao_J():
    # TODO: Executar instrução do tipo J
    return


def executar(script_em_lista, banco_regs, memoria_dados, conj_de_instrucoes, flags_no_arq):
    for linha in script_em_lista:
        # Descobrir em qual indexação da lista está o comando
        i = 0
        if ':' in linha[i]:
            i += 1

        nome_comando = linha[i]
        instrucao = conj_de_instrucoes[nome_comando]

        if instrucao.tipo == 'R':
            # TODO: Executar instrução do tipo R
            processar_instrucao_R()
        elif instrucao.tipo == 'I':
            # TODO: Executar instrução do tipo I
            processar_instrucao_I()
        else:  # elif instrucao.tipo == 'J'
            # TODO: Executar instrução do tipo J
            processar_instrucao_J()

    return
