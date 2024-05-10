class Gato():
  def sonido(self):
    return "Miau"

class Perro():
  def sonido(self):
    return "Guau"

def hacer_sonido(animal):
  print(animal.sonido())

gato = Gato()
perro = Perro()

# Polimorfismo cambiando argumento para la función
hacer_sonido(gato)

# Polimorfismo cambiando el objeto para la llamada al método
print (gato.sonido())

# Términos relacionados:
# Duck Typing
# Enlaces dinámicos (mecanismo interno en el que da prioridad a un método u otro) / Enlaces estáticos
# Tipo real (origen de todo) / Tipo declarado (origen de la variable)
