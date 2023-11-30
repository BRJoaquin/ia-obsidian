La Eliminación Iterada de Estrategias Débilmente Dominadas (IDWDS, por sus siglas en inglés) es un proceso de refinamiento de estrategias en la teoría de juegos que permite a los analistas predecir los resultados de juegos estratégicos con múltiples jugadores. Este proceso es similar a la Eliminación Iterada de Estrategias Estrictamente Dominadas (IEDS), pero se aplica a un conjunto más amplio de estrategias, incluyendo aquellas que son "débilmente" dominadas.

Una estrategia débilmente dominada para un jugador es aquella para la cual existe al menos otra estrategia que siempre resulta en una recompensa igual o mejor, sin importar lo que hagan los demás jugadores, y en al menos una situación, produce una recompensa mejor. A diferencia de las estrategias estrictamente dominadas, donde la estrategia dominante es siempre mejor, la estrategia débilmente dominante podría ser solo igual de buena como la estrategia dominada en ciertas contingencias.

El proceso IDWDS se desarrolla de la siguiente manera:

1. **Identificación de Estrategias Débilmente Dominadas**: Se comienza identificando todas las estrategias que son débilmente dominadas para cada jugador.
    
2. **Eliminación**: Se eliminan estas estrategias del conjunto de estrategias posibles de los jugadores. Al eliminar una estrategia débilmente dominada, se puede alterar el conjunto de estrategias restantes, lo que podría hacer que una estrategia previamente no dominada se convierta en débilmente dominada.
    
3. **Iteración**: Este proceso de identificación y eliminación se repite. Después de cada ronda de eliminación, se revisa el conjunto de estrategias restante para buscar nuevas estrategias débilmente dominadas que puedan haber surgido debido a la eliminación anterior.
    
4. **Convergencia**: El proceso continúa iterativamente hasta que no se pueden eliminar más estrategias débilmente dominadas.
    

El resultado de IDWDS puede llevar a una predicción más precisa del comportamiento de los jugadores en comparación con la eliminación de estrategias estrictamente dominadas, ya que considera un conjunto más amplio de posibilidades y es menos restrictivo.

Sin embargo, la eliminación iterada de estrategias débilmente dominadas no siempre lleva a un único resultado como puede ser el caso con la eliminación de estrategias estrictamente dominadas. Esto se debe a que la eliminación de una estrategia débilmente dominada puede depender del orden en que se eliminan las estrategias, lo que puede llevar a múltiples subconjuntos finales de estrategias que no son comparables entre sí.

![[Pasted image 20231130110348.png]]

Un aspecto importante a considerar es que, mientras que el Equilibrio de Nash es un concepto de equilibrio estable y no depende del orden de eliminación de estrategias, el resultado de IDWDS puede variar en función de este orden. Por lo tanto, IDWDS puede no llevar a un equilibrio en juegos donde la eliminación de estrategias débilmente dominadas depende del orden en que se lleve a cabo.

![[Pasted image 20231130105247.png]]

![[Pasted image 20231130105926.png]]

![[Pasted image 20231130110042.png]]

