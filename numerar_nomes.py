#!/usr/bin/python3

# try:
#     with open('frutas.txt','r') as arquivo:
#         var = arquivo.readlines()
#     alterado = []
#     cont = 1
#     for linha in var:    
#         linha = linha.replace('\n','-{}\n'.format(cont)) # -- inserir no final da lista
#         alterado.append(linha)
#         # alterado.append('{} - {}'.format(cont,linha)) # -- inserir no começo da linha
#         cont += 1
#     with open('novo.txt','w') as arquivo:
#         for linha in alterado:
#             arquivo.write(linha)
# except FloatingPointError as e:
#     print('Arquivo não existe')

from time import sleep
while True:
    print('Ola! ')
    sleep(3) # --gera a cada 3 segundos
    


