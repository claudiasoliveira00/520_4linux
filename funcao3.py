#!/usr/bin/python3

# def boas_vindas(*nomes):
#     for item in nomes:
#         print('Olá {}. Seja bem vindo!'.format(item))# -- Exibe a msg para cada nome
#         # pass
#     # print(nomes)
#     # print(len(nomes))

# boas_vindas('daniel', 'rafael', 'lucia')

#args para lista

# def boas_vindas(*nomes): # * identifica que é infinito (*args) = (*nomes) Esse args é um parãmetro e pode ser inserido qualquer nome
#     for item in nomes:
#         pass
#     print(nomes)
#     print(len(nomes))
# boas_vindas('daniel', 'rafael', 'lucia') # Nesse caso o len se torna uma tupla


# kargs para dicionario
# def boas_vindas(**kargs): 
#     print('Olá {} {}. Seja bem vindo!'.format(kargs['nome'],kargs['sobrenome']))      
# boas_vindas(nome='daniel',sobrenome='prata')

def calcular_retorno(**frutas):       
        return frutas['preco'] * frutas['qtd']    


a = calcular_retorno(preco=5.0,qtd=50)
print(a)





