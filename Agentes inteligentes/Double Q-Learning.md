
Double Q-Learning es un algoritmo de aprendizaje por refuerzo que aborda el problema del [[Sesgo de Maximización]] en Q-Learning. Fue propuesto por Hado van Hasselt en 2010.

El Sesgo de Maximización ocurre en Q-Learning porque el algoritmo usa la misma muestra para determinar la mejor acción y para estimar el valor de esa acción. Esto puede llevar a una sobreestimación sistemática de los valores Q.

El Double Q-Learning aborda este problema utilizando dos funciones de valor Q, cada una aprendida de diferentes experiencias. De esta manera, una función Q se usa para determinar la acción óptima y la otra se usa para estimar el valor de esa acción. Este enfoque reduce la probabilidad de seleccionar acciones sobreestimadas.

El algoritmo Double Q-Learning es similar a Q-Learning con la diferencia de que tiene dos funciones de valor Q y alterna entre ellas en cada paso de tiempo. La actualización para Double Q-Learning es la siguiente:

1. Para un paso de tiempo, selecciona una acción A del estado S utilizando la política derivada de Q1 + Q2.
2. Luego, toma la acción A y observa la recompensa R y el estado siguiente S'.
3. A continuación, con una probabilidad de 0.5, actualiza Q1 utilizando la recompensa R y la estimación de Q2 para el estado y acción siguiente, es decir:
   
$$Q1(S, A) \leftarrow Q1(S, A) + \alpha \left[ R + \gamma Q2(S', \arg\max_a Q1(S', a)) - Q1(S, A) \right]$$
   
De lo contrario, actualiza Q2 utilizando la recompensa R y la estimación de Q1 para el estado y acción siguiente, es decir:
  $$Q2(S, A) \leftarrow Q2(S, A) + \alpha \left[ R + \gamma Q1(S', \arg\max_a Q2(S', a)) - Q2(S, A) \right]$$

Estas actualizaciones reducen la probabilidad de seleccionar acciones sobreestimadas y, por lo tanto, mitigar el Sesgo de Maximización.

![[Pasted image 20230705153048.png]]

![[Pasted image 20230705153107.png]]

![[Pasted image 20230705152941.png]]


Richard S. Sutton y Andrew G. Barto presentan Double Q-Learning en su libro  como una solución efectiva al Sesgo de Maximización que puede surgir en algoritmos como Q-Learning. 

Destacan que Double Q-Learning, al mantener y actualizar dos funciones de valor Q independientes, reduce la sobreestimación sistemática de los valores Q que es común en Q-Learning. 

Una función Q se utiliza para determinar la acción óptima y la otra para estimar el valor de esa acción. De esta manera, se evita la sobreestimación que surge del uso de la misma muestra para seleccionar la mejor acción y actualizar su valor. 

Sutton y Barto también señalan que Double Q-Learning ha demostrado ser efectivo en una variedad de tareas y puede resultar en una mejora significativa en el rendimiento sobre Q-Learning en situaciones en las que el Sesgo de Maximización es un problema.
