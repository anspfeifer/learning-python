import re

lista_nomes = []

def cadastrar(lista_nomes):
    print('Digite nome do iten')
    nome = raw_input()
    lista_nomes.append(nome)


def busca_avancada(lista_nomes):
    print('Digite algo para buscar!')
    lista_nomes = 'Digite algo para buscar!'

    valor = raw_input()
    resultado = re.findall('([' + valor + ' ]\w+)', lista_nomes)

    print resultado

def menu():
    lista_nomes = []
    escolha = ''

    while (escolha != '0'):
        print "Escolha 1 = Cadastrar, 2 = Buscar"
        escolha = raw_input()

        if escolha == '1':
            cadastrar(lista_nomes)

        elif escolha == '2':
            busca_avancada(lista_nomes)
menu()
