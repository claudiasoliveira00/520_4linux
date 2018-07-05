#!/usr/bin/python3

class Dog():
    def __init__(self,nome,idade):
        self.nome = nome # idade é um atributo
        self.idade = idade # idade é um atributo
        self.energia = 10        

    def latir(self):
        print('Au au!')
    
    def andar(self):
        if self.energia > 0:
            self.energia -= 1    
            print('Andando... energia {}.'.format(self.energia))
        else:
            print('estou cansado')
            self.dormir
        

    def dormir(self):
        self.energia = 10
        print('dormindo...')        
    
dog1 = Dog('bilu',2)
dog2 = Dog('bolinha',3)
print(dog1.nome)
dog1.latir()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()
dog1.andar()



