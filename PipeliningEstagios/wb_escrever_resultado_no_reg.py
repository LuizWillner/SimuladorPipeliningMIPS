
def pipe4_salvar_no_reg(linha_de_instrucao_processada, banco_regs):
    instrucao = linha_de_instrucao_processada[1]

    if instrucao.nome == 'ADD' or instrucao.nome == 'ADDI' or instrucao.nome == 'SUB':
        rd = linha_de_instrucao_processada[2]
        rd.valor = linha_de_instrucao_processada[-1]  # Última posição do vetor é o resultado da operação

    elif instrucao.nome == 'AND' or instrucao.nome == 'OR':
        rd = linha_de_instrucao_processada[2]
        rd.valor = linha_de_instrucao_processada[-1]  # Última posição do vetor é o resultado da operação

    elif instrucao.nome == 'SLL' or instrucao.nome == 'SRL':
        rd = linha_de_instrucao_processada[2]
        rd.valor = linha_de_instrucao_processada[-1]  # Última posição do vetor é o resultado da operação

    elif instrucao.nome == 'LW':
        rt = linha_de_instrucao_processada[2]
        rt.valor = linha_de_instrucao_processada[-1]  # Última posição do vetor é o resultado da operação

    elif instrucao.nome == 'JAL':
        ra = linha_de_instrucao_processada[2]
        ra.valor = linha_de_instrucao_processada[-2] + 1  # salva endereço da próxima instrução no reg $ra

    return
