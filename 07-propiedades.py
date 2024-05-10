class Persona:
  def __init__(self, nombre, edad):
    self.__nombre = nombre
    self.__edad = edad

  @property
  def nombre(self):
    return self.__nombre
  
  @nombre.setter
  def nombre(self, nombre):
    self.__nombre = nombre
  
  @nombre.deleter
  def nombre(self):
    del self.__nombre

persona = Persona('Lucas', 21)
nombre = persona.nombre
persona.nombre = 'Cesar'

print(nombre)
print(persona.nombre)

del persona.nombre
# print(persona.nombre)
