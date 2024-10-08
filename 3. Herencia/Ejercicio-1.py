#Electrodomestico

class Electrodomestico:
    def __init__(self,marca, color, capacidad):
        self.marca = marca
        self.color = color 
        self.capacidad = capacidad
        self.consumo = int(input("Ingrese el consumo de su Electrodomestico: "))
        
    def registrar(self):
        print("------------------------------------------")
        print("Registro del electrodomestico fue un exito")
        print("------------------------------------------")
        print(f"Tu eletrodomestico de la marca {self.marca}\nDe color {self.color}\nDe capacidad {self.capacidad} kg\nCon el consumo de energia {self.consumo} kWh")
        
class Refrigerador(Electrodomestico):
    def __init__(self, marca, color, capacidad, tipo):
        super().__init__(marca, color, capacidad)
        self.tipo = tipo
        self.temperatura = int(input("Ingrese la temperatura de su refrigerador: "))
    
    def encerder(self):
        self.energia = True
        if self.energia == True:
            print("Tu refrigerador esta conetado puede encender")
        elif self.energia == False:
            print("Tu refrigerador no puede encender")
            
    def medidorTemperatura(self):
        if self.temperatura >= 2 and self.temperatura <= 8:
            print(f"La temperatura de {self.temperatura} es normal")
            
        else:
            print(f"Revisa tu refrigerador tiene una temperatura de {self.temperatura} puede dañarse")
            
            
            
nevera1 = Refrigerador("haced","Plateado",2,"Frost")
nevera1.registrar()
nevera1.encerder()
nevera1.medidorTemperatura()