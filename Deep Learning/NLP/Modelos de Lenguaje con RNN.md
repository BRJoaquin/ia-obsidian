![[Pasted image 20231202160912.png]]

![[Pasted image 20231202160928.png]]

Los Modelos de Lenguaje basados en Redes Neuronales Recurrentes (RNN) son una mejora significativa con respecto a los modelos de lenguaje basados en ventanas fijas de palabras. Las RNN están diseñadas para manejar secuencias de entrada de longitud variable y son capaces de mantener un estado o memoria a través de las secuencias, lo cual es esencial para entender el contexto en el lenguaje.

## Cómo Funcionan los LM con RNN

1. **Entrada Secuencial**: En cada paso de tiempo, una palabra (o su embedding correspondiente) se alimenta a la RNN.
2. **Estado Oculto**: La RNN actualiza su estado oculto $ℎ_t$​ en función del estado oculto anterior $ℎ_{t−1}$​ y la entrada actual.
3. **Predicción de Palabras**: La salida del estado oculto en cada paso de tiempo se pasa a través de una capa softmax para obtener una distribución de probabilidad sobre el vocabulario.
4. **Elección de Palabra**: La palabra con la mayor probabilidad en la distribución softmax se elige como la predicción para la siguiente palabra en la secuencia.

## Ventajas de los LM con RNN

- **Memoria a Largo Plazo**: Idealmente, las RNN pueden recordar información a lo largo de largas secuencias, lo que les permite mantener el contexto de lo que ha sido generado o visto anteriormente.
- **Modelado de Dependencias**: Pueden capturar dependencias a largo plazo entre las palabras, lo que es crucial para la coherencia y la gramaticalidad en la generación de texto.
- **Flexibilidad de Entrada y Salida**: Pueden manejar secuencias de entrada y salida de diferentes longitudes sin necesidad de una ventana de tamaño fijo.

## Desafíos de los LM con RNN

- **Desvanecimiento y Explosión de Gradientes**: En la práctica, las RNN estándar a menudo tienen dificultades para aprender dependencias a largo plazo debido a estos problemas técnicos durante el entrenamiento.
- **Requerimientos Computacionales**: Pueden ser intensivas en términos de computación y memoria debido a la naturaleza secuencial de su entrenamiento.

Para abordar algunos de estos desafíos, variantes de RNN como las [[Redes Neuronales Recurrentes (RNN)#Tipos de RNN#LSTM (Long Short-Term Memory)|LSTM]] (Long Short-Term Memory) y [[Redes Neuronales Recurrentes (RNN)#Tipos de RNN#GRU (Gated Recurrent Unit)|GRU]] (Gated Recurrent Units) introducen mecanismos de puertas que les permiten manejar mejor la información a lo largo del tiempo y facilitar el entrenamiento de redes más profundas y complejas. Estos avances han hecho de las RNN una herramienta poderosa para tareas como la generación de texto, la transcripción de voz a texto y la traducción automática.

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
