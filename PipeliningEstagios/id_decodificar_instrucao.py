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
        nome_rs = linha_de_instrucao[1].lower()
        rs = banco_regs[nome_rs]

        pc_antigo = rs.valor - 1

        return [rs, pc_antigo]


def processar_instrucao_I(linha_de_instrucao, banco_regs, flags_no_arq, pc_atual):

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

    elif linha_de_instrucao[0] == 'BEQ':
        nome_rs = linha_de_instrucao[1].lower()
        rs = banco_regs[nome_rs]

        nome_rt = linha_de_instrucao[2].lower()
        rt = banco_regs[nome_rt]

        label = linha_de_instrucao[3]

        if rs.valor == rt.valor:
            # Desvia se igual
            label_linha = flags_no_arq[label] - 1
            return [rt, rs, label_linha]
        else:
            # Não desvia
            return [rt, rs, pc_atual]

    elif linha_de_instrucao[0] == 'BNE':
        nome_rs = linha_de_instrucao[1].lower()
        rs = banco_regs[nome_rs]

        nome_rt = linha_de_instrucao[2].lower()
        rt = banco_regs[nome_rt]

        label = linha_de_instrucao[3]

        if rs.valor != rt.valor:
            # Desvia se diferente
            label_linha = flags_no_arq[label] - 1
            return [rt, rs, label_linha]
        else:
            # Não desvia
            return [rt, rs, pc_atual]


def processar_instrucao_J(linha_de_instrucao, banco_regs, flags_no_arq, pc_atual):
    if linha_de_instrucao[0] == 'J':
        label = linha_de_instrucao[1]
        label_linha = flags_no_arq[label] - 1

        return [label_linha]

    elif linha_de_instrucao[0] == 'JAL':
        label = linha_de_instrucao[1]
        label_linha = flags_no_arq[label] - 1
        ra = banco_regs['$ra']
        return [ra, pc_atual, label_linha]


def pipe1_decodificar_instrucao(linha_de_instrucao, conj_de_instrucoes, banco_regs, flags_no_arq, pc_atual):

    nome_instrucao = linha_de_instrucao[0]
    instrucao = conj_de_instrucoes[nome_instrucao]
    # instrucao.print_instruction()

    if instrucao.tipo == 'R':
        linha_de_instrucao_processada = processar_instrucao_R(linha_de_instrucao, banco_regs)
        linha_de_instrucao_processada.insert(0, instrucao)
        linha_de_instrucao_processada.insert(0, linha_de_instrucao)

    elif instrucao.tipo == 'I':
        linha_de_instrucao_processada = processar_instrucao_I(linha_de_instrucao, banco_regs, flags_no_arq, pc_atual)
        linha_de_instrucao_processada.insert(0, instrucao)
        linha_de_instrucao_processada.insert(0, linha_de_instrucao)

    else:  # instrucao.tipo == 'J'
        linha_de_instrucao_processada = processar_instrucao_J(linha_de_instrucao, banco_regs, flags_no_arq, pc_atual)
        linha_de_instrucao_processada.insert(0, instrucao)
        linha_de_instrucao_processada.insert(0, linha_de_instrucao)

    return linha_de_instrucao_processada
