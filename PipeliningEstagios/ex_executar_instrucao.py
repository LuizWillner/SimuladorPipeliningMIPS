# ======================== FUNCTIONS =============================
def executar_instrucao_R(linha_de_instrucao_processada, banco_regs):
    instrucao = linha_de_instrucao_processada[0]
    if instrucao.nome == 'ADD':
        rs = linha_de_instrucao_processada[2]
        rt = linha_de_instrucao_processada[3]
        res = rs.valor + rt.valor
        return res


def executar_instrucao_I():
    return


def executar_instrucao_J():
    return


def pipe2_executar_instrucao(linha_de_instrucao_processada, banco_regs, flags_no_arq):
    instrucao = linha_de_instrucao_processada[0]

    if instrucao.tipo == 'R':
        res = executar_instrucao_R(linha_de_instrucao_processada, banco_regs)
        linha_de_instrucao_processada.append(res)
        return linha_de_instrucao_processada
    elif instrucao.tipo == 'I':
        pass
    else:  # instrucao.tipo == 'J'
        pass
    return
