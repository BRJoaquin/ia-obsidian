
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

Con esta definición, el error de N pasos se puede definir como:

$$ \delta_t = G_{t:t+N} - \hat{v}(S_t, w) $$

Y la actualización de los pesos se puede definir como:

$$ w \leftarrow w + \alpha \delta_t \nabla \hat{v}(S_t, w) $$

Donde:
- $\alpha$ es la tasa de aprendizaje.
- $\nabla \hat{v}(S_t, w)$ es el gradiente de la función de valor con respecto a los pesos.

La idea detrás del bootstrapping de N pasos es tratar de obtener lo mejor de ambos mundos. Aprovecha la eficiencia computacional de TD, ya que no es necesario esperar hasta el final de un episodio para hacer una actualización, pero también incorpora información de varias recompensas futuras como Monte Carlo, lo que puede mejorar la precisión de las actualizaciones. Sin embargo, como con cualquier compromiso, la elección de N puede requerir
