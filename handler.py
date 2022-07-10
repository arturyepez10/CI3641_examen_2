# ------------------------ IMPORTS ----------------------------- #
# locals
from datatypes import *

# ------------------------ HANDLER ----------------------------- #
class TypesHandler:
  """
  """

  # -------------- CONSTRUCTOR --------------
  def __init__(self) -> None:
    self.atomics : list[Atomic] = []
    self.structs : list[Struct] = []
    self.unions : list[Union] = []

    # We create a list to facilite the search of types
    self.type_names : list[str] = []

  # -------------- INICIALIZADORES --------------
  def add_atomic(self, name: str, rep: int, aligned: int) -> None:
    '''Agrega un tipo de dato atomic a la lista de tipos atomicos.
    '''
    # We verify if the atomic is already in the list
    for atom in self.atomics:
      if atom.name == name:
        raise ValueError('El tipo de dato \'' + name + '\' ya existe.')

    # We create the atomic and add it to the list
    atomic = Atomic(name, rep, aligned)

    self.atomics.append(atomic)
    self.type_names.append(name)

  def add_struct(self, name: str, struct_types: list[str]) -> None:
    '''Agrega un tipo de dato struct a la lista de tipos struct.
    '''

    # We verify if the struct is already in the list
    for st in self.structs:
      if st.name == name:
        raise ValueError('El tipo de dato \'' + name + '\' ya existe.')

    # We verify if the struct has unknown types, and if not we add them
    list = []
    for atom_name in struct_types:
      if atom_name in self.type_names:
        # We look for the atomic in the list
        for a in self.atomics:
          if a.name == atom_name:
            list.append(a)
            break

      else:
        raise ValueError('El tipo de dato \'' + atom_name + '\' contiene un tipo de dato no declarado.')

    # We create the struct and add it to the list
    struct = Struct(name, list)
    self.structs.append(struct)

  def add_union(self, name: str, struct_types: list[str]) -> None:
    '''Agrega un tipo de dato union a la lista de tipos union.
    '''

    # We verify if the union is already in the list
    for un in self.unions:
      if name == un.name:
        raise ValueError('El tipo de dato \'' + un.name + '\' ya existe.')

    # We verify if the union has unknown types, and if not we add them
    list = []
    for atom_name in struct_types:
      if atom_name in self.type_names:
        # We look for the atomic in the list
        for a in self.atomics:
          if a.name == atom_name:
            list.append(a)
            break
      else:
        raise ValueError('El tipo de dato \'' + atom_name + '\' contiene un tipo de dato no declarado.')

    # We create the union and add it to the list
    union = Union(name, list)
    self.unions.append(union)
  
  # -------------- DESCRIPTOR OF MEMORY --------------
  def describe(self, name: str):
    '''
    '''
    print(self.type_names)

    for atomic in self.atomics:
      print(atomic.name, atomic.rep, atomic.aligned)

    for struct in self.structs:
      print(struct.name)
      for atom in struct.struct_types:
        print('\t', atom.name, atom.rep, atom.aligned)

    for union in self.unions:
      print(union.name)
      for atom in union.struct_types:
        print('\t', atom.name, atom.rep, atom.aligned)
