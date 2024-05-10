from openai import OpenAI

client = OpenAI(api_key='')

system_rol = '''Hace de cuenta que sos un analizador de sentimientos.
                Yo te paso sentimientos y vos analizas el sentimiento de los mensajes
                y me das una respuesta con al menos 1 caracter y como máximo 4 caracteres
                SOLO RESPUESTAS NUMÉRICAS. donde -1 es negatividad máxima, 0 es neutral y
                1 es positividad máxima. Podes ir entre esos rangos, es decir 0.3, -0.5,
                etc también son válidos. (podes responder solo con ints o floats)'''

# Roles: system (cómo se tiene que comportar, user (inputs que da el usuario) y assistant (respuestas de chatgpt)
messages = [{ "role": "system", "content": system_rol }]

class Sentimiento:
  def __init__(self, nombre, color):
    self.nombre = nombre
    self.color = color
  def __str__(self):
    return '\x1b[1;{}m{}'.format(self.color, self.nombre)

class AnalizadorDeSentimientos:
  def __init__(self, rangos):
    self.rangos = rangos

  def analizador_sentimiento(self, polaridad):
    for rango, sentimiento in self.rangos:
      if rango[0] < polaridad <= rango[1]:
        return sentimiento
    return Sentimiento('Muy negativo', '31')

rangos = [
  ((-0.8,-0,3), Sentimiento('Negativo', '31')),
  ((-0.3,-0.1), Sentimiento('Algo negativo', '31')),
  ((-0.1,0.1), Sentimiento('Neutral', '33')),
  ((0.1,0.4), Sentimiento('Algo positivo', '32')),
  ((0.4,0.9), Sentimiento('Positivo', '32')),
  ((0.9,1), Sentimiento('Muy positivo', '32'))
]

analizador = AnalizadorDeSentimientos(rangos)

while True:
  user_prompt = input('\x1b[1;32m' + '\nDecime algo: ' + '\x1b[0;37m')
  messages.append({ "role": "user", "content": user_prompt })

  response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=messages,
    max_tokens=8
  )
  
  respuesta = response.choices[0].message.content
  
  messages.append({ "role": "assistant", "content": respuesta })
  print(respuesta)
  sentimiento = analizador.analizador_sentimiento(float(respuesta))
  
  print(sentimiento)
