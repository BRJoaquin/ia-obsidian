**Informe de Proyecto: Aplicación de Técnicas Avanzadas de Aprendizaje por Refuerzo en Juegos de Múltiples Jugadores**

**Autor:** Joaquin Vigna

### Introducción

Este proyecto se enfoca en la implementación y análisis de técnicas avanzadas de aprendizaje por refuerzo, específicamente Counterfactual Regret Minimization (CFR) y Monte Carlo Tree Search (MCTS), aplicadas a juegos de información imperfecta como Kuhn Poker y Leduc Poker. Se exploran distintas configuraciones de juego, incluyendo variaciones de dos y tres jugadores, y se examina la eficacia de estas técnicas en entornos de decisión complejos y dinámicos.

### Metodología y Experimentación

#### Implementación de CFR

El algoritmo CFR se implementó para experimentar en juegos de póker, enfocándose en desarrollar y refinar estrategias en entornos de información imperfecta. Se destaca el diseño agnóstico al juego de las implementaciones de agentes, permitiendo su uso en una variedad de juegos que cumplen con los requisitos de la biblioteca PettingZoo.

#### Experimentación con Kuhn Poker

Se realizaron experimentos con Kuhn Poker, un juego de póker simplificado ideal para estudiar algoritmos de aprendizaje por refuerzo en juegos de información imperfecta. Se exploró tanto la versión clásica de dos jugadores como una variante de tres jugadores. Se utilizó CFR para desarrollar estrategias efectivas y analizar cómo los agentes aprenden y se adaptan a lo largo de múltiples juegos.

#### Kuhn Poker con 2 Jugadores

En la configuración de dos jugadores, se compararon los resultados del agente CFR contra un agente que elige acciones de manera aleatoria. Se observó que el agente CFR aprende a jugar de manera óptima en cada estado del juego, mostrando una efectividad superior a la estrategia aleatoria.

#### Kuhn Poker con 3 Jugadores

La extensión del experimento a tres jugadores introdujo una dinámica de juego adicional, requiriendo estrategias más sofisticadas. Los resultados confirmaron que el tercer jugador, al ser el último en actuar, obtenía la mayor utilidad, seguido del segundo jugador y finalmente el primer jugador.

### Estimación de Valor de Estados

Dada la complejidad de algunos juegos, se utilizó la estimación de valor de estados para evaluar la calidad de los estados del juego en profundidades específicas. Se implementaron funciones de evaluación y se aplicó MCTS para manejar eficientemente juegos con un espacio de estado extenso.

### CFR con Estimación de Valor y MCTS en Leduc Poker

Se aplicó MCTS en Leduc Poker, un juego con mayor complejidad estratégica que Kuhn Poker. Los experimentos mostraron que el agente MCTS superó consistentemente a los agentes que toman decisiones aleatorias, demostrando la efectividad de MCTS en este contexto.

### Conclusiones

Este proyecto ha establecido una base sólida para el uso de técnicas avanzadas de aprendizaje por refuerzo en juegos alternados de múltiples jugadores. Los principales logros incluyen:

- Implementación exitosa del algoritmo CFR en Kuhn Poker.
- Demostración de la eficacia de MCTS en Leduc Poker.
- Observaciones clave sobre la eficacia de las funciones de evaluación y la importancia de equilibrar la exploración y explotación en MCTS.

Mirando hacia el futuro, hay varias direcciones emocionantes para continuar este trabajo, incluyendo la comparación con agentes más avanzados, la optimización de algoritmos y la aplicación en otros juegos de información imperfecta.