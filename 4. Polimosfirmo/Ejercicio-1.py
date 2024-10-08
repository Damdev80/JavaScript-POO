class Carro:
    def __init__(self,nombre,modelo, tipo,marca):
        self.nombre = nombre
        self.modelo = modelo
        self.tipo = tipo
        self.marca = marca
        
        
    def description(self):
        print("------------------------------------")
        print(f"Es un: {self.nombre}\nDel modelo: {self.modelo}\nEs de tipo: {self.tipo}\nDe la marca: {self.marca}")
        print("------------------------------------")
        

class Moto:
    def __init__(self,nombre,modelo, tipo,marca):
        self.nombre = nombre
        self.modelo = modelo
        self.tipo = tipo
        self.marca = marca
        
        
    def description(self):
        print(f"\nEs un: {self.nombre}\nDel modelo: {self.modelo}\nEs de tipo: {self.tipo}\nDe la marca: {self.marca}")
        print("------------------------------------")
        

class Bicicleta:
    def __init__(self,nombre,modelo, tipo,marca):
        self.nombre = nombre
        self.modelo = modelo
        self.tipo = tipo
        self.marca = marca
        
        
    def description(self):
        
        print(f"\nEs un: {self.nombre}\nDel modelo: {self.modelo}\nEs de tipo: {self.tipo}\nDe la marca: {self.marca}")
        print("------------------------------------")

vehiculo1 = Carro("Toyota",2022,"Electrico","BMW")
vehiculo1.description()
vehiculo2 = Moto("Z100",2024,"Automatica","HONDA")
vehiculo2.description()
vehiculo3 = Bicicleta("Terreneitor",2023,"Automatica","Ciclo pedal")
vehiculo3.description()