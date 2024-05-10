# class MiClase:
#   def __init__(self):
#     self._atributo_privado = 'Valor privado'
#     self.__atributo_muy_privado = 'Valor muy provado'

# objeto = MiClase()
# print(objeto._atributo_privado)
# print(objeto.__atributo_muy_privado)



class Persona:
  def __init__(self, nombre, edad):
    self.__nombre = nombre
    self.__edad = edad

  def get_nombre(self):
    return self.__nombre
  
  def set_nombre(self, nombre):
    self.__nombre = nombre

dalto = Persona("Lucas", 21)
nombre = dalto.get_nombre()
dalto.set_nombre('Cesar')
print(nombre)
print(dalto.get_nombre())
