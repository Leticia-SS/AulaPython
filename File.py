# Abrir arquivos em python
arq = open('Sinopse.txt','r') # r de read, ele não pode ser reescrito

for linha in arq:
    print(linha, end='')

# É necessário sempre fechar o arquivo para que não haja brechas de segurança
arq.close()


# Modo Escrita

arq = open('Sinopse.txt','w') # w de write

arq.write('Linha 1')

arq.close()


# Contando palavras

num_palavras = 0

for linha in arq:
    #print(linha)
    palavra = linha.split()
    #print(palavra)

    num_palavras = num_palavras + len(palavra)

arq.close()

# Palavras totais, para palavras unicas usar set() e use len()
print(f'Quantidade de palavras: {num_palavras}')


# Escrita em Arquivo

arq = open('arq_texto.txt', 'w')

# o comando write não introduz quebra de linha no fim do texto
arq.write('Linha 1')
arq.write('linha 2')
# Output = Linha1Linha2

arq.write('Linha 1\n')
arq.write('Linha 2\n')
arq.write('linha 3\n')
# Output = 
# Linha 1
# Linha 2
# Linha 3 

arq.close()

# Pegar informações da CPU e Memória do PC
import time, psutil

arq = open('log.txt', 'a')

for i in range(10):
    tempo_atual = time.ctime(time.time())
    uso_mem = '{:6.2f}'.format(psutil.virtual_memory().percent)
    uso_cpu = '{:6.2f}'.format(psutil.cpu_percent)
    texto = tempo_atual
    texto = texto + uso_mem + ' '
    texto = texto + uso_cpu + '\n'
    arq.write(texto)
    time.sleep(1)

arq.close()