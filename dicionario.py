#!/usr/bin/python3


# sempre que vai buscar algo, é necessário buscar pela chave 

# pessoa = {}
# pessoa = {'nome':'daniel','email':'daniel@daniel'}
# pessoa['nome']
# 'daniel'

# pprint é uma biblioteca para organizar o dicionario e exibir um abaixo do outro
# from pprint import pprint
# pessoas = [
#     {'nome':'daniel', 'idade':24},
#     {'nome':'joao', 'idade':45},
#     {'nome':'maria', 'idade':45},
#     {'nome':'pedro', 'idade':20},
# ]
# # print(type(pessoas[0])) -- ver o tipo
# print(pessoas)

# pessoa.key() -- para exibir as chaves
# pessoa.value() -- exibir os valores das chaves
# pessoa.items() -- exibe as chaves e os valores separadamente
# list(pessoa.key()) -- exibe os valores

# pessoa = {'nome':'daniel','email':'daniel@daniel'}
# for x in pessoa.keys():
#     print(x)
# for x in pessoa.values():
#     print(x)

# pessoa = {'nome':'daniel','email':'daniel@daniel'}
# for x,y in pessoa.items(): # sempre quando for percorrer items é necessário 2 variáveis
#     print(x,y)

# pessoa = {'nome':'daniel','email':'daniel@daniel'}
# print(pessoa.get('idade', 0)) # get é para fazer uma busca dentro do dicionário
# print(pessoa.get('idade', 'nao achei'))
# print(pessoa.get('nome', 'nao achei'))

# pessoa = {'nome':'daniel','email':'daniel@daniel'}
# del pessoa['nome'] # --     deleta uma pessoa 
# print(pessoa)