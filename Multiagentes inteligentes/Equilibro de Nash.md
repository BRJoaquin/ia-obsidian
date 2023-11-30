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

# Ejemplo 1

![[Pasted image 20231130102807.png]]

# Ejemplo 2

![[Pasted image 20231130103337.png]]

El subrayado del número 5 en la celda correspondiente a (U, L) en la matriz de pagos del juego indica que esta es la mejor respuesta para el Jugador 1 cuando el Jugador 2 elige L. Es el pago más alto que el Jugador 1 puede obtener dado que el Jugador 2 ha elegido L.

Sin embargo, este no está marcado como un Equilibrio de Nash porque, aunque es la mejor respuesta para el Jugador 1 dado L, no es la mejor respuesta para el Jugador 2 dada la estrategia U del Jugador 1. Para que una celda represente un Equilibrio de Nash, debe ser la mejor respuesta para ambos jugadores simultáneamente.

El subrayado generalmente se utiliza para resaltar la mejor respuesta en la matriz de pagos. Si ambos jugadores tienen sus mejores respuestas subrayadas en la misma celda, entonces esa celda representa un Equilibrio de Nash. En el ejemplo dado, el 5 en (U, L) está subrayado porque es el mejor resultado para el Jugador 1 si se elige L, pero dado que la mejor respuesta del Jugador 2 para U no es L, (U, L) no se considera un Equilibrio de Nash.

- La estrategia (D, C) es un equilibrio de Nash. Aquí, D es la mejor respuesta de Player 1 a la estrategia C de Player 2, y C es la mejor respuesta de Player 2 a la estrategia D de Player 1. Esto se indica con los números subrayados 3 en D y 6 en C.
    
- De manera similar, (M, R) es un equilibrio de Nash. M es la mejor respuesta de Player 1 a R de Player 2, y R es la mejor respuesta de Player 2 a M de Player 1. Esto se señala con los números subrayados 4 en M y 5 en R.

# Ejemplo 3

![[Pasted image 20231130103620.png]]
