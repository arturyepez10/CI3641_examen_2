
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

## FAMILIA DE FUNCIONES

Para esta pregunta se utilizo el lenguaje de programacion `Python`. Este lenguaje escogido, es uno considerado imperativo, con estructuras de control tales como: **seleccion**, **repetición**, **recursión**, etc. 

La implementación de esta pregunta debe utilizar los valores de `alpha` y `beta` dependientes de `X`, `Y` y `Z` (definidos para cada uno de los estudiantes del parcial) para definir una funcion las constantes que terminan de definir a la familia de funciones. Asi entonces, en el contexto actual, esos valores terminaron siendo:
```
alpha = (( X + Y) mod 5) + 3 = ((5 + 5) mod 5) + 3 = (10 mod 5) + 3 = 0 + 3 = 3
beta = ((Y + Z) mod 5) + 3 = ((5 + 1) mod 5) + 3 = (6 mod 5) + 3 = 1 + 3 = 4
```

Dada la definicion de una familia de funciones en el enunciado, se pidio la implementación de esa función en un lenguaje de programación imperativo de varias formas. Las implementaciones debian ser:

1. Una subrutina recursiva que calcule la familia de funciones para los valores de `alpha` y `beta` correspondientes. Esta implementación debe ser directa de la formula resultante a código.
1. Una subrutina recursiva **de cola** que calcule a la familia de funciones.
1. La conversión de la familia de funciones a una version iterativa, mostrando los componentes de la implementacion recursiva que corresponden a cuales otras de la implementación iterativa.

Las 3 implementaciones se pueden encontrar en el archivo `answer.py`.

Ahora, para cada implementación:

### Recursiva

Tal como los requisitos de la pregunta, se implementó como una traducción directa de la formula resultante a código.

### Recursión de Cola

Como se vio en clases, la traducción de una función recursiva a una recursión de cola no necesariamente es trivial. Este caso es un ejemplo de ello.

Una de las características de esta familia de funciones, es que uno de sus casos particulares (`alpha = 2` y `beta = 1`) forma la familia de funciones que calcula el numero de Fibonacci, y ese es un caso que hemos visto multiples veces como recursión de cola. Por lo tanto, se "generalizo" la implementación para que soportara el caso actual.

De allí, se obtiene el resultado actual.

### Iterativa

Para esta implementación, se tomaron los siguientes pasos:

1. Sabemos que esta version debe iterar sobre una verificación antes de retornar el valor. Identificamos en la recursión de cola que este valor es cuando un `counter` sea menor a cero, por lo que imitamos ese comportamiento. ¿Por qué cuando el contador sea menor a cero? Porque es el único caso donde la recursión de cola se detiene. Así entonces, se crea una iteración `while` con sus variables asociada y en cada iteración se disminuye en uno el contador.
1. En el caso de seguir la iteración, tal como vimos en clase reemplazamos la llamada recursiva por una asignación de valores a las variables de la iteración.
1. Retornamos el valor principal sobre el que asignamos en la iteración.

El resultado final se puede ver en el archivo de implementación.

### Análisis Comparativo de Desempeño

En el siguiente enlace podemos encontrar un análisis comparativo de desempeño de las 3 implementaciones: [análisis](https://docs.google.com/spreadsheets/d/1iVFOtNFWt6g_Jmi5JvUIRtw8FVY80UDIHLjtlmwEID0/edit?usp=sharing).

Dado que el autor realizó el desarrollo en Windows, se utilizo el siguiente comando para hacer la recolección de valores medicion de desempeño:

```
Measure-Command { // python answer.py // }
``` 

Esto se hizo realizando la medición alternando entre las llamadas de las distintas funciones. Los valores de `n` para los que se recolectó información fueron: `10`, `50`, `100`, `100000` y `10000000`. En el análisis comparativo, podemos ver distintas gráficas que muestran las diferencias de las implementaciones (sobre los promedios de 5 valores obtenidos en la ejecución), y la tendencia de las mismas para mayor cantidad de valores.

Para el caso de los últimos 2 valores, solo pudieron aplicar al caso de la recursión de cola, por lo que se omitieron en los otros dos. Esto, debido a que en el caso de la recursión y la iteración, la ejecución de la función no arroja resultado despues de varios minutos.