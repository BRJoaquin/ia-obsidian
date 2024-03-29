
TD(0) es el método más básico de [[Métodos de Diferencias temporales]]. **Este método se basa en la idea de que la estimación de un estado puede ser mejorada al considerar la recompensa inmediata y la estimación de valor del estado siguiente.**

A diferencia de los [[Métodos Monte Carlo]] que esperan hasta el final de un episodio para calcular una recompensa acumulativa y hacer una actualización, TD(0) hace sus actualizaciones después de cada paso.

El pseudocódigo para el algoritmo TD(0) sería:

```python
Initialize V(s) for all s in states, arbitrarily except V(terminal) = 0

Repeat (for each episode):
    Initialize S
    Repeat (for each step of episode):
        A = action given by policy for S
        Take action A, observe R, S'
        V(S) = V(S) + alpha * [R + gamma * V(S') - V(S)]
        S = S'
    until S is terminal
```

Donde:

- `V(s)` es la función de valor del estado `s`.
- `alpha` es la tasa de aprendizaje.
- `R` es la recompensa inmediata después de tomar la acción `A`.
- `gamma` es el factor de descuento, que determina cuánto valor se da a las recompensas futuras en comparación con las recompensas inmediatas.
- `S'` es el estado siguiente después de tomar la acción `A`.
- `V(S')` es la estimación de valor del estado siguiente `S'`.

En clase:
![[Pasted image 20230624190820.png]]

1. **Objetivo de Monte Carlo (MC)**: En los métodos de Monte Carlo, el objetivo es estimar el valor esperado del retorno total `Gt` a partir de un estado específico. `Gt` es la suma total de las recompensas futuras a partir del tiempo `t`, teniendo en cuenta un factor de descuento `γ`. En los métodos de Monte Carlo, necesitamos esperar hasta el final del episodio para conocer el valor exacto de `Gt` antes de que podamos hacer una actualización. **Es decir, la actualización se basa en un valor "real" o experimentado.**

2. **Objetivo de Diferencias Temporales (TD Learning)**: Por otro lado, en TD Learning, el objetivo es estimar el valor esperado de la recompensa inmediata `Rt+1` más el valor estimado del estado siguiente `γV(St+1)`. A diferencia de MC, TD Learning no necesita esperar hasta el final del episodio para hacer una actualización. En su lugar, hace una actualización basada en la recompensa inmediata y **la estimación de valor del estado siguiente**. **En otras palabras, TD Learning utiliza una estimación para hacer otra estimación**. Este proceso se conoce como "**bootstrapping**".

3. **Bootstrapping**: **Bootstrapping en el aprendizaje por refuerzo es cuando las estimaciones actuales se actualizan en función de otras estimaciones**. En este caso, la estimación de valor de un estado en TD Learning se actualiza en función de la recompensa inmediata y la estimación de valor del estado siguiente. Esto contrasta con los métodos de **Monte Carlo, que se basan en recompensas "reales" o experimentadas y no en estimaciones**.

Ambos métodos, MC y TD Learning, buscan estimar el mismo valor, es decir, el valor esperado de la recompensa futura a partir de un estado específico bajo una política determinada `vπ(s)`. La principal diferencia entre ellos es si se basan en recompensas reales (MC) o en estimaciones (TD Learning).

# Estimación de Q

![[Pasted image 20230624191555.png]]

# MC vs TD ejemplo

Claro, aquí tienes un ejemplo:

Imagina un escenario donde tienes un agente que está aprendiendo a jugar al ajedrez. 

- **Monte Carlo (MC)**: En este caso, el agente juega una partida completa de ajedrez, eligiendo acciones de acuerdo con su política actual. Al final de la partida, el agente recibe una recompensa (1 si ganó, -1 si perdió, 0 si es un empate). Entonces, el agente retrocede y actualiza el valor de todos los estados (es decir, las posiciones del tablero de ajedrez) que experimentó durante la partida en función de la recompensa obtenida. Si el agente ganó, todos los estados que llevan a la victoria aumentarán su valor, y si el agente perdió, todos los estados que llevaron a la derrota disminuirán su valor. En este caso, la actualización se basa en el resultado "real" o experimentado de la partida.

- **Diferencias Temporales (TD Learning)**: Por otro lado, en TD Learning (específicamente, TD(0)), el agente no tiene que esperar hasta el final de la partida para hacer una actualización. Después de cada movimiento, el agente observa la recompensa inmediata (que podría ser 0 si la partida aún no ha terminado) y la estimación de valor del siguiente estado (la posición del tablero de ajedrez después de su movimiento), y utiliza esta información para actualizar el valor del estado actual. Esta actualización se basa en una estimación (la estimación de valor del estado siguiente), lo que permite al agente aprender más rápidamente porque no tiene que esperar hasta el final de la partida para hacer una actualización.


# Sesgo y varianza con respecto a MC

1. Sesgo:
    - Monte Carlo: Los métodos de Monte Carlo no tienen sesgo inherente en las estimaciones de los valores de la función de valor. Debido a que se basan en la promediación de las recompensas obtenidas a lo largo de múltiples episodios, las estimaciones tienden a ser imparciales. Sin embargo, el sesgo puede introducirse debido a la función de promediación utilizada o a errores de muestreo en la recopilación de datos.
      
    - TD(0): Los métodos TD(0) pueden tener un sesgo inherente en las estimaciones de la función de valor. Esto se debe a que los valores se actualizan utilizando estimaciones basadas en el siguiente estado y la siguiente acción, en lugar de esperar hasta el final del episodio como en Monte Carlo. Este sesgo puede afectar las estimaciones de la función de valor, especialmente si hay errores sistemáticos en las transiciones de estado y las recompensas.
      
2. Varianza:
    - Monte Carlo: Los métodos de Monte Carlo tienden a tener una mayor varianza en las estimaciones de la función de valor debido a que se basan en promedios de múltiples episodios. Esto se debe a que las estimaciones se ven afectadas por la variabilidad inherente en los resultados de cada episodio, especialmente cuando el número de episodios es limitado.
      
    - TD(0): Los métodos TD(0) tienen una varianza más baja en las estimaciones de la función de valor en comparación con Monte Carlo. Esto se debe a que los valores se actualizan a lo largo del tiempo en cada transición de estado, lo que permite una propagación más rápida de las actualizaciones de valores y una convergencia más rápida en entornos estacionarios.
