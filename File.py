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