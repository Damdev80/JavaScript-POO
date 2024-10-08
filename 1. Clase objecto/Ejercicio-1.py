#Defino la clase 
import time
import sys

class Celular():
    """"""
    def __init__(self, nombre, marca, imei, bateria, camara):
        self.nombre = nombre
        self.marca = marca
        self.imei = imei
        self.bateria = bateria
        self.camara = camara
    #Metodo para mostrar detalles del objecto:
    def showInfo(self):
        print(f"El nombre de su celular es:{self.nombre}\n la marca es{self.marca}\n El numero de imei de tu telefono es: {self.imei} \n La cantidad de bateria de tu telefono es {self.bateria} MAH \n y la camara es de {self.camara}px")
    
    def turnOn(self):
        print("-------------------------------------------------------")
        self.energia = int(input("Ingrese la cargad de su dispositivo: "))
        if self.energia > 0:
            print("El celular puede encender")
            self.energia = True
        else:
            print("No puede prender")
            self.energia = False
        print("-------------------------------------------------------")

    def turnOff(self):
        if self.energia == True:
            print("El telefono se puede apagar")
        elif self.energia == False:
            print("El telefono no se puede prender porque no tiene suficiente carga")
            
    #def cargando(self):


        
celular1 =  Celular("Ipone 16 pro max", "Apple","20384","6000","64")
celular1.showInfo()
celular1.turnOn()
celular1.turnOff()


