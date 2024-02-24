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


