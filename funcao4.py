#!/usr/bin/python3

from random import choice, randint

# nomes =   ['daniel','maria','pedro','joao']
# a = randint(0,100) #  biblioteca randomica de númerooos
# print(choice(nomes),a) # choice é uma biblioteca randômica. Seleciona um item da lista

# função args que passa infinitas pessoas (args) e sorteia um valor e mostraaa no print

def pessoas_randon(*args):
    return choice(args)


## a = (randint(0,100))
b = pessoas_randon('claudia','daniel','camila')
## print(b,a)

with open('nomes.txt','r') as arq:
    pessoas = arq.readlines()
    print(choice(pessoas))