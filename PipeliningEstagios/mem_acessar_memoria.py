def pipe3_acessar_memoria(linha_de_instrucao_processada, memoria_dados):
    instrucao = linha_de_instrucao_processada[0]

    if instrucao.nome != 'LW' or instrucao.nome != 'SW':
        return linha_de_instrucao_processada
    else:
        return
