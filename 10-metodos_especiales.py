# from os import system
# # Limpiar consola
# system('clear')
# print('\n\n')

class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  
  def __str__(self):
    return f'Persona(nombre={self.nombre},edad={self.edad})'
  
  def __repr__(self):
    return f'Persona("{self.nombre}",{self.edad})'
  
  # Sobrecarga de operadores
  def __add__(self, otro):
    nuevo_valor = self.edad + otro.edad
    return Persona(self.nombre+otro.nombre, nuevo_valor)

dalto = Persona('Lucas', 21)
# print(dalto)

repre = repr(dalto)
resultado = eval(repre)
print((repre))
print(resultado)
print(resultado.nombre)

cesar = Persona('Cesar', 30)
maria = Persona('Maria', 18)

nueva_persona = dalto + cesar + maria
print(nueva_persona)




"""

Aritméticos:
__add__(self, other): Sobrecarga del operador de suma (+).
__sub__(self, other): Sobrecarga del operador de resta (-).
__mul__(self, other): Sobrecarga del operador de multiplicación (*).
__div__(self, other): Sobrecarga del operador de división (/).
__mod__(self, other): Sobrecarga del operador de módulo (%).
__pow__(self, other): Sobrecarga del operador de exponenciación (**).

Comparación:
__eq__(self, other): Sobrecarga del operador de igualdad (==).
__ne__(self, other): Sobrecarga del operador de desigualdad (!=).
__lt__(self, other): Sobrecarga del operador menor que (<).
__gt__(self, other): Sobrecarga del operador mayor que (>).
__le__(self, other): Sobrecarga del operador menor o igual que (<=).
__ge__(self, other): Sobrecarga del operador mayor o igual que (>=).

Asignación:
__iadd__(self, other): Sobrecarga del operador de suma en asignación (+=).
__isub__(self, other): Sobrecarga del operador de resta en asignación (-=).
__imul__(self, other): Sobrecarga del operador de multiplicación en asignación (*=).
__idiv__(self, other): Sobrecarga del operador de división en asignación (/=).
__imod__(self, other): Sobrecarga del operador de módulo en asignación (%=).
__ipow__(self, other): Sobrecarga del operador de exponenciación en asignación (**=).

Otros:
__str__(self): Sobrecarga del operador str(). Devuelve una representación legible como cadena del objeto.
__len__(self): Sobrecarga del operador len(). Devuelve la longitud del objeto.
__getitem__(self, index): Sobrecarga del operador de indexación ([)). Permite acceder a elementos del objeto por indice.

"""



