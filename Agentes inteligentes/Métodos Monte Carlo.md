Los métodos Monte Carlo son una clase de algoritmos en el [[Aprendizaje por refuerzo]] que se basan en la **generación de muestras y la promediación para estimar las funciones de valor y las políticas**.

> **A diferencia de los métodos de programación dinámica, los métodos Monte Carlo son model-free, es decir, no requieren un modelo completo del entorno**. Sin embargo pueden conocer la dinámica del entorno, eso les permite hacer episodios simulados.
> ![[Pasted image 20230624145717.png]]

# Conceptos básicos

En el contexto del aprendizaje por refuerzo, un experimento Monte Carlo implica la simulación de [[Episodio]]s de interacción con el [[Entorno (ambiente)]], a partir de los cuales se calculan las [[Recompensa]]s acumuladas (o retornos) para estimar las [[Función de valor]].

**Los métodos Monte Carlo estiman el valor de un estado como el promedio de los retornos observados después de visitas a ese estado**.

> **Dado que los retornos son promediados, el número de veces que se visita un estado tiene un impacto en la precisión de la estimación. Si un estado se visita frecuentemente, la estimación de su valor será más precisa.** Por ende si un estado se visita poco podría no tener una buena estimación. 

# Métodos de Muestreo

Existen principalmente dos enfoques de muestreo en los métodos Monte Carlo: muestreo de primer visita (first visit) y muestreo de todas las visitas (every visit).

- **Muestreo de Primer Visita Monte Carlo**: Este método estima el valor de un estado como el promedio de los retornos siguientes a la primera visita a ese estado en cada episodio.

- **Muestreo de Todas las Visitas Monte Carlo**: Este método estima el valor de un estado como el promedio de los retornos siguientes a todas las visitas a ese estado en cada episodio.

# Algoritmos

## Estimación de V (first visit)

Inicializar, para todos $s \in S$:
    $N(s) \leftarrow 0$
    $V(s) \leftarrow$ valor arbitrario

Para cada episodio:
    Generar un episodio siguiendo $\pi$: $S_0, A_0, R_1, ..., S_{T-1}, A_{T-1}, R_T$
    $G \leftarrow 0$
    Loop para cada paso del episodio, $t = T-1, T-2, ..., 0$:
        $G \leftarrow \gamma G + R_{t+1}$
        Si $S_t$ no aparece en $S_0, S_1, ..., S_{t-1}$:
            $N(S_t) \leftarrow N(S_t) + 1$
            $V(S_t) \leftarrow V(S_t) + (1/N(S_t)) * (G - V(S_t))$

> En los algoritmos de Monte Carlo, `N(s)` representa la cantidad de veces que el agente ha visitado el estado `s` durante la generación de episodios. Esto se utiliza para calcular el promedio de las recompensas retornadas para cada estado en el proceso de estimación de la función de valor `V(s)`. En otras palabras, se utiliza para determinar cuánto peso dar a una nueva actualización de la función de valor para un estado dado.


## Estimación de V (every visit)

Inicializar, para todos $s \in S$:
    $N(s) \leftarrow 0$
    $V(s) \leftarrow$ valor arbitrario

Para cada episodio:
    Generar un episodio siguiendo $\pi$: $S_0, A_0, R_1, ..., S_{T-1}, A_{T-1}, R_T$
    $G \leftarrow 0$
    Loop para cada paso del episodio, $t = T-1, T-2, ..., 0$:
        $G \leftarrow \gamma G + R_{t+1}$
        $N(S_t) \leftarrow N(S_t) + 1$
        $V(S_t) \leftarrow V(S_t) + (1/N(S_t)) * (G - V(S_t))$

## Estimación de Q (first visit)

Inicializar, para todos $s \in S, a \in A$:
    $N(s, a) \leftarrow 0$
    $Q(s, a) \leftarrow$ valor arbitrario

Para cada episodio:
    Generar un episodio siguiendo $\pi$: $S_0, A_0, R_1, ..., S_{T-1}, A_{T-1}, R_T$
    $G \leftarrow 0$
    Loop para cada paso del episodio, $t = T-1, T-2, ..., 0$:
        $G \leftarrow \gamma G + R_{t+1}$
        Si la pareja $(S_t, A_t)$ no aparece en $(S_0, A_0), (S_1, A_1), ..., (S_{t-1}, A_{t-1})$:
            $N(S_t, A_t) \leftarrow N(S_t, A_t) + 1$
            $Q(S_t, A_t) \leftarrow Q(S_t, A_t) + (1/N(S_t, A_t)) * (G - Q(S_t, A_t))$

## Estimación de Q (every visit)

