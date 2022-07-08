# ------------------------ IMPORTS ----------------------------- #
# libraries
from cmd import Cmd
from textwrap import dedent
import os
import re

# locals
from utils.constants import *
from BooleanExpression import BooleanExpression

# ------------------------ REPL ----------------------------- #
class BooleanExpressionCMD(Cmd):
  """Intérprete de línea de comandos para el cliente del manejador de expresiones booleanas.
    
  Aplica los métodos principales para la REPL de BooleanExpression. Utiliza los métodos
  base de Cmd, personalizados para ofrecer las funcionalidades especificadas.
  """

  prompt = f'{GREEN}accion => {RESET}{BOLD}'

  # Mensajes de la REPL
  intro = (f'¡Bienvenido a la CMD del manejador de Expresiones Booleanas!\n'
    'Utiliza "?" para mostrar los comandos disponibles.')
  doc_header = ('''Lista de comandos basicos (escribe 'help <nombre>' '''
    'para informacion detallada)')
  misc_header = ('''Lista de funciones disponibles (escribe 'help '''
    '''<nombre>' para informacion detallada)''')
  
  def __init__(self):
    # Llama el constructor de la superclase e inicializa la máquina virtual
    Cmd.__init__(self)

  # -------------- MÉTODOS QUE ENVIAN AL HANDLER --------------
  def send_evaluate(self, command: str):
    """
    """

    try:
      # Verificamos si existe mala sintaxis en el <orden>
      if not (self.match_command('PRE', command) or self.match_command('POST', command)):
        raise ValueError('El orden debe ser PRE (pre-fijo) o POST (post-fijo).')

      # Entrada decompuesta como arreglo
      [order, *expr] = command.split(' ')

      # Verificamos si existen al menos dos argumentos
      if len(expr) < 1:
        raise ValueError('Faltan argumentos.')

      # Creamos la expresion booleana
      bool_expr = BooleanExpression(order, expr)

      if self.match_command('PRE', command):
        out = bool_expr.prefix()
      else:
        out = bool_expr.postfix()

      self.handle_output(out)
    except ValueError as ex:
      self.handle_output('ERROR: ' + str(ex))
    except IndexError:
      self.handle_output('ERROR: Expresion incorrecta.')

  def send_show(self, command: str):
    """
    """

    try:
      # Verificamos si existe mala sintaxis en el <orden>
      if not (self.match_command('PRE', command) or self.match_command('POST', command)):
        raise ValueError('El orden debe ser PRE (pre-fijo) o POST (post-fijo).')

      # Entrada decompuesta como arreglo
      [order, *expr] = command.split(' ')

      # Verificamos si existen al menos dos argumentos
      if len(expr) < 1:
        raise ValueError('Faltan argumentos.')

      # Creamos la expresion booleana
      bool_expr = BooleanExpression(order, expr)

      # Obtenemos la expresion en infija
      out = bool_expr.show_infix()

      self.handle_output(out)
    except ValueError as ex:
      self.handle_output('ERROR: ' + str(ex))
    except IndexError:
      self.handle_output('ERROR: Expresion incorrecta.')

  # -------------- COMANDOS DE DOCUMENTACION DE COMANDOS EN REPL --------------
  def help_mostrar(self):
    print(dedent('''
      Pide al manejador de Expresiones Boolenas que imprima de forma infija una expresion.

      El manejador se encarga de procesar la entrada, y retorna la expresion de entrada como infija.

      Su ejecucion se realiza mediante:
      >>> MOSTRAR <orden> <expr>'''))

  def help_eval(self):
    print(dedent('''
      Pide al manejador de Expresiones Boolenas que evalue una expresion.

      El manejador se encarga de procesar la entrada, y retorna la expresion de entrada evaluada.

      Su ejecucion se realiza mediante:
      >>> EVAL <orden> <expr>
      '''))

  # -------------- MÉTODOS SUPERCLASE CUSTOMIZADOS --------------
  def cmdloop(self, intro = None):
    """Ver clase base. Agrega manejo de interrupciones del teclado."""
    print(self.intro)
    while True:
      try:
        super(BooleanExpressionCMD, self).cmdloop(intro='')
        break
      except KeyboardInterrupt:
        self.handle_output(f'\n(Para salir, utiliza el comando SALIR)')

  def do_exit(self, line: str) -> bool:
    """Finaliza el CMD/REPL de BooleanExpressionCMD. Retorna True.
    
    Se puede ejecutar de dos maneras:
      >>> exit
      >>> SALIR
    """
    return True

  def do_clear(self, line: str):
    """Limpia la pantalla de la terminal de los comandos anteriores."""
    command = 'clear'

    # Si el SO es Windows, cambia el comando
    if os.name in ('nt', 'dos'):
      command = 'cls'
    os.system(command)

  def emptyline(self) -> bool:
    """Procesador de lineas en blanco. Retorna False.
    
    El comportamiendo por defecto es no hacer nada.
    """
    return False

  def default(self, line: str) -> None:
    """Procesador de entrada por defecto.

    Retorna:
      True si se termina la ejecucion de la VM.
      None cuando se interpreta un comando e imprime su salida.
    """

    if self.match_command('SALIR', line):
      return self.do_exit(line)
    elif self.match_command('EVAL', line):
      command = line[4:].strip()
      self.send_evaluate(command)
    elif self.match_command('MOSTRAR', line):
      command = line[7:].strip()
      self.send_show(command)
    else:
      self.handle_output('ERROR: comando no reconocido (\'' + line + '\').')
  
  # -------------- MISCELÁNEA --------------

  def handle_output(self, line: str, color: str = BLUE, end = '\n'):
    """Imprime con un color en específico los resultados de la REPL al
    usuario.
    """
    # Si es un error, se imprime de rojo y se guarda la tupla con información
    if line.startswith('ERROR:'):
      color = RED

    print(f'{RESET}{color}{line}{RESET}', end=end)

  def match_command(self, name: str, line: str) -> bool:
    '''Retorna un booleano indicando si la línea contiene un comando.
    
    Argumentos:
      name: Nombre del comando magico.
      line: Línea a analizar.
    '''
    return bool(re.match(f'{name}($| )', line, re.IGNORECASE))