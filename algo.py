supermercados = ["Carrefour", "Guanabara", "Mundial", "Prezunic"]
produtos = ["Arroz", "Feijão", "Açúcar", "Óleo", "Café"]

precos = [
    [5.10, 4.98, 5.00, 5.80, 23.12],
    [4.98, 4.89, 5.10, 6.22, 23.10],
    [5.02, 5.10, 4.98, 6.10, 23.04],
    [4.87, 4.90, 4.80, 5.98, 23.11]
]

def somas():
    resultado = []
    for i in range(len(supermercados)):
        total = 0
        for j in range(len(produtos)):
            total += precos[i][j]
        resultado.append(total)
    return resultado

def medias():
    lista = []
    for j in range(len(produtos)):
        soma = 0
        for i in range(len(supermercados)):
            soma += precos[i][j]
        lista.append(soma / len(supermercados))
    return lista

def menor(s):
    m = s[0]
    idx = 0
    for i in range(1, len(s)):
        if s[i] < m:
            m = s[i]
            idx = i
    return m, supermercados[idx]

def tabela(s, m):
    print("Supermercado    ", end="")
    for p in produtos:
        print(f"{p:<8}", end="")
    print("Soma")
    for i in range(len(supermercados)):
        print(f"{supermercados[i]:<14}", end="")
        for j in range(len(produtos)):
            print(f"{precos[i][j]:<8.2f}", end="")
        print(f"{s[i]:.2f}")
    print("Média           ", end="")
    for j in range(len(m)):
        print(f"{m[j]:<8.2f}", end="")
    print()

s = somas()
m = medias()
tabela(s, m)
menor_valor, mercado = menor(s)
print(f"\nMenor valor da cesta: R$ {menor_valor:.2f} ({mercado})")
