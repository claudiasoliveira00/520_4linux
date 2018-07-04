#!/usr/bin/python3

# with open('nome.txt','r') as arquivo:
#     conteudo = arquivo.readlines()

# def ler_arquivo(nome):
#     with open(nome,'r') as arquivo:
#         conteudo = arquivo.readlines()
#         return conteudo


# variavel1 = ler_arquivo('frutas.txt')
# variavel2 = ler_arquivo('pessoas.txt')
# variavel3 = ler_arquivo('novo.txt')

# print(variavel1)
# print(variavel2)
# print(variavel3)


# def ler_arquivo(nome):
#     with open(nome,'r') as arquivo:
#         conteudo = arquivo.readlines()
#         return conteudo


# while True:
#     arq = input('Digite o nome do arquivo ou sair: ')
#     ir arq == 'sair':
#         break
#         print(ler_arquivo(arq)) # nesse caso vai digitar o nome do arquivo e se o arquivo existir vai abrir



def manipular_arquivo(nome, modo,conteudo=None):
    if modo == 'r':
        with open(nome, modo) as arquivo:        
            return arquivo.readlines()
    elif modo == 'a':
        with open(nome,modo) as arquivo:
            arquivo.write(conteudo)
            return True

a = manipular_arquivo('nomes.txt','r')
manipular_arquivo('nomes.txt','a','josevaldo')
print(a)
