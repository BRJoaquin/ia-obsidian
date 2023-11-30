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


### Kuhn Poker con 2 Jugadores: resultados

#### CFR vs Jugador Aleatorio

En la primera fase de nuestras experimentaciones, enfrentamos un agente implementando el algoritmo Counterfactual Regret Minimization (CFR) como jugador 1 contra un agente que elige acciones de manera aleatoria. Los resultados obtenidos son significativos:

Podemos observar que la estrategia aprendida por el agente CFR es mucho más efectiva que la estrategia aleatoria, ya que en promedio gana más fichas. Esto se debe a que el agente CFR aprende a jugar de manera óptima en cada estado del juego, mientras que el agente aleatorio simplemente toma decisiones aleatorias.

> Cabe destacar que en este caso el agente CFR es siempre el primer jugador, por lo que tiene una [desventaja inicial](https://en.wikipedia.org/wiki/Kuhn_poker#Optimal_strategy). 

#### CFR vs CFR

En una segunda fase, experimentamos enfrentando dos agentes que utilizan el algoritmo CFR. Los resultados de estos enfrentamientos apuntan a un interesante fenómeno en la teoría de juegos.

Podemos concluir que llegamos a un [Equilibrio de Nash](https://es.wikipedia.org/wiki/Equilibrio_de_Nash), donde el primer jugador (jugador 1) tiene una recompensa esperada de aproximadamente 1/18:

> "The game has a mixed-strategy Nash equilibrium; when both players play equilibrium strategies, the first player should expect to lose at a rate of −1/18 per hand (as the game is zero-sum, the second player should expect to win at a rate of +1/18). There is no pure-strategy equilibrium." - [Wikipedia](https://en.wikipedia.org/wiki/Kuhn_poker#Optimal_strategy)

Estos resultados son indicativos de la robustez y efectividad del algoritmo CFR en la búsqueda de estrategias óptimas en juegos de información imperfecta.

![[Pasted image 20231129221138.png]]

#### Conclusión de la Experimentación en Kuhn Poker con 2 Jugadores

Tras las series de experimentaciones realizadas en el contexto del Kuhn Poker con 2 jugadores, podemos concluir satisfactoriamente que el algoritmo Counterfactual Regret Minimization alcanzó su objetivo. Los resultados indican que el agente CFR fue capaz de aprender y adaptarse eficientemente a las dinámicas del juego, superando significativamente a un oponente que toma decisiones de manera aleatoria.

La parte más relevante de estos experimentos fue la confirmación de que el agente CFR, cuando se enfrenta a un oponente que también utiliza una estrategia basada en CFR, llega a un Equilibrio de Nash. Este resultado es un hito importante, ya que demuestra la capacidad del algoritmo CFR para encontrar estrategias que son óptimas en un sentido teórico y práctico, incluso en un entorno de juego tan simplificado y abstracto como el Kuhn Poker.

### Kuhn Poker con 3 Jugadores

La extensión de nuestro estudio al Kuhn Poker de tres jugadores representa un paso hacia un entorno de juego más complejo y desafiante. Este formato introduce una dinámica adicional y requiere estrategias más sofisticadas debido a la presencia de un tercer jugador. Esta variante nos permite examinar la adaptabilidad y el rendimiento del algoritmo CFR en un contexto más intrincado.

#### CFR vs CFR vs CFR

En esta etapa, llevamos a cabo un experimento donde tres agentes, cada uno operando con el algoritmo CFR, compitieron entre sí. 

#### Hipótesis de Utilidad: \( u_1 < u_2 < u_3 \)

Anticipamos una relación específica en las utilidades de los tres agentes, con el tercer jugador (\( u_3 \)) obteniendo la mayor utilidad, seguido por el segundo (\( u_2 \)) y el primero (\( u_1 \)). Esta hipótesis se basa en la ventaja del tercer jugador al actuar último en cada ronda, obteniendo así más información que los otros dos jugadores. Esta fase nos brinda insights valiosos sobre las dinámicas de juegos con información imperfecta y las estrategias óptimas en tales entornos.

### Resultados de la Experimentación

Los resultados confirman nuestra hipótesis inicial: el tercer jugador obtiene consistentemente la mayor utilidad, seguido por el segundo y luego el primer jugador.

> "A family of Nash equilibria for 3-player Kuhn poker is known analytically, which makes it the largest game with more than two players with analytic solution. The family is parameterized using 4–6 parameters (depending on the chosen equilibrium). In all equilibria, player 1 has a fixed strategy, and he always checks as the first action; player 2's utility is constant, equal to –1/48 per hand. The discovered equilibrium profiles show an interesting feature: by adjusting a strategy parameter $\beta$ (between 0 and 1), player 2 can freely shift utility between the other two players while still remaining in equilibrium; player 1's utility is equal to $-\frac{1+2\beta}{48}$ (which is always worse than player 2's utility), player 3's utility is $\frac{1+\beta}{24}$." - [Wikipedia](https://en.wikipedia.org/wiki/Kuhn_poker#3-player_Kuhn_Poker)

![[Pasted image 20231129221258.png]]

Estos hallazgos corroboran las teorías existentes y demuestran la consistencia del algoritmo CFR con las expectativas teóricas en juegos de múltiples jugadores.


## Estimación de Valor de Estados en Juegos Complejos

Una de las consideraciones críticas en la aplicación de inteligencia artificial en juegos es la gestión efectiva de la profundidad en los árboles de juego. En muchos casos, los juegos poseen un espacio de estado tan extenso que hace inviable explorar todas las posibles trayectorias del juego hasta su conclusión. Esta limitación impone la necesidad de emplear estrategias de estimación de valor de estados en ciertos niveles de profundidad, en lugar de optar por una exploración completa.

### Profundidad del Árbol de Juego y Explosión Combinatoria

La profundidad del árbol de juego se define por la cantidad de movimientos hacia adelante que el algoritmo analiza antes de tomar una decisión. En contextos de juegos complejos, esta profundidad puede incrementarse exponencialmente, dando lugar al fenómeno conocido como "explosión combinatoria". Esta situación resulta en un costo computacional elevado y, en muchas ocasiones, insostenible para una exploración completa y detallada.

### Estrategias para la Estimación de Valor

Para superar este desafío, implementamos estrategias específicas que nos permiten evaluar los estados del juego en profundidades particulares:

1. **Funciones de Evaluación**: Estas funciones son esenciales para asignar valores numéricos a los estados del juego, basándose en sus características inherentes. Varían en complejidad, desde heurísticas basadas en reglas simples hasta modelos avanzados desarrollados mediante técnicas de aprendizaje automático.

2. **Monte Carlo Tree Search (MCTS)**: El MCTS es una técnica clave que utiliza simulaciones aleatorias partiendo del estado actual para estimar el valor de los estados. Esta estrategia es especialmente valiosa en juegos con un vasto número de posibles estados futuros, ya que proporciona una manera eficiente de evaluar opciones sin la necesidad de una exploración exhaustiva del árbol de juego.

Estas metodologías nos permiten abordar de manera efectiva los retos presentados por la complejidad y el tamaño de los juegos, mejorando significativamente la toma de decisiones en entornos de juego de alta profundidad y con gran cantidad de posibilidades.

## Funciones de Evaluación

### CFR Mejorado con Estimación de Valor

Hemos avanzado en la implementación del algoritmo Counterfactual Regret Minimization, creando una versión mejorada llamada `EnhancedCounterFactualRegret`, ubicada en `agentes/counterfactualregretv2.py`. Esta versión introduce una innovación esencial: la estimación de valor a cierta profundidad en el árbol de juego. Las características clave de esta implementación son:

1. **Estimación de Valor en Profundidad Limitada**: Se utiliza una función (`value_estimator`) para evaluar los estados del juego al alcanzar una profundidad máxima (`max_depth`), optimizando así el manejo de juegos con grandes espacios de estado.

2. **Recursión Modificada con Estimación de Valor**: La función `cfr_rec` se adapta para incorporar la estimación de valor cuando se alcanza la profundidad máxima, utilizando `estimate_value` para obtener una evaluación del estado actual.

3. **Selección de Acciones Mejorada**: El método `action` se ha modificado para seleccionar una acción aleatoria si la lógica base de CFR falla, asegurando una toma de decisiones continua.

### Demostración con Kuhn Poker y Función de Evaluación "Dummy"

Para ilustrar el impacto de las funciones de evaluación, seleccionamos Kuhn Poker (khun2) por su simplicidad y su naturaleza de información imperfecta. Hemos diseñado una función de evaluación "dummy" para khun2, que, aunque no busca optimizar el juego, sirve para demostrar cómo se valoran los diferentes estados del juego y cómo esto influye en las decisiones del agente. La función considera elementos como la carta en mano del agente y la última acción del oponente.























# TODO

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