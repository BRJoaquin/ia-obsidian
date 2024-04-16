# TD(0)

Supongamos que tienes un agente que se mueve en una cuadrícula de 4x4. El objetivo del agente es llegar a la esquina inferior derecha (4,4) partiendo de la esquina superior izquierda (1,1). Las recompensas son -1 por cada movimiento. Los movimientos posibles en cada estado son abajo, arriba, izquierda y derecha. 

Asuma que con una pólitica $\pi$ se generaron los siguientes episodios:
- **Episodio 1**: Derecha (D), Derecha (D), Derecha (D), Abajo (A), Abajo (A), Abajo (A)
- **Episodio 2**: Derecha (D), Abajo (A), Abajo (A), Derecha (D), Derecha (D), Abajo (A)
- **Episodio 3**: Abajo (A), Abajo (A), Derecha (D), Derecha (D), Derecha (D), Abajo (A)

Utilize el enfoque de SARSA para estimar $V(s)$ y $Q(s,a)$

Notas:
- Tasa de aprendizaje ($\alpha$): 0.1
- Factor de descuento ($\gamma$): 0.9

> Asuma que el valor $Q$ es cero para todos los pares estado-acción.
# Ejercicio 2: Q-Learning

Utilizando la estimación de $Q(s,a)$ del ejercicio anterior. Genere un episodio desde (1,1) greedymente, y en caso de que dos ó mas acciones tengan el mismo valor se prefieren tomar las acciones en este orden: derecha, abajo, izquierda, arriba.


Sin embargo, esta vez, asume que siempre se selecciona la acción con el mayor Q-value (política greedy).

# Ejercicio 3: Evitando el Abismo

Utiliza la misma cuadrícula de 4x4 de los ejercicios anteriores, pero esta vez añade un "abismo" en la celda (3, 2) (utilizando la notación (fila, columna) con base en 1). La recompensa de caer en el abismo es -10, y moverse incurre en una recompensa de -1 como antes. Las reglas de movimiento siguen siendo las mismas.

## Parte A: SARSA con Abismo

Realiza una iteración de actualización del algoritmo SARSA teniendo en cuenta el abismo. Supongamos que la política inicial lleva al agente a una ruta que incluye el abismo:

1. Describe el efecto esperado del abismo en la política aprendida con SARSA, considerando que SARSA es un algoritmo on-policy.
2. Realiza y describe una iteración de actualización específica que involucre el abismo, usando los mismos parámetros ($\alpha = 0.1$, $\gamma = 0.9$, ε-greedy con $\epsilon = 0$).

## Parte B: Q-Learning con Abismo

Ahora aplica el algoritmo Q-Learning teniendo en cuenta el abismo:

1. Describe cómo el abismo afectaría la política aprendida con Q-Learning en comparación con SARSA, especialmente en términos de exploración y explotación.
2. Realiza y describe una iteración de actualización específica que involucre el abismo, asumiendo una selección greedy de acciones basada en los Q-values, con los mismos parámetros de aprendizaje.

## Reflexión sobre el Abismo

- **Comparación de Estrategias**: Después de completar ambas partes, reflexiona sobre cómo el abismo afecta las decisiones de política en SARSA y Q-Learning. Considera cómo cada algoritmo se adapta a las recompensas negativas severas y qué esto puede decir sobre su uso en entornos con penalizaciones significativas.

- **Riesgo vs. Seguridad**: Piensa en cómo la presencia del abismo puede cambiar la estrategia de exploración del agente. ¿El agente se vuelve más cauteloso con SARSA en comparación con Q-Learning, o viceversa?

Para más info:
- Example 6.6: Cliff Walking (cap 6.5, Reinforcement Learning. An Introduction", R.S. Sutton & A.G. Barto (2018)
- [Temporal Difference Learning (including Q-Learning) | Reinforcement Learning Part 4](https://www.youtube.com/watch?v=AJiG3ykOxmY&pp=ygUkY2xpZmYgd2Fsa2luZyByZWluZm9yY2VtZW50IGxlYXJuaW5n)