
# EXAMEN 2 | CI3641
### Arturo Yepez 15-11551

## Descripcion del Examen

Para el examen se requirio que algunas de las preguntas fueran programas. Para ello, las condiciones fueron que se llevaran a cabo en un repositorio de GitHub y fuera compartido con el profesor.

El grupo de preguntas que debian de ser resueltas mediante una solucion de programacion, fueron:

1. (1-b) Se debian de implementar los siguientes programas:
  i. Defina un tipo de datos recursivo que represente numerales de Church.
  ii. Defina un árbol binario con información en ramas y hojas.
1. (2) Modelado e implementacion de un programa que simule un manejador expresiones booleanas.
1. (3-c) Modelado e implementacion de un programa que genere todas las expresiones *bien parentizadas* posibles.
1. (4) Modelado e implementacion de un programa que cumpla con la definicion de una familia de funciones.
1. (5) En base a lo visto en clases, modelar e implementar un programa que simule un
manejador de tipos de datos.

## Respuestas

Las respuestas fueron alojadas en diferentes ramas del repositorio. Las ramas disponibles son:

- `pregunta-1`: Contiene la solucion a las preguntas 1(b).
- `pregunta-2`: Contiene la solucion a la pregunta 2.
- `pregunta-3`: Contiene la solucion a la pregunta 3(c).
- `pregunta-4`: Contiene la solucion a la pregunta 4.
- `pregunta-5`: Contiene la solucion a la pregunta 5.

En cada una de las ramas, se pueden encontrar los archivos que forman su respectiva respuesta y ademas, en este mismo archivo se extiende para presentar una descripcion del problema, detalles de la implementacion y formas de uso.

---

## Manejador de Tipos de Datos

Para esta pregunta se utilizo el lenguaje de programacion `Python`.

Dado que el ejercicio requiere una interfaz que permita de forma interactiva ingresar comandos, se hizo la implementacion utilizando principios del paradigma de programacion orientado a objetos. Donde, entre las librerias de `Python`, se encuentra una que se puede utilizar para simular una `CMD` o `SHELL` al correr el script, totalmente personalizable.

<!-- TODO: resto de la documentacion -->

Para correr el programa, simplemente hay que ejecutar el siguiente comando desde el directorio del repositorio:
```
python run.py
```

Esto da inicio al simulador de `REPL`, donde se pueden utilizar los comandos descritos en los requerimientos del programa.

### Pie de Pagina

- En el REPL, todos los comandos son ajenos a __"case insensitive"__.

- Si te sientes agobiado por la cantidad de informacion, prueba a utilizar el comando `clear` :)

- Si quieres conocer la documentacion de un comando, simplemente escribe `help <comando>` en el REPL, o `help`/`?` para conocer la lista de comandos.