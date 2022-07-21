# ======================== FUNCTIONS =============================
def executar_instrucao_R(linha_de_instrucao_processada, banco_regs):
    instrucao = linha_de_instrucao_processada[0]

    if instrucao.nome == 'ADD':
        rs = linha_de_instrucao_processada[2]
        rt = linha_de_instrucao_processada[3]
        res = rs + rt
        return res

    elif instrucao.nome == 'AND':
        rs = linha_de_instrucao_processada[2]
        rt = linha_de_instrucao_processada[3]
        res = rs & rt  # operador & é bitwise AND
        return res

    elif instrucao.nome == 'OR':
        rs = linha_de_instrucao_processada[2]
        rt = linha_de_instrucao_processada[3]
        res = rs | rt  # operador | é bit-wise OR
        return res

    elif instrucao.nome == 'SLL':
        rs = linha_de_instrucao_processada[2]
        shamt = linha_de_instrucao_processada[3]
        res = rs << shamt
        return res

    elif instrucao.nome == 'SRL':
        rs = linha_de_instrucao_processada[2]
        shamt = linha_de_instrucao_processada[3]
        res = rs >> shamt
        return res

    elif instrucao.nome == 'SUB':
        rs = linha_de_instrucao_processada[2]
        rt = linha_de_instrucao_processada[3]
        res = rs - rt
        return res


def executar_instrucao_I(linha_de_instrucao_processada, banco_regs):
    instrucao = linha_de_instrucao_processada[0]

    if instrucao.nome == 'ADDI' or instrucao.nome == 'LW' or instrucao.nome == 'SW':
        rs = linha_de_instrucao_processada[2]
        imediato = linha_de_instrucao_processada[3]
        res = rs + imediato
        return res


def pipe2_executar_instrucao(linha_de_instrucao_processada, banco_regs, flags_no_arq):
    instrucao = linha_de_instrucao_processada[0]

    if instrucao.tipo == 'R':
        res = executar_instrucao_R(linha_de_instrucao_processada, banco_regs)
        linha_de_instrucao_processada.append(res)
        return linha_de_instrucao_processada

    elif instrucao.tipo == 'I':
        res = executar_instrucao_I(linha_de_instrucao_processada, banco_regs)
        linha_de_instrucao_processada.append(res)
        return linha_de_instrucao_processada

    else:  # instrucao.tipo == 'J'
        pass

    return
