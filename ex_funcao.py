#!/usr/bin/python3
# abrir o arquivo 


def escr_arq(nome_arq,conteudo):   
    try:
        with open(nome_arq, 'w') as arq:        
            arq.writelines(conteudo)
            return True
    except Exception as e:
        return 'Erro: {}'.format(e)

nomes = ['daniel\n','pedro\n', 'joao\n', 'julio\n']
escr_arq('nomes.txt',nomes)

def alterar_lista(lista):
    lista1 = []
    for item in lista:
        lista1.append('{}\n'.format(item))
    return lista1
nomes = ['daniel','pedro', 'joao', 'julio']
alterado = alterar_lista(nomes)
escr_arq('nomes.txt',alterado)

# for x in nomes:
#     nomes1.append('{}\n'.format(x))
# print(nomes1)



