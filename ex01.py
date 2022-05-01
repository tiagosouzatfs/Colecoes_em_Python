
##### FAZENDO COM LISTA #########
print("Lista")
#Letra a)
A = [1, 0, 5, -2, -5, 7]
print(A)
print(type(A))

#Letra b)
#Forma 1
soma1 = A[0] + A[1] + A[5]
print(soma1)

#forma 2
soma2 = 0
for indice, valor in enumerate(A):
    if indice == 0 or indice == 1 or indice == 5:
        soma2 = soma2 + A[indice]
        #soma2 = soma2 + valor #tb da certo
print(soma2)

#Letra c) Posição 4 corresponde ao índice 3
for i, v in enumerate(A):
    if i == 3:
        A[i] = 100
print(A)

#Letra d)

for v in A:
    print(v, end="\n")


### FAZENDO COM TUPLA #####
print("Tupla")
#Letra a)
tupla = (1, 0, 5, -2, -5, 7)
print(tupla)
print(type(tupla))

#Letra b)
#Forma 1
soma3 = tupla[0] + tupla[1] + tupla[5] # acessa o elemento igual uma lista
print(soma3)

#Forma 2
soma4 = 0
for i, v in enumerate(tupla):
    if i == 0 or i == 1 or i == 5:
        soma4 = soma4 + v
        # soma4 = soma4 + tupla[i] # tb da certo
print(soma4)

#A letra c) não vai dá para fazer com tupla pq as tuplas são imutáveis e nessa questão ele pede para modificar a posição de número 4, aí não dá

#Letra d)
print(tupla)
for valor in tupla:
    print(valor, end='\n')


#### FAZENDO COM DICIONÁRIOS - MAPAS ########
print("Dicionário")
#Letra a)
dicionario = {"0":1, "1":0, "2":5, "3":-2, "4":-5, "5":7} #Utilizando o conceito de chave e valor
print(dicionario)
print(type(dicionario))

#Letra b)
#Forma 1
soma5 = dicionario["0"] + dicionario["1"] + dicionario["5"]
print(soma5)

#Forma 2
soma6 = 0
for chave in dicionario:    
    if chave == "0" or chave == "1" or chave == "5":
        soma6 = soma6 + (dicionario[chave])
print(soma6)

#Letra c)
#Forma1
dicionario["4"] = 100
print(dicionario)

#Forma2
dicionario = {"0":1, "1":0, "2":5, "3":-2, "4":-5, "5":7} #reutilizando para outra forma

for chave in dicionario:
    if chave == "4":
        dicionario[chave] = 100
print(dicionario)

#Letra d)

for chave in dicionario:
    print(f'Chave: {chave} e Valor: {dicionario[chave]}', end="\n")


#### FAZENDO COM CONJUNTOS - SETS ########
print("Conjuntos - set's")

#Letra a) não dá certo pois o conjunto não mantem a ordem ele tem sua própria forma de ordenação, veja na impressão abaixo.
s = {1, 0, 5, -2, -5, 7}
print(s)
print(type(s))

#Letra b) não dá certo, mas se precisar, para este caso vamos ter que mudar o conjunto como uma lista ou uma tuplo, pois 
# o conjunto não tem posições para acessar como numa tupla ou lista, ou com uma chave no caso de tupla, apesar de ser 
# iterável com o for, apenas para mostrar os valores do conjunto, exemplo:

for numero in s:
    print(numero)
# seria assim para o caso
lista1 = list(s) # transformar em lista
print(lista1)
tupla1 = tuple(s) # transformar em tupla
print(tupla1)
dicionario1 = {}.fromkeys([1, 0, 5, -2, -5, 7], 'dict') # transformar em dicionário
print(dicionario1) # aí vc pesquisa pela chave e não pelo valor, pq como não pode ter chave igual fica mais fácil assim.

#Letra c) não vai dá para fazer com set's pq os conjuntos são imutáveis e nessa questão ele pede para modificar a posição de número 4, aí não dá

#Letra d) 
for i in s:
    print(i)