# ------------------------ ITERADOR ----------------------------- #
def bienParentizadas(n: int) -> list[str]:
  """Funcion que genera un arreglo de strings con expresiones de parentesis, bien parentizados.

  Se utiliza un iterador interno para generar las expresiones. En este arreglo se guardan TODAS las
  posibles expresiones resultantes de n juego de parentesis.
    
  Parametros:
    n: int, numero de parentesis compuestos a utilizar para generar expresiones.

  Retorno:
    list[str], arreglo de strings con todas las combinaciones posibles de expresiones bien parentizados.
  """
  def generador(word: str, left: int, right: int):
    """Iterador interno que genera las expresiones bien parentizadas, en base a los principios de un iterador
    personalizado por el desarrollador.

    Parametros:
      word: str, expresion bien parentizada en contruccion.
      left: int, numero de parentesis abiertos en la expresion.
      right: int, numero de parentesis cerrados en la expresion.
    """
    if 0 <= left <= right:
      if not right:
        yield word

      for q in generador(word + '(', left - 1, right):
        yield q

      for q in generador(word + ')', left, right - 1): 
        yield q
  return list(generador('', n, n))
      
# ------------------------ EJEMPLO ----------------------------- #
for ans in bienParentizadas(3):
  print(ans)
