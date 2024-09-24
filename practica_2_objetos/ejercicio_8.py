# EJERCICIO 8
# Considere la siguiente jerarquía de clases:
#                           |--- Felinos
# Animales --- Mamíferos ---|--- Cánidos
#                           |--- Primates --- Hacker
# Programe un conjunto de seis clases que modele esta taxonomía utilizando clases. Luego, agregue un
# método speak a cada clase imprimiendo un mensaje apropiado a cada clase (por ejemplo, una instancia
# de animal podría imprimir "Soy un animal").
# Luego, agregue un método talk a la clase Animal, que simplemente delegue el funcionamiento en
# speak. ¿Qué ocurre al llamar a talk en una subclase? ¿Qué ocurre si borramos el método speak de la
# clase Hacker?
class Animales():
    def speak(self):
        print("soy un animal")
    
    def talk(self):
        self.speak()

class Mamiferos(Animales):
    def speak(self):
        print("soy un mamifero")

class Felinos(Mamiferos):
    def speak(self):
        print("soy un felino")

class Canidos(Mamiferos):
    def speak(self):
        print("soy un canino")

class Primates(Mamiferos):
    def speak(self):
        print("soy un primate")

class Hacker(Primates):
    def speak(self):
        print("soy un hacker")
gato = Felinos()
gato.speak()
gato.talk()
# ¿Qué ocurre al llamar al método talk en una subclase? Al invocar talk en una subclase 
# (por ejemplo, una instancia de Felino), este método debería llamar a speak, pero el 
# método speak invocado será el de la subclase, gracias a la naturaleza polimórfica de Python.
# Esto significa que si llamas a talk en una instancia de Felino, se ejecutará el speak de Felino,
# no el de Animal.
pablo = Hacker()
pablo.speak()

# Si eliminamos el método speak de Hacker
del Hacker.speak
pablo.speak() # soy un primate
# Qué ocurre si borramos el método speak en la clase Hacker? Si eliminamos el método speak de 
# la clase Hacker, Python buscará el método speak en las clases superiores de la jerarquía, 
# siguiendo la cadena de herencia. En este caso, buscará primero en Primates, luego en Mamíferos, y 
# finalmente en Animales. Si lo encuentra en alguna de estas clases, lo usará. Si no, arrojará un error.
