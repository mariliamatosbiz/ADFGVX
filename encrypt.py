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

def encontrar_posicao(char):
    """Retorna a posicao da letra na matriz."""
    for i, linha in enumerate(MATRIZ_ADFGVX):
        if char in linha:
            return i, linha.index(char)
    raise ValueError(f"Caractere '{char}' nao encontrado na matriz.")

def substituir(texto):
    """Realiza a substituicao usando a matriz ADFGVX."""
    resultado = ""
    for char in texto.upper():
        if char.isspace():  # Preservar espacos
            resultado += " "
        elif char.isalnum():
            linha, coluna = encontrar_posicao(char)
            resultado += LETTERS[linha] + LETTERS[coluna]
    return resultado

def transpor(texto, chave):
    """Realiza a transposicao das colunas com base na chave."""
    colunas = sorted((chave[i], i) for i in range(len(chave)))
    texto_matriz = [texto[i:i + len(chave)] for i in range(0, len(texto), len(chave))]

    # Preencher a ultima linha, se necessario
    ultimo_tamanho = len(texto_matriz[-1])
    padding = len(chave) - ultimo_tamanho
    if padding > 0:
        texto_matriz[-1] += 'X' * padding  # 'X' como caractere de preenchimento

    # Transpor as colunas
    transposto = ""
    for _, indice in colunas:
        for linha in texto_matriz:
            if indice < len(linha):
                transposto += linha[indice]

    # Adiciona o numero de caracteres de padding ao final
    transposto += str(padding)
    return transposto

def cifrar(entrada, saida, chave):
    with open(entrada, 'r') as f:
        texto_claro = f.read()

    substituido = substituir(texto_claro)
    texto_cifrado = transpor(substituido, chave)

    with open(saida, 'w') as f:
        f.write(texto_cifrado)

if __name__ == "__main__":
    entrada = sys.argv[1]
    saida = sys.argv[2]
    chave = sys.argv[3]
    cifrar(entrada, saida, chave)
