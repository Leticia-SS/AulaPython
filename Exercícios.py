#
#

num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

print(f' \n Soma: {sum:.0f} \n Subtração: {sub:.0f} \n Multiplicação: {mult:.0f} \n Divisão: {round(div,2)} \n')

#
#

numMin = float(input('Insira uma quantidade de minutos para ser convertida: '))

hora = numMin / 60
min = numMin % 60

print(f'\n Conversão para Horas:{hora:.0f}:{min:.0f}h\n')

numHora = float(input('Insira uma quantidade de horas para ser convertida: '))

min = numHora * 60

print(f'\n Conversão para Minutos:{min:.0f} min')

#
#

import random

name1 = input('Digite um nome:')
name2 = input('Digite outro nome:')

listNames = list(name1 + name2)

random.shuffle(listNames)

mixedNames = ''.join(listNames).lower()

print(f'Novo nome: {mixedNames}')

#
#

n1 = float(input('\nPrimeiro valor: '))
n2 = float(input('Segundo valor: '))
choice = int(input('\nEscolha uma operação: \n1=Soma \n2=Subtração \n3=Multiplicação \n4=Divisão\n'))

sum = n1 + n2
subt = n1 - n2
div = n1 / n2
mult = n1 * n2

if choice==1:
  print(f'\n={sum:.0f}')
elif choice==2:
  print(f'\n={subt:.0f}')
elif choice==3:
  print(f'\n={mult:.0f}')
elif choice==4:
  print(f'\n={div:.2f}')
else:
  print('\nOperação inválida ... tente outra opção..')

#
#

import random

nome = list(input('Digite seu nome:'))
sobrenome = list(input('\nDigite seu sobrenome:'))

random.shuffle(nome)
random.shuffle(sobrenome)

novoNome = ''.join(nome)
novoSobrenome = ''.join(sobrenome)

print(f'Saudações {novoNome} {novoSobrenome}')

#
#

import random

numberRandom = random.randint(0,100)
guess = int(input('Escolha um número entre 0 e 100: '))

if numberRandom == guess:
  print(f'Você acertou, número sorteado foi {numberRandom}')
elif numberRandom > guess:
  print(f'Hm, o palpite foi muito baixo, o sorteado da vez foi {numberRandom}')
else:
  print(f'Ohf, essa passou longe, muito alto, o sorteado foi {numberRandom}')

#
#
  
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

IMC = peso / (altura**2)

if IMC <= 18.5:
  print(f'Abaixo do peso, IMC = {IMC:.2f}')
elif IMC > 18.5 and IMC <= 24.9:
  print(f'Peso normal, IMC = {IMC:.2f}')
elif IMC > 24.9 and IMC <=29.9:
  print(f'Sobrepeso, IMC = {IMC:.2f}')
elif IMC > 29.9 and IMC <=34.9:
  print(f'Obesidade I, IMC = {IMC:.2f}')
elif IMC > 34.9 and IMC <=40:
  print(f'Obesidade II, IMC = {IMC:.2f}')
else:
  print(f'Obesidade III, IMC = {IMC:.2f}')

#
#

idade = int(input('Digite sua idade: '))

if idade >= 18:
  print('Maior de idade')
else:
  print('Menor de idade')

#
#

value = float(input('Digite o valor da compra: '))

if value < 100:
  discount = value * 0.95
  print(f'\nValor com desconto de 5% aplicado \nTotal: {discount:.2f}')
elif value >= 100 and value < 200:
  discount = value * 0.9
  print(f'\nValor com desconto de 10% aplicado \nTotal: {discount:.2f}')
elif value >= 200 and value < 300:
  discount = value * 0.8
  print(f'\nValor com desconto de 20% aplicado \nTotal: {discount:.2f}')
else:
  discount = value * 0.7
  print(f'\nValor com desconto de 30% aplicado \nTotal: {discount:.2f}')

#
#

import random

