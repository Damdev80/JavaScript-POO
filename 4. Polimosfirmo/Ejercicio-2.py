class Perro:
    def __init__(self,nombre,raza, edad,sexo):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        
        
    def description(self):
        print("------------------------------------")
        print(f"Se llama: {self.nombre}\nEs de la raza: {self.raza}\nTiene la de edad: {self.edad}\nEs un: {self.sexo}")
        print("------------------------------------")
        

class Gato:
    def __init__(self,nombre,raza, edad,sexo):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        
        
    def description(self):
        print(f"\nEs un: {self.nombre}\nDel raza: {self.raza}\nEs de edad: {self.edad} Años\nDe la sexo: {self.sexo}")
        print("------------------------------------")
        

class Pájaro:
    def __init__(self,nombre,raza, edad,sexo):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.sexo = sexo
        
        
    def description(self):
        
        print(f"\nEs un: {self.nombre}\nDel raza: {self.raza}\nEs de edad: {self.edad}\nDe la sexo: {self.sexo}")
        print("------------------------------------")

Aniamal1 = Perro("Pocholo","Pinche",5,"Macho")
Aniamal1.description()
Aniamal2 = Gato("Mono","Tigrado",3,"Macho")
Aniamal2.description()
Aniamal3 = Pájaro("Coti","Cotorro",1,"Hembra")
Aniamal3.description()