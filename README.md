# PreguntaBits
Juego de preguntas de opción múltiple para la enseñanza de lógica de computación

Universidad Autónoma Metropolitana
Unidad Cuajimalpa

Tecnologías y Sistemas de la Información
Trimestre: 20-I

UEA: Laboratorio Temático 4

Proyecto: Videojuego para la enseñanza de la programación

Jurado: Jaime Gonzales Carlos Roberto y Luna Ramirez Wulfrano Arturo

Alumno: Ayala De La Rosa José Daniel (2173071015)
Título del juego: PreguntaBits
Objetivo del aprendizaje: Aprender y mejorar la lógica de programación por medio de preguntas sencillas de opción múltiple en contra reloj, el usuario aprenderá por medio de prueba y error al seleccionar la respuesta correcta a las preguntas y memorizando mejorará su habilidad para encontrar nuevas formas de resolver problemas.
Nivel educativo: Este juego es para estudiantes nuevos en el mundo de la programación (no hay una edad mínima ya que hay niños que aprenden a programar antes del bachillerato pero dado que hay muchas escuelas preparatorias con carreras técnicas donde se enseña a programar se recomienda que sea el usuario mayor a 1ro de bachillerato)
Metodología: El proyecto se hizo tomando en cuenta como base “El manifiesto del desarrollo ágil”
Individuals and interactions over processes and tools
Working software over comprehensive documentation
Customer collaboration over contract negotiation
Responding to change over following a plan
Ya que el proyecto es individual (evitando los problemas de comunicación entre integrantes), el tiempo de desarrollo es muy limitado, no hay una retroalimentación directa con los evaluadores y no hay tantas decisiones de cambio de diseño, se tomó en cuenta el principio de Working software over comprehensive documentation como el más importante y se hizo un desarrollo iterativo incremental, empezando con el módulo que se cree más importante (Explicación más adelante), siempre pensando en la escalabilidad del proyecto.
Bitácora de desarrollo:

Iteración 0: 
Se hizo un análisis de:
-Cuáles serían las metas alcanzables para el proyecto (Tener 2 niveles completos Tutorial y Nivel 0)
-Se dividió el proyecto en módulos (Módulo “MENU” que contendrá 2 opciones Niveles y Puntajes, estos corresponden a los Módulos “GAMES” y “SCORES” respectivamente, el primer Módulo contendrá los 2 niveles completos y el segundo módulo contendrá una lista de los mejores 10 puntajes)
-Se definió la estética del juego completo (Paleta de colores, colores de los elementos, distribución de elementos en pantalla y fuente)
-Se definió cuál sería la arquitectura (Web service REST/API)
-Las tecnologías a usar (Flask con python para backend y HTML/JS/CSS/Bootstrap para frontend)
-Y se seleccionó el módulo más importante (Módulo “GAMES” con el Nivel “Tutorial”).

Al final de esta iteración se espera tener la mitad del Módulo “GAMES”, donde se pueda acceder a los diferentes niveles (en este caso el tutorial) por medio de un menú y al seleccionar el nivel este se ejecute.

