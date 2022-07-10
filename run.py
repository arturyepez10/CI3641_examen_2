# ------------------------ IMPORTS ----------------------------- #
# libraries
from sys import argv

# locals
from shell import TypesHandlerCMD

# ------------------------ INIT ----------------------------- #
if __name__ == '__main__':
  if len(argv) == 1:
    pass
    repl = TypesHandlerCMD()

    repl.cmdloop()
  else:
    raise ValueError('Necesita 1 parametros.')