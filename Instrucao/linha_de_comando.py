
class LinhaDeComando:
    def __init__(self, comandoo_em_string, instrucao, rd=None, rs=None, rt=None, imediato=None, shamt=None):
        self.comando_em_string = comandoo_em_string
        self.instrucao = instrucao
        self.rd = rd
        self.rs = rs
        self.rt = rt
        self.imediato = imediato
        self.shamt = shamt
