﻿# Python-FreeGames_Actividad-2
Snake Recuperado de Grant Jenkins Código original http://www.grantjenks.com/docs/freegames/snake.html

Autores Jorge E. Turner Escalante Manuel Camacho Padilla

Modificaciones
Buscamos hacer el juego menos monótono e incrementar la dificultad, por lo que se cambió la selección de colores
y el comportamiento de la comida.

Jorge:
Se agregó la función color que toma índices aleatorios de la lista color_list y se los asigna al color del cuerpo de la 
serpiente y al de la comida al inicio del juego. De esta manera al iniciar el juego, tendrán colores diferentes cada vez.

Manuel:
En la función move se agregaron dos líneas cada una encargada (x, y) de mover un espacio hacia una dirección aleatoria 
la posición de la comida. Esta acción se realiza cada vez que la función move es llamada.
