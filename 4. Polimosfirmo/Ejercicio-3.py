class Guitarra:
    def __init__(self,marca,modelo, material,tipo):
        self.marca = marca
        self.modelo = modelo
        self.material = material
        self.tipo = tipo
        
        
    def description(self):
        print("------------------------------------")
        print(f"Su guitarra es de la: {self.marca}\nEs del modelo: {self.modelo}\nEs de: {self.material}\nEs de tipo: {self.tipo}")
        print("------------------------------------")
        

class Piano:
    def __init__(self,marca,modelo, material,tipo):
        self.marca = marca
        self.modelo = modelo
        self.material = material
        self.tipo = tipo
        
        
    def description(self):
        print(f"Su Piano es de la: {self.marca}\nEs del modelo: {self.modelo}\nEs de: {self.material}\nEs de tipo: {self.tipo}")
        print("------------------------------------")
        

class Trompeta:
    def __init__(self,marca,modelo, material,tipo):
        self.marca = marca
        self.modelo = modelo
        self.material = material
        self.tipo = tipo
        
        
    def description(self):
        print(f"Su Trompeta es de la: {self.marca}\nEs del modelo: {self.modelo}\nEs de: {self.material}\nEs de tipo: {self.tipo}")
        print("------------------------------------")

istrumento1 = Guitarra("Room",2023,"Madera","Acustico")
istrumento1.description()
istrumento2 = Piano("Zaas",2022,"Metal","Eletrico")
istrumento2.description()
istrumento3 = Trompeta("Rios",2015,"Oro","Acustico")
istrumento3.description()