#Defino la cargo 
class Empleado():
    """"""
    def __init__(self, sexo, nombre, edad, cargo, estadocl):
        self.sexo = sexo
        self.nombre = nombre
        self.edad = edad
        self.cargo = cargo
        self.estadocl = estadocl
    #Metodo para mostrar detalles del objecto:
    def showInfo(self):
        print("-------------------------------------------------")
        print(f"El sexo de su Empleado es:{self.sexo}\nEl nombre es {self.nombre}\nla edad de{self.nombre} es: {self.edad} años\nEs del cargo {self.cargo}\ny su estado civil de{self.nombre} es {self.estadocl}")
        print("-------------------------------------------------")
    def isWorking(self):
        self.work = print(f"El trabajador {self.nombre} esta trabajando")
    def isEat(self):
        self.work = print(f"El trabajador {self.nombre} esta comiendo")
        

empleado1 =  Empleado("Hombre", "Ever","18","Ing","Soltero")
empleado1.showInfo()
