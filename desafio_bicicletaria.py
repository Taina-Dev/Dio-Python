class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor  


    def buzinar(self): 
        print("Plim plim.....") 


    def parar(self):
        print("Parando Bicicleta...")
        print("Bicicleta parada!")  


    def correr(self):
        print("La vai o marcoooo Velhoooo!!....")


b1 = Bicicleta("Vermelha","caloi", 2024, 600) 
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)






     