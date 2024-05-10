class Persona:
  def __init__(self, nombre, edad, nacionalidad):
    self.nombre = nombre
    self.edad = edad
    self.nacionalidad = nacionalidad
  
  def hablar(self):
    print('Hola estoy hablando un poco')

# Herencia Simple
class Empleado(Persona):
  def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
    super().__init__(nombre, edad, nacionalidad)
    self.trabajo = trabajo
    self.salario = salario


class Estudiante(Persona):
  def __init__(self, nombre, edad, nacionalidad, notas, universidad):
    super().__init__(nombre, edad, nacionalidad)
    self.notas = notas
    self.universidad = universidad
    
  def hablar(self):
    print('No quiero hablar tanto')

cesar = Empleado('César', 43, 'salvadoreño', 'Programador', 3600)

alele = Estudiante('César', 43, 'salvadoreño', 10, 'quitatonga')

print(cesar.nombre)
cesar.hablar()
print(cesar.trabajo)

print(alele.universidad)


class EscupeCodigo:
  def __init__(self, lenguaje):
    self.lenguaje = lenguaje

# Herencia Múltiple
class Programador(Persona, EscupeCodigo):
  def __init__(self, nombre, edad, nacionalidad, lenguaje, segundo_lenguaje):
    Persona.__init__(self, nombre, edad, nacionalidad)
    EscupeCodigo.__init__(self, lenguaje)
    self.segundo_lenguaje = segundo_lenguaje
    
  def hablar_programador(self):
    super().hablar()

elmeromero = Programador('Cesar', 27, 'salvadoreño', 'python', 'react')
print('________________\n')
print(elmeromero.nombre)
print(elmeromero.lenguaje)
print(elmeromero.segundo_lenguaje)
elmeromero.hablar_programador()

print(issubclass(Programador, Persona))
print(isinstance(elmeromero, Programador))
