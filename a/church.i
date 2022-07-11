/*--------------- NUMERO DE CHURCH ---------------*/
struct Church {
  int is_cero;
  pointer next;
  /*
    Es equivalente decir que el tipo de hijo_izq es Church*, a decir que
    el next es un "pointer".

    Esto demuestra que el tipo "pointer" es el mismo para todo tipo de dato.
  */
}

/*--------------- OPERACIONES ---------------*/
func suma(numero1, numero2) {
  if (numero1->is_cero || numero1->next == NULL) {
    return numero2;
  }

  numero2->next = numero1
  return suma(numero1->next, numero2)
}

func multiplicacion(numero1, numero2) {
  if (numero1->is_cero || numero1->next == NULL) {
    return numero1;
  }

  aux = numero1
  while (numero1->next != NULL) {
    numero2 = suma(aux, numero2)

    aux = numero1->next;
  }

  return multiplicacion(numero1->next, numero2)
}