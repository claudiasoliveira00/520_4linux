#!/usr/bin/python3

# lambda: função anonima. Quando vou utilizar uma vez só
fruta = {'nome':'laranja', 'valor':5.55, 'qtd':26}
var = lambda x,y: x * y

print(var(fruta['valor'], fruta['qtd']))

