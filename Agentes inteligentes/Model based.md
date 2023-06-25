Los algoritmos model-based en el aprendizaje por refuerzo son aquellos **métodos que intentan aprender o utilizar un modelo del entorno para tomar decisiones**. **Un modelo del entorno simula las transiciones de estado y las recompensas, lo que permite a los agentes predecir qué sucederá en el futuro sin necesidad de realizar acciones en el entorno real**. 

Aquí están algunos ejemplos de algoritmos model-based:

- Dynamic Programming (DP) 
Los algoritmos de [[Programación dinámica]], como la iteración de valor y la iteración de políticas, son model-based ya que utilizan un modelo del entorno para realizar actualizaciones de valor.

- Tree Search
Los algoritmos de búsqueda en árbol, como Monte Carlo Tree Search (MCTS), utilizan un modelo del entorno para simular resultados de diferentes secuencias de acciones.

- Dyna-Q
[[Dyna-Q]] es un algoritmo que combina aspectos de aprendizaje model-free y model-based. Aprende un modelo del entorno para realizar simulaciones, además de aprender directamente de la interacción con el entorno real.

- Model Predictive Control (MPC)
MPC utiliza un modelo del entorno para prever los efectos de diferentes secuencias de acciones, y selecciona la acción que conduzca al mejor resultado previsto.

- World Models
Los World Models aprenden un modelo generativo del entorno y lo utilizan para planificar.

**En general, los algoritmos model-based pueden ser más eficientes que los algoritmos model-free, ya que utilizan la información sobre las dinámicas del entorno para guiar el aprendizaje. Sin embargo, aprender un modelo preciso puede ser difícil para entornos complejos, y los errores en el modelo pueden llevar a políticas subóptimas.**
