/*--------------- TIPO DE ARBOL ---------------*/
struct Arbol {
  long valor;
  pointer hijo_izq, hijo_der;  
  /*
    Es equivalente decir que el tipo de hijo_izq es Arbol*, a decir que
    el hijo_izq es un "pointer".

    Esto demuestra que el tipo "pointer" es el mismo para todo tipo de dato.
  */
}

/*--------------- FUNCION PARA HEAP SIMETRICO ---------------*/
func esMaxHeapSimétrico(arbol) {
  if (arbol->hijo_izq == NULL && arbol->hijo_der == NULL) {
    return true;
  }

  if (arbol->hijo_izq != NULL) {
    return (arbol->valor >= arbol->hijo_izq->valor &&
            esMaxHeapSimétrico(arbol->hijo_izq));
  }

  if (arbol->hijo_der != NULL) {
    return (arbol->valor >= arbol->hijo_der->valor &&
            esMaxHeapSimétrico(arbol->hijo_der));
  }

  return false;
}