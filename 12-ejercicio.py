from textblob import TextBlob

class AnalizadorDeSentimientos:
  def analizar_sentimiento(self, texto):
    analisis = TextBlob(texto)
    if analisis.sentiment.polarity > 0:
      return 'positive'
    elif analisis.sentiment.polarity == 0:
      return 'neutral'
    else:
      return 'negative'

analizador = AnalizadorDeSentimientos()
resultado = analizador.analizar_sentimiento('this day is a piece of shit')
print(resultado)
resultado = analizador.analizar_sentimiento('this day was normal')
print(resultado)
resultado = analizador.analizar_sentimiento('this day was amazing')
print(resultado)



