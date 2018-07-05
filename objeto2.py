#!/home/developer/520/venv/bin/python3

class Carro():
    def __init__(self,nome_carro,cor,marca,ano_fabricacao):
        self.nome_carro = nome_carro 
        self.cor = cor 
        self.marca = marca
        self.ano_fabricacao = ano_fabricacao
        self.combustivel = 5   
      
    def correr(self):
        if self.combustivel > 0: 
            self.combustivel -= 1                                   
            print('acelerando... até combustivel acabar. Valor{}'.format(self.combustivel))
        else:           
            print('freiando...Combustível acabando')
            print('...')
            if self.combustivel == 0:
                print('Carro sem gasolina. Abastecer!!!')                           
                
      
    def freiar(self):                 
        print('freiando...')   

class Carro_eletrico(Carro):
    def __init__(self,nome_carro,cor,marca,ano_fabricacao):
        super().__init__(nome_carro,cor,marca,ano_fabricacao)  
        self.combustivel = 'energia'

carro1 = Carro('Tracker','branco','chevrolet',2018)
carro2 = Carro_eletrico('X5','branca','BMW',2017)
print(carro1.combustivel)
print('...')
print(carro2.combustivel)
carro1.correr()
carro1.correr()
carro1.correr()
