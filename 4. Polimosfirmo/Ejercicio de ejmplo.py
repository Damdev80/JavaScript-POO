class Aprendiz:
    def __init__(self,nombre,apellido, cedula,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.sexo = sexo
        
        
    def description(self):
        print("------------------------------------")
        print(f"El Aprendiz: {self.nombre}\nDe apellido: {self.apellido}\nCedula: {self.cedula}\nSexo: {self.sexo}")
        print("------------------------------------")
        

class Instructor:
    def __init__(self,nombre,apellido, cedula,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.sexo = sexo
        
        
    def description(self):
        print(f"El Instructor: {self.nombre}\nDe apellido: {self.apellido}\nCedula: {self.cedula}\nSexo: {self.sexo}")
        print("------------------------------------")
        

class Coordinador:
    def __init__(self,nombre,apellido, cedula,sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.sexo = sexo
        
        
    def description(self):
        
        print(f"El Coordinador: {self.nombre}\nDe apellido: {self.apellido}\nCedula: {self.cedula}\nSexo: {self.sexo}")
        print("------------------------------------")

persona1 = Aprendiz("Toyota",2022,"Electrico","BMW")
persona1.description()
persona2 = Instructor("Z100",2024,"Automatica","HONDA")
persona2.description()
persona3 = Coordinador("Terreneitor",2023,"Automatica","Ciclo pedal")
persona3.description()