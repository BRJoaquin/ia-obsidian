
El bootstrapping de N pasos es una técnica en el aprendizaje por refuerzo que combina las ideas del [[Métodos Monte Carlo]] y de los [[Métodos de Diferencias temporales]] para actualizar las estimaciones de los valores de las acciones o de los estados.

En el aprendizaje por refuerzo, el objetivo es aprender una política que maximice la suma total de las recompensas futuras, también conocida como retorno. En este contexto, el bootstrapping se refiere a la idea de actualizar las estimaciones de los valores basándose en otras estimaciones de los valores. 

Las técnicas de Monte Carlo y TD representan dos extremos de cómo se pueden hacer estas actualizaciones. Monte Carlo utiliza el retorno real observado al final de un episodio para hacer las actualizaciones, mientras que TD utiliza la recompensa inmediata más la estimación del valor del próximo estado.

![[Pasted image 20230705153745.png]]

El bootstrapping de N pasos se sitúa en algún punto intermedio entre estas dos técnicas. En lugar de esperar hasta el final del episodio como en Monte Carlo, o de usar solo la próxima recompensa y el valor estimado del próximo estado como en TD, el bootstrapping de N pasos utiliza las N próximas recompensas y el valor estimado del estado después de N pasos para hacer la actualización.

Por lo tanto, el bootstrapping de N pasos se puede ver como un compromiso entre la alta varianza de Monte Carlo y el sesgo de TD. Con N = 1, obtenemos el método TD(0), y a medida que N se acerca al tamaño del episodio, el bootstrapping de N pasos se aproxima a Monte Carlo.

La actualización de N pasos se puede definir como:

$$\Large
 G_{t:t+N} = R_{t+1} + \gamma R_{t+2} + \ldots + \gamma^{N-1} R_{t+N} + \gamma^N \hat{v}(S_{t+N}, w) $$

Donde:
- $G_{t:t+N}$ es la recompensa acumulada de N pasos.
- $R_{t+k}$ es la recompensa en el paso de tiempo t+k.
- $\gamma$ es el factor de descuento.
- $\hat{v}(S_{t+N}, w)$ es la estimación del valor del estado después de N pasos.

![[Pasted image 20230705154552.png]]
  
La idea detrás del bootstrapping de N pasos es tratar de obtener lo mejor de ambos mundos. Aprovecha la eficiencia computacional de TD, ya que no es necesario esperar hasta el final de un episodio para hacer una actualización, pero también incorpora información de varias recompensas futuras como Monte Carlo, lo que puede mejorar la precisión de las actualizaciones. Sin embargo, como con cualquier compromiso, la elección de N puede requerir  alguna experimentación y depende del problema específico que se esté resolviendo. 

Por ejemplo, en problemas con recompensas raras o esporádicas, podría ser beneficioso utilizar un valor más grande de N para capturar la contribución de estas recompensas en las actualizaciones de valor. Por otro lado, en problemas con recompensas frecuentes, un valor más pequeño de N podría ser suficiente. 

Aunque el bootstrapping de N pasos puede ser más complejo de implementar que TD(0) o Monte Carlo debido a la necesidad de mantener y actualizar una ventana de recompensas y estados, ha demostrado ser una técnica efectiva en la práctica. En particular, puede ser útil en problemas de aprendizaje por refuerzo con horizontes de tiempo largo, donde esperar hasta el final de un episodio para hacer una actualización como en Monte Carlo podría ser impracticable. 

Los algoritmos que utilizan el bootstrapping de N pasos incluyen n-step TD, n-step SARSA, y n-step Tree Backup. Estos algoritmos aplican la idea del bootstrapping de N pasos a los métodos on-policy TD(0), SARSA, y off-policy Q(σ), respectivamente. 

Finalmente, es importante destacar que aunque el bootstrapping de N pasos puede reducir la varianza de las estimaciones de los valores en comparación con TD(0), todavía puede estar sujeto a un sesgo debido a la dependencia en las estimaciones de los valores para hacer las actualizaciones. Sin embargo, a medida que el algoritmo aprende y las estimaciones de los valores se vuelven más precisas, este sesgo se reduce.

# Algortimos



# Sesgo y Varianza en Métodos de Bootstrapping de N Pasos, TD y Monte Carlo

## Sesgo

En el contexto de TD, Monte Carlo y bootstrapping de N pasos, el sesgo se refiere a la diferencia entre las expectativas de sus estimaciones de valor y los verdaderos valores. 

- **Monte Carlo:** Este método no tiene sesgo ya que las estimaciones se basan en las recompensas reales de episodios completos. No obstante, es importante tener en cuenta que aunque las estimaciones de Monte Carlo son insesgadas, pueden tener una alta varianza debido a la dependencia de las recompensas individuales que pueden ser estocásticas.

- **TD:** En TD(0) existe un sesgo introducido por la dependencia en las estimaciones actuales de los valores para las actualizaciones. TD es un método de un paso que utiliza la recompensa inmediata más la estimación del valor del siguiente estado para actualizar el valor del estado actual. Por tanto, las estimaciones de TD pueden estar sesgadas si las estimaciones actuales de los valores son inexactas.

- **Bootstrapping de N pasos:** Este método combina ideas de Monte Carlo y TD y su sesgo depende del número de pasos, N. Con N = 1, obtenemos el método TD(0), y a medida que N se acerca al tamaño del episodio, el bootstrapping de N pasos se aproxima a Monte Carlo. Por lo tanto, el sesgo en este método disminuye a medida que N aumenta y las estimaciones se basan más en las recompensas reales y menos en las estimaciones de los valores.

## Varianza

- **Monte Carlo:** Aunque Monte Carlo no tiene sesgo, puede tener una alta varianza. Las estimaciones de los valores dependen de las recompensas individuales que pueden variar considerablemente de un episodio a otro. 

- **TD:** TD(0) tiene menor varianza que Monte Carlo ya que las actualizaciones se basan en la recompensa inmediata más la estimación del valor del siguiente estado. Esto suaviza las actualizaciones y reduce su variabilidad en comparación con Monte Carlo.

- **Bootstrapping de N pasos:** La varianza de este método también depende de N. A medida que N aumenta y el método se aproxima a Monte Carlo, la varianza aumenta. A medida que N disminuye y el método se aproxima a TD, la varianza disminuye.

En resumen, existe un compromiso entre sesgo y varianza en estos métodos. Monte Carlo tiene alta varianza pero no tiene sesgo. TD tiene bajo sesgo y baja varianza. Bootstrapping de N pasos proporciona un compromiso entre los dos, y la elección de N permite ajustar este compromiso.
