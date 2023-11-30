El equilibrio de Nash es un concepto esencial en la [[Teoría de Juegos]]. Representa una situación en la que ningún jugador puede beneficiarse cambiando su estrategia, siempre y cuando los demás mantengan las suyas inalteradas. En términos matemáticos:

$$\large
\text{Si } s^* \text{ es un equilibrio de Nash, entonces } u_i(s^*) \geq u_i(s'_i, s^*_{-i}) \text{ para todo } s'_i \text{ y todo } i
$$

donde $u_i$ es la utilidad del jugador $i$, $s^*$ es el perfil de estrategia en equilibrio, $s'_i$ es una estrategia alternativa para el jugador $i$ y $s^*_{-i}$ son las estrategias de los demás jugadores.

## Ejemplo

Considera el siguiente juego:

|        | Estrategia A | Estrategia B |
|--------|--------------|--------------|
| **Estrategia X** | (3, 2)       | (1, 1)       |
| **Estrategia Y** | (2, 1)       | (2, 2)       |

Si el jugador 1 elige la Estrategia X y el jugador 2 la Estrategia A, los pagos serían (3, 2).

El equilibrio de Nash se encuentra en una celda donde ninguno de los jugadores tiene incentivo para cambiar su estrategia. En este caso, la celda (3, 2) es un equilibrio de Nash.

# Equilibrio de Nash en Sistemas Multiagentes Inteligentes

El equilibrio de Nash, originario de la [[Teoría de Juegos|teoría de juegos]], encuentra aplicaciones en [[Sistema multiagente|sistemas multiagentes inteligentes]]. En este contexto, los agentes inteligentes interactúan entre sí, y el equilibrio de Nash describe una situación en la que ninguno de los agentes tiene incentivo para cambiar su estrategia, dado lo que hacen los demás.

El Equilibrio de Nash puede ser puro o mixto:

- **Equilibrio de Nash Puro**: Cada jugador elige una estrategia específica y no cambia su elección a lo largo del tiempo. Esto es común en juegos estáticos donde los jugadores toman una decisión simultáneamente.
    
- **Equilibrio de Nash Mixto**: Los jugadores eligen una estrategia aleatoria según una distribución de probabilidad fija. Esto es relevante en juegos con un elemento de azar o incertidumbre, donde las estrategias mixtas pueden estabilizar el juego al hacer que las intenciones de los jugadores sean menos predecibles.


Sin embargo, el Equilibrio de Nash no necesariamente garantiza que el resultado sea óptimo desde el punto de vista del grupo o de la sociedad. A veces, el equilibrio puede llevar a un "equilibrio ineficiente" o a un "equilibrio subóptimo", donde los jugadores se asientan en un estado que no es socialmente óptimo, un fenómeno conocido como la "Tragedia de los Comunes".
