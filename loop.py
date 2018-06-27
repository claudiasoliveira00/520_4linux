# !/usr/bin/python3

nomes = ['claudia','maria','joao', 'jose']
nomes = [nome.title() for nome in nomes]

nome = 'claudia'

print('sim' if nome == 'claudia' else 'nao')



# Lista de nome vazia
# ler nomes, adicionar na lista ate digitar sair
# mostrar a lista no final

# nomes = []
# while True:
#     nome = input('Digite um nome: ')
#     if nome.strip().lower() == 'sair':
#         break
#     nomes.append(nome)


# soma = 0
# while True:
#     num = int(input('Digite um numero ou 1 para sair'))
#     soma += num
#     if num == 1:
#         break
   
# print('total: {}'.format(soma))

# cont = 0
# while cont >= 10:
#     print('excuto')
#     cont += 1

