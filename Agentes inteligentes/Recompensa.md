La recompensa y el castigo son señales que el agente recibe del entorno como resultado de sus acciones. La recompensa es una señal positiva que indica que una acción fue beneficiosa o deseable, mientras que el castigo es una señal negativa que indica que una acción fue perjudicial o indeseable. El objetivo del agente es maximizar la suma total de las recompensas a lo largo del tiempo y minimizar las penalizaciones.

# Estocástica

Una recompensa **estocástica** es aquella que puede cambiar en cada iteración o episodio. Por ejemplo, en un juego de ajedrez, la recompensa puede ser la victoria o la derrota, pero si el oponente cambia de estrategia en cada juego, la recompensa será estocástica.

# No estocástica

Por otro lado, una recompensa **no estocástica** es aquella que no cambia en cada iteración o episodio. Por ejemplo, en un juego de damas, la recompensa puede ser el número de piezas capturadas, que no cambia de un juego a otro.

# Estacionaria

Una recompensa **estacionaria** es aquella que no cambia con el tiempo. Por ejemplo, en un juego de ajedrez, la recompensa por ganar siempre es la misma, independientemente de cuánto tiempo lleve el juego.
Vease [[Problemas estacionarios]]

# No Estacionaria

Una recompensa **no estacionaria** es aquella que cambia con el tiempo. Por ejemplo, en un juego de fútbol, la recompensa por marcar un gol puede ser mayor al inicio del partido que en los últimos minutos, ya que el tiempo restante influye en la importancia del gol.

Es importante tener en cuenta el tipo de recompensa en el diseño del algoritmo de aprendizaje por refuerzo, ya que puede afectar la manera en que el agente aprende y optimiza su comportamiento.

# Ejemplos

Supongamos que estás jugando un videojuego en el que debes recoger monedas en diferentes habitaciones. Cada vez que recoges una moneda, recibes una recompensa.

1. Recompensa estocástica y estacionaria: En este caso, la cantidad de recompensa que obtienes al recoger una moneda varía de forma aleatoria, pero el promedio de las recompensas se mantiene constante en todas las habitaciones. Por ejemplo, en la Habitación A, puedes recibir 5, 7 o 10 puntos al recoger una moneda, pero en promedio obtienes 7 puntos.
2. Recompensa no estocástica y estacionaria: Aquí, la cantidad de recompensa que obtienes al recoger una moneda es siempre la misma en todas las habitaciones. Por ejemplo, en la Habitación B, siempre recibes exactamente 8 puntos por cada moneda que recojas.
3. Recompensa estocástica y no estacionaria: En este caso, la cantidad de recompensa que obtienes al recoger una moneda varía de forma aleatoria, y también cambia a lo largo del tiempo. Por ejemplo, en la Habitación C, al principio del juego puedes recibir 3, 5 o 7 puntos al recoger una moneda, pero a medida que avanzas en el juego, las recompensas aumentan y puedes recibir 10, 12 o 15 puntos.
4. Recompensa no estocástica y no estacionaria: Aquí, la cantidad de recompensa que obtienes al recoger una moneda es siempre la misma, pero varía a lo largo del tiempo. Por ejemplo, en la Habitación D, al principio del juego recibes 5 puntos por cada moneda, pero a medida que avanzas, la cantidad de puntos aumenta gradualmente y pasas a recibir 8, 10 o 12 puntos por cada moneda.