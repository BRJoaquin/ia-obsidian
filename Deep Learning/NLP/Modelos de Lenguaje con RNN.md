








# Teacher Forcing en Modelos de Lenguaje

![[Pasted image 20231202160427.png]]

Teacher Forcing es una técnica utilizada durante el entrenamiento de modelos de lenguaje secuenciales, especialmente en redes neuronales recurrentes (RNN). Esta estrategia implica utilizar la palabra correcta de la secuencia de entrada como entrada siguiente, en lugar de la palabra predicha por el modelo.

## Cómo Funciona el Teacher Forcing

- **Paso Inicial**: Se alimenta la primera palabra de una secuencia al modelo.
- **Predicción**: El modelo intenta predecir la siguiente palabra.
- **Corrección**: Independientemente de si la predicción es correcta o no, la siguiente entrada real (la palabra correcta) se proporciona como entrada al modelo para la siguiente predicción.
- **Repetición del Proceso**: Este proceso se repite para cada palabra en la secuencia durante el entrenamiento.

## Objetivo del Teacher Forcing

- **Rápida Convergencia**: Ayuda a que el modelo aprenda más rápidamente al proporcionarle siempre la respuesta correcta en el paso siguiente.
- **Reducción del Error Acumulado**: Evita que los errores se propaguen a través de la secuencia durante el entrenamiento.

## Aplicaciones

- **Entrenamiento de RNNs**: Utilizado comúnmente en RNNs para tareas como generación de texto, traducción automática y descripción de imágenes.

## Ventajas

- **Eficiencia**: Acelera el entrenamiento al guiar al modelo con la respuesta correcta en cada paso.
- **Mejores Modelos**: Puede conducir a la rápida convergencia y al desarrollo de modelos que generalizan mejor en la tarea de predicción.

## Desventajas

- **Dependencia de la Guía**: Puede resultar en modelos que no aprenden a recuperarse de sus propios errores, ya que nunca se exponen a sus propias predicciones incorrectas durante el entrenamiento.
- **Discrepancia de Exposición**: Puede ocurrir una discrepancia entre el entrenamiento y la inferencia, ya que en la inferencia el modelo no tendrá la guía de la palabra correcta y deberá depender de sus propias predicciones.

Teacher Forcing es una técnica poderosa, pero su uso debe ser equilibrado con estrategias que también expongan al modelo a sus propias predicciones para garantizar que sea robusto durante la inferencia.
