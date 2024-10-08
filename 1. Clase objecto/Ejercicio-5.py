#Defino la color 
class Figuras():
    """"""
    def __init__(self, tipo, nombre, lados, color, altura):
        self.tipo = tipo
        self.nombre = nombre
        self.lados = lados
        self.color = color
        self.altura = altura
    #Metodo para mostrar detalles del objecto:
    def showInfo(self):
        print("-------------------------------------------------")
        print(f"El tipo es un:{self.tipo}\n Su nombre es {self.nombre}\nTiene lados de{self.nombre} es: {self.lados} años\nEs del color {self.color}\ny su estado altura de{self.nombre} es {self.altura} m")
        print("-------------------------------------------------")
    def perimetro(self):
        self.perimetro = print(f"La figura  {self.nombre} cuenta con perimetro")
    def isEat(self):
        self.area = print(f"La figura {self.nombre} cuenta con area")
        

figuras1 =  Figuras("Triangulo Equilatero", "Triangulo","3","rojo","3")
figuras1.showInfo()
figuras1.perimetro()
figuras1.isEat()
