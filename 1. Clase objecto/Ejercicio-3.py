import time 

class Carro:
    def __init__(self, marca,nombre, velocidadMax, color):
        self.marca = marca
        self.nombre = nombre 
        self.max = velocidadMax
        self.color = color
    def showInfo(self):
        print(f"La marca de tu carro es f{self.marca}\nEl nombre de tu carro es {self.nombre}\nAlcanza los {self.max} km/h\nEl color de tu {self.nombre} es {self.color}")
    def tunrOn(self):
        self.encerder = input("Hola bienvenido [Precione Enter] para encender el carro")
        print("------------------")
        time.sleep(1)
        print("El carro se esta ecendiendo")
        print("------------------")
        time.sleep(2)
        print("Espere unos segundos")
        time.sleep(2)
        print("Carro encendido")
        print("------------------")
        time.sleep(2)
        print("A donde quieres ir?")
        print("------------------")
        
        self.prender = True
        if self.prender == True:
            print("¿Deseas apagar tu carro?")
            self.apagar = input("[Precione y] si desea apagar su carro, si no [Precione cualquier numero o letra]")
            if self.apagar == "y" or self.apagar == "Y" :
                print("El carro se apago")
            else:
                print("No se apagara")
    def beep (self):
        time.sleep(1)
        self.pito = print("Precione [Enter] para pitar")
        time.sleep(5)
        print("PIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
carro1 = Carro("Fort", "Mustang GT","380", "Azul")
carro1.showInfo()
carro1.tunrOn()
carro1.beep()