import sys

# Matriz da cifra ADFGVX (6x6), usando letras e digitos
MATRIZ_ADFGVX = [
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['G', 'H', 'I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P', 'Q', 'R'],
    ['S', 'T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z', '0', '1', '2', '3'],
    ['4', '5', '6', '7', '8', '9']
]

LETTERS = ['A', 'D', 'F', 'G', 'V', 'X']

def inverter_chave(chave):
    """Retorna a ordem original da transposicao com base na chave."""
    return sorted(range(len(chave)), key=lambda k: chave[k])

def destranspor(texto, chave):
    """Reverte a transposicao com base na chave."""
    colunas = len(chave)
    linhas = len(texto) // colunas

    # Verificar se a ultima linha esta incompleta
    sobra = len(texto) % colunas

    # Obter a ordem das colunas na transposicao
    indices = inverter_chave(chave)
    matriz = [''] * colunas

    posicao = 0
    for i, indice in enumerate(indices):
        # Distribuir os caracteres nas colunas, considerando a sobra
        num_linhas = linhas + 1 if i < sobra else linhas
        matriz[indice] = texto[posicao:posicao + num_linhas]
        posicao += num_linhas

    # Reconstruir o texto por leitura em ordem de linhas
    return ''.join(''.join(linha) for linha in zip(*matriz))

def encontrar_char(linha, coluna):
    """Encontra o caractere correspondente na matriz."""
    return MATRIZ_ADFGVX[linha][coluna]

def reverter_substituicao(texto):
    """Reverte a substituicao da matriz ADFGVX."""
    resultado = ""
    i = 0
    while i < len(texto) - 1:
        if texto[i].isspace():
            resultado += " "
            i += 1
        else:
            linha = LETTERS.index(texto[i])
            coluna = LETTERS.index(texto[i + 1])
            resultado += encontrar_char(linha, coluna)
            i += 2
    return resultado

def decifrar(entrada, saida, chave):
    with open(entrada, 'r') as f:
        texto_cifrado = f.read().strip()

    # Ler o numero de padding do final
    padding = int(texto_cifrado[-1])
    texto_cifrado = texto_cifrado[:-1]  # Remover o numero de padding

    # Verificar se o texto tem um numero par de caracteres
    if len(texto_cifrado) % 2 != 0:
        raise ValueError("O texto cifrado nao tem um numero par de caracteres.")

    # Desfazer a transposicao
    transposto = destranspor(texto_cifrado, chave)

    # Remover padding se for detectado corretamente
    if padding > 0:
        transposto = transposto[:-padding]

    # Reverter a substituicao usando a matriz ADFGVX
    texto_decifrado = reverter_substituicao(transposto)

    # # Debug: Verificar variaveis intermediarias
    # print(f"Texto cifrado (apos remover padding): {texto_cifrado}")
    # print(f"Texto transposto: {transposto}")
    # print(f"Texto decifrado (antes de remover padding): {texto_decifrado}")

    # Escrever a saida
    with open(saida, 'w') as f:
        f.write(texto_decifrado)


if __name__ == "__main__":
    entrada = sys.argv[1]
    saida = sys.argv[2]
    chave = sys.argv[3]
    decifrar(entrada, saida, chave)
