# -*- coding: UTF-8 -*-

def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome

def cadastrar(nomes):
    print('Digite seu nome:')
    nome = raw_input()
    nomes.append(nome)

    print('Digite ano de nascimento:')
    ano_nascimento = int(raw_input())


def menu():
    nomes = []
    escolha = ''

    while (escolha != '0'):
        print "Escolha 1 para cadastrar, 2 para listar  ou 0 para Sair"
        escolha = raw_input()

        if escolha == '1':
            cadastrar(nomes)

        if escolha == '2':
            listar(nomes)

menu()


