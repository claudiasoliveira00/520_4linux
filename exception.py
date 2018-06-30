#!/usr/bin/python3
# while True:
#     try:
#         num = int(input('Digite um número: '))
#         print(num)
#         break
#     except ValueError as e:
#         print('Não é um inteiro: {}'.format(e))

# while True:
#     try:
#         num = int(input('Digite um número: '))
#         print(num)
#         break
#     except ValueError as e:
#         print('Não é um inteiro: {}'.format(e))        
#     except Exception as e: # quando não sabemos o tipo de erro, insere esse exception
#         print('Não é um inteiro: {}'.format(e))     

from   datetime import datetime

users = ['1-daniel','2-joao', '3-pedro', '4-maria']
while True:
    try:
        d = datetime.now()
        num = input('''
        USER:
        0- daniel
        1- joao
        2- pedro
        3- maria'
        S- sair\n''')
        if num.lower() == 's':          
            break
        print('O usuario {} esta logado'.format(users[int(num)]))
    except IndexError as e:        
        with open('python.log','a') as arquivo:
            result= '{}, {}'.format(e, d.strftime('%Y-%m-%d %H:%M'))
            arquivo.write(result)
        break
    except KeyboardInterrupt as e:       
        with open('python.log','a') as arquivo:
            result= '{}, {}'.format(e, d.strftime('%Y-%m-%d %H:%M'))
            arquivo.write(result)
        break



    
    