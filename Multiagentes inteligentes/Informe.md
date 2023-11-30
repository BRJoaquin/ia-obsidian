**Informe de Proyecto: Aplicación de Técnicas Avanzadas de Aprendizaje por Refuerzo en Juegos de Múltiples Jugadores**

**Autor:** Joaquin Vigna

# Introducción

En este trabajo, exploramos la implementación y experimentación de algoritmos de aprendizaje avanzados en el contexto de juegos alternados de múltiples jugadores. Nos enfocamos específicamente en dos algoritmos clave: CFR (Counterfactual Regret Minimization) y MCTS (Monte Carlo Tree Search), aplicados a variantes de póker. Nuestro objetivo es no solo implementar estos algoritmos sino también investigar su rendimiento y efectividad en diferentes escenarios de juego.
## Objetivos del Trabajo

El principal objetivo de este trabajo es profundizar en el entendimiento y aplicación práctica de los algoritmos CFR y MCTS en entornos de juego competitivos, así como explorar posibles extensiones y mejoras a estos métodos.

### Entorno de Ejecución

[PettingZoo](https://pettingzoo.farama.org/index.html) es una biblioteca de juegos multiagentes que proporciona una amplia variedad de entornos diseñados específicamente para la investigación en aprendizaje por refuerzo. Este entorno será la base de nuestros experimentos, permitiéndonos simular y analizar de manera efectiva las interacciones y estrategias de los agentes en diferentes juegos.

### Características Clave de PettingZoo

- **Variedad de Juegos**: Ofrece una extensa colección de juegos, incluyendo clásicos y nuevos desafíos, lo que nos permite explorar una amplia gama de escenarios y dinámicas de juego.
- **Compatibilidad con Aprendizaje por Refuerzo**: Diseñado para ser compatible con las técnicas y algoritmos de aprendizaje por refuerzo más comunes, facilitando la integración y experimentación.
- **Entorno Multiagente**: Especialmente orientado a entornos multiagentes, lo que lo hace ideal para estudiar juegos alternados de múltiples jugadores como los que abordaremos.

### Implementación de los Juegos

En nuestro trabajo, la cátedra nos proporcionó una implementación de los juegos Kuhn Poker y Leduc Poker, que utilizaremos para nuestros experimentos. Estas implementaciones se basan en la biblioteca PettingZoo.

1. **Kuhn Poker**: Un juego de póker simplificado que servirá como campo de prueba para el algoritmo CFR. Experimentaremos tanto con versiones de 2 como de 3 jugadores.
2. **Leduc Poker**: Un juego de póker más complejo que será utilizado para probar y evaluar el algoritmo MCTS, así como las funciones de evaluación integradas.

Estos juegos nos proporcionarán una plataforma sólida para implementar, probar y analizar los algoritmos de aprendizaje en un contexto competitivo y controlado.

# Metodología y Experimentación

## Implementación de CFR

En este proyecto, hemos implementado el algoritmo Counterfactual Regret Minimization (CFR) para experimentar en juegos de póker, aunque su aplicación puede extenderse a otros contextos. Esta implementación se centra en desarrollar y refinar estrategias de juego en entornos de información imperfecta. El código completo para esta implementación se puede encontrar en el archivo `/agents/counterfactualregret.py` del proyecto.

### Descripción de la Implementación

La implementación de CFR en nuestro proyecto consta de varias partes clave:

1. **Clase `Node`**: Representa un nodo en el árbol de juego. Cada nodo contiene información sobre el estado del juego (information set), el agente actual, la observación recibida y mantiene un registro del arrepentimiento acumulado y la política aprendida.

2. **Métodos de Actualización y Estrategia**: Dentro de la clase `Node`, se implementan métodos para actualizar los valores de arrepentimiento contrafactual (contrafactico) y para ajustar la estrategia actual basada en estos arrepentimientos.

3. **Clase `CounterFactualRegret`**: Extiende la clase `Agent` (basado en `PettingZoo`) y se utiliza para representar un agente que emplea CFR. Contiene métodos para realizar acciones, entrenar utilizando CFR y realizar el algoritmo de CFR de manera recursiva.

4. **Función `cfr_rec`**: Implementa la lógica del CFR de manera recursiva, calculando la utilidad de cada nodo y actualizando la estrategia y los arrepentimientos.

### Naturaleza Agnóstica al Juego de las Implementaciones de Agentes

Es importante destacar un aspecto fundamental de nuestras implementaciones de agentes, incluido el agente que utiliza el algoritmo Counterfactual Regret Minimization (CFR). Estos agentes son **agnósticos al juego**, lo que significa que su diseño y funcionamiento no están limitados o definidos por las reglas o acciones específicas de un juego en particular, o por la cantidad de jugadores. En cambio, estos agentes se pueden utilizar en cualquier juego que cumpla con los requisitos básicos de la biblioteca PettingZoo, lo que los hace altamente adaptables y reutilizables.

## Experimentación con Kuhn Poker

[Kuhn Poker](https://en.wikipedia.org/wiki/Kuhn_poker) es un juego de póker simplificado que sirve como un modelo excelente para estudiar algoritmos de aprendizaje por refuerzo en juegos de información imperfecta. Este juego representa una versión reducida del póker tradicional, lo que lo convierte en un entorno ideal para experimentos y análisis en el campo de la teoría de juegos y la inteligencia artificial.

### Descripción del Kuhn Poker

- **Jugadores**: El juego clásico involucra a 2 jugadores, aunque puede adaptarse para 3 jugadores.
- **Baraja**: Se utiliza una baraja reducida, típicamente con tres cartas (por ejemplo, un As, un Rey y una Reina).
- **Dinámica del Juego**: Cada jugador recibe una carta y tiene la opción de apostar (bet) o pasar (check). El juego tiene una estructura de apuestas limitada y presenta oportunidades para [farolear](https://es.wikipedia.org/wiki/Farol_(envite)) y realizar estrategias basadas en la información limitada.

### Experimentación Planeada

En nuestro proyecto, experimentaremos con Kuhn Poker de la siguiente manera:

1. **Con 2 Jugadores**: Inicialmente, nos enfocaremos en la versión clásica de Kuhn Poker con 2 jugadores. Aquí, aplicaremos y evaluaremos el algoritmo de Counterfactual Regret Minimization para desarrollar estrategias efectivas y analizar cómo los agentes aprenden y se adaptan a lo largo de múltiples juegos.

2. **Expansión a 3 Jugadores**: Posteriormente, expandiremos nuestra experimentación para incluir una versión de 3 jugadores del juego. Esta variante presenta desafíos adicionales y complejidades, permitiéndonos explorar cómo los algoritmos se adaptan a un entorno de juego más dinámico y a la presencia de un jugador adicional.

Estas experimentaciones nos permitirán obtener una comprensión más profunda de la efectividad del algoritmo CFR y cómo se puede adaptar a diferentes configuraciones de juego.






























# TODO

### Experimentación con Kuhn Poker

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