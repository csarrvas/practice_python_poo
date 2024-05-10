from abc import ABC, abstractmethod

class Persona(ABC):
  @abstractmethod
  def __init__(self, nombre, edad, sexo, actividad):
    self.nombre = nombre
    self.edad = edad
    self.sexo = sexo
    self.actividad = actividad
  
  @abstractmethod
  def trabajar(self):
    pass
  
  def presentarse(self):
    print(f'Hola me llamo {self.nombre} y tengo {self.edad} años')

class Estudiante(Persona):
  def __init__(self, nombre, edad, sexo, actividad):
    super().__init__(nombre, edad, sexo, actividad)
  def trabajar(self):
    pass

# persona = Persona('César', 27, 'M', 'Programador')
# persona.presentarse()

persona = Estudiante('César', 27, 'M', 'Programador')
persona.presentarse()
