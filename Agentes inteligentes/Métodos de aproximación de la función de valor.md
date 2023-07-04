Los **métodos de aproximación de la función de valor** se utilizan en el aprendizaje por refuerzo cuando el espacio de estados o el espacio de acción **es demasiado grande para representar la función de valor en una tabla**.

Estos métodos se basan en **aprender una función aproximada que puede estimar el valor de un estado (o par estado-acción**) dado su representación de [[Agentes inteligentes/Características|Características]].

![[Pasted image 20230704101213.png]]

Los métodos de aproximación de la función de valor pueden dividirse en dos categorías principales, según si tratan de aproximar la función de valor estado-valor ($V$) o la función de valor acción-valor ($Q$):

1. **Métodos de Aproximación de la Función de Valor Estado-Valor (V)**: Estos métodos tratan de aprender una función $V(s; w)$ que estima el valor de un estado $s$ dada una representación de características $x(s)$ y un vector de parámetros $w$. Ejemplos de este tipo de métodos son el [[Descenso de Gradiente Estocástico (Stochastic Gradient Descent, SGD)]] y el [[Actor-Critic]].

2. **Métodos de Aproximación de la Función de Valor Acción-Valor (Q)**: Estos métodos tratan de aprender una función $Q(s, a; w)$ que estima el valor de una acción $a$ en un estado $s$ dada una representación de características $x(s, a)$ y un vector de parámetros $w$. Ejemplos de este tipo de métodos son el Q-Learning con Aproximación de la Función de Valor y el Aprendizaje Profundo por Refuerzo (DRL).

# Ventajas y Desventajas

La principal ventaja de los métodos de aproximación de la función de valor es que pueden manejar espacios de estado y acción mucho más grandes que los métodos tabulares. También pueden manejar espacios de estado y acción continuos, mientras que los métodos tabulares sólo pueden manejar espacios discretos.

Sin embargo, los métodos de aproximación de la función de valor son **generalmente más difíciles de implementar y afinar que los métodos tabulares**. Además, **la convergencia a la política óptima no siempre está garantizada**, especialmente en los casos en que la función de aproximación no puede representar exactamente la función de valor de la política óptima.

## Problemas de Convergencia

Los métodos de aproximación de la función de valor pueden tener problemas de convergencia. Esto se debe a que la función de aproximación puede no ser capaz de representar exactamente la función de valor de la política óptima. Además, el proceso de ajuste de los parámetros del modelo es un proceso de optimización que puede converger a mínimos locales en lugar de al mínimo global.

# Overfitting y Underfitting

Al igual que en otros tipos de aprendizaje supervisado, los métodos de aproximación de la función de valor pueden sufrir de [[Sobreajuste (Overfitting)]] y [[Subajuste (Underfitting)]]. 

El **sobreajuste** ocurre cuando el modelo se ajusta demasiado a los datos de entrenamiento y pierde la capacidad de generalizar a nuevos datos. Esto puede suceder cuando la función de aproximación es demasiado compleja en relación con la cantidad de datos de entrenamiento disponibles.

El **subajuste** ocurre cuando el modelo no se ajusta lo suficiente a los datos de entrenamiento y no captura la estructura subyacente de los datos. Esto puede suceder cuando la función de aproximación es demasiado simple para representar la complejidad de la función de valor real.

## Regularización

La [[Regularización|regularización]] es una técnica que se utiliza para prevenir el sobreajuste al añadir un término de penalización a la función de error que el algoritmo trata de minimizar. Este término de penalización tiende a reducir la complejidad del modelo y a hacer que el modelo prefiera soluciones más simples. La regularización puede ser especialmente útil en los métodos de aproximación de la función de valor cuando se dispone de datos de entrenamiento limitados.

# Ajuste de Parámetros del Modelo

Los métodos de aproximación de la función de valor dependen de un conjunto de parámetros o pesos, generalmente denotados como $w$. **La tarea del algoritmo de aprendizaje es ajustar estos parámetros para que la función de valor aproximada se acerque lo más posible a la función de valor real**.

El ajuste de los parámetros se realiza típicamente utilizando métodos de optimización basados en el gradiente, como el descenso del gradiente estocástico (SGD). En cada paso, se calcula el gradiente de la función de error con respecto a los parámetros, y se actualizan los parámetros en la dirección opuesta al gradiente.

# Métodos de Aproximación de Base Lineal

Los métodos de aproximación de base lineal utilizan una combinación lineal de características para representar la función de valor. La forma general de la función de valor aproximada es:

$V(s; w) = w_1 \cdot f_1(s) + w_2 \cdot f_2(s) + \ldots + w_n \cdot f_n(s)$

donde $f_i(s)$ son las características del estado $s$, y $w_i$ son los parámetros del modelo. Los métodos de aproximación de base lineal son simples y eficientes, pero pueden ser limitados en su capacidad para representar funciones de valor complejas.

# Métodos de Aproximación de Base no Lineal

Los métodos de aproximación de base no lineal utilizan una combinación no lineal de características para representar la función de valor. Estos métodos pueden representar funciones de valor más complejas que los métodos de aproximación de base lineal.

Una forma común de realizar una aproximación de base no lineal es utilizar una red neuronal. La red neuronal toma las características del estado como entrada y produce una estimación de la función de valor como salida. Los parámetros del modelo son los pesos y los sesgos de la red neuronal.

El uso de aproximaciones de base no lineal puede mejorar la capacidad de los métodos de aprendizaje por refuerzo para resolver problemas complejos. Sin embargo, estos métodos también pueden ser más difíciles de entrenar y requieren más recursos computacionales.

# Error Cuadrático Medio del Valor (Mean Squared Value Error)

El **Error Cuadrático Medio del Valor (MSVE)** es una función de pérdida comúnmente utilizada en el aprendizaje por refuerzo y en otros problemas de aprendizaje supervisado. 

El MSVE mide la diferencia cuadrática media entre los valores reales (o deseados) y los valores predichos por el modelo de aprendizaje. En el contexto del aprendizaje por refuerzo, los "valores reales" suelen ser los retornos obtenidos siguiendo una política dada, y los "valores predichos" son las estimaciones de la función de valor por parte del modelo.

Matemáticamente, el MSVE se define de la siguiente manera:

$$VE(\pi) = \sum_{s \in S} d(s|\pi) [v_\pi(s) - V(s; w)]^2$$

donde:

- $S$ es el conjunto de todos los estados.
- $\pi$ es la política que se está siguiendo.
- $d(s|\pi)$ es la distribución de estados bajo la política $\pi$.
- $v_\pi(s)$ es el valor verdadero del estado $s$ bajo la política $\pi$.
- $V(s; w)$ es la estimación del valor del estado $s$ por el modelo con parámetros $w$.

La función de pérdida MSVE penaliza más fuertemente las predicciones que están lejos del valor real, debido al cuadrado de la diferencia. Por lo tanto, minimizar la MSVE tiende a hacer que el modelo se ajuste a los valores reales lo más cerca posible, en términos del error cuadrático medio.

Un aspecto importante a tener en cuenta es que el MSVE pondera los errores en cada estado por la probabilidad de visitar ese estado bajo la política que se está siguiendo. Esto significa que los estados que son visitados con frecuencia tendrán un mayor impacto en el valor de la MSVE.

![[Pasted image 20230704102127.png]]


# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/Vky0WVh_FSk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> 
