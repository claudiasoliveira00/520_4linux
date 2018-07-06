#!/usr/bin/python3
from pymongo import MongoClient
from random import choice as sorteio
ids = list(range(999))

try:
    frutas = MongoClient()
    db = frutas['4linux']
except Exception as e:
    print('ERRO: {}'.format(e))

frutas = [
    {'item':'caqui', 'preco':4,'qtd':5},
    {'item':'mamao', 'preco':2.4,'qtd':2},
]
db.frutas.remove()
for fruta in frutas:
    a = sorteio(ids)
    ids.remove(a)
    fruta['_id'] = a
    db.frutas.insert(fruta)


dados = db.frutas.find()
dados = [x for x in dados]

print(dados)