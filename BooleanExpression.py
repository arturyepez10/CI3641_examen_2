# ------------------------ IMPORTS ----------------------------- #
# locals
from utils.constants import tokens

# ------------------------ CLASE ----------------------------- #
class BooleanExpression:
  """
  Representacion de una Expresion Booleana, que es una serie de terminos del mismo tipo
  en conjunto con funciones del mismo tipo.
  
  Atributos:
    order: el orden en que se debe leer la expresion booleana.
    expr: la expresion booleana a evaluar, introducida como lista de strings.
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self, order: str, expr: list):
    self.order = order.upper()
    self.expr = expr

  # -------------- METODOS DE CLASE --------------
  def prefix(self):
    """Evalua una expresion booleana en forma prefija
    """
    # Volteamos la lista de expresiones
    expr_list = self.expr
    expr_list.reverse()

    # Pila para guardar las expresiones formadas
    stack = []

    # # Recorremos todos los elementos de la expresion en orden inverso
    for token in expr_list:
      # Verificamos si el token es un operador
      if self.isOperator(token):
        # Si es un operador, lo formamos una expresion con los ultimos tokens de la pila y evaluamos la expresion
        # Variables
        var1, var2 = stack.pop(), stack.pop()

        # Verificamos si son variables no-evaluadas (cadenas de caracteres)
        if isinstance(var1, str):
          var1 = tokens[var1.lower()]

        if isinstance(var2, str):
          var2 = tokens[var2.lower()]

        # Evaluamos la expresion
        if token == '&':
          stack.append(self.conjunction(var1, var2))
        elif token == '|':
          stack.append(self.disjunction(var1, var2))
        elif token == '=>':
          stack.append(self.implication(var1, var2))

      # Si no es un operador, ingresa a la pila
      else:
        # Consideramos el caso de la negacion
        if token == '^':
          prev_token = stack.pop()

          # Verificamos si el token es un operador, para cambiar el orden del operando
          if not self.isOperator(prev_token):
            # Verificamos el tipo de instancia de la expresion a evaluar
            if isinstance(prev_token, str):
              prev_token = tokens[prev_token.lower()]

            stack.append(self.negation(prev_token))
          else:
            stack.append(prev_token)
            stack.append(token)
        else:
          stack.append(token)
    
    # Devolvemos la expresion resultante
    if len(stack) == 1:
      return 'true' if stack[0] == True else 'false'
    else:
      raise ValueError('La expresion no es valida.')

  def postfix(self):
    """Evalua una expresion booleana en forma postfija
    """
    # Pila para guardar las expresiones formadas
    stack = []

    # Recorremos todos los elementos de la expresion en orden inverso
    for token in self.expr:
      # Verificamos si el token es un operador
      if self.isOperator(token):
        # Si es un operador, lo formamos una expresion con los ultimos tokens de la pila
        # Variables
        var1, var2 = stack.pop(), stack.pop()

        # Verificamos si son variables no-evaluadas (cadenas de caracteres)
        if isinstance(var1, str):
          var1 = tokens[var1.lower()]

        if isinstance(var2, str):
          var2 = tokens[var2.lower()]

        # Evaluamos la expresion
        if token == '&':
          stack.append(self.conjunction(var1, var2))
        elif token == '|':
          stack.append(self.disjunction(var1, var2))
        elif token == '=>':
          stack.append(self.implication(var1, var2))
        elif token == '^':
          stack.append(self.negation(var1))
          stack.append(var2)

      # Si no es un operador, ingresa a la pila
      else:

        # # Consideramos el caso de la negacion
        if token == '^':
          prev_token = stack.pop()
          # Verificamos si el token es un operador, para cambiar el orden del operando
          if not self.isOperator(prev_token):
            # Verificamos el tipo de instancia de la expresion a evaluar
            if isinstance(prev_token, str):
              prev_token = tokens[prev_token.lower()]

            stack.append(self.negation(prev_token))
          else:
            stack.append(prev_token)
            stack.append(token)
        else:
          stack.append(token)

        # stack.append(token)
    
    # Devolvemos la expresion resultante
    if len(stack) == 1:
      return 'true' if stack[0] == True else 'false'
    else:
      raise ValueError('La expresion no es valida.')

  def show_infix(self) -> str:
    """De la expresion booleana, retorna la forma infija correctamente parentizada
    """
    # Lista de expresiones
    expr_list = self.expr

    # Verificamos el order, para guardar segun el orden
    if self.order == 'PRE':
      expr_list.reverse()

    # Pila para guardar las expresiones formadas
    stack = []

    # Recorremos todos los elementos de la expresion en orden inverso
    for token in expr_list:
      # Verificamos si el token es un operador
      if self.isOperator(token):
        # Si es un operador, lo formamos una expresion con los ultimos tokens de la pila
        stack.append("( " + stack.pop() + " " + token + " " + stack.pop() + " )")
      # Si no es un operador, ingresa a la pila
      else:
        stack.append(token)
    
    if len(stack) == 1:
      return stack[0]
    else:
      raise ValueError('La expresion no es valida.')
  
  # -------------- OPERADORES --------------
  def conjunction(self, left: bool, right: bool):
    """Retorna una expresion de conjuncion evaluada
    """
    return left and right

  def disjunction(self, left: bool, right: bool):
    """Retorna una expresion de disyuncion evaluada
    """
    return left or right

  def implication(self, left: bool, right: bool):
    """Retorna una expresion de implicacion evaluada
    """
    return (not left) or right

  def negation(self, expr: bool):
    """Retorna una expresion de negacion evaluada
    """
    return not expr

  # -------------- MISCELANEA --------------
  def isOperator(self, token: str):
    """Verifica si un token de entrada es un operador booleano
    """
    return token in ['&', '|', '=>']