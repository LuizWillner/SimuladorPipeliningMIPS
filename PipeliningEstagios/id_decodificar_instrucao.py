# ======================== FUNCTIONS =============================

def processar_instrucao_R(linha_de_instrucao, banco_regs):

    if linha_de_instrucao[0] == 'ADD' or linha_de_instrucao[0] == 'AND' or linha_de_instrucao[0] == 'OR' or linha_de_instrucao[0] == 'SUB':
        nome_rd = linha_de_instrucao[1].lower()
        rd = banco_regs[nome_rd]
        # rd.print_register()

        nome_rs = linha_de_instrucao[2].lower()
        rs = banco_regs[nome_rs].valor
        # rs.print_register()

        nome_rt = linha_de_instrucao[3].lower()
        rt = banco_regs[nome_rt].valor
        # rt.print_register()

        return [rd, rs, rt]

    elif linha_de_instrucao[0] == 'SLL' or linha_de_instrucao[0] == 'SRL':
        nome_rd = linha_de_instrucao[1].lower()
        rd = banco_regs[nome_rd]

        nome_rs = linha_de_instrucao[2].lower()
        rs = banco_regs[nome_rs].valor

        shamt = linha_de_instrucao[3]
        shamt = int(shamt)

        return [rd, rs, shamt]

    elif linha_de_instrucao[0] == 'JR':
        # TODO: Verificar se tá certo
        nome_rs = linha_de_instrucao[1].lower()
        rs = banco_regs[nome_rs]

        return [rs]


def processar_instrucao_I(linha_de_instrucao, banco_regs, flags_no_arq):

    if linha_de_instrucao[0] == 'ADDI':
        nome_rt = linha_de_instrucao[1].lower()
        rt = banco_regs[nome_rt]

        nome_rs = linha_de_instrucao[2].lower()
        rs = banco_regs[nome_rs].valor

        imediato = linha_de_instrucao[3].lower()
        imediato = int(imediato)

        return [rt, rs, imediato]

    elif linha_de_instrucao[0] == 'LW':
        nome_rt = linha_de_instrucao[1].lower()
        rt = banco_regs[nome_rt]

        nome_rs = linha_de_instrucao[3].lower()
        rs = banco_regs[nome_rs].valor

        imediato = linha_de_instrucao[2]
        imediato = int(imediato)

        return [rt, rs, imediato]

    elif linha_de_instrucao[0] == 'SW':
        nome_rt = linha_de_instrucao[1].lower()
        rt = banco_regs[nome_rt].valor

        nome_rs = linha_de_instrucao[3].lower()
        rs = banco_regs[nome_rs].valor

        imediato = linha_de_instrucao[2]
        imediato = int(imediato)

        return [rt, rs, imediato]

    elif linha_de_instrucao[0] == 'BEQ' or linha_de_instrucao[0] == 'BNE':
        # TODO: Verificar se tá certo
        nome_rs = linha_de_instrucao[1].lower()
        rs = banco_regs[nome_rs]

        nome_rt = linha_de_instrucao[1].lower()
        rt = banco_regs[nome_rt]

        label = linha_de_instrucao[3]
        label_linha = flags_no_arq[label]

        return [rs, rt, label_linha]


def processar_instrucao_J(linha_de_instrucao, flags_no_arq):
    # TODO: Verificar se tá certo
    if linha_de_instrucao[0] == 'J' or linha_de_instrucao[0] == 'JAL':
        label = linha_de_instrucao[1]
        label_linha = flags_no_arq[label]

        return [label_linha]


def pipe1_decodificar_instrucao(linha_de_instrucao, conj_de_instrucoes, banco_regs, flags_no_arq):

    nome_instrucao = linha_de_instrucao[0]
    instrucao = conj_de_instrucoes[nome_instrucao]
    # instrucao.print_instruction()

    if instrucao.tipo == 'R':
        linha_de_instrucao_processada = processar_instrucao_R(linha_de_instrucao, banco_regs)
        linha_de_instrucao_processada.insert(0, instrucao)

    elif instrucao.tipo == 'I':
        linha_de_instrucao_processada = processar_instrucao_I(linha_de_instrucao, banco_regs, flags_no_arq)
        linha_de_instrucao_processada.insert(0, instrucao)

    else:  # instrucao.tipo == 'J'
        linha_de_instrucao_processada = processar_instrucao_J(linha_de_instrucao, flags_no_arq)
        linha_de_instrucao_processada.insert(0, instrucao)

    return linha_de_instrucao_processada
