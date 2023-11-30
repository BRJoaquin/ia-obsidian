
Regret matching es un algoritmo de aprendizaje en teoría de juegos que forma parte de los procesos de aprendizaje adaptativo y se utiliza para llegar a equilibrios en juegos repetidos. Desarrollado por Sergiu Hart y Andreu Mas-Colell en 2000, el concepto de "regret" (lamento o arrepentimiento) es clave en este algoritmo. Se refiere a la diferencia entre la recompensa que un jugador ha obtenido y la que podría haber obtenido si hubiera jugado de otra manera.

En el contexto del regret matching, los jugadores ajustan sus estrategias con el tiempo, basándose en el nivel de arrepentimiento por no haber jugado las mejores respuestas en el pasado. Aquí hay una descripción más detallada de cómo funciona y sus implicaciones:

**Mecanismo Básico:**

- **Arrepentimiento**: Los jugadores calculan el arrepentimiento para cada acción posible, que es la diferencia entre la utilidad que habrían recibido si hubieran jugado esa acción en cada ronda anterior y la utilidad que realmente recibieron.
    
- **Actualización de Estrategias**: En cada período, los jugadores tienen la posibilidad de cambiar sus estrategias basándose en sus niveles de arrepentimiento. Si no hay arrepentimiento por la estrategia actual, no hay razón para cambiarla. Si hay arrepentimiento, hay una mayor probabilidad de cambiar a una estrategia que podría haber funcionado mejor en el pasado.
    
- **Matching del Regret**: La probabilidad de cambiar a una estrategia particular es proporcional al arrepentimiento acumulado para esa estrategia. Así, las estrategias que habrían dado mejores resultados en el pasado son elegidas con mayor frecuencia.
    

**Ventajas del Regret Matching:**

1. **Convergencia**: Bajo ciertas condiciones, se ha demostrado que el regret matching converge a un equilibrio de Nash en juegos repetidos con dos jugadores y en algunos juegos con múltiples jugadores.
    
2. **Simplicidad**: A diferencia de otros algoritmos de aprendizaje que pueden requerir un seguimiento complejo de la historia del juego o suposiciones sobre las estrategias de los oponentes, el regret matching solo requiere que los jugadores recuerden su propio historial de utilidades y acciones.
    
3. **Robustez**: El algoritmo es bastante robusto en diferentes entornos y no necesita ajustes finos para diferentes juegos.
    

**Desventajas del Regret Matching:**

1. **Velocidad de Convergencia**: La velocidad con la que el regret matching converge a un equilibrio de Nash puede ser lenta, especialmente en juegos complejos con muchos jugadores y estrategias.
    
2. **Dependencia de la Historia**: Aunque más simple que otros algoritmos, el regret matching todavía depende de mantener un registro histórico de utilidades y acciones, lo cual puede no ser factible o deseable en todos los contextos.
    
3. **Necesidad de Repetición**: El regret matching está diseñado para juegos que se juegan repetidamente, y su aplicación en situaciones de una sola vez no es directa.

# FP vs RM

**Fictitious Play (FP):**

- En FP, cada agente es considerado como un observador ficticio que tiene un conocimiento completo del juego.
- Los agentes observan y consideran todas las estrategias posibles de todos los agentes en el juego.
- Tienen acceso a la matriz de recompensas completa del juego, lo que les permite conocer las recompensas de todas las acciones posibles para todos los jugadores.
- A lo largo del tiempo, los agentes actualizan sus creencias sobre las estrategias de los oponentes basándose en las frecuencias de las acciones jugadas y eligen la mejor respuesta a estas estrategias supuestas.

**Regret Matching (RM):**

- RM considera agentes que son informados y observadores de su propio historial de juego.
- Los agentes conocen su propia estrategia y tienen un registro de sus recompensas pasadas.
- Observan el "vector de recompensas" dado una estrategia específica, que esencialmente es una lista de las recompensas obtenidas para cada acción posible en el pasado.
- Utilizan esta información para calcular el "regret" por no haber jugado otras estrategias y ajustan su comportamiento en consecuencia, favoreciendo las estrategias que habrían dado mejores recompensas en el pasado.

**Agente Naïve:**

- Un agente naïve tiene una comprensión más limitada y básica de su entorno de juego.
- Conoce su propia estrategia y observa las recompensas que obtiene, pero no necesariamente hace un análisis profundo del historial de juego o las estrategias de los oponentes.
- Este agente puede no tener una estrategia para ajustar su comportamiento basado en el historial de juego y, en su lugar, podría tomar decisiones más simplistas o aleatorias.

**Comparación entre FP y RM:**

- **FP vs RM**: Mientras que FP se basa en el concepto de frecuencias y supone que los oponentes juegan estrategias estacionarias, RM se basa en el concepto de arrepentimiento y busca ajustar las estrategias basándose en las recompensas que se podrían haber obtenido. FP requiere una visión más global y estratégica del juego, mientras que RM es más reactivo y centrado en el historial individual de recompensas.
    
- **Convergencia**: Ambos procesos, bajo ciertas condiciones, pueden converger a un equilibrio de Nash, pero el camino hacia la convergencia y la velocidad pueden diferir significativamente entre los dos.
    
- **Complejidad de la Información**: FP requiere una comprensión más compleja y completa del juego, mientras que RM puede ser implementado con información más limitada y se enfoca en el desempeño individual a lo largo del tiempo.

# Video


<iframe width="560" height="315" src="https://www.youtube.com/embed/_XIdEr-wtJg?si=fsbNVbINuPI7SCA0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
