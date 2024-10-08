import time
class Reloj:
    def __init__(self,tipo, marca, material):
        self.tipo = tipo
        self.marca = marca 
        self.material = material
        self.precio = int(input("Ingrese la precio que desea para si Reloj: "))
        
    def registrar(self):
        print("------------------------------------------")
        print("Registro del Reloj fue un exito")
        print("------------------------------------------")
        print(f"Tu Reloj es del tipo {self.tipo}\nDe la marca {self.marca}\nDel material {self.material}\nCon el precio de el Reloj de: ${self.precio} ")
        
class SmartWatch(Reloj):
    def __init__(self, tipo, marca, material, pantalla):
        super().__init__(tipo, marca, material)
        self.pantalla = pantalla
        self.duracion_bateria = input("Ingrese la duracion la bateria de su SmartWatch : ")

    def encender(self):
        self.bateria = int(input("Ingrese en cuanta bateria tiene su SmartWatch: "))
        if self.bateria > 0:
            print("Comprobando que su dispositivo tenga la bateria suficiente para encender")
            time.sleep(2)
            print("Tu SmartWatch tiene la bateria suficiente para prender")
            time.sleep(2)
            print("Bienvenido ¡Buenos Dias!")
            time.sleep(0.5)
            print("Estas son sus activides para hoy:")
            time.sleep(1)
            print("9:00 AM: ¡No olvides tomar tu desayuno saludable!\n10:30 AM: Revisa los correos electrónicos importantes del proyecto X.\n12:00 PM: ¡Hora de la reunión virtual con el equipo de diseño!\n2:00 PM: Llama a tu mamá para desearle feliz cumpleaños.\n4:00 PM: Ve a la clase de yoga para relajarte después del trabajo. ‍♀️\n6:00 PM: ¡No olvides recoger a los niños de la escuela!\n8:00 PM: Prepara la cena y disfruta de un momento en familia.")
        elif self.bateria <= 0:
            print("Tu SmartWatch no tiene la bateria suficiente para encender")
            
            
            
            
SmartWatch1 = SmartWatch("Deportivo","Apple","Acero", "OLED")
SmartWatch1.encender()
SmartWatch1.registrar()

