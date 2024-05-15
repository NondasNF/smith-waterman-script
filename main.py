match = 1
missmatch = -1
gap = -2


def get_formated_matriz(entrada1, entrada2, tabela):
    tabela2 = [[0] * (len(entrada2) + 2) for _ in range(len(entrada1) + 2)]
    tabela2[0][0] = "  "
    tabela2[1][0] = "U"
    tabela2[0][1] = "U"

    for index in range(len(entrada1)):
        letra = entrada1[index]
        tabela2[index+2][0] = letra

    for index in range(len(entrada2)):
        letra = entrada2[index]
        tabela2[0][index+2] = letra

    for linha in range(len(entrada1)+1):
        for coluna in range(len(entrada2)+1):
            tabela2[linha+1][coluna+1] = tabela[linha][coluna]

    return tabela2

def get_match(letra1, letra2):
    if letra1 == letra2:
        return match
    return missmatch

def get_smith_waterman(entrada1, entrada2):
    linha, coluna = len(entrada1), len(entrada2)
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
            letra_vertical = entrada1[tabela_linha-1]
            letra_horizontal = entrada2[tabela_coluna-1]
            diagonal = valor_da_celula + get_match(letra_vertical, letra_horizontal)
            direita = tabela[tabela_linha][tabela_coluna-1] + gap
            cima = tabela[tabela_linha-1][tabela_coluna] + gap

            tabela[tabela_linha][tabela_coluna] = max(diagonal, direita, cima)

    return tabela

def get_backtrace(tabela, entrada1, entrada2):
    linha, coluna = len(entrada1), len(entrada2)
    aux_linha, aux_coluna = linha, coluna
    codon1 = ""
    codon2 = ""
    score = 0
    current_value = tabela[aux_linha][aux_coluna]
    while 1:
        if aux_coluna == 0 and aux_linha == 0: 
            break
        
        letra_horizontal = entrada1[aux_linha-1]
        letra_vertical = entrada2[aux_coluna-1]
        diagonal = tabela[aux_linha-1][aux_coluna-1] + get_match(letra_vertical, letra_horizontal)
        direita = tabela[aux_linha][aux_coluna-1] + gap
        cima = tabela[aux_linha-1][aux_coluna] + gap
        if current_value == diagonal:
            score += get_match(letra_vertical, letra_horizontal)
            current_value = tabela[aux_linha-1][aux_coluna-1]
            codon1 = codon1 + letra_horizontal
            codon2 = codon2 + letra_vertical
            if aux_coluna > 0: aux_coluna -= 1
            if aux_linha > 0: aux_linha -= 1
        elif current_value == direita:
            score += gap
            current_value = tabela[aux_linha][aux_coluna-1]
            codon1 = codon1 + "-"
            codon2 = codon2 + letra_vertical
            if aux_coluna > 0: aux_coluna -= 1
        elif current_value == cima:
            score += gap
            current_value= tabela[aux_linha-1][aux_coluna]
            codon1 = codon1 + letra_horizontal
            codon2 = codon2 + "-"
            if aux_linha > 0: aux_linha -= 1

    return [codon1[::-1], codon2[::-1]], score

entrada1= ""
entrada2= ""
with open('input.txt', 'r') as file:
    entrada1 = file.readline().strip()
    entrada2 = file.readline().strip()
    gap = file.readline().strip()
    missmatch = file.readline().strip()
    match = file.readline().strip()
    gap = int(gap)
    missmatch = int(missmatch)
    match = int(match)

tabela = get_smith_waterman(entrada1, entrada2)
backtrace, score = get_backtrace(tabela, entrada1, entrada2)
tabela = get_formated_matriz(entrada1, entrada2, tabela)

print("================================================================================")
for linha in tabela[::-1]:
    print(linha)
print("================================================================================")
print("------------------------------------------------------------------")
print("Alinhamento ** Score: ", score, "** Match: ", match, "** Missmatch: ", missmatch, "** Gap: ", gap)
print("------------------------------------------------------------------")

print(backtrace[0])
print(backtrace[1])
print("Número: 11")
print("Nome: Epaminondas Noronha Feitosa")
with open('input.txt', 'a') as file:
    file.write("================================================================================\n")
    for linha in tabela[::-1]:
        file.write(' '.join(map(str, linha)) + '\n')
    file.write("================================================================================\n")
    file.write("------------------------------------------------------------------\n")
    file.write("Alinhamento ** Score: " + str(score) + " ** Match: " + str(match) + " ** Missmatch: " + str(missmatch) + " ** Gap: " + str(gap) + "\n")
    file.write("------------------------------------------------------------------\n")
    file.write(backtrace[0] + "\n")
    file.write(backtrace[1] + "\n")
    file.write("Número: 12\n")
    file.write("Nome: Epaminondas Noronha Feitosa\n")
