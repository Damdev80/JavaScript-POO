class Medico:
    def __init__(self,nombre,edad, area,especializacion):
        self.nombre = nombre
        self.edad = edad
        self.area = area
        self.especializacion = especializacion
        
        
    def mostrarInfo(self):
        print("------------------------------------")
        print(f"El Doctor: {self.nombre}\nTiene del edad: {self.edad}\nEs del area: {self.area}\nEsta especializado en: {self.especializacion}")
        print("------------------------------------")
        

class Ingeniero:
    def __init__(self,nombre,edad, area,especializacion):
        self.nombre = nombre
        self.edad = edad
        self.area = area
        self.especializacion = especializacion
        
        
    def mostrarInfo(self):
        print(f"El Ingeniero: {self.nombre}\nTiene del edad: {self.edad}\nEs del area: {self.area}\nEsta especializado en: {self.especializacion}")
        print("------------------------------------")
        

class Docente:
    def __init__(self,nombre,edad, area,especializacion):
        self.nombre = nombre
        self.edad = edad
        self.area = area
        self.especializacion = especializacion
        
        
    def mostrarInfo(self):
        print(f"El Docente: {self.nombre}\nTiene del edad: {self.edad}\nEs del area: {self.area}\nEsta especializado en: {self.especializacion}")
        print("------------------------------------")

istrumento1 = Medico("Mariangel",18,"Salud","Fonoaudiologia")
istrumento1.mostrarInfo()
istrumento2 = Ingeniero("Daniel",19,"Desarrollo","Front end")
istrumento2.mostrarInfo()
istrumento3 = Docente("Jose",18,"Colegios","Socilaes e Historias")
istrumento3.mostrarInfo()