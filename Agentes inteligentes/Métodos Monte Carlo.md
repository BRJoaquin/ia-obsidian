Los métodos Monte Carlo son una clase de algoritmos en el [[Aprendizaje por refuerzo]] que se basan en la **generación de muestras y la promediación para estimar las funciones de valor y las políticas**.

> **A diferencia de los métodos de programación dinámica, los métodos Monte Carlo son model-free, es decir, no requieren un modelo completo del entorno**. Sin embargo pueden conocer la dinámica del entorno, eso les permite hacer episodios simulados.
> ![[Pasted image 20230624145717.png]]

# Conceptos básicos

En el contexto del aprendizaje por refuerzo, un experimento Monte Carlo implica la simulación de [[Episodio]]s de interacción con el [[Entorno]], a partir de los cuales se calculan las [[Recompensa]]s acumuladas (o retornos) para estimar las [[Función de valor]].

**Los métodos Monte Carlo estiman el valor de un estado como el promedio de los retornos observados después de visitas a ese estado**.

> **Dado que los retornos son promediados, el número de veces que se visita un estado tiene un impacto en la precisión de la estimación. Si un estado se visita frecuentemente, la estimación de su valor será más precisa.** Por ende si un estado se visita poco podría no tener una buena estimación. 

# Métodos de Muestreo

Existen principalmente dos enfoques de muestreo en los métodos Monte Carlo: muestreo de primer visita (first visit) y muestreo de todas las visitas (every visit).

- **Muestreo de Primer Visita Monte Carlo**: Este método estima el valor de un estado como el promedio de los retornos siguientes a la primera visita a ese estado en cada episodio.

- **Muestreo de Todas las Visitas Monte Carlo**: Este método estima el valor de un estado como el promedio de los retornos siguientes a todas las visitas a ese estado en cada episodio.

# Algoritmos

$$
\begin{verbatim} 
Inicializar, para todos s ∈ S, a: N(s) ← 0 V(s) ← valor arbitrario Para cada episodio hacer: Generar un episodio siguiendo π: S0, A0, R1, ..., ST-1, AT-1, RT G ← 0 Loop para cada paso del episodio, t = T-1, T-2, ..., 0: G ← γG + R_t+1 Si S_t no aparece en S0, S1, ..., S_t-1: N(S_t) ← N(S_t) + 1 V(S_t) ← V(S_t) + (1/N(S_t)) * (G - V(S_t))
\end{verbatim}
$$

# Métodos Monte Carlo de Control

Para encontrar políticas óptimas, los métodos Monte Carlo utilizan generalización de la estrategia de iteración de política, alternando entre evaluación y mejora de la política. Estos métodos incluyen:

- **Monte Carlo con Exploración Constante**: Este es un enfoque simple en el que la política se mantiene estocástica con una probabilidad constante de exploración.

- **Monte Carlo con $\epsilon$-greedy Policies**: Este método mejora la política volviéndola "greedy" con respecto a la función de valor actual con una probabilidad $1-\epsilon$, y selecciona una acción aleatoria con una probabilidad $\epsilon$.

- **Monte Carlo con Soft Policies**: En este método, todas las acciones tienen una probabilidad no nula de ser seleccionadas, pero las acciones que se estiman como mejores tienen una mayor probabilidad.

Los métodos Monte Carlo ofrecen una manera simple y poderosa de aprender de la interacción con el entorno sin requerir un modelo completo de las dinámicas del entorno. **Sin embargo, como requieren la finalización de episodios para realizar actualizaciones, pueden ser ineficientes o inaplicables en entornos con episodios muy largos o infinitos.**
