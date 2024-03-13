# ======================= IMPORTS ==============================

# ==================== CONSTANTS & GLOBALS =======================

KEY_SIZE = 4
NAME_SIZE = 4
INST_TYPE_SIZE = 1
OPCODE_SIZE = 1
INST_FUNCT_SIZE = 1
INSTRUCTION_SIZE = KEY_SIZE + NAME_SIZE + INST_TYPE_SIZE + OPCODE_SIZE + INST_FUNCT_SIZE
ALL_INSTS_FILE_NAME = 'instruction_set.txt'


# ======================= CLASSES ==============================

# Classe Instrução
class Instruction:
    def __init__(self, nome, opcode, tipo, funct):
        self.nome = nome  # Nome da instrução (ex: ADD)
        self.opcode = opcode  # Opcode da instrução (ex: 0)
        self.tipo = tipo
        self.funct = funct

    def print_instruction(self, one_line=False):
        if not one_line:
            print(f'Instrução {self.nome}:')
            print(f'Opcode: {self.opcode}')
            print(f'Tipo: {self.tipo}')
            print(f'Funct: {self.funct}')
            print()
        else:
            print(f'Instrução {self.nome}:', end='\t')
            print(f'Opcode: {self.opcode}', end='\t')
            print(f'Tipo: {self.tipo}', end='  ')
            print(f'Funct: {self.funct}')

# ======================== FUNCTIONS ===============================

# Função para carregar uma Instrução de um arquivo texto para a memória principal
def ler_instrucao(file):
    # ler NOME
    linha_nome = file.readline()
    linha_nome = linha_nome.replace('Instrucao ', '')
    linha_nome = linha_nome.replace('\n', '')
    nome = linha_nome.upper()

    # ler OPCODE
    linha_opcode = file.readline()
    linha_opcode = linha_opcode.replace('Opcode: ', '')
    linha_opcode = linha_opcode.replace('\n', '')
    opcode = int(linha_opcode)

    # ler TIPO
    linha_tipo = file.readline()
    linha_tipo = linha_tipo.replace('Tipo: ', '')
    linha_tipo = linha_tipo.replace('\n', '')
    tipo = linha_tipo.upper()

    # ler FUNCT
    linha_funct = file.readline()
    linha_funct = linha_funct.replace('Funct: ', '')
    linha_funct = linha_funct.replace('\n', '')
    if linha_funct == 'None':
        funct = None
    else:
        funct = int(linha_funct)

    # PULAR LINHA EM BRANCO DE SEPARAÇÃO
    file.readline()

    return Instruction(nome, opcode, tipo, funct)


'''
def print_instruction_file(file_name):
    print(f'=================== ARQUIVO: {file_name} ===================')
    file = open(file_name, 'rb')
    file_size = os.path.getsize(file_name)
    for i in range(0, file_size, INSTRUCTION_SIZE):
        instruction = load_instruction_from_file(file)
        instruction.print_instruction()
    file.close()
'''
