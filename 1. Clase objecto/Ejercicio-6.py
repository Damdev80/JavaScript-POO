import time 

class Moto:
    def __init__(self, marca,nombre, velocidadMax, color):
        self.marca = marca
        self.nombre = nombre 
        self.max = velocidadMax
        self.color = color
    def showInfo(self):
        print(f"La marca de tu Moto es f{self.marca}\nEl nombre de tu Moto es {self.nombre}\nAlcanza los {self.max} km/h\nEl color de tu {self.nombre} es {self.color}")
    def tunrOn(self):
        self.encerder = input("Hola bienvenido [Precione Enter] para encender el Moto")
        print("------------------")
        time.sleep(1)
        print("El Moto se esta ecendiendo")
        print("------------------")
        time.sleep(2)
        print("Espere unos segundos")
        time.sleep(2)
        print("Moto encendido")
        print("------------------")
        time.sleep(2)
        print("A donde quieres ir?")
        print("------------------")
        
        self.prender = True
        if self.prender == True:
            print("¿Deseas apagar tu Moto?")
            self.apagar = input("[Precione y] si desea apagar su Moto, si no [Precione cualquier numero o letra]")
            if self.apagar == "y" or self.apagar == "Y" :
                print("El Moto se apago")
            else:
                print("No se apagara")
    def beep (self):
        time.sleep(1)
        self.pito = print("Precione [Enter] para pitar")
        time.sleep(5)
        print("PIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII")
Moto1 = Moto("Fort", "Mustang GT","380", "Azul")
Moto1.showInfo()
Moto1.tunrOn()
Moto1.beep()