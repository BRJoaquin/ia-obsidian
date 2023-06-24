La función de valor de acción $Q(s, a)$ de una política $\pi$ es el valor esperado de la suma total de las recompensas futuras descontadas después de tomar la acción $a$ en el estado $s$, y luego seguir la política $\pi$. Esta función mide cuánto "valor" tiene una acción en un estado dado en términos de la cantidad de recompensa que un agente puede esperar obtener en el futuro después de tomar esa acción y luego seguir una política específica.

En términos formales, la función de valor de acción se define como:

$$
Q^{\pi}(s, a) = E^{\pi}\left[ R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \ldots | S_t = s, A_t = a \right]
$$

donde:
- $E^{\pi}$ es el valor esperado dado que el agente sigue la política $\pi$ después de tomar la acción $a$.
- $R_{t+1}$ es la recompensa inmediata después del tiempo $t$.
- $\gamma$ es el factor de descuento, que determina cuánto se valora la recompensa inmediata en comparación con las recompensas futuras.

La principal diferencia entre la función de valor de estado y la función de valor de acción es que la primera se refiere a estados, mientras que la última se refiere a pares estado-acción.
