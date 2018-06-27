#!/usr/bin/python3

'''
ler o numero e verificar se ele é par ou impar
e adicionar ele em uma lista com resultado

[2, 'par']
[3, 'impar']
'''

numero = float(input('Digite um número: '))
resultado = []
# resultado.append(numero)

if numero % 2 == 0:
    resultado.append('número é par')
else:
    resultado.append('número é ímpar')