Inicializar, para todos $s \in S, a \in A$:
    $N(s, a) \leftarrow 0$
    $Q(s, a) \leftarrow$ valor arbitrario

Para cada episodio:
    Generar un episodio siguiendo $\pi$: $S_0, A_0, R_1, ..., S_{T-1}, A_{T-1}, R_T$
    $G \leftarrow 0$
    Loop para cada paso del episodio, $t = T-1, T-2, ..., 0$:
        $G \leftarrow \gamma G + R_{t+1}$
        $N(S_t, A_t) \leftarrow N(S_t, A_t) + 1$
        $Q(S_t, A_t) \leftarrow Q(S_t, A_t) + (1/N(S_t, A_t)) * (G - Q(S_t, A_t))$

> No es necesario usar 1/N, tambien se puede usar un $\alpha$  entre 0-1. Esto se llama: constant-$\alpha$ MC
> ![[Pasted image 20230709144428.png]]


# Métodos Monte Carlo de Control

Para encontrar políticas óptimas, los métodos Monte Carlo utilizan generalización de la estrategia de iteración de política, alternando entre evaluación y mejora de la política. Estos métodos incluyen:

- **Monte Carlo con Exploración inicial**: En este enfoque, cada par estado-acción es inicialmente explorado una cierta cantidad de veces antes de que el agente comience a explotar su conocimiento actual. Esto a veces se conoce como método de exploración optimista, porque inicialmente se asume que todas las acciones podrían ser óptimas. Una vez que se ha explorado cada par estado-acción suficientes veces, el agente pasa a una política greedy que siempre elige la acción que actualmente estima como la mejor.
  
  ![[Pasted image 20230624162129.png]]
Libro:
![[Pasted image 20230624184050.png]]
> La idea principal es que si o si se explore todos los pares estato accion alguna vez

- **Monte Carlo con $\epsilon$-greedy**: Este método mejora la política volviéndola "greedy" con respecto a la función de valor actual con una probabilidad $1-\epsilon$, y selecciona una acción aleatoria con una probabilidad $\epsilon$.
  
  ![[Pasted image 20230624162437.png]]

Los métodos Monte Carlo ofrecen una manera simple y poderosa de aprender de la interacción con el entorno sin requerir un modelo completo de las dinámicas del entorno. **Sin embargo, como requieren la finalización de episodios para realizar actualizaciones, pueden ser ineficientes o inaplicables en entornos con episodios muy largos o infinitos.**


<iframe width="560" height="315" src="https://www.youtube.com/embed/bpUszPiWM7o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


# Ventajas

1. **Flexibilidad**: Los métodos de Monte Carlo pueden aplicarse a una amplia variedad de problemas, ya que se basan en la generación de números aleatorios y no requieren suposiciones específicas sobre la distribución de los datos.
2. **Precisión**: Con un número suficientemente grande de iteraciones o simulaciones, los métodos de Monte Carlo pueden proporcionar estimaciones precisas de cantidades desconocidas o difíciles de calcular.
3. **Tratamiento de problemas complejos**: Los métodos de Monte Carlo pueden abordar problemas con múltiples variables y relaciones no lineales, lo que los hace especialmente útiles para modelar sistemas complejos.
4. **Incorporación de incertidumbre**: Estos métodos permiten tener en cuenta la incertidumbre en los datos de entrada, lo que puede ser crucial para la toma de decisiones y la evaluación de riesgos.

# Desventajas

1. **Tiempo de cálculo**: En algunos casos, los métodos de Monte Carlo pueden requerir un tiempo de cálculo considerablemente largo, especialmente si se necesitan muchas iteraciones para obtener resultados precisos. Esto puede limitar su aplicabilidad en problemas que requieren respuestas rápidas.
2. **Error de muestreo**: Existe la posibilidad de que los resultados obtenidos mediante métodos de Monte Carlo contengan un error de muestreo debido a la aleatoriedad inherente en la generación de números aleatorios. El tamaño de la muestra y la calidad de los generadores de números aleatorios pueden afectar la precisión de los resultados.
3. **Convergencia lenta**: Algunas veces, los métodos de Monte Carlo pueden tener una convergencia lenta, lo que significa que se necesitan muchas iteraciones para obtener una estimación precisa. Esto puede ser problemático cuando se dispone de recursos computacionales limitados.
4. **Dificultad para representar relaciones no lineales**: Si bien los métodos de Monte Carlo son adecuados para abordar problemas complejos, pueden enfrentar dificultades para representar relaciones no lineales complejas entre las variables.

# Opcional: off-policy

![[Pasted image 20230624162713.png]]

![[Pasted image 20230624163243.png]]


<iframe width="560" height="315" src="https://www.youtube.com/embed/C3p2wI4RAi8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
