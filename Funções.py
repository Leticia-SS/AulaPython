#
# A função sempre retorna algo, mesmo que seja NONE (nada)
#

# Criando função STUB e chamando ela
def funcao_Vazia():
    ...

funcao_Vazia()


# Função com argumentos
def soma(a,b):
    resultado = a + b
    return resultado

var = soma(1,2)
print(var)


# Em python, return não é obrigatório, mas sem o return a função abaixo retorna NONE
# Se as condições dos ifs não forem recebiad ele retorna nada
def nada(x):
    if x==2:
        return x
    elif x>2:
        return x+1

# Tem como criar argumentos pré definidos, mas devem ser no final da lista de argumentos
#
def multi_Arg(a, b=4,c=3):
    return a+b+c

#def multi_Arg(b=4, a, c=3) #Isso é um erro, pré definido na frente


# Podemos configurar funcções para aceitar um número quaquer de argumentos
# Para infinitos, usar *arg
# Para finitos, usar **kwargs
# Args sempre antes de Kwargs
def multiplos_Args(*args,**kwargs):
    print(args)
    print(kwargs)

multiplos_Args(1,2,3,name='Lara',name='JP', teste='op') #ele separa os numeros e o dicionário com as chaves


# Uma função retorna mais de um valor
# Em python você retorna mais de um objeto
def funcao_3(a,b=2,c=3):
    ret1 = a*b*c
    ret2 = a+b+c
    ret3 = (a/b)+c
    return ret1, ret2. ret3

var1, var2, var3 = funcao_3(10,20,30)
print(var1)
print(var2)
print(var3)


# Ao usar global você puxa as variáveis de dentro para fora da função

def funcao_Global():
    global a,b
    a = 1
    b = 2
    return a+b

def funcao_4():
    c = 3
    return a+c

