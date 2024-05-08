match = 1
missmatch = -1
gap = -2

def get_formated_matriz(entrada1, entrada2, tabela):
    tabela2 = [[0] * (len(entrada1)+2) for _ in range(len(entrada2) + 2)]
    tabela2[0][0] = "  "
    tabela2[1][0] = "U"
    tabela2[0][1] = "U"

    for index in range(len(entrada1)):
        letra = entrada1[index]
        tabela2[0][index+2] = letra

    for index in range(len(entrada2)):
        letra = entrada2[index]
        tabela2[index+2][0] = letra
        

    for linha in range(len(entrada2)+1):
        for coluna in range(len(entrada1)+1):
            tabela2[linha+1][coluna+1] = tabela[linha][coluna]

    return tabela2

def is_match(letra1, letra2):
    if letra1 == letra2:
        return match
    return missmatch

def get_smith_waterman(entrada1, entrada2):
    coluna, linha = len(entrada1), len(entrada2)
    tabela = [[0] * (coluna+1) for _ in range(linha + 1)]
    tabela_linha = 0
    tabela_coluna = 0

    while tabela_coluna < coluna:
        tabela_coluna += 1
        tabela[0][tabela_coluna] = tabela[0][tabela_coluna-1] + gap

    while tabela_linha < linha:
        tabela_linha += 1
        tabela[tabela_linha][0] = tabela[tabela_linha-1][0] + gap

    tabela_linha = 0
    while tabela_linha < linha:
        tabela_linha += 1
        tabela_coluna = 0
        while tabela_coluna < coluna:
            tabela_coluna += 1
            valor_da_celula = tabela[tabela_linha-1][tabela_coluna-1]
            letra_vertical = entrada2[tabela_linha-1]
            letra_horizontal = entrada1[tabela_coluna-1]
            diagonal = valor_da_celula + is_match(letra_vertical, letra_horizontal)
            direita = tabela[tabela_linha][tabela_coluna-1] + gap
            cima = tabela[tabela_linha-1][tabela_coluna] + gap

            tabela[tabela_linha][tabela_coluna] = max(diagonal, direita, cima)

    return tabela

def get_backtrace(tabela, entrada1, entrada2):
    coluna, linha = len(entrada1), len(entrada2)
    aux_linha, aux_coluna = linha, coluna
    codon1 = ""
    codon2 = ""
    current_value = tabela[aux_linha][aux_coluna]
    while 1:
        if aux_coluna == 0 and aux_linha == 0: 
            break
        
        letra_horizontal = entrada2[aux_linha-1]
        letra_vertical = entrada1[aux_coluna-1]
        diagonal = tabela[aux_linha-1][aux_coluna-1] + is_match(letra_vertical, letra_horizontal)
        direita = tabela[aux_linha][aux_coluna-1] + gap
        cima = tabela[aux_linha-1][aux_coluna] + gap
        if current_value == diagonal:
            current_value = tabela[aux_linha-1][aux_coluna-1]
            codon1 = codon1 + letra_horizontal
            codon2 = codon2 + letra_vertical
            if aux_coluna > 0: aux_coluna -= 1
            if aux_linha > 0: aux_linha -= 1
        elif current_value == direita:
            current_value = tabela[aux_linha][aux_coluna-1]
            codon1 = codon1 + "-"
            codon2 = codon2 + letra_vertical
            if aux_coluna > 0: aux_coluna -= 1
        elif current_value == cima:
            current_value= tabela[aux_linha-1][aux_coluna]
            codon1 = codon1 + letra_horizontal
            codon2 = codon2 + "-"
            if aux_linha > 0: aux_linha -= 1

    return [codon1[::-1], codon2[::-1]]

entrada1 = "TCG"
entrada2 = "ATCG"
tabela = get_smith_waterman(entrada1, entrada2)
backtrace = get_backtrace(tabela, entrada1, entrada2)

tabela = get_formated_matriz(entrada1, entrada2, tabela)
for linha in tabela[::-1]:
    print(linha)

print(backtrace[0])
print(backtrace[1])
