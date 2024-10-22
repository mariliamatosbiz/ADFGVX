import sys

# Matriz da cifra ADFGVX (6x6), usando letras e dígitos
MATRIZ_ADFGVX = [
    ['A', 'B', 'C', 'D', 'E', 'F'],
    ['G', 'H', 'I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P', 'Q', 'R'],
    ['S', 'T', 'U', 'V', 'W', 'X'],
    ['Y', 'Z', '0', '1', '2', '3'],
    ['4', '5', '6', '7', '8', '9']
]

LETTERS = ['A', 'D', 'F', 'G', 'V', 'X']

CHAVE = "EXEMPLO"

def inverter_chave():
    return sorted(range(len(CHAVE)), key=lambda k: CHAVE[k])

def destranspor(texto):
    colunas = len(CHAVE)
    linhas = len(texto) // colunas
    sobra = len(texto) % colunas
    indices = inverter_chave()
    matriz = [''] * colunas

    posicao = 0
    for i, indice in enumerate(indices):
        num_linhas = linhas + 1 if i < sobra else linhas
        matriz[indice] = texto[posicao:posicao + num_linhas]
        posicao += num_linhas

    return ''.join(''.join(linha) for linha in zip(*matriz))

def reverter_substituicao(texto):
    resultado = ""
    i = 0
    while i < len(texto) - 1:
        if texto[i].isspace():
            resultado += " "
            i += 1
        else:
            linha = LETTERS.index(texto[i])
            coluna = LETTERS.index(texto[i + 1])
            resultado += MATRIZ_ADFGVX[linha][coluna]
            i += 2
    return resultado

def decifrar(entrada, saida):
    with open(entrada, 'r') as f:
        texto_cifrado = f.read().strip()

    if not texto_cifrado[-1].isdigit():
        raise ValueError("O texto cifrado não contém um padding válido.")

    padding = int(texto_cifrado[-1])
    texto_cifrado = texto_cifrado[:-1]

    if len(texto_cifrado) % 2 != 0:
        raise ValueError("O texto cifrado não tem um número par de caracteres após remoção do padding.")

    transposto = destranspor(texto_cifrado)

    if padding > 0:
        transposto = transposto[:-padding]

    texto_decifrado = reverter_substituicao(transposto)

    with open(saida, 'w') as f:
        f.write(texto_decifrado)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python decrypt.py <entrada> <saida>")
        sys.exit(1)

    entrada = sys.argv[1]
    saida = sys.argv[2]

    try:
        decifrar(entrada, saida)
        print("Decifração concluída com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)
