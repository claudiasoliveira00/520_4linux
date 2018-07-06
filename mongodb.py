#!/usr/bin/python3
from pymongo import MongoClient

try:
    client = MongoClient()
    db = client['4linux'] # chave de dados '4linux' é a base de dados
except Exception as e:
    print('ERRO: {}'.format(e))

# dados = db.pessoas.find_one({'_id':1}) # trazer uma pessoa em específico
dados = db.pessoas.find() 
dados = [x for x in dados] # comprimir a tabela em uma lista, com cada elemento

# db.pessoas.insert({'_id':6, 'nome':'carolina', 'sobrenome':'silva','idade':30}) # inserir
# db.pessoas.update({'_id':6},{'$set':{'idade':30}}) #alterar
# db.pessoas.remove({'_id':6}) #remover


print(dados)


