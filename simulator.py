# =========================== IMPORTS ============================

# ==================== CONSTANTS & GLOBALS =======================

# ======================== FUNCTIONS =============================

def processar_instrucao_R(comando, banco_regs):
    # TODO: Executar instrução do tipo R
    if comando[0] == 'ADD':
        nome_rd = comando[1].lower()
        rd = banco_regs[nome_rd]
        # rd.print_register()

        nome_rs = comando[2].lower()
        rs = banco_regs[nome_rs]
        # rs.print_register()

        nome_rt = comando[3].lower()
        rt = banco_regs[nome_rt]
        # rt.print_register()

        rd.valor = rs.valor + rt.valor
    return


def processar_instrucao_I(comando, banco_regs):
    # TODO: Executar instrução do tipo I
    if comando[0] == 'ADDI':
        nome_rt = comando[1]
        rt = banco_regs[nome_rt]

        nome_rs = comando[2]
        rs = banco_regs[nome_rs]

        imediato = comando[3]
        imediato = int(imediato)

        rt.valor = rs.valor + imediato
    return


def processar_instrucao_J():
    # TODO: Executar instrução do tipo J
    return


def executar(script_em_lista, banco_regs, memoria_dados, conj_de_instrucoes, flags_no_arq):
    pipelining = [None, None, None, None, None]

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

    ciclo = 1
    for linha in script_em_lista:
        # Descobrir em qual indexação da lista está o comando
        i = 0
        if ':' in linha[i]:
            i += 1
        print(f'\n================================= CICLO {ciclo} =================================\n')
        #  Pipelining ESTÁGIO 0 - IF: "Buscar" próxima instrução na fila de pipelining e adicionar no início da fila;
        pipelining.insert(0, linha[i:])
        pipelining.pop()
        print(f'Atualmente no estágio 0: {pipelining[0]}')

        # Pipelining ESTÁGIO 4 - WB: Escreve o resultado da operação do estágio 4 (se houver) no banco de registradores
        # O estágio 4 (de ecrita) ocorre antes do estágio 1 (de leitura).
        if pipelining[4]:
            pass
        print(f'Atualmente no estágio 4: {pipelining[4]}')

        # Pipelining ESTÁGIO 1 - ID: Decodificar (se houver) a instrução que está no estágio 1 do pipe, fazendo
        # a leitura dos registradores.
        # Instruções J, JR, JAL, BEQ e BNE fazem o desvio no estágio 1 (ID).
        if pipelining[1]:
            nome_comando = pipelining[1][0]
            instrucao = conj_de_instrucoes[nome_comando]
            # instrucao.print_instruction()
        print(f'Atualmente no estágio 1: {pipelining[1]}')

        # Pipelining ESTÁGIO 2 - EX: Calcula o endereço ou executa a operação expressa pela instrução que está na etapa 2 (se houver)
        if pipelining[2]:
            pass
        print(f'Atualmente no estágio 2: {pipelining[2]}')

        # Pipelining ESTÁGIO 3 - MEM: Acessa a memória de dados da forma que a instrução do estágio 3 pedir
        if pipelining[3]:
            pass
        print(f'Atualmente no estágio 3: {pipelining[3]}')

        print('\n####### PIPELINING #######')
        print(pipelining)
        print('##########################\n')

        ciclo += 1

    return
