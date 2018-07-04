#!/usr/bin/python3

# parâmetro posicional
# def boas_vindas(nome,idade): 
#     # print('Olá {}'.format(nome))
#     print('Oi, sou o(a) {} e tenho {} anos'.format(nome,idade))
# boas_vindas('daniel', 24)  # daniel é um argumento
# boas_vindas('jose', 25)
# boas_vindas('maria', 43)    


# Parametros nomeados  
# def boas_vindas(nome,idade): 
#     print('Oi, sou o(a) {} e tenho {} anos'.format(nome,idade))
# boas_vindas(idade=24, nome='daniel')

# # parametro default
# def boas_vindas(idade=24, nome='daniel'): 
#     print('Oi, sou o(a) {} e tenho {} anos'.format(nome,idade))
# boas_vindas()


# palavra reservada return

# def boas_vindas(nome,idade=24): 
#     return('Oi, sou o(a) {} e tenho {} anos'.format(nome,idade))
# a= boas_vindas('daniel')
# print(a)

def somar(x,y):
    return x + y
b = somar(3,2)
somar(4,2)
somar(5,2)
print(b)