acoes = ['correndo','nadando','saltando','pulando','andando','jogando','dirigindo','vigiando','cortando','acariciando']
objetos = ['uma folha','uma panela','um cachorro','uma lampada','um videogame','um carro','um copo','um gato','um celular']
lugares = ['na praia','na rua','na praça','na piscina','na cozinha','no quarto','na floresta','no parque','no vizinho','na árvore'] 
pessoas = ['O menino','A menina','O idoso','O cachorro','A arara','O gato','O fantasma']

pessoa = random.sample(pessoas, k=1)
acao = random.sample(acoes, k=1)
lugar = random.sample(lugares, k=1)
objeto = random.sample(objetos, k=1)

print(f'{pessoa} {acao} {lugar} com {objeto}')

#
#

import random

dados = int(input('Digite a quantidade de dados a ser lançada: '))
lados = int(input('Digite a quantidade de lados do dado: '))

for _ in range(dados):
  print(random.randint(0,lados))

#
#
  
palavra = input('Digite uma palavra: ')

if len(palavra) <5:
  print('Palavra muito curta')
else:
  print('Palavra muito longa')

#
#

palavra = input('Insira uma palavraa qualquer: ')

reverso = list(palavra)
reverso.reverse()

reverso = ''.join(reverso)

if palavra == reverso:
  print('A palavra é um palíndromo')
else:
  print('A palavra não é um palíndromo')


# 
# Ímpares
  
for n in range(50):
  if n%2 != 0:
    print(n)


#
#

paisA = 80000
paisB = 200000
ano = 0

while paisA <= paisB:
  paisA = paisA*1.03
  paisB = paisB*1.015

  ano += 1

print(ano)


#
#

num = input('Digite números separados por vírgula: ').split(',')
print(num)


#
#

numLista = []
for _ in range(10):
  num = int(input('Digite um número: '))
  numLista.append(num)

for index,numero in enumerate(numLista):
  num = numero**2
  numLista[index] = num

soma = sum(numLista)
print(soma)


#
#

number = int(input('Insira um número inteiro: '))

def calculo(x):
  quadrado = x**2
  raiz = x**(1/2)
  return quadrado, raiz

quadrado, raiz = calculo(number)

print(f'\nNúmero: {number} \nQuadrado: {quadrado} \nRaíz: {raiz}')


#
#

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

def calculo(x,y):
  sum = x+y
  sub = x-y
  mult = x*y
  div = x/y
  rest = x%y

  return sum,sub,mult,div,rest

sum,sub,mult,div,rest = calculo(num1,num2)

print(f'\nSoma: {sum}\nSubtração: {sub}\nMultiplicação: {mult}\nDivisão: {div:.0f} com resto {rest}')


#
#

def inclui_imposto(custo, taxa = 5):
  total = custo + (custo*(taxa/100))
  return total

custo = int(input('Digite o custo do item: '))
taxa = int(input('Digite a taxa em % (caso não possua, digite 0): '))

if taxa == 0:
  print(f'Valor do item: {inclui_imposto(custo)}')
else:
  print(f'Valor do item: {inclui_imposto(custo,taxa)}')


#
# Docstring função anterior

""" Função para calcular o custo com taxa com valor já definido de taxa"""
def inclui_imposto(custo, taxa = 5):
  """ total do item, usando a taxa em porcentagem e dividindo por 100 """
  total = custo + (custo*(taxa/100))
  return total

""" Requerindo ao usuário um valor de custo e taxa """
custo = int(input('Digite o custo do item: '))
taxa = int(input('Digite a taxa em % (caso não possua, digite 0): '))

""" Se a taxa for 0 ela será sempre 5% portanto seu valor já é inputado na função """
if taxa == 0:
  print(f'Valor do item: {inclui_imposto(custo)}')
else:
  """ Se houver taxa, ela será substituida e calculada na função """
  print(f'Valor do item: {inclui_imposto(custo,taxa)}')


#
#

nome = list(input('Digite seu nome: ').upper())
reverso = ''.join(reversed(nome))

print(reverso)


#
# Formatar data sem biblioteca

data = (input('Insira a data no formato 00/00/0000: ')).split("/")

