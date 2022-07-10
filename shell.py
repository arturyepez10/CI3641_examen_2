# ------------------------ IMPORTS ----------------------------- #
# libraries
from cmd import Cmd
from textwrap import dedent
import os
import re

# locals
from handler import TypesHandler
from utils.constants import *

# ------------------------ REPL ----------------------------- #
class TypesHandlerCMD(Cmd):
  """
  """

  prompt = f'{GREEN}accion => {RESET}{BOLD}'

  # Mensajes de la REPL
  intro = (f'¡Bienvenido al CMD del Manejador de Tipos!\n'
    'Utiliza "?" para mostrar los comandos disponibles.')
  doc_header = ('''Lista de comandos basicos (escribe 'help <nombre>' '''
    'para informacion detallada)')
  misc_header = ('''Lista de funciones disponibles (escribe 'help '''
    '''<nombre>' para informacion detallada)''')

  def __init__(self):
    # Llama el constructor de la superclase e inicializa la máquina virtual
    Cmd.__init__(self)
    self.handler = TypesHandler()

  # -------------- MÉTODOS QUE ENVIAN AL MANEJADOR --------------
  def send_atomico(self, command: str):
    """Envía un comando al manejador, para definir a un tipo atomico.

    El manejador procesa la entrada y define segun el tipo requerido, o indica error en caso de haber.
    """

    try:
      [name, rep, aligned] = command.split(' ')

      self.handler.add_atomic(name, int(rep), int(aligned))

      self.handle_output(f'Tipo ATOMICO \'{name}\' definido.')
    except ValueError as ex:
      self.handle_output('ERROR: ' + str(ex))


  def send_struct(self, command: str):
    """Envía un comando al manejador, para definir a un tipo STRUCT.

    El manejador procesa la entrada y define segun el tipo requerido, o indica error en caso de haber.
    """

    try:
      [name, *fields] = command.split(' ')

      self.handler.add_struct(name, fields)

      self.handle_output(f'Tipo STRUCT \'{name}\' definido.')
    except ValueError as ex:
      self.handle_output('ERROR: ' + str(ex))

  def send_union(self, command: str):
    """Envía un comando al manejador, para definir a un tipo UNION.

    El manejador procesa la entrada y define segun el tipo requerido, o indica error en caso de haber.
    """

    try:
      [name, *fields] = command.split(' ')

      self.handler.add_union(name, fields)

      self.handle_output(f'Tipo UNION \'{name}\' definido.')
    except ValueError as ex:
      self.handle_output('ERROR: ' + str(ex))

  def send_describir(self, command: str):
    """Envia un comando al manejador para describir uno de los tipos definidos.
    
    El manejador procesa la entrada y define segun el tipo requerido, o indica error en caso de haber.
    """

    try:
      out = self.handler.describe(command)

      # self.handle_output(f'Tipo \'{command}\' descrito.')
    except ValueError as ex:
      self.handle_output('ERROR: ' + str(ex))

  # -------------- COMANDOS DE DOCUMENTACION DE COMANDOS EN REPL --------------
  def help_atomico(self):
    print(dedent('''
      Aplica al manejador de tipos, para definir un tipo ATOMICO.

      El manejador se encarga de procesar la entrada para enviarlo a la instancia
      del manejador de tipos. En caso de error, se le notifica al usuario el problema.

      Este modelo de dato sirve para la representacion de datos en un tipo atomico, con su
      representacion y alineacion en bytes.

      Su ejecucion se realiza mediante:
      >>> ATOMICO <nombre> <representacion> <alineacion>'''))

  def help_struct(self):
    print(dedent('''
      Aplica al manejador de tipos, para definir un tipo STRUCT.

      El manejador se encarga de procesar la entrada para enviarlo a la instancia
      del manejador de tipos. En caso de error, se le notifica al usuario el problema.

      Este modelo de dato sirve para la representacion de datos en un tipo registro.

      Su ejecucion se realiza mediante:
      >>> STRUCT <nombre> [<tipos>]'''))

  def help_union(self):
    print(dedent('''
      Aplica al manejador de tipos, para definir un tipo UNION.

      El manejador se encarga de procesar la entrada para enviarlo a la instancia
      del manejador de tipos. En caso de error, se le notifica al usuario el problema.

      Este modelo de dato sirve para la representacion de datos en un tipo union.

      Su ejecucion se realiza mediante:
      >>> UNION <nombre> [<tipos>]'''))

  def help_describir(self):
    print(dedent('''
      Aplica al manejador de tipos, para describir uno de los tipos definidos.

      El manejador se encarga de procesar la entrada para enviarlo a la instancia
      del manejador de tipos. En caso de error, se le notifica al usuario el problema.

      Esta información debe incluir, tamaño, alineación y cantidad de bytes desperdiciados
      para el tipo, si:
        • El lenguaje guarda registros y registros viariantes sin empaquetar.
        • El lenguaje guarda registros y registros viariantes empaquetados.
        • El lenguaje guarda registros y registros viariantes reordenando los campos de
        manera óptima (minimizando la memoria, sin violar reglas de alineación).

      Su ejecucion se realiza mediante:
      >>> DESCRIBIR <nombre>'''))

  # -------------- MÉTODOS SUPERCLASE CUSTOMIZADOS --------------

  def cmdloop(self, intro = None):
    """Ver clase base. Agrega manejo de interrupciones del teclado."""
    print(self.intro)
    while True:
      try:
        super(TypesHandlerCMD, self).cmdloop(intro='')
        break
      except KeyboardInterrupt:
        self.handle_output(f'\n(Para salir, utiliza el comando SALIR o escribe .)')

  def do_exit(self, line: str) -> bool:
    """Finaliza el CMD/REPL de BuddySystem. Retorna True.
    
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
    elif self.match_command('ATOMICO', line):
      command = line[7:].strip()
      self.send_atomico(command)
    elif self.match_command('STRUCT', line):
      command = line[6:].strip()
      self.send_struct(command)
    elif self.match_command('UNION', line):
      command = line[5:].strip()
      self.send_union(command)
    elif self.match_command('DESCRIBIR', line):
      command = line[9:].strip()
      self.send_describir(command)
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