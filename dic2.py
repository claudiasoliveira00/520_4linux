#!/usr/bin/python3

# Criar um dicionário de frutas e armazenar nome e valor


frutas = [
    {'fruta':'abacaxi', 'preco':4.5, 'qtd':10},
    {'fruta':'uva', 'preco':5.0, 'qtd':20},
    {'fruta':'maçã', 'preco':3.6, 'qtd':2},
    {'fruta':'kiwi', 'preco':2.8, 'qtd':4},
]

#soma = 0
for fruta in frutas:
    soma = fruta['preco'] * fruta['qtd']
    
print('total: {:.2f}'.format(soma)) # :. define as casas depois da vírgula
   

# frutas2 = []
# for fruta in frutas:
#     fruta['preco'] += fruta['preco'] * 0.1 # acrescenta 10% do valor. Se for pra retirar inseir -=
#     frutas2.append(fruta)
# print(frutas2)


