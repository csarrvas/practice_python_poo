'''

S - SRP, Principio de responsabilidad único (cada cosa solo la responsabilidad que le toca)
O - OCP, Principio de abierto/cerrado (abierto a extensión, cerrado a modificación)
L - LSP, Principio de sustitución de liskov (un objeto de una subclase debería poder hacer todo lo que hace la clase padre)
I - ISP, Principio de segregación de interfaz (desglosar las interfaces para que las clases no se vean obligadas a implementar métodos que no usan)
D - DIP, Principio de inversión de dependencias (la clase más importante no debe depender de la menos importante)

'''
# DIP
from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
  @abstractmethod
  def verificar_palabra(self, palabra):
    pass

class Dicionario(VerificadorOrtografico):
  def verificar_palabra(self, palabra):
    #Lógica para verificar palabras si está en el diccionario
    pass

class ServicioOnline(VerificadorOrtografico):
  def verificar_palabra(self, palabra):
    #Lógica para verificar palabras desde el servicio web
    pass

# Clase principal
class CorrectorOrtografico:
  def _init__(self, verificador):
    self.verificador = verificador

  def corregir_texto(self, texto):
    # usamos el verificador para corregir texto
    pass

corrector = CorrectorOrtografico(Dicionario())
corrector = CorrectorOrtografico(ServicioOnline())

'''
Es decir, como verificador es una clase abstracta tenemos todos los métodos que necesitamos ahi mismo,
si tiene más métodos, como por ej: buscar_similares) o corregir_ortografial o agregar_acento) podemos
quedarnos tranquilos de que podemos seguir usando los mismos métodos que tenga el verificador, porque
al ser una subclase tendria que poder hacer todo lo que hace la clase base (Principio de sustitución
de Liskov)
'''


