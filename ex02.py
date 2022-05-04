# Forma 1
"""n=0
lista = []
contador = 0
while contador <= 5:
    n = int(input("Digite um número inteiro: "))
    if n <= 0:
        print("Digite novamente, digite um número inteiro.")
    else:
        lista.append(n)
        contador += 1

print(lista)"""

# Forma 2
"""n=0
lista = []
contador = 0
while contador <= 5:
    n = int(input("Digite um número inteiro: "))
    if n <= 0:
        print("Digite novamente, digite um número inteiro.")
    else:
        for i,v in enumerate(range(contador,contador)):
            lista[i] = n
            print(f"Lista[i] = {lista[i]}")
        contador += 1

print(lista)"""

# Forma 3
"""lista = [1,2,3,4,5,6]
print("[", end="")
for i,n in enumerate(lista):
    if i == 5:
        print(lista[i], end="")
    else:
        print(f"{lista[i]}, ", end="")
        #print(n, end=" ") tb dá certo
print("]")"""

# Forma 4
lista randomica