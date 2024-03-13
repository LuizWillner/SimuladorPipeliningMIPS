# =========================== IMPORTS ============================
from PipeliningEstagios.id_decodificar_instrucao import *
from PipeliningEstagios.ex_executar_instrucao import *
from PipeliningEstagios.mem_acessar_memoria import *
from PipeliningEstagios.wb_escrever_resultado_no_reg import *
from Saida.saida import *


# ==================== CONSTANTS & GLOBALS =======================

# ======================== FUNCTIONS =============================

def avancar_pipelining(fila_pipeline, pc_atual, linha_de_instrucao_para_inserir, conj_de_instrucoes, banco_regs,
                       memoria_dados, flags_no_arq):
    #  Pipelining ESTÁGIO 0 - IF: "Buscar" próxima instrução na fila de pipeline e adicionar no início da fila;
    fila_pipeline.insert(0, linha_de_instrucao_para_inserir)
    fila_pipeline.pop()
    print(f'Atualmente no estágio 0: {fila_pipeline[0]}')

    # Pipelining ESTÁGIO 4 - WB: Escreve o resultado da operação do estágio 4 (se houver) no banco de registradores
    # O estágio 4 (de ecrita) ocorre antes do estágio 1 (de leitura).
    if fila_pipeline[4]:
        pipe4_salvar_no_reg(fila_pipeline[4], banco_regs)
    print(f'Atualmente no estágio 4: {fila_pipeline[4]}')

    # Pipelining ESTÁGIO 1 - ID: Decodificar (se houver) a instrução que está no estágio 1 do pipe, fazendo
    # a leitura dos registradores.
    # Instruções J, JR, JAL, BEQ e BNE fazem o desvio nesse estágio (ID).
    if fila_pipeline[1]:
        fila_pipeline[1] = pipe1_decodificar_instrucao(fila_pipeline[1], conj_de_instrucoes, banco_regs, flags_no_arq,
                                                       pc_atual)
        if fila_pipeline[1][1].nome == 'BEQ' or fila_pipeline[1][1].nome == 'BNE' or fila_pipeline[1][1].nome == 'J' or \
                fila_pipeline[1][1].nome == 'JAL' or fila_pipeline[1][1].nome == 'JR':
            pc_atual = fila_pipeline[1][-1]
    print(f'Atualmente no estágio 1: {fila_pipeline[1]}')

    # Pipelining ESTÁGIO 2 - EX: Calcula o endereço ou executa a operação expressa pela instrução que está na etapa 2 (se houver)
    if fila_pipeline[2]:
        fila_pipeline[2] = pipe2_executar_instrucao(fila_pipeline[2], banco_regs, flags_no_arq)
    print(f'Atualmente no estágio 2: {fila_pipeline[2]}')

    # Pipelining ESTÁGIO 3 - MEM: Acessa a memória de dados da forma que a instrução do estágio 3 pedir
    if fila_pipeline[3]:
        fila_pipeline[3] = pipe3_acessar_memoria(fila_pipeline[3], memoria_dados)
    print(f'Atualmente no estágio 3: {fila_pipeline[3]}')

    pc_atual += 1
    return pc_atual


def executar(script_em_lista, banco_regs, memoria_dados, conj_de_instrucoes, flags_no_arq, arq_saida):
    pipeline = [None, None, None, None, None]

    arq_saida.write('<section id="todos_os_ciclos">')

    # Ler script linha por linha e adicionar pouco a pouco as linhas de instrução na fila de pipeline
    ciclo = 1
    pc_atual = 0
    while pc_atual < len(script_em_lista):
        linha = script_em_lista[pc_atual]

        # Descobrir em qual indexação da lista está o comando
        i = 0
        while ':' in linha[i]:
            i += 1
        linha_sem_flag = linha[i:]

        # Se o comando for NOP, atribuímos None a linha_sem_flag para simular a bolha
        if linha_sem_flag[0] == 'NOP':
            linha_sem_flag = None

        print(f'\n================================= CICLO {ciclo} =================================\n')
        pc_atual = avancar_pipelining(fila_pipeline=pipeline,
                                      pc_atual=pc_atual,
                                      linha_de_instrucao_para_inserir=linha_sem_flag,
                                      conj_de_instrucoes=conj_de_instrucoes,
                                      banco_regs=banco_regs,
                                      memoria_dados=memoria_dados,
                                      flags_no_arq=flags_no_arq)

        print('\n####### PIPELINING #######')
        for p in pipeline:
            print(p)
        print('##########################\n')

        memoria_dados.print_memory()
        print()

        print_ciclo_html(arq_saida, ciclo, pipeline, banco_regs, memoria_dados)

        ciclo += 1

    # Após colocar todas as instruções do script em fila, terminar de executar o pipeline até ele ficar vazio
    while pipeline != [None, None, None, None, None]:
        print(f'\n================================= CICLO {ciclo} =================================\n')
        pc_atual = avancar_pipelining(fila_pipeline=pipeline,
                                      pc_atual=pc_atual,
                                      linha_de_instrucao_para_inserir=None,
                                      conj_de_instrucoes=conj_de_instrucoes,
                                      banco_regs=banco_regs,
                                      memoria_dados=memoria_dados,
                                      flags_no_arq=flags_no_arq)
        print('\n####### PIPELINING #######')
        for p in pipeline:
            print(p)
        print('##########################\n')

        memoria_dados.print_memory()
        print()

        print_ciclo_html(arq_saida, ciclo, pipeline, banco_regs, memoria_dados)

        ciclo += 1

    for nome_reg in banco_regs:
        reg = banco_regs[nome_reg]
        reg.print_register()

    arq_saida.write('</section>\n')

    return
