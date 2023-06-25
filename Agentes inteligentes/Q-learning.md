Q-Learning es uno de los algoritmos más populares y fundamentales en el campo del [[Aprendizaje por refuerzo]]. Es un [[Métodos de Diferencias temporales]] que busca aprender la [[Función de valor]] de acción óptima, Q*, **sin requerir un modelo del entorno**. Q-Learning es un método "**off-policy**", lo que significa que busca aprender la política óptima **independientemente** de la política que sigue el agente para seleccionar las acciones.

# Concepto general

El objetivo de Q-Learning es aprender una política que maximice la suma total de las recompensas futuras([[Control]]. Para esto, define una función Q que asigna un par estado-acción a un número real, interpretado como el valor esperado de seguir una política fija después de ver algún estado y tomar una acción.

La función Q se actualiza de acuerdo con la siguiente regla:

$$\Large
Q(s,a) ← Q(s,a) + α [r + γ max_a' Q(s',a') - Q(s,a)]
$$

donde:
- `α` es la tasa de aprendizaje.
- `r` es la recompensa recibida después de tomar la acción `a` en el estado `s`.
- `γ` es el factor de descuento, que determina cuánto valoramos las recompensas futuras en comparación con las inmediatas.
-  $max_aQ(s',a')$ es el valor máximo posible en el siguiente estado `s'`.

# Algoritmo

![[Pasted image 20230625112411.png]]

# Por que es off-policy?

Esto se logra a través del uso de la función `max` en la actualización de los valores Q. El agente selecciona la acción con el valor Q más alto para la siguiente actualización, **independientemente** de la acción que eligió bajo su política actual.

Esto es diferente del aprendizaje on-policy, donde las actualizaciones de los valores Q dependen de las acciones seleccionadas por la política actual del agente.



# Ventajas y desventajas

El Q-Learning tiene varias ventajas. En primer lugar, es un método model-free, lo que significa que no necesita un modelo preciso del entorno para aprender. En segundo lugar, es off-policy, lo que significa que puede aprender la política óptima mientras sigue otra política, lo que lo hace muy flexible.

Sin embargo, el Q-Learning también tiene desventajas. Por ejemplo, puede ser muy lento para converger, especialmente en entornos con muchos estados y acciones. Además, aunque teóricamente puede aprender la política óptima, en la práctica a menudo necesita un número muy grande de episodios para hacerlo.













# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/AJiG3ykOxmY?start=1142" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>