#Defino la clase 
class Animal():
    """"""
    def __init__(self, especie, nombre, edad, clase, color):
        self.especie = especie
        self.nombre = nombre
        self.edad = edad
        self.clase = clase
        self.color = color
    #Metodo para mostrar detalles del objecto:
    def showInfo(self):
        print("-------------------------------------------------")
        print(f"El especie de su Animal es:{self.especie}\nEl nombre es {self.nombre}\nla edad de tu {self.nombre} es: {self.edad} años\nEs de clase {self.clase}\ny la color es del {self.nombre} es {self.color}")
        print("-------------------------------------------------")
    

animal1 =  Animal("Canino", "Perro","12","Terreste","Blanco con negro")
mostrar = animal1.showInfo()

