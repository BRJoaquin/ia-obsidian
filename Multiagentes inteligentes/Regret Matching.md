
Regret matching es un algoritmo de aprendizaje en teoría de juegos que forma parte de los procesos de aprendizaje adaptativo y se utiliza para llegar a equilibrios en juegos repetidos. Desarrollado por Sergiu Hart y Andreu Mas-Colell en 2000, el concepto de "regret" (lamento o arrepentimiento) es clave en este algoritmo. Se refiere a la diferencia entre la recompensa que un jugador ha obtenido y la que podría haber obtenido si hubiera jugado de otra manera.

En el contexto del regret matching, los jugadores ajustan sus estrategias con el tiempo, basándose en el nivel de arrepentimiento por no haber jugado las mejores respuestas en el pasado. Aquí hay una descripción más detallada de cómo funciona y sus implicaciones:

**Mecanismo Básico:**

- **Arrepentimiento**: Los jugadores calculan el arrepentimiento para cada acción posible, que es la diferencia entre la utilidad que habrían recibido si hubieran jugado esa acción en cada ronda anterior y la utilidad que realmente recibieron.
    
- **Actualización de Estrategias**: En cada período, los jugadores tienen la posibilidad de cambiar sus estrategias basándose en sus niveles de arrepentimiento. Si no hay arrepentimiento por la estrategia actual, no hay razón para cambiarla. Si hay arrepentimiento, hay una mayor probabilidad de cambiar a una estrategia que podría haber funcionado mejor en el pasado.
    
- **Matching del Regret**: La probabilidad de cambiar a una estrategia particular es proporcional al arrepentimiento acumulado para esa estrategia. Así, las estrategias que habrían dado mejores resultados en el pasado son elegidas con mayor frecuencia.
    

**Ventajas del Regret Matching:**

1. **Convergencia**: Bajo ciertas condiciones, se ha demostrado que el regret matching converge a un equilibrio de Nash en juegos repetidos con dos jugadores y en algunos juegos con múltiples jugadores.
    
2. **Simplicidad**: A diferencia de otros algoritmos de aprendizaje que pueden requerir un seguimiento complejo de la historia del juego o suposiciones sobre las estrategias de los oponentes, el regret matching solo requiere que los jugadores recuerden su propio historial de utilidades y acciones.
    
3. **Robustez**: El algoritmo es bastante robusto en diferentes entornos y no necesita ajustes finos para diferentes juegos.
    

**Desventajas del Regret Matching:**

1. **Velocidad de Convergencia**: La velocidad con la que el regret matching converge a un equilibrio de Nash puede ser lenta, especialmente en juegos complejos con muchos jugadores y estrategias.
    
2. **Dependencia de la Historia**: Aunque más simple que otros algoritmos, el regret matching todavía depende de mantener un registro histórico de utilidades y acciones, lo cual puede no ser factible o deseable en todos los contextos.
    
3. **Necesidad de Repetición**: El regret matching está diseñado para juegos que se juegan repetidamente, y su aplicación en situaciones de una sola vez no es directa.
    


# FP vs RM



# Video


<iframe width="560" height="315" src="https://www.youtube.com/embed/_XIdEr-wtJg?si=fsbNVbINuPI7SCA0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
