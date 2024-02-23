# Listas Tuplas e Dicionários são estruturas para armazenar informação. (existe uma quarta chamada set que caiu em desuso)
#
#
#Listas: mutáveis, indexadas e ordenadas, armazenam valores, delimitador []
#Tuplas: imutáveis, indexadas e ordenadas, armazenam valores, delimitador () 
#Dicionário: mutável, não ordenado e não indexado (a forma de acessar os elementos é pelas chaves), armazenam pares (chave-valor), delimitador {}
#
# Em comparativo de tamanho, as tuplas ocupam o menor espaço, pois não podem mudar, enquanto as listas que são mutáveis ocupam um espaço maior 
# de memória, e por fim o dicionário ocupa muito espaço pois ele tem uma estrutura pesada de chave e valor, sendo ainda mutáveis.

#Lista vazia

lista = []
lista = list()
print(lista)
Elemento = 2000

# A partir de outros objetos
lista1 = [1,2,3]
lista2 = ['a','b','c']
lista3 = ['a', 1,'b','Python',2]


# Ordenando uma lista

Lista_Ordenar = [34, 54, 23, 65, 3, 4, 64]
Lista_Ordenar.sort()
print(Lista_Ordenar)

# Inverter a ordem
Lista_Ordenar.sort(reverse=True)
print(Lista_Ordenar)

# Se for com string
Lista_Ordenar2 = ['a','B','C','d','1','z','b','á','+','cas','Cas']
Lista_Ordenar2.sort()
print(Lista_Ordenar2)

# Python não consegue ordenar listar de diferentes tipos, ele não entende string e número juntos na hora de ordenar
# Ex: Lista_Ordenar3 = ['a','d','c',1,'b']

Lista_Ordenar3 = [0,1,2,3,4,5,6,7,8,9]

# Cortar uma lista, primeiro número é o indice inicial (incluido), o segundo é o indice final (não incluido) // intervalo de indice
print(Lista_Ordenar3[3:6])

# Alterando elementos
Lista_Ordenar3[2] = 1000
print(Lista_Ordenar3)

# Adicionando com append
carros = ['Nissan', 'Ford', 'Volkswagen', 'Fiat']
carros.append('GM')
print(carros)

# Adicionando em posição específica
carros.insert(1, 'Renault')
print(carros)

# Formando lista com outras listas
Lista_Conjunta = [Lista_Ordenar, Lista_Ordenar2,Lista_Ordenar3,Elemento]
print(Lista_Conjunta)

# Concatenando Listas
Lista_Agregada = Lista_Ordenar + Lista_Ordenar2 + Lista_Ordenar3
print(Lista_Agregada)

# Removendo pelo Indice
removido = carros.pop(1)
print(carros)
print('Marca removida: ', removido)

removido = carros.pop() # pop vazio remove ultimo valor
print(carros)
print('Marca Removida: ', removido) 

# Iteração simples (percorrer de forma automática sem incrementar explicitamente)
for carro in carros:
    print(carro)

# Iteração com enumerate()
for index, carro in enumerate(carros):
    print('A marca na posição ', index, 'é', carro)

# Iteração sem variável de armazenamento
for _ in carros:
    print('Não sei dirigir')
