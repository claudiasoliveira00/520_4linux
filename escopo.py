#!/usr/bin/python3

var = 10 # --variável global

def escopo():
    global var   # especifica a global dentro da função
    var = 5     # --variável local
    print(var)  # - sistema dá prioridade para a variável local e depois procura a global

print(var)
escopo()
print(var)