def pipe3_acessar_memoria(linha_de_instrucao_processada, memoria_dados):
    instrucao = linha_de_instrucao_processada[0]

    if instrucao.nome == 'LW':
        index_mem = linha_de_instrucao_processada[-1]
        valor_mem = memoria_dados.values[index_mem]
        linha_de_instrucao_processada[-1] = valor_mem

    elif instrucao.nome == 'SW':
        rt = linha_de_instrucao_processada[1]
        valor_mem = rt.valor
        index_mem = linha_de_instrucao_processada[-1]
        memoria_dados.values[index_mem] = valor_mem
        memoria_dados.filled_values[index_mem] = valor_mem

    return linha_de_instrucao_processada
