
TD(0) es el método más básico de [[Métodos de Diferencias temporales]]. **Este método se basa en la idea de que la estimación de un estado puede ser mejorada al considerar la recompensa inmediata y la estimación de valor del estado siguiente.**

A diferencia de los métodos de Monte Carlo que esperan hasta el final de un episodio para calcular una recompensa acumulativa y hacer una actualización, TD(0) hace sus actualizaciones después de cada paso.

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



1. **Objetivo de Monte Carlo (MC)**: En los métodos de Monte Carlo, el objetivo es estimar el valor esperado del retorno total `Gt` a partir de un estado específico. `Gt` es la suma total de las recompensas futuras a partir del tiempo `t`, teniendo en cuenta un factor de descuento `γ`. En los métodos de Monte Carlo, necesitamos esperar hasta el final del episodio para conocer el valor exacto de `Gt` antes de que podamos hacer una actualización. Es decir, la actualización se basa en un valor "real" o experimentado.

2. **Objetivo de Diferencias Temporales (TD Learning)**: Por otro lado, en TD Learning, el objetivo es estimar el valor esperado de la recompensa inmediata `Rt+1` más el valor estimado del estado siguiente `γV(St+1)`. A diferencia de MC, TD Learning no necesita esperar hasta el final del episodio para hacer una actualización. En su lugar, hace una actualización basada en la recompensa inmediata y la estimación de valor del estado siguiente. En otras palabras, TD Learning utiliza una estimación para hacer otra estimación. Este proceso se conoce como "bootstrapping".

3. **Bootstrapping**: Bootstrapping en el aprendizaje por refuerzo es cuando las estimaciones actuales se actualizan en función de otras estimaciones. En este caso, la estimación de valor de un estado en TD Learning se actualiza en función de la recompensa inmediata y la estimación de valor del estado siguiente. Esto contrasta con los métodos de Monte Carlo, que se basan en recompensas "reales" o experimentadas y no en estimaciones.

Ambos métodos, MC y TD Learning, buscan estimar el mismo valor, es decir, el valor esperado de la recompensa futura a partir de un estado específico bajo una política determinada `vπ(s)`. La principal diferencia entre ellos es si se basan en recompensas reales (MC) o en estimaciones (TD Learning).