if len(data)==3:
  day = data[0]
  month = data[1]
  year = data[2]

  if len(day) == 2 and len(month) == 2 and len(year)==4:
    if day.isdigit()==True and month.isdigit()==True and year.isdigit()==True:

      day = int(day)
      month = int(month)
      year = int(year)

      def date(mes,dia=day,ano=year):
        print(f'{dia} de {mes} de {ano}')

      if 0<day<=31 and 0<month<=12:
        match month:
          case 1:
            date('Janeiro')
          case 2:
            date('Fevereiro')
          case 3:
            date('Março')
          case 4:
            date('Abril')
          case 5:
            date('Maio')
          case 6:
            date('Junho')
          case 7:
            date('Julho')
          case 8:
            date('Agosto')
          case 9:
            date('Setembro')
          case 10:
            date('Outubro')
          case 11:
            date('Novembro')
          case 12:
            date('Dezembro')
          
      else:
        print('Dia ou mês inválido')
    else:
      print('Insira somente Números')
  else:
    print('Dados Inválidos')
else:
  print('Formato Incorreto')


#
#
  
string1 = input('Digite uma palavra: ')
string2 = input('Digite outra palavra: ')

def validar(x):
  string = x.strip()

  return string, len(string)

string1, largura1 = validar(string1)
string2, largura2 = validar(string2)

if string1 == string2:
  print(f'Primeira e Segunda palavras são iguais e a largura delas é: {largura1}')
else:
  print(f'A Primeira e Segunda palavra são diferentes, a primeira tem comprimento: {largura1}, e a segunda comprimento: {largura2}')

#
#
  
frase = list(input('Digite uma frase: ').lower())

def contador():
  branco = frase.count(' ')
  A = frase.count('a')
  E = frase.count('e')
  I = frase.count('i')
  O = frase.count('o')
  U =  frase.count('u')

  vogSum = A + E + I + O + U

  print(f'Espaços em branco: {branco}\nVogais: {vogSum}')

contador()

#
#

num1 = float(input('Insira o primeiro valor: '))
num2 = float(input('Insira o segundo valor: '))

def Calculos(x,y):
  sum = f'{x} + {y} = {(x)+(y)}'
  sub = f'{x} - {y} = {(x)-(y)}'
  mult = f'{x} - {y} = {((x)*(y)):.02f}'
  if x==0:
    div = f'{x} / {y} = 0'
    divInt = f'{x} // {y} = 0'
    rest = f'{x} % {y} = 0'
  elif y==0:
    div = 'Proibido Divisão por 0'
    divInt = 'Proibido Divisão por 0'
    rest = 'Proibida Divisão por 0'
  else:
    div = f'{x} / {y} = {(x)/(y)}'
    divInt = f'{x} // {y} = {(x)//(y)}'
    rest = f'{x} % {y} = {(x)%(y)}'

  return sum, sub, mult, div, divInt, rest

soma, subtr, multp, divi, diviInt, resto = Calculos(num1,num2)

operacao = int(input('Escolha uma das operações digitando o número correspondente:\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Divisão Inteira\n6 - Resto da Divisão\n Número:  '))

match(operacao):
  case 1:
    print(soma)
  case 2:
    print(subtr)
  case 3:
    print(multp)
  case 4:
    print(divi)
  case 5:
    print(diviInt)
  case 6:
    print(resto)
  case _:
    print('Escolha uma operação válida')

#
#
  
salary = float(input('Digite o seu salário: '))

def newSalary(value):
  if value <= 1500:
    value = value * 1.2
    percentage = '20%'
    return value,percentage
  elif 1500 < value <= 2000:
    value = value * 1.15
    percentage = '15%'
    return value,percentage
  else:
    value = value * 1.05
    percentage = '5%'
    return value,percentage

newSalary, percentage = newSalary(salary)

print(f'\nSalário antes do reajuste: R${salary:.02f}\nPercentual de aumento: {percentage}\nAumento: R${(newSalary - salary):.02f}\nSalário com reajuste: R${(newSalary):.02f}')


#
#

numero=1
lista = []

