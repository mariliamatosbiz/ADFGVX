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

# Defina a chave fixa
CHAVE = "EXEMPLO"

def encontrar_posicao(char):
    for i, linha in enumerate(MATRIZ_ADFGVX):
        if char in linha:
            return i, linha.index(char)
    raise ValueError(f"Caractere '{char}' não encontrado na matriz.")

def substituir(texto):
    resultado = ""
    for char in texto.upper():
        if char.isspace():
            resultado += " "
        elif char.isalnum():
            linha, coluna = encontrar_posicao(char)
            resultado += LETTERS[linha] + LETTERS[coluna]
    return resultado

def transpor(texto):
    colunas = sorted((CHAVE[i], i) for i in range(len(CHAVE)))
    texto_matriz = [texto[i:i + len(CHAVE)] for i in range(0, len(texto), len(CHAVE))]

    ultimo_tamanho = len(texto_matriz[-1])
    padding = len(CHAVE) - ultimo_tamanho
    if padding > 0:
        texto_matriz[-1] += 'X' * padding

    transposto = ""
    for _, indice in colunas:
        for linha in texto_matriz:
            if indice < len(linha):
                transposto += linha[indice]

    transposto += str(padding)  # Adicionar padding ao final
    return transposto

def cifrar(entrada, saida):
    with open(entrada, 'r') as f:
        texto_claro = f.read().strip()  # Remover espaços extras

    substituido = substituir(texto_claro)
    texto_cifrado = transpor(substituido)

    with open(saida, 'w') as f:
        f.write(texto_cifrado)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python encrypt.py <entrada> <saida>")
        sys.exit(1)

    entrada = sys.argv[1]
    saida = sys.argv[2]

    try:
        cifrar(entrada, saida)
        print("Cifragem concluída com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
        sys.exit(1)
