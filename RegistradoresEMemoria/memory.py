class Memory:
    def __init__(self, lenght):
        self.lenght = lenght
        self.values = [0] * lenght
        self.filled_values = dict({})

    def print_memory(self):
        print('############# MEMÓRIA #############')
        for key in self.filled_values:
            print(f'Memoria[{key}] = {hex(self.filled_values[key])}')
        print('###################################')

    def print_all_memory(self):
        print('######### MEMÓRIA COMPLETA #########')
        for i in range(self.lenght):
            print(f'Memoria[{i}] = {hex(self.values[i])}')
        print('###################################')