Iteración 1
No se logró terminan el módulo más importante  de la iteración pasada pero se terminaron otros aspectos que resultaron necesarios para la implementación del módulo como lo fueron el creador de niveles (Un pequeño script que ayuda a homogeneizar la información en la base de datos “levels.txt”.
Se planea:
-terminar para esta iteración el módulo más importante -agregar las funcionalidades de cambiar entre módulos las cuales se implementaron ayer
-terminar gran parte de la documentación a entregar

Al final de la iteración se espera tener el videojuego terminado en un 80%, por cuestiones de tiempo el módulo SCORES no será implementado

Iteración 2
Se logró la meta del módulo anterior pero con varios bugs, entonces se logró un 80% de la meta anterior
Se planea para este módulo:
-Eliminar los bugs visuales
-Agregar un temporizador para el tiempo y el refresco de los elementos en pantalla
-Actualizar todo el proyecto en github
-Hacer el vídeo de presentación del proyecto
-Terminar de agregar los elementos faltantes a la documentación

Fin de las iteraciones:
Fué un reto interesante hacer un proyecto en un periodo de tiempo tan limitado (2 días y unas horas del día de la inscripción de la recuperación hasta sú día de entrega a las 10 am)
Creo que hay potencial si no en el cliente, en el servicio y cómo entrega la información a quienes hacen las peticiones
Me hubiera gustado tener más tiempo para agregar perfiles y así poder implementar el módulo de SCORES
Debo de mejorar mis habilidades con el manejo de elementos visuales en pantalla porque fué lo que más consumió tiempo
Tal vez sería mejor implementar el servicio en node.js para homogeneizar aún más el proyecto o inclusive a un lenguaje más robusto como C#, aunque no tengo quejas con python, hizo el desarrollo muy sencillo
Las cosas que más se me complicaron y en las cuales invertí más tiempo fueron en el levantamiento de requerimientos y el diseño del sistema (estetica y funcionalmente) porque si no pensaba bien el diseño eso traería problemas en la mitad de laguna de las iteraciones pero creo fueron acertadas las elecciones
También como ya lo mencioné, aunque se vea sencillo el cliente fué el que más me costó trabajo, tal vez porque trate de hacer un SPA (Single Page Application) y nunca había intentado algo así sin un framework JS, entonces también la diseño de funcionalidad fué algo que no contemple en el primer diseño, entonces fué una mala práctica ir diseñando y desarrollando pero el tiempo lo tenía encima como para hacer documentación de ello, así que sólo modularice todo para abstraer el probelmas en problemas pequeños.




Justificación: Los videojuegos como medio de aprendizaje en su mayoría fallan en su componente principal “ser un videojuego” lo cual casi siempre los convierte en un rotundo fracaso ya que el objetivo de un video es ser jugado sea por el motivo que fuere (la historia, la jugabilidad, pasatiempo, ocio, etc) y esto se debe (en mi parecer como jugador de videojuegos) a que se centra todo en adaptar una UEA a un software parecido a un videojuego, cuando en realidad lo que buscamos (los videojugadores) muchas veces es pasar un buen rato, divertirnos y olvidarnos un rato de nuestra realidad para sumergirnos en otra, juegos como assassin's creed con su historia, call of duty con sus elementos del entorno (armas y contexto histórico) e inclusive minecraft con su crafteos nos demuestran que el aprendizaje es una consecuencia de una buena jugabilidad, capturar la atención del videojugador y una buena elección de elementos complementarios para la enseñanza (la historia, las armas y los crafteos).
En el libro “Abre tu mente a los números” de Barbara Oakley se explica el proceso por el cual el ser humano aprende y el libro ofrece una pequeña guía o referencia de cómo podemos teóricamente aprender cualquier cosa indiferentemente si es o no nuestra área predilecta de estudio o interés, dentro de todos los puntos que se tocan quiero hacer énfasis en 3 la constancia, la repetición y la memorización.
Las primeras dos van tan pegadas de la mano que pueden parecer lo mismo pero la constancia nos habla de hacer una actividad si no diaria, la mayor de cantidad de veces posible dentro de un periodo determinado y la repetición explica el como una tarea que repetimos muchas veces nos puede ayudar tener una maestría, la maestría se gana conforme a la memorización de acciones, patrones o respuestas, permitiendo a nuestro cerebro acceder de manera fácil y rápida a una actividad tan marcada en nuestro memoria, estos tres elementos se encuentran muy seguido en los videojuegos, la constancia es más una consecuencia del poder de convencimiento del videojuego sobre el videojugador, pero la repetición y como consecuencia la memorización de actividades o conceptos está tan arraigada que no la vemos como una característica destacable si no como algo natural en los videojuegos (mata 20 jabalíes, talar 10 árboles,  habla con cierto personaje, se muestra en pantalla el nombre de un hechizo, el score o la puntuación por hacer una actividad, crear o craftear cierta cantidad de objetos usando cierto patrón de creación, poner en los diálogos de los personajes secundarios todo el tiempo del protagonista o del objetivo e inclusive saber que el jefe final no tiene una sola vida) hace que el usuario de manera consciente o inconscientemente aprenda las características del videojuego.
Estos aspectos (el fin del videojuego como un medio de entretenimiento, los elementos de aprendizaje como objetos complementarios y la forma en la que aprende el humano por medio de la repetición y la memorización) los usé y creo deberían de usarse como principios básicos para hacer videojuegos orientados al aprendizaje.
También usé estos principios porque he visto que la mayoría de videojuegos hoy en día son tan efímeros (hablando que la comunidad de videojugadores ha crecido gracias al uso de smartphones y ya no se consumen tanto en consolas de sobremesa si no en sus dispositivos para pasar el rato o como interludio) pero creo son muy pocos los que tiene éxito (ser jugados por muchos usuarios) y dejan algún aprendizaje útil en el usuario más allá de entender una historia de fantasía o elementos surrealistas (no desmerito ningún juego porque todos a su modo enseñan algo sólo que el propósito de los videojuegos orientados al aprendizaje es que sean usados como herramientas auxiliares o complementarias en la educación) y los 2 juegos en los que me basé creo cumplen el éxito y la enseñanza, como consecuencia satisfacen la necesidad de tener un videojuego que ayude en la enseñanza de nociones básicas de la lógica de programación (estructuras condicionales).
Características: Para este proyecto se tienen contemplados 2 niveles:
Tutorial: Aquí se enseñará el funcionamiento del videojuego y cómo interactuar con él, sin ninguna repercusión en la puntuación del videojugador.
Nivel 0: Aquí se dará una introducción a la condicional if junto con el uso del operador lógico de comparación.











Manual técnico:
Documentación de análisis:
Se dividió el proyecto en módulos (Módulo “MENU” que contendrá 2 opciones Niveles y Puntajes, estos corresponden a los Módulos “GAMES” y “SCORES” respectivamente, el primer Módulo contendrá los 2 niveles completos y el segundo módulo contendrá una lista de los mejores 10 puntajes)
-Se definió la estética del juego completo (Paleta de colores, colores de los elementos, distribución de elementos en pantalla y fuente)

Arquitectura:

Las tecnologías escogidas para la implementación de esta arquitectura fueron Flask (Python) para el servicio y HTML/CSS/JS para el cliente

Estética:
Se usó como inspiración el juego de PAC-MAN para la selección de colores, lo cual dará una sensación de familiaridad y al ser una paleta sencilla, no rompe reglas de usabilidad básica.


REST / API:
Requerimientos:
Python en versión superior a 3.7

Herramientas y dependencias:
Flask (Framework de python para desarrollo web
Cors (Librería que ayuda a evitar los problemas acceso cruzado)
Bootstrap (Librería de CSS para diseñar de manera rápida y sencilla interfaz web)

Código del proyecto:
https://github.com/MrQuadBit/PreguntaBits

Manual de usuario:
Pregunta Bits es un juego web que te desiafará a responder preguntas sobre lógica de programación, en contra reloj, no te preocupes si fallas, ese es el objetivo del juego que aprendas de tus errores y conforme te encuentres  preguntas nuevas y no conozcas la respuesta puedas aprender nuevas soluciones que antes no conocía.
Para aprender a como jugar hemos preparado un pequeño tutorial, sólo inicia el servicio, ejecuta el cliente y dirígete a la opción de Niveles > Turorial y que empiece el juego.
Si quieres ver un vídeo explicativo de todo el proyecto y como jugar revisa el siguiente link: https://youtu.be/Af46lUoGDb4

Evaluación:
Siendo completamente honesto creo que el sistema funciona como herramienta para lograr un aprendizaje pero sólo como herramienta, se necesita de personas más especializadas en pedagogía para que este sistema funcione y cumpla el objetivo principal. 
Código:
https://github.com/MrQuadBit/PreguntaBits
Vídeo demo del juego:
https://youtu.be/Af46lUoGDb4