while numero<=10:
  multp = 3 * numero
  lista.append(multp)
  numero += 1

print(lista)
for num in lista:
      print(f'3 x {num} = {num*3}')

#
#
      
import random
inicio = input('\n----------------------------------\n       BEM-VINDO AO CRAPS\n\nAperte qualquer tecla para lançar os dados\n       ')
dados=[random.randint(1,6) for _ in range(2)]

def jogarDado(qnt=2,faces=6):
  dados=[random.randint(1,faces) for _ in range(qnt)]
  return sum(dados)

dado = jogarDado()

match dado:
  case 7 | 11:
    print(f'\n----------------------------------\n\nSOMA DOS DADOS: {dado}\n\n--------NATURAL POINT--------\n\n----------GAME WON----------')
  case 2 | 3 | 12:
    print(f'\n----------------------------------\n\nSOMA DOS DADOS: {dado}\n\n------------CRAPS------------\n\n----------GAME OVER----------')
  case 4 | 5 | 6 | 8 | 9 | 10:
    print(f'PONTUAÇÃO: {dado}')
    confirm = int(input(f'\n----------------------------------\n\nUUHFF QUASE LÁ, MAS AINDA TEM CHANCE\n\n     DESEJA CONTINUAR ? ? ? \n\nSEU PONTO ATUAL: {dado}\n\nPara ganhar deverá igualar soma dos dados a sua pontuação,\nBasta escolher a quantidade de dados a ser lançada\n e o número de faces, variando entre 3 a 12 ! ! !\n\n1- CONTINUAR\n2- SAIR\n\n= '))
    ponto = dado
    while confirm != 2:
      quant = int(input('\nQuantidade de dados: '))
      lados = int(input('Quantidade de lados: '))

      novoDado = jogarDado(quant,lados)

      match novoDado:
        case 7:
          print(f'\n----------------------------------\n\nPONTO: {ponto}\nPONTUAÇÃO ATUAL: {novoDado}\n\n----------GAME OVER----------')
          break
        case _:
          if ponto == novoDado:
            print(f'\n----------------------------------\n\nPONTO: {ponto}\nPONTUAÇÃO ATUAL: {novoDado}\n\n----------GAME WON----------')
            break
      confirm = int(input(f'\n----------------------------------\n\n     DESEJA CONTINUAR ? ? ? \n\nPONTO: {ponto}\nPONTUAÇÃO ATUAL: {novoDado}\n\n1- CONTINUAR\n2- SAIR\n\n= '))
      print('\n\nBasta escolher a quantidade de dados a ser lançada\n e o número de faces, variando entre 3 a 12 ! ! !\n')


#
#

frase = input('Digite uma palavra ou frase para verificar se é um palindromo: ')

def palindromo(value):
  normal = value
  inverso = ''.join(reversed(value))
  if (normal.replace(' ','')).upper()==(inverso.replace(' ','')).upper():
    print(f'\nÉ um Palíndromo\n\nNormal: {normal}\nInvertido: {inverso}')
  else:
    print(f'\nNÃO é um Palíndromo\n\nNormal: {normal}\nInvertido: {inverso}')

palindromo(frase)

#
#

notas = []
nota = float(input('Insira as notas para o registro (digite -1 para sair)\n== '))
while nota!= -1:
  notas.append(nota)
  nota = float(input('== '))

print(f'\nForam registradas {len(notas)} notas\n')

for indx,n in enumerate(notas):
  print(f'{n}', end=' | ')
  print(f'\n\n' if indx == (len(notas)-1) else '', end='')

for n in notas[::-1]:
  print(f'{n}')

media = sum(notas)/len(notas)

print(f'\nSoma total: {sum(notas):.0f}\n')
print(f'Média: {media:.02f}\n')

acima = [x for x in notas if x>=media]
print(f'Notas acima ou na média: {len(acima)}\n')
abaixo = [x for x in notas if x<media]
print(f'Notas abaixo da média: {len(abaixo)}\n')


#
#

cubo = [(x+1)**3 for x in range(10)]
for c in cubo:
  print(f'{c}', end=' | ')
     
