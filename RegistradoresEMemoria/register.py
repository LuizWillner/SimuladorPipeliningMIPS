# ======================= IMPORTS ==============================

# ======================= CLASSES ==============================

# Classe Registrador
class Register:
    def __init__(self, id_num, nome, valor=0):
        self.id = id_num
        self.nome = nome
        self.valor = valor

    def print_register(self):
        print(f'Registrador {self.nome} ({self.id}):\t{self.valor}')

    def save_in_file(self, file):
        # SALVAR ID DO REGISTRADOR
        file.write('Registrador ')
        file.write(str(self.id) + '\n')

        # SALVAR NOME DO REGISTRADOR
        file.write('Nome: ')
        file.write(self.nome + '\n')

        # SALVAR VALOR ARMAZENADO NO REGISTRADOR
        file.write('Valor armazenado: ')
        file.write(str(self.valor) + '\n')

        # ESCREVER SEPARADOR
        file.write('\n')


# ======================== FUNCTIONS =============================

def ler_registrador(file):
    # LER ID DO REGISTRADOR
    linha_id = file.readline()
    linha_id = linha_id.replace('Registrador ', '')
    linha_id = linha_id.replace('\n', '')
    reg_id = int(linha_id)

    # LER NOME DO REGISTRADOR
    linha_nome = file.readline()
    linha_nome = linha_nome.replace('Nome: ', '')
    linha_nome = linha_nome.replace('\n', '')
    nome = linha_nome.lower()

    # LER VALOR ARMAZENADO NO REGISTRADOR
    linha_valor = file.readline()
    linha_valor = linha_valor.replace('Valor armazenado: ', '')
    linha_valor = linha_valor.replace('\n', '')
    valor = int(linha_valor)

    # PULAR LINHA EM BRANCO DE SEPARAÇÃO
    file.readline()

    return Register(reg_id, nome, valor)


'''
def print_register_file(file_name):
    print(f'=================== ARQUIVO: {file_name} ===================')
    file = open(file_name, 'rb')
    file_size = os.path.getsize(file_name)
    for i in range(0, file_size, REGISTER_SIZE):
        register = load_register_from_file(file)
        register.print_register()
    file.close()
'''