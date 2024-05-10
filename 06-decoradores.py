def decorador(funcion):
  def funcion_modificada():
    print('Antes')
    funcion()
    print('Después')
  return funcion_modificada

# def saludo():
#   print('Hola Mundo')

# saludo_modificado = decorador(saludo)
# saludo_modificado()

@decorador
def saludo():
  print('Hola César, cómo estás?')

saludo()


