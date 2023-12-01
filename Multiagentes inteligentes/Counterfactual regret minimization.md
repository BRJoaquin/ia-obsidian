  
Counterfactual Regret Minimization (CFR) es un algoritmo iterativo de aprendizaje utilizado en la teoría de juegos para encontrar una estrategia aproximadamente equilibrada en juegos de información imperfecta. El "arrepentimiento" en este contexto se refiere a la diferencia entre la recompensa que un jugador podría haber recibido al tomar la mejor acción posible en retrospectiva y la recompensa que realmente recibió. La "minimización del arrepentimiento contrafactual" busca reducir la cantidad de arrepentimiento que un jugador experimentaría al no haber jugado la estrategia óptima en cada decisión del juego.

CFR es una técnica poderosa para encontrar estrategias en juegos de información imperfecta, lo que lo hace particularmente útil para juegos como el póker.

## Conceptos Clave en CFR

### Arrepentimiento Counterfactual
- Se refiere al arrepentimiento que un jugador tiene por no haber jugado la estrategia óptima en un momento particular, dado el conocimiento de lo que hubiera sido óptimo después del hecho.

### Actualización Iterativa
- CFR se basa en la idea de iterar a través de muchas rondas de juego, actualizando las estrategias basadas en el arrepentimiento acumulado.

### Utilidad de las Acciones
- En cada iteración, CFR evalúa la utilidad de cada acción posible desde el punto de vista de un jugador, considerando lo que hubiera pasado si se hubieran tomado diferentes acciones en cada punto de decisión.

## Funcionamiento de CFR

1. **Inicialización**: Todos los arrepentimientos y estrategias se inicializan a cero.
2. **Juego Iterativo**: Se juegan varias manos del juego, y en cada mano, se calculan los arrepentimientos para cada acción.
3. **Cálculo de Arrepentimiento**:
   - Para cada acción no tomada, se calcula la diferencia entre la utilidad que se hubiera obtenido de haber tomado esa acción y la utilidad de la acción realmente tomada.
4. **Actualización de Estrategia**:
   - Se actualizan las estrategias para favorecer las acciones con arrepentimiento positivo y se reducen las probabilidades de las acciones con arrepentimiento negativo.
5. **Convergencia**:
   - Con suficientes iteraciones, la estrategia converge a un equilibrio de Nash aproximado, donde el arrepentimiento promedio se minimiza.

## Ventajas de CFR

- **Eficiencia**: CFR ha demostrado ser capaz de resolver juegos de información imperfecta de gran tamaño, como el póker.
- **Robustez**: Puede encontrar estrategias que son robustas contra oponentes que pueden cambiar sus estrategias con el tiempo.
- **Adaptabilidad**: Aunque el cálculo puede ser intensivo, se adapta bien al aprendizaje en juegos complejos.

## Desafíos y Limitaciones

- **Computacionalmente Intensivo**: CFR puede requerir una gran cantidad de memoria y tiempo de cálculo, especialmente para juegos con muchas posibles historias.
- **Dependencia de los Datos**: La calidad de la solución de CFR puede depender de la cantidad y calidad de las iteraciones de juego realizadas.

CFR continúa siendo un área activa de investigación y desarrollo, impulsando los límites de lo que se puede lograr en el campo de la inteligencia artificial para juegos de información imperfecta.

# Pseudo-codigo

![[Pasted image 20231201173237.png]]