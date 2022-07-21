def salvar_res(linha_de_instrucao_processada):
    instrucao = linha_de_instrucao_processada[0]

    if instrucao.nome == 'ADD':
        rd = linha_de_instrucao_processada[1]
        rd.valor = linha_de_instrucao_processada[-1]  # Última posição do vetor é o resultado da operação
        return


def pipe4_salvar_no_reg(linha_de_instrucao_processada, banco_regs):
    instrucao = linha_de_instrucao_processada[0]

    if instrucao.tipo == 'R':
        salvar_res(linha_de_instrucao_processada)
    elif instrucao.tipo == 'I':
        pass
    else:  # instrucao.tipo == 'J'
        pass
    return
