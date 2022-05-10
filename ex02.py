
# Forma 1
n=0
lista1 = []
contador = 0
while contador <= 5:
    n = int(input("Digite um número inteiro: "))
    if n <= 0:
        print("Digite novamente, digite um número inteiro.")
    else:
        lista1.append(n)
        contador += 1
print(lista1)

# Forma 2
n=0
lista2 = []
contador = 0
while contador <= 5:
    n = int(input("Digite um número inteiro: "))
    if n <= 0:
        print("Digite novamente, digite um número inteiro.")
    else:
        lista2.insert(contador,n)
        contador += 1
print(lista2)

# Forma 3
lista3 = [1,2,3,4,5,6]
print("[", end="")
for i,n in enumerate(lista3):
    if i == 5:
        print(lista3[i], end="")
    else:
        print(f"{lista3[i]}, ", end="")
        #print(n, end=" ") tb dá certo
print("]")

from random import randint

# Forma 4
lista4 = []
for i in range(0,6):
    lista4.append(randint(1,100))
print(lista4)
