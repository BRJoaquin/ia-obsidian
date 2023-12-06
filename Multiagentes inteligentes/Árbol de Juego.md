Los árboles de juego son una herramienta fundamental en la [[Teoría de Juegos|teoría de juegos]] que se utiliza para representar de manera gráfica las decisiones secuenciales en juegos con turnos alternados. Estos árboles ayudan a los jugadores y analistas a visualizar cómo las interacciones y las decisiones se desarrollan a lo largo del tiempo en el juego.

![[Pasted image 20231201101734.jpg]]

**Componentes de un Árbol de Juego:**

- **Nodos**: Cada punto de decisión en el juego se representa con un nodo. Los nodos pueden ser de dos tipos:
    
    - **Nodos de Decisión**: Representan puntos en el juego donde un jugador debe tomar una decisión.
    - **Nodos de Azar**: Representan puntos donde el resultado es determinado por el azar (por ejemplo, el lanzamiento de un dado).
      
- **Aristas o Ramas**: Las líneas que conectan los nodos se llaman aristas o ramas y representan las [[Acción|acciones]] posibles o los movimientos que los jugadores pueden realizar desde un nodo de decisión.
    
- **Nodos Terminales o Hojas**: Estos son los nodos al final de las ramas, donde el juego termina. Los nodos terminales suelen estar etiquetados con las [[Recompensa|utilidades]] o pagos para cada jugador, indicando el resultado de seguir ese camino específico a través del árbol.
    
- **Información Perfecta vs. Imperfecta**: En un árbol de [[Juegos con Información perfecta|juego con información perfecta]], cada nodo de decisión muestra claramente a qué jugador le toca mover, y todas las acciones anteriores son conocidas. En un árbol de [[Juegos con Información imperfecta| información imperfecta]], algunos nodos pueden agruparse en [[Information set|conjuntos de información]] que representan que el jugador no tiene información completa sobre las acciones previas.


![[Pasted image 20231201103016.png]]


**Análisis de un Árbol de Juego:**

- **Inducción hacia Atrás**: Es una técnica común para analizar árboles de juego **con información perfecta**. Comenzando desde los nodos terminales, los analistas calculan la mejor estrategia en cada nodo de decisión, "subiendo" por el árbol hasta el primer movimiento.
    
- **Estrategias Óptimas**: Mediante el uso de árboles de juego, los jugadores pueden determinar estrategias óptimas que maximicen sus utilidades esperadas o minimicen sus pérdidas en función de las estrategias de los otros jugadores.
    
- **Equilibrios de Nash**: Los árboles de juego pueden ayudar a identificar los equilibrios de Nash en juegos secuenciales, donde las estrategias de los jugadores son mutuamente las mejores respuestas a las estrategias de los otros.
    
# Valor de un juego

![[Pasted image 20231201103322.png]]


# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/IwBUXH-L4yQ?si=xmI9NOxrzwrADCDB" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
