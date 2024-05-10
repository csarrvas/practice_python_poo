class Auto():
  def __init__(self):
    self.__estado = 'apagado'
  
  def encender(self):
    self.__estado = 'encendido'
    print(f'El auto está {self.__estado}')
  
  def conducir(self):
    if self.__estado == 'apagado':
      self.encender()
    print('Conduciendo...')

auto = Auto()
auto.encender()
