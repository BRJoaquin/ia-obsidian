Un Proceso de Decisión de Markov (MDP, por sus siglas en inglés) es un modelo matemático que describe cómo un [[Agente]] toma decisiones en un [[Entorno]] incierto y dinámico. En términos simples, un MDP es como un juego en el que un jugador (el agente) interactúa con un mundo que cambia y debe tomar decisiones para lograr un objetivo, como ganar puntos o completar una tarea.

El MDP se compone de cuatro elementos principales:

1.  Estados: son las diferentes situaciones o configuraciones en las que puede encontrarse el agente dentro del entorno. Véase [[Estado]]
2.  Acciones: son las posibles decisiones o movimientos que el agente puede realizar en cada estado. Véase [[Acción]]
3.  Transiciones: son las probabilidades de pasar de un estado a otro, dada una acción específica. Véase [[Transición]]
4.  Recompensas: son los puntos o beneficios que el agente recibe al realizar acciones en el entorno. Véase [[Recompensa]]

El agente toma decisiones basándose en su conocimiento actual del entorno y las recompensas asociadas a las acciones. El objetivo del agente es encontrar una política óptima ([[Política#Política optima]]), que es una estrategia para seleccionar acciones en cada estado de manera que maximice el valor total de las recompensas a lo largo del tiempo.

Un aspecto clave de los MDP es que tienen **la propiedad de Markov**, lo que significa que **el estado actual del entorno contiene toda la información necesaria para decidir la acción óptima**, sin importar cómo llegamos a ese estado. En otras palabras, el pasado no importa y sólo necesitamos considerar el estado presente para tomar decisiones.

