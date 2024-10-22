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

def inverter_chave(chave):
    """Retorna a ordem original da transposição com base na chave."""
    return sorted(range(len(chave)), key=lambda k: chave[k])

def destranspor(texto, chave):
    """Reverte a transposição com base na chave."""
    colunas = len(chave)
    linhas = len(texto) // colunas

    sobra = len(texto) % colunas

    indices = inverter_chave(chave)
    matriz = [''] * colunas

    posicao = 0
    for i, indice in enumerate(indices):
        num_linhas = linhas + 1 if i < sobra else linhas
        matriz[indice] = texto[posicao:posicao + num_linhas]
        posicao += num_linhas

    return ''.join(''.join(linha) for linha in zip(*matriz))

def encontrar_char(linha, coluna):
    """Encontra o caractere correspondente na matriz."""
    return MATRIZ_ADFGVX[linha][coluna]

def reverter_substituicao(texto):
    """Reverte a substituição da matriz ADFGVX."""
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

    # Verificar se o último caractere é número (padding)
    if not texto_cifrado[-1].isdigit():
        raise ValueError("O texto cifrado não contém um padding válido.")
    
    padding = int(texto_cifrado[-1])
    texto_cifrado = texto_cifrado[:-1]

    if len(texto_cifrado) % 2 != 0:
        raise ValueError("O texto cifrado não tem um número par de caracteres após remoção do padding.")

    transposto = destranspor(texto_cifrado, chave)

    if padding > 0:
        transposto = transposto[:-padding]

    texto_decifrado = reverter_substituicao(transposto)

    with open(saida, 'w') as f:
        f.write(texto_decifrado)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Uso: python decrypt.py <entrada> <saida> <chave>")
        sys.exit(1)

    entrada = sys.argv[1]
    saida = sys.argv[2]
    chave = sys.argv[3]

    try:
        decifrar(entrada, saida, chave)
        print("Decifração concluída com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)
