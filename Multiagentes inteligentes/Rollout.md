El método de rollout es una técnica de evaluación utilizada en la planificación y la toma de decisiones **bajo incertidumbre**, comúnmente aplicada en el contexto de la inteligencia artificial para juegos y problemas de optimización secuencial. Es una forma de aproximación Monte Carlo que se utiliza para estimar la calidad de un estado o una decisión particular mediante la simulación de su desempeño a lo largo de varias trayectorias posibles hasta alcanzar un estado final.

![[Pasted image 20231201152246.png]]


Rollout es un método de simulación utilizado para evaluar estados en juegos o situaciones de toma de decisiones. La idea es simular el juego varias veces desde un estado específico hasta un estado terminal, y luego promediar los resultados para obtener una estimación del valor de ese estado. Aquí está el proceso detallado:

1. Repetir $m$ veces:
   - Simular un episodio $j$ desde el estado $s$.
   - Actualizar el valor de $s$ basado en el resultado del episodio.

2. La actualización del valor se realiza según la fórmula:
   $$ V_{\text{rollout}}(s) = V_{\text{rollout}}(s) + V^j_{\pi_a,\pi_o}(s) $$

3. Después de realizar $m$ simulaciones, el valor de rollout de $s$ se calcula como:
   $$ V_{\text{rollout}}(s) = \frac{V_{\text{rollout}}(s)}{m} $$

4. Cuanto mayor sea el número de simulaciones $m$, mejor será la aproximación del valor de $s$, pero también mayor será el tiempo de ejecución.

5. Dado que las trayectorias deben llegar a un estado final, y algunos juegos o problemas pueden tener trayectorias muy largas, se pueden tomar las siguientes medidas:
   - Acotar la longitud del camino a explorar.
   - Utilizar una función de evaluación $Eval_{\text{rollout}}(s)$ para estimar la utilidad en el último estado del camino.

El método de rollout es útil en juegos complejos y en problemas de optimización donde no es posible o práctico evaluar todas las posibles secuencias de acciones hasta el final. Al promediar los resultados de múltiples simulaciones, el método de rollout proporciona una estimación robusta del valor esperado de un estado sin necesidad de una búsqueda exhaustiva.

