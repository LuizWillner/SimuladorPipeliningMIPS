# =========================== IMPORTS ============================

from RegistradoresEMemoria.register import *
from RegistradoresEMemoria.memory import *
from Instrucao.instruction import *
from Saida.saida import *
import simulator


# ==================== CONSTANTS & GLOBALS =======================


# ======================== FUNCTIONS =============================

def gerar_lista_instruction_fields(command_line):
    command_line = command_line.upper()
    command_line = command_line.replace(',', ' ')
    command_line = command_line.replace('\n', '')
    command_line = command_line.replace('(', ' ')
    command_line = command_line.replace(')', '')

    bitfield_list = command_line.split()
    return bitfield_list


def ler_instruction_fields(arq_assembly):
    linha = arq_assembly.readline()
    instruction_fields = []
    num_linha = 0

    while linha:
        linha_lista = gerar_lista_instruction_fields(linha)

        if linha_lista:  # se a lista tiver alguma coisa dentro, ou seja, não for vazia...
            instruction_fields.append(linha_lista)  # ... adicionar na matriz geral de linhas

            if ':' in linha_lista[0]:  # se tiver ':', é uma flag, então...
                # Adicionar flag no dicionario de flags junto com sua posição no arquivo
                flag_nome = linha_lista[0].replace(':', '')
                # flag_pos = arq_assembly.tell()
                flag_pos = num_linha
                flags_no_arq[flag_nome] = flag_pos

        linha = arq_assembly.readline()  # passar pra próxima linha
        num_linha += 1

    return instruction_fields


# ========================== MAIN ================================

# Abrir os arquivos
arq_assembly = open('exemplo.asm', 'r')
arq_regset = open('RegistradoresEMemoria/register_set.txt', 'r')
arq_instset = open('Instrucao/instruction_set.txt', 'r')
arq_saida = open('saida.html', 'w')

# Gerar matriz em memória que representa o script assembly.
# Cada lista dessa matriz é uma linha do código fonte.
# Cada item da lista é um campo de instrução (ex: ADD $V0, $ZERO, $AT --> ['ADD', '$V0', '$ZERO', '$AT']
# Além disso, gerar também dicionário que associa todas as flags do código com suas respectivas posições no arquivo
flags_no_arq = dict({})
instruction_fields = ler_instruction_fields(arq_assembly)

# Dicionário que representa o banco de registradores
banco_regs = dict({})
for i in range(32):  # 32 é a quantidade de registradores do processador
    reg = ler_registrador(arq_regset)
    banco_regs[reg.nome] = reg

# Lista que representa a memória de dados
memoria_dados = Memory(1000)

# Dicionário que representa o conjunto de instruções, montado a partir da leitura do arquivo "instruction_set.txt"
instrucoes_dict = dict({})
for i in range(14):  # 14 é a quantidade de instruções do conjunto de instruções fornecidos no exercício
    inst = ler_instrucao(arq_instset)
    instrucoes_dict[inst.nome] = inst

# Iniciar saída formatada em HTML
init_html(arq_saida)

# Escrever subheader do HTML
arq_saida.write('<section id="subheader">')
print_banco_regs_html(arq_saida, banco_regs)
print_conj_de_instrucoes_html(arq_saida, instrucoes_dict)
print_text_file_html(arq_saida, arq_assembly)
arq_saida.write('</section>')


# Executrar simulador de pipelining
simulator.executar(script_em_lista=instruction_fields,
                   banco_regs=banco_regs,
                   memoria_dados=memoria_dados,
                   conj_de_instrucoes=instrucoes_dict,
                   flags_no_arq=flags_no_arq,
                   saida=arq_saida)


# Concluir HTML, criando footer e fechando body
conclude_html(arq_saida)

# Fechar os arquivos
arq_assembly.close()
arq_regset.close()
arq_instset.close()
arq_saida.close()
