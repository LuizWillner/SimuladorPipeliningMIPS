# =========================== IMPORTS ============================

# ==================== CONSTANTS & GLOBALS =======================

# ======================== FUNCTIONS =============================

def processar_instrucao_R(linha_de_instrucao, banco_regs):

    if linha_de_instrucao[0] == 'ADD':
        nome_rd = linha_de_instrucao[1].lower()
        rd = banco_regs[nome_rd]
        # rd.print_register()

        nome_rs = linha_de_instrucao[2].lower()
        rs = banco_regs[nome_rs]
        # rs.print_register()

        nome_rt = linha_de_instrucao[3].lower()
        rt = banco_regs[nome_rt]
        # rt.print_register()

        return [rd, rs, rt]

    # TODO: Completar processamento com as outras instruções do tipo R


def processar_instrucao_I(linha_de_instrucao, banco_regs):

    if linha_de_instrucao[0] == 'ADDI':
        nome_rt = linha_de_instrucao[1].lower()
        rt = banco_regs[nome_rt]

        nome_rs = linha_de_instrucao[2].lower()
        rs = banco_regs[nome_rs]

        imediato = linha_de_instrucao[3].lower()
        imediato = int(imediato)

        return [rt, rs, imediato]

    # TODO: Completar processamento com as outras instruções do tipo I


def processar_instrucao_J():
    # TODO: Executar instrução do tipo J
    return


def pipe1_decodificar_instrucao(linha_de_instrucao, conj_de_instrucoes, banco_regs):
    linha_de_instrucao_processada = []

    nome_instrucao = linha_de_instrucao[0]
    instrucao = conj_de_instrucoes[nome_instrucao]
    # instrucao.print_instruction()

    if instrucao.tipo == 'R':
        linha_de_instrucao_processada = processar_instrucao_R(linha_de_instrucao, banco_regs)
        linha_de_instrucao_processada.insert(0, instrucao)

    elif instrucao.tipo == 'I':
        linha_de_instrucao_processada = processar_instrucao_I(linha_de_instrucao, banco_regs)
        linha_de_instrucao_processada.insert(0, instrucao)

    else:  # instrucao.tipo == 'J'
        pass

    return linha_de_instrucao_processada


def pipe2_executar_instrucao():
    return


def avancar_pipelining(fila_pipeline, linha_de_instrucao_para_inserir, conj_de_instrucoes, banco_regs, ciclo_atual):
    print(f'\n================================= CICLO {ciclo_atual} =================================\n')
    #  Pipelining ESTÁGIO 0 - IF: "Buscar" próxima instrução na fila de pipeline e adicionar no início da fila;
    fila_pipeline.insert(0, linha_de_instrucao_para_inserir)
    fila_pipeline.pop()
    print(f'Atualmente no estágio 0: {fila_pipeline[0]}')

    # Pipelining ESTÁGIO 4 - WB: Escreve o resultado da operação do estágio 4 (se houver) no banco de registradores
    # O estágio 4 (de ecrita) ocorre antes do estágio 1 (de leitura).
    if fila_pipeline[4]:
        pass
    print(f'Atualmente no estágio 4: {fila_pipeline[4]}')

    # Pipelining ESTÁGIO 1 - ID: Decodificar (se houver) a instrução que está no estágio 1 do pipe, fazendo
    # a leitura dos registradores.
    # Instruções J, JR, JAL, BEQ e BNE fazem o desvio no estágio 1 (ID).
    if fila_pipeline[1]:
        fila_pipeline[1] = pipe1_decodificar_instrucao(fila_pipeline[1], conj_de_instrucoes, banco_regs)
    print(f'Atualmente no estágio 1: {fila_pipeline[1]}')

    # Pipelining ESTÁGIO 2 - EX: Calcula o endereço ou executa a operação expressa pela instrução que está na etapa 2 (se houver)
    if fila_pipeline[2]:
        pass
    print(f'Atualmente no estágio 2: {fila_pipeline[2]}')

    # Pipelining ESTÁGIO 3 - MEM: Acessa a memória de dados da forma que a instrução do estágio 3 pedir
    if fila_pipeline[3]:
        pass
    print(f'Atualmente no estágio 3: {fila_pipeline[3]}')

    print('\n####### PIPELINING #######')
    for p in fila_pipeline:
        print(p)
    print('##########################\n')

    ciclo_atual += 1
    return ciclo_atual


def executar(script_em_lista, banco_regs, memoria_dados, conj_de_instrucoes, flags_no_arq):
    pipeline = [None, None, None, None, None]

    print('############# SCRIPT #############')
    for linha in script_em_lista:
        print(linha)
    print()

    print('######## BANCO DE REGISTRADORES ########')
    for reg in banco_regs:
        banco_regs[reg].print_register()
    print()
    print(banco_regs)

    print('########## FLAGS NO ARQ ##########')
    print(flags_no_arq)
    print()

    # Ler script linha por linha e adicionar pouco a pouco as linhas de instrução na fila de pipeline
    ciclo = 1
    for linha in script_em_lista:
        # Descobrir em qual indexação da lista está o comando
        i = 0
        if ':' in linha[i]:
            i += 1

        ciclo = avancar_pipelining(fila_pipeline=pipeline,
                                   linha_de_instrucao_para_inserir=linha[i:],
                                   conj_de_instrucoes=conj_de_instrucoes,
                                   banco_regs=banco_regs,
                                   ciclo_atual=ciclo)

    # Após colocar todas as instruções do script em fila, terminar de executar o pipeline até ele ficar vazio
    while pipeline != [None, None, None, None, None]:
        ciclo = avancar_pipelining(fila_pipeline=pipeline,
                                   linha_de_instrucao_para_inserir=None,
                                   conj_de_instrucoes=conj_de_instrucoes,
                                   banco_regs=banco_regs,
                                   ciclo_atual=ciclo)

    return
