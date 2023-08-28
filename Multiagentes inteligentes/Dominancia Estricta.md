
La dominancia estricta es un concepto en la [[Teoría de Juegos]] que describe una relación entre dos estrategias. Una estrategia domina estrictamente a otra si proporciona una mayor utilidad al jugador que la elige, sin importar las estrategias elegidas por los demás jugadores.

Matemáticamente, la estrategia $s_i$ domina estrictamente a la estrategia $s'_i$ para el jugador $i$ si:

$$\Large
u_i(s_i, s_{-i}) > u_i(s'_i, s_{-i}) \text{ para todo } s_{-i}
$$

donde:
- $u_i$ es la utilidad del jugador $i$
- $s_i$ y $s'_i$ son las estrategias del jugador $i$
- $s_{-i}$ son las estrategias de los demás jugadores

## Ejemplo

Considere el siguiente juego:

|        | Estrategia A | Estrategia B |
|--------|--------------|--------------|
| **Estrategia X** | (4, 3)       | (3, 2)       |
| **Estrategia Y** | (2, 2)       | (1, 1)       |

En este caso, para el jugador 1, la Estrategia X domina estrictamente la Estrategia Y, ya que los pagos son mayores en ambas celdas correspondientes (4 > 2 y 3 > 1).

## Importancia

La dominancia estricta es útil para simplificar el análisis de un juego. Si una estrategia está estrictamente dominada, entonces nunca será una respuesta racional, y puede ser eliminada de consideración.