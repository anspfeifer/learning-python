# -*- coding: UTF-8 -*-

def listar(lista_nomes):
    print 'Listando nomes:'
    for nome in lista_nomes:
        print nome

def cadastrar(lista_nomes):
    print('Digite seu nome:')
    nome = raw_input()
    lista_nomes.append(nome)

    print('Digite ano de nascimento:')
    ano_nascimento = int(raw_input())


def remover(nome, lista_nomes):

    if not lista_nomes:
        print('Nao tem nomes na lista')
    else:
        print('Digite o nome para remover:')
        nome = raw_input()

        if nome in lista_nomes:
            print('Deletando nome ' + nome)
            lista_nomes.remove(nome)
        else:
            print('O nome nao esta na lista!')


def alterar(nome, lista_nomes):
    print('Digite o nome que deseja alterar:')
    nome = raw_input()

    if nome not in lista_nomes:
        print('Nome nao esta na lista!')
    else:
        print('Digite o NOVO para ' + nome)
        novo_nome = raw_input()
        indice_nome = lista_nomes.index(nome)
        print('Removendo nome da lista!')
        lista_nomes[indice_nome] = novo_nome
        print('Voce alterou nome de ' + nome + 'para: ' + novo_nome)


def menu():
    lista_nomes = []
    escolha = ''
    nome = ''

    while (escolha != '0'):
        print "Escolha 1 = Cadastrar, 2 = Listar , 3 = Remover , 4 = Alterar ou 0 = Sair"
        escolha = raw_input()

        if escolha == '1':
            cadastrar(lista_nomes)

        elif escolha == '2':
            listar(lista_nomes)

        elif escolha == '3':
            remover(nome, lista_nomes)

        elif escolha == '4':
            alterar(nome, lista_nomes)

menu()
