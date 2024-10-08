import time
class Instrumento:
    def __init__(self,tipo, marca, material):
        self.tipo = tipo
        self.marca = marca 
        self.material = material
        self.precio = int(input("Ingrese el precio de su Instrumento: "))
        
    def registrar(self):
        print("------------------------------------------")
        print("Registro del Instrumento fue un exito")
        print("------------------------------------------")
        print(f"Tu Instrumento es del tipo {self.tipo}\nDe la marca {self.marca}\nDel material {self.material}\nCon el precio de el instrumento de: ${self.precio} ")
        
class Guitarra(Instrumento):
    def __init__(self, tipo, marca, material, numeroDeCuerdas):
        super().__init__(tipo, marca, material)
        self.numeroDeCuerdas = numeroDeCuerdas
        self.acordes = input("Ingrese el numero de acordes basicos que conozcas: ")

    def tocar(self):
        self.tocar = input("Quieres tocar algo para nosotros? si(y)/no(n)").lower()
        if self.tocar == "y":
            print("𝄟  \n 𝅘𝅥𝅮  \n𝅘𝅥𝅱 𝅘𝅥𝅮")
            time.sleep(1)
            print("𝄟 𝅘𝅥𝅮  𝅘𝅥𝅱  \n𝅘𝅥𝅮")
            time.sleep(1)
            print("𝄟  \n𝅘𝅥𝅮  𝅘𝅥𝅱 𝅘𝅥𝅮")
            time.sleep(2)
            print("𝄟 𝅘𝅥𝅮  \n𝅘𝅥𝅱 𝅘𝅥𝅮")
            time.sleep(1)
            print("𝄟 \n𝅘𝅥𝅮  𝅘𝅥𝅱 𝅘𝅥𝅮")
        else:
            print("No gracias")
            
            
            
guitarra1 = Guitarra("Acustico","Martin","Madera pura","5")
guitarra1.tocar()
guitarra1.registrar()

