"""_Summario_

Neste código está sendo feito uma Lista de Tarefas interativa, onde o usuário tem a escolha de: 
Adicionar, Listar, Verificar e Remover tarefas, tudo isso envolto de um loop com funções sendo 
chamadas para cada funcionalidade.

"""

# Bibliotecas usadas no documento
import time

# Inicializando a Lista de Tarefas
directory_Task = []

# Inicializando o loop do Menu de Tarefas
while True:
    
    print('\033[36m\n________________________________________\n\n\033[m')
    print('\033[36mLISTA DE TAREFAS\n\n1- Adicionar Tarefa\n2- Listar Tarefas\n3- Alterar Status\n4- Remover Tarefa\n5- Sair\033[m')

    # Input das escolhas disponíveis
    choice = input('\033[33m\nEscolha uma opção: \033[m')

    print('\033[36m\n________________________________________\n\n\033[m')

    # Função para adicionar Tarefa
    def add_Task():
        
        # Descrevendo a tarefa
        task = input('\033[33mDescreva a Tarefa: \033[m')
        
        # Verificando se foi escrito um número e retorna False
        if not task.isdigit():
            print('\n\n|Completa|Em Andamento|Pendente|')
            # Descrevendo o status da tarefa
            status = input('\033[33mDigite o Status: \033[m').lower()
            
            # Verificando se o status está de acordo com o que foi solicitado
            if status == 'completa' or status == 'em andamento' or status == 'pendente':
                
                # Adicionando um dicionário com Tarefa e Status á lista de tarefas
                directory_Task.append({'Tarefa': task, 'Status': status})
                print('\033[32m\nTarefa Adicionada\n\033[m')
            else:
                print('\033[31m\nInsira um status válido\n\033[m')
        else:
            print('\033[31m\nInsira uma tarefa válida\n\033[m')
            
    # Função para listar todas as tarefas
    def list_Task():
        
        # Verificando se lista está vazia
        if not directory_Task:
            print('\033[35m\nNão possuem tarefas na Lista\n\033[m')
        else:
            print('\033[33m\nLISTA DE TAREFAS\n\033[m')
            # Enumerando cada tarefa de acordo com a posição na lista, começando em 1
            for position, task in enumerate(directory_Task,1):
                print(f'\033[36m\n{position}- {task["Tarefa"]} | Status: {task["Status"]}\033[m')
    
    # Função para alterar o status
    def status_Task():
        
        # Verificando se lista está vazia
        if not directory_Task:
            print('\033[35m\nNão possuem tarefas na Lista\n\033[m')
        else:
            print('\033[33mALTERAR STATUS\n\033[m')
            list_Task()
            
            # Escolhendo tarefa para alterar status
            change_Status = input('\033[33m\nDigite o número da tarefa que deseja alterar: \033[m')
            
            # Verificando se foi digitado um valor
            if change_Status.isdigit():
                
                # Ajustando o valor para o valor real no index da Lista
                change_Status = int(change_Status) -1
                
                # Verificando se a tarefa está dentro da Lista
                if  len(directory_Task) > change_Status >= 0:
                    print('\n|Completa|EmAndamento|Pendente|')
                    
                    # Inserindo novo status
                    new_Status = input(f'\033[33mDigite o novo Status da tarefa: \033[m').lower()
                    
                    # Verificando se status é válido
                    if new_Status == 'completa' or new_Status == 'em andamento' or new_Status == 'pendente':
                        
                        # Alterando status dentro da lista
                        directory_Task[change_Status]['Status'] = new_Status
                        print('\033[32m\nStatus Atualizado\n\033[m')
                    else:
                        print('\033[31m\nDigite um status válido\n\033[m')
                else:
                    print('\033[31m\nNúmero da tarefa incorreto\n\033[m')
                        
            else:
                print('\033[31m\nDigite um número válido\n\033[m')
    
    # Função para remover tarefa
    def remove_Task():
        
        # Verificando se lista está vazia
        if not directory_Task:
            print('\033[35m\nNão possuem tarefas na Lista\n\033[m')
        else:
            print('\033[33m\nREMOVER TAREFA\n\033[m')
            list_Task()
            
            # Escolhendo tarefa para remover
            delete_Task = input('\033[33m\nDigite o número da tarefa que deseja excluir: \033[m')
            
            # Verificando se foi digitado um valor
            if delete_Task.isdigit():
                
                # Ajustando o valor para o valor real do index da Lista
                delete_Task = int(delete_Task) -1
                
                # Verificando se a tarefa está dentro da Lista
                if  len(directory_Task) > delete_Task >= 0:
                    
                    # Removendo a tarefa
                    del directory_Task[delete_Task]
                    print('\033[32m\nTarefa Excluída\n\033[m')
                else:
                    print('\033[31m\nNúmero da tarefa incorreto\n\033[m')
            else:
                print('\033[31m\nDigite um número válido\n\033[m')
                   
            
    # Escolhas do Menu que acionam as funções        
    match choice:
        case '1':
            add_Task()
        case '2':
            list_Task()
        case '3':
            status_Task()
        case '4':
            remove_Task()
        case '5':
            print('\033[36m\nFechando\n\033[m')
            time.sleep(1)
            for _ in range(3):
                print('\033[36m . \033[m', end='', flush=True)
                time.sleep(1)
            print('\033[36m\n\nAté logo\n\033[m')
            
            # Break para fechar o loop do Menu
            break
        
        # Case genérico para detectar se algum outra coisa foi escrita além do requerido
        case _ :
            print('\033[31m\nEscolha uma opção verídica\n\033[m')