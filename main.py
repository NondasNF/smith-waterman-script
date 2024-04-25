match = 3
missmatch = -1
gap = -2

def is_match(letra1, letra2):
    if letra1 == letra2:
        return match
    return missmatch

def smith_waterman(entrada1, entrada2):
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
            diagonal = valor_da_celula + is_match(letra_vertical, letra_horizontal)
            direita = tabela[tabela_linha][tabela_coluna-1] + gap
            cima = tabela[tabela_linha-1][tabela_coluna] + gap

            tabela[tabela_linha][tabela_coluna] = max(diagonal, direita, cima)

    return tabela

entrada1 = "ACGT"
entrada2 = "CGAT"
tabela = smith_waterman(entrada1, entrada2)

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

for index1 in range(len(entrada1)+1):
    for index2 in range(len(entrada2)+1):
        tabela2[index1+1][index2+1] = tabela[index1][index2]

for linha in tabela2:
    print(linha)
