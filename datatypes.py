# ------------------------ ATOMICO ----------------------------- #
class Atomic:
  """Representacion del modelo de dato 'ATOMICO'.

  Este modelo de dato sirve para la representacion de datos atomicos creados por el usuario.

  A su vez, permite introducir datos para la representacion en memoria de los mismos.

  Atributos y Parametros:
    name: Nombre que representa al programa.
    representation: cantidad de bytes que ocupa el programa.
    aligned: numero de bytes a los que debe alinearse el programa en la memoria.
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self, name: str, rep: int, aligned: int) -> None:
    self.name = name
    self.rep = rep
    self.aligned = aligned

  # -------------- DESCRIPTOR --------------
  def describe(self) -> list[list[str]]:
    '''Descripcion del tipo ATOMICO.
    '''
    return [[self.rep, self.aligned]]

  # -------------- DEFINICION DE STRINGS --------------
  def __str__(self) -> str:
    return self.name + ' - ' + self.rep + ' bytes - ' + self.aligned + ' bytes'

# ------------------------ STRUCT ----------------------------- #
class Struct:
  """Representacion del modelo de dato 'STRUCT'.

  Este modelo de dato sirve para la representacion de datos en un tipo registro.

  Los datos de representacion y alineacion, se calculan segun lo planteado en clase.

  Atributos y Parametros:
    name: Nombre que representa al programa.
    struct_types: Lista de tipos de datos que componen el registro, deben de ser tipo 'Atomico'.
  """

  # -------------- CONSTRUCTOR --------------
  # TODO: averiguar como es la representacion de un struct
  def __init__(self, name: str, struct_types: list[Atomic]) -> None:
    self.name = name
    self.struct_types = struct_types
    
    # We calculate the size of the struct
    self.rep = 0
    self.aligned = 0
    for type in struct_types:
      self.rep += type.rep

  # -------------- DESCRIPTOR --------------
  def describe(self) -> list[list[str]]:
    '''Descripcion del tipo STRUCT.

    Debe tomar en consideracion de los siguientes casos:
     - Registros sin empaquetar.
     - Registros con empaquetamiento.
     - Registros con reordenamiento de los campos de forma optima (minimizando la memoria, sin violar la alineación).
    '''
    return []

  # -------------- DEFINICION DE STRINGS --------------
  def __str__(self) -> str:
    return self.name + ' - ' + self.rep + ' bytes - ' + self.aligned + ' bytes'

# ------------------------ UNION ----------------------------- #
class Union:
  """Representacion del modelo de dato 'Union'.

  Este modelo de dato sirve para la representacion de datos en un tipo 'UNION', donde, el tipo
  de dato que se utiliza es uno de los indicados en la entrada.

  Los datos de representacion y alineacion, se calculan segun lo planteado en clase, es decir,
  va a coincidir con el tipo de dato con mayor representacion que se utiliza.

  Atributos y Parametros:
    name: Nombre que representa al programa.
    struct_types: Lista de tipos de datos que componen el registro, deben de ser tipo 'Atomico'.
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self, name: str, struct_types: list[Atomic]) -> None:
    self.name = name
    self.struct_types = struct_types

    # We calculate the size and alignment of the union
    self.rep = 0
    self.aligned = 0

    for type in struct_types:
      if type.rep > self.rep:
        self.rep = type.rep
        self.aligned = type.aligned
      elif type.rep == self.rep and type.aligned > self.aligned:
        self.aligned = type.aligned

  def describe(self) -> list[list[str]]:
    '''Descripcion del tipo UNION.
    '''
    return [[self.rep, self.aligned]]

  # -------------- DEFINICION DE STRINGS --------------
  def __str__(self) -> str:
    return self.name + ' - ' + self.rep + ' bytes - ' + self.aligned + ' bytes'