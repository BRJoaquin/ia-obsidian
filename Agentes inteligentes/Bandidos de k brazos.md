El problema de los bandidos de k brazos (k-armed bandit problem, en inglés) es un problema clásico en el campo del aprendizaje por refuerzo y la teoría de la toma de decisiones. El nombre proviene de la analogía con una máquina tragamonedas (también conocida como "bandido de un brazo"), pero en este caso, la máquina tiene k brazos en lugar de uno solo.

El problema se describe de la siguiente manera: se tiene una máquina con k palancas (brazos) para jalar. Cada vez que se jala una palanca, se obtiene una recompensa aleatoria de una distribución específica para esa palanca. Las distribuciones de recompensa son diferentes para cada brazo y son desconocidas por el agente. El objetivo es encontrar una estrategia para jalar las palancas de manera que se maximice la recompensa acumulada en un número determinado de intentos.

Este problema ilustra el dilema fundamental de la exploración versus la explotación en el aprendizaje por refuerzo:

-   [[Exploración]]: El agente debe jalar diferentes palancas para obtener información sobre las distribuciones de recompensa y descubrir cuál es la mejor opción.
-   [[Explotación]]: Una vez que el agente tiene alguna información, debe jalar la palanca que cree que proporcionará la mayor recompensa en función de lo que ha aprendido.

El desafío en el problema de los bandidos de k brazos es equilibrar la exploración y la explotación de manera eficiente. Si el agente explora demasiado, pierde oportunidades de obtener recompensas más altas de las palancas que ya ha identificado como buenas. Por otro lado, si el agente explota demasiado pronto, puede perderse mejores opciones que aún no ha descubierto.

Hay varias estrategias y algoritmos para abordar el problema de los bandidos de k brazos, como la regla ε-greedy, la regla de confianza superior (UCB) y el algoritmo de muestreo de Thompson, entre otros. Cada uno de estos enfoques aborda el equilibrio entre exploración y explotación de diferentes maneras, y su rendimiento puede variar según el problema específico y las características de las distribuciones de recompensa.

> En el caso teórico, es posible que los brazos ofrezcan recompensas positivas en promedio, lo que permitiría ganar a lo largo del tiempo si el agente selecciona correctamente las palancas. La clave en este problema teórico es cómo el agente aprende a tomar decisiones óptimas, equilibrando la exploración y la explotación para maximizar sus ganancias.

