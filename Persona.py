#Crear una clase Persona () que tenga como atributos nombre, edad y profesion
#Al instanciar la clase tiene que saludar igual que el dino

class Persona:
    def __init__(self,un_nombre="", una_edad="", una_profesion=""):            #constructor de la clase
        self.nombre = un_nombre
        self.edad = una_edad
        self.profesion = una_profesion
        print("Hola mi nombre es ",un_nombre, "tengo", una_edad, "años", "y soy", una_profesion )

student = Persona("Aldo","33", "psicologo")
student1 = Persona("Anonimo", "22", "actor")