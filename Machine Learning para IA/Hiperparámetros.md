En el [[Machine Learning]] y en las redes neuronales, los hiperparámetros son variables que influyen en el proceso de entrenamiento y en la estructura del modelo. A diferencia de los parámetros del modelo, que son aprendidos durante el entrenamiento, los hiperparámetros se configuran antes del entrenamiento y no se actualizan automáticamente durante el proceso de aprendizaje.

Los hiperparámetros pueden tener un impacto significativo en el rendimiento y la generalización de un modelo. A continuación se enumeran algunos ejemplos comunes de hiperparámetros en diferentes contextos de aprendizaje automático:

1.  **Tasa de aprendizaje (learning rate):** Es un hiperparámetro que determina la magnitud de los cambios en los parámetros del modelo durante el entrenamiento. Una tasa de aprendizaje alta puede conducir a una convergencia más rápida, pero también puede causar oscilaciones o divergencia, mientras que una tasa de aprendizaje baja puede resultar en una convergencia más lenta pero más estable.

2.  **Número de épocas:** Es el número de veces que el algoritmo de entrenamiento pasa por todo el conjunto de datos de entrenamiento. Un número demasiado bajo de épocas puede resultar en un modelo subajustado, mientras que un número demasiado alto puede causar un sobreajuste.

3.  **Tamaño del lote (batch size):** Es la cantidad de ejemplos de entrenamiento utilizados para calcular el gradiente en cada iteración del algoritmo de gradiente descendente. El tamaño del lote afecta la velocidad de convergencia y la calidad de la solución final.

4.  **Número de capas y neuronas en una red neuronal:** Estos hiperparámetros definen la arquitectura de una red neuronal y pueden afectar la capacidad del modelo y su habilidad para generalizar a datos no vistos.

5.  **Función de activación:** Es la función utilizada para calcular la salida de una neurona en una red neuronal. Ejemplos comunes de funciones de activación incluyen ReLU, tanh y sigmoide.

6.  **Tamaño de los filtros y número de filtros en una red convolucional:** Estos hiperparámetros definen la arquitectura de una capa convolucional en una red neuronal convolucional y pueden afectar la capacidad del modelo para aprender características jerárquicas y espaciales de los datos.

7.  **Regularización:** La regularización es una técnica utilizada para prevenir el sobreajuste en el aprendizaje automático. Los hiperparámetros de regularización, como el coeficiente de regularización L1 o L2, controlan la magnitud de la penalización aplicada a los parámetros del modelo.


La selección de hiperparámetros es un aspecto crítico en el proceso de aprendizaje automático, ya que puede afectar significativamente el rendimiento del modelo. Hay varias técnicas para seleccionar y ajustar hiperparámetros, como la validación cruzada, la búsqueda de cuadrícula (grid search) y la búsqueda aleatoria (random search). Estos métodos implican entrenar y evaluar múltiples modelos con diferentes combinaciones de hiperparámetros para encontrar la configuración que produce el mejor rendimiento en un conjunto de datos de validación.