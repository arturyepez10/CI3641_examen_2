# ------------------------ IMPORTS ----------------------------- #
# libraries
from sys import argv

# locals
from shell import BooleanExpressionCMD

# ------------------------ INIT ----------------------------- #
if __name__ == '__main__':
  if len(argv) == 1:
    repl = BooleanExpressionCMD()

    repl.cmdloop()
  else:
    raise ValueError('La ejecucion no recibe argumentos extra.')