palavras = ("python", "programação", "computador", "aprendizado", "inteligência", 
            "artificial", "linguagem", "algoritmo", "desenvolvimento", "web",
            "dados", "estrutura", "variável", "condicional", "iteração",
            "função", "lista", "dicionário", "tupla", "loop")
for p in palavras:
    print(f'\nNa palavra {p} temos ',end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')