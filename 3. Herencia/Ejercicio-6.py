import time
class Electronico:
    def __init__(self,modelo, marca, procesador):
        self.modelo = modelo
        self.marca = marca 
        self.procesador = procesador
        self.ram = int(input("Ingrese la ram que desea para si Electronico: "))
        
    def registrar(self):
        print("------------------------------------------")
        print("Registro del Electronico fue un exito")
        print("------------------------------------------")
        print(f"Tu Electronico es del modelo {self.modelo}\nDe la marca {self.marca}\nDel procesador {self.procesador}\nCon el ram de el Electronico de: {self.ram} GB ")
        
class Laptop(Electronico):
    def __init__(self, modelo, marca, procesador, disco_duro):
        super().__init__(modelo, marca, procesador)
        self.disco_duro = disco_duro
        self.duracion_bateria = input("Ingrese la duracion la bateria de su Laptop : ")

    def encender(self):
        self.bateria = int(input("Ingrese en cuanta bateria tiene su Laptop: "))
        if self.bateria > 0:
            print("Tu Laptop tiene la bateria suficiente para prender")
        elif self.bateria <= 0:
            print("Tu Laptop no tiene la bateria suficiente para encender")
            
            
            
            
Laptop1 = Laptop("2021","MSI","Intel 512400F","SSD 1T")
Laptop1.encender()
Laptop1.registrar()

