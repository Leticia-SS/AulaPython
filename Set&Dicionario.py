# Armazena uma coleção de itens exclusivos em uma única variável
# Não ordenado 
# Não indexado (parece uma tupla mas não é)
# Mutável (pode ser modificado para inteiro ou tupla)
# Iterável, podemos fazer loop nos itens do conjunto
#
# Set = {,,} // Dicionário = {"":"",}
#
# Embora Set seja mutável, seus itens devem ser dados imutáveis, exemplo: Inteiro, flutuante, tuplas ou strings.
#
# Principais aplicações: Remoção de duplicatas, verificação da associação ao conjunto, execução de operações ,atemáticas relacionadas diretamenta a conjuntos como união, interseção ou diferença


# Criando objeto tipo set
set1 = set([1,1,1,2,2,3,4,5,5]) #adicionando elementos da lista ao conjunto
set2 = set(('a','a','a','b','b','c')) #adicionando elementos da tupla
set3 = set('colab') #string

# Criando com chaves
set4 = {1,1,'colab','colab', 8.6, (1,2,3), None}

# set1 = {1,2,3}
# set2 = {'a','c','b'}
# set3 = {'l','o','b','a','c'} 
# set4 = {1, 8.6, (1, 2, 3), None, 'colab'}

set5 = {1,1,'colab','colab', 8.6, (1,2,3), None, [1,2,3], {1,2,3}}
# error: inhashable type: list, set (pois set é mutável e dentro de set só tem itens imutáveis)


# Só usar chaves não cria um set vazio e sim um dicionário
vazio1 = {}
vazio2 = set()

# Iniciando o conjunto
conjunto = set()

conjunto.add('a') # item imutável

conjunto.add({'b','c'}) # conjunto de itens 

conjunto.add('d','d','d') # lista de itens imutáveis

conjunto.add(['f'],['f']) # diversas listas imutáveis

# error: unhasgable type: list

# discard(): remove um item específico
# remove(): remove um item específico
# pop(): remove item aleatório item e salva na variável