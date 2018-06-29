#!/usr/bin/python3

# arquivo = open('frutas.txt','a')
# arquivo.write('Abacaxi''\n')
# arquivo.close

# with open('frutas.txt','a') as arquivo:
#     arquivo.write('laranja''\n')

# with open('teste.pdf','w') as arquivo:
# #     # --print(type(arquivo.read()))
#      arquivo.write('teste de pdf''\n')

# # readLines cria uma lista com os elementos. Dessa forma fica mais fácil manipular os dados
# with open('frutas.txt','r') as arquivo:#     
#     print(arquivo.readlines())


# with open('frutas.txt','r') as arquivo:
#     print(arquivo.readline())
#     print(arquivo.readline())
#     arquivo.seek(0) # --zerar o cursor
#     print(arquivo.readline()) # --apresenta a posição 0

# Abrir o arquivo, e ao lado do nome inserir uma numeração
# with open('frutas.txt','r') as arquivo:
#     var = arquivo.readlines()
# print(var)

with open('frutas.txt','r') as arquivo:
    var = arquivo.readlines()
alterado = []
cont = 1
for linha in var:
    alterado.append('{} - {}'.format(cont,linha))
    cont += 1
print(alterado)