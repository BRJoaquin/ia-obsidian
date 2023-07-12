
La **curva de aprendizaje** en Machine Learning es una representación gráfica que muestra el rendimiento del modelo en el eje vertical y la cantidad de datos de entrenamiento en el eje horizontal. Esta curva ayuda a entender cómo el rendimiento del modelo cambia a medida que se incrementa el tamaño del conjunto de datos de entrenamiento.

![[Pasted image 20230708141656.png]]

Existen dos tipos comunes de curvas de aprendizaje:

1. **Curvas de aprendizaje del modelo**: Estas curvas muestran cómo cambia el rendimiento del modelo a medida que se incrementa la cantidad de datos de entrenamiento. Normalmente, se observa que al principio el rendimiento del modelo mejora rápidamente a medida que se añaden más datos, pero luego la tasa de mejora disminuye y se estabiliza, llegando a un punto de "aprendizaje asintótico" donde añadir más datos no mejora significativamente el rendimiento del modelo.

2. **Curvas de validación**: Estas curvas muestran cómo cambia el rendimiento del modelo en el conjunto de entrenamiento y en el conjunto de validación a medida que varía algún hiperparámetro del modelo. Las curvas de validación ayudan a identificar el punto óptimo para el hiperparámetro en cuestión, donde la generalización del modelo es mejor (es decir, el rendimiento en el conjunto de validación es máximo).

Las curvas de aprendizaje son una herramienta útil para la selección y ajuste de modelos, ya que ayudan a identificar problemas como el [[sobreajuste (overfitting)]] y el subajuste (underfitting). 

Además, las curvas de aprendizaje pueden ayudar a decidir si recopilar más datos de entrenamiento será útil. Si las curvas de aprendizaje de entrenamiento y validación han convergido y ambos errores son altos, recopilar más datos probablemente no ayudará y puede ser más útil cambiar a un modelo más complejo. Por otro lado, si las curvas de aprendizaje aún no han convergido, recopilar más datos podría ayudar a mejorar el rendimiento del modelo.
