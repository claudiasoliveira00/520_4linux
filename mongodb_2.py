#!/usr/bin/python3
from pymongo import MongoClient

try:
    fruta = MongoClient()
    db = fruta['4linux'] # chave de dados '4linux' é a base de dados
except Exception as e:
    print('ERRO: {}'.format(e))

# db.frutas.insert({'_id':1, 'fruta':'pera', 'preco':5.5,'qtd':30}) # inserir
# db.frutas.insert({'_id':2, 'fruta':'maça', 'preco':5.5,'qtd':30})
# db.frutas.insert({'_id':3, 'fruta':'uva', 'preco':6,'qtd':2})
# db.frutas.insert({'_id':4, 'fruta':'banana', 'preco':2.5,'qtd':5})
# db.frutas.insert({'_id':5, 'fruta':'kiwi', 'preco':6.5,'qtd':20})

dados = db.frutas.find()
dados = [x for x in dados]

print(dados)