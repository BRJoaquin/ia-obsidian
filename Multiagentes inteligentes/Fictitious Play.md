El "Fictitious Play" (juego ficticio) es un proceso de aprendizaje en [[Teoría de Juegos|teoría de juegos]] donde los jugadores hacen suposiciones sobre las estrategias de los otros jugadores y luego ajustan sus propias estrategias en consecuencia a lo largo del tiempo. Fue introducido por primera vez por George Brown en 1951.

El proceso se basa en la idea de que cada jugador cree que los oponentes están jugando estrategias estacionarias (es decir, estrategias que no cambian con el tiempo), aunque esto no necesariamente sea cierto. Los jugadores hacen conjeturas iniciales sobre las frecuencias de las acciones de los oponentes y luego, basándose en la observación de las acciones reales de los oponentes, revisan y actualizan estas conjeturas después de cada ronda de juego. La actualización se realiza de tal manera que los jugadores incrementan la probabilidad asignada a las acciones que sus oponentes han elegido más frecuentemente en el pasado.

![[Pasted image 20231130163505.png]]

Aquí hay algunos puntos clave sobre el juego ficticio:

1. **Conjeturas Iniciales**: Los jugadores comienzan con una conjetura inicial sobre la distribución de probabilidad de las estrategias de los otros jugadores.
    
2. **Aprendizaje y Actualización**: Después de cada ronda de juego, los jugadores observan las acciones de los otros y actualizan sus conjeturas para reflejar la frecuencia de las acciones observadas.
    
3. **Mejor Respuesta**: Basándose en sus conjeturas actualizadas, los jugadores eligen la mejor respuesta a las estrategias que creen que están jugando sus oponentes.
    
4. **Convergencia**: Bajo ciertas condiciones, las conjeturas de los jugadores pueden converger a un [[Equilibro de Nash|equilibrio de Nash]] del juego a medida que el número de rondas tiende a infinito. Esto significa que, eventualmente, las estrategias de los jugadores se estabilizarán y ya no cambiarán, porque han llegado a las mejores respuestas a las estrategias de los otros.
    
5. **Aplicaciones**: El juego ficticio tiene aplicaciones en economía y otras ciencias sociales, donde los agentes deben hacer conjeturas y aprender sobre el comportamiento de otros agentes en el mercado o en situaciones estratégicas.
    
6. **Limitaciones**: El juego ficticio puede no converger en todos los juegos o puede converger solo bajo ciertas reglas de actualización. Además, si los jugadores no son completamente racionales o si están limitados por la información imperfecta, la convergencia al equilibrio de Nash puede no ser garantizada.
    
7. **Tipos de Juego Ficticio**: Existen variantes del juego ficticio, como el "fictitious play continuo", donde los jugadores actualizan sus creencias de manera continua a medida que reciben nueva información, y el "fictitious play discontinuo", donde las actualizaciones ocurren en intervalos discretos.
    

El juego ficticio es un mecanismo de aprendizaje y una herramienta analítica que ayuda a entender cómo los jugadores pueden llegar a estrategias de equilibrio en juegos repetidos, y cómo las dinámicas de aprendizaje y adaptación pueden impactar en la estrategia y la toma de decisiones en entornos interactivos.


**Ventajas del Juego Ficticio:**

1. **Convergencia a Equilibrios**: Bajo ciertas condiciones, especialmente en juegos con estrategias puras y [[Juego de suma cero|juegos de suma cero]], el juego ficticio puede converger a un equilibrio de Nash, proporcionando a los jugadores un método para aprender estrategias óptimas a través de la interacción.
    
2. **Simplicidad y Aplicabilidad**: Es conceptualmente simple y se puede aplicar en una variedad de entornos, incluso sin conocimiento completo de la estructura del juego o de las preferencias de los otros jugadores.
    
3. **Modelado de Expectativas**: Permite modelar cómo los jugadores pueden formar expectativas y aprender de las acciones de los demás en un entorno dinámico, lo que es útil en la investigación económica y en ciencias del comportamiento.
    
4. **Bases para Algoritmos de Aprendizaje**: Sirve como base para algoritmos de aprendizaje más sofisticados en inteligencia artificial, donde las entidades pueden adaptar sus estrategias basándose en el historial de juego.
    

**Desventajas del Juego Ficticio:**

1. **Convergencia No Garantizada**: En algunos juegos, especialmente aquellos con estrategias mixtas o con múltiples equilibrios de Nash, el juego ficticio puede no converger, o puede tomar un tiempo extremadamente largo para hacerlo.
    
2. **Información Completa**: Para que el juego ficticio funcione efectivamente, los jugadores deben tener acceso a un registro completo de las acciones pasadas, lo que puede no ser factible en todos los entornos.
    
3. **Suposiciones de Racionalidad**: Se basa en la suposición de que los jugadores son racionales y buscan maximizar su utilidad. Sin embargo, en la práctica, los jugadores pueden tener limitaciones cognitivas o pueden no comportarse de manera completamente racional.
    
4. **Estrategias Estacionarias**: El juego ficticio asume que los jugadores creen que los demás están jugando estrategias estacionarias, lo cual puede no ser cierto, especialmente en juegos dinámicos donde los jugadores pueden adaptar sus estrategias constantemente.

![[Pasted image 20231130163624.png]]

**¿Cómo se Aplica el Juego Ficticio?**

El juego ficticio puede ser aplicado en juegos reales a medida que suceden, o en un entorno simulado para entrenar a los jugadores (o algoritmos) antes de jugar en un escenario real. En el primer caso, los jugadores actualizan sus creencias y estrategias sobre la marcha, basándose en la información recopilada durante el juego. En el segundo caso, se puede simular el juego muchas veces para que los jugadores o algoritmos aprendan las mejores respuestas a través de la experiencia antes de enfrentarse a situaciones reales.


<iframe width="560" height="315" src="https://www.youtube.com/embed/_XIdEr-wtJg?si=rZxsFHQcknl8StEI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
