class Dispositivo:
    def __init__(self,marca, modelo, año):
        self.marca = marca
        self.modelo = modelo 
        self.año = año
        self.capaciadad = int(input("Ingrese el capaciadad de bateria de su Dispositivo: "))
        
    def registrar(self):
        print("------------------------------------------")
        print("Registro del Dispositivo fue un exito")
        print("------------------------------------------")
        print(f"Tu Dispositivo de la marca {self.marca}\nDe modelo {self.modelo}\nDel año {self.año}\nCon la capaciadad de bateria {self.capaciadad} mAh")
        
class Smartphone(Dispositivo):
    def __init__(self, marca, modelo, año, os):
        super().__init__(marca, modelo, año)
        self.os = os
        self.conetividad = input("Ingrese el tipo de conectividad que tiene el Smartphone")
        
    
    def conetividades(self):
        print(f"Su conetividad de su {self.modelo} es de {self.conetividad}")
        
        
    def encender(self):
        self.bateria = int(input("Ingrese en cuanto esta la bateria del telefono: "))
        if self.bateria > 0:
            print("Tu Smartphone esta conetado puede encender")
        elif self.bateria <= 0:
            print("Tu Smartphone no puede encender")
            

            
            
            
iphone16 = Smartphone("Apple","Iphone 16 pro Max",2024,"IOS")
iphone16.conetividades()
iphone16.registrar()
iphone16.encender()
