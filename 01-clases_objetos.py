class Celular():
  marca = "Samsung",
  modelo = "S23",
  camara = "48MP"

class Celular2:
  def __init__(self, marca, modelo, camara):
    self.marca = marca
    self.modelo = modelo
    self.camara = camara
    
  def llamar(self):
    print(f'Estás haciendo una llamada desde {self.modelo}')
    
  def llamar(self):
    print(f'Cortaste la llamada desde {self.marca}')

celular1 = Celular()
celular2 = Celular2('Apple', '14', '12MP')

# print(dir(celular1))
# print(__name__)
# print(celular1.marca)
# print(celular2.marca)

celular2.llamar()
  