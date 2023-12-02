

![[Pasted image 20231202160607.png]]

Los modelos de lenguaje basados en redes neuronales artificiales (ANN) sin el uso de redes recurrentes (RNN) buscan capturar las relaciones estadísticas entre palabras en un texto. Estos modelos utilizan una "ventana" de palabras contiguas para predecir la siguiente palabra en una secuencia. Aquí, se muestra cómo se implementa este enfoque:

1. **Ventana de Palabras Fija**: Se define una ventana de tamaño 'n' para observar una cantidad fija de palabras en cada paso.
2. **Embeddings de Palabras**: Cada palabra dentro de la ventana se convierte en un vector mediante embeddings preentrenados o aprendidos durante el entrenamiento.
3. **Capa Oculta**: Los embeddings se combinan (usualmente concatenados o sumados) y luego se pasan a través de una o más capas ocultas de la red neuronal.
4. **Predicción**: La última capa de la red es una capa softmax que predice la siguiente palabra en la secuencia.

Las mejoras de este enfoque con respecto a los modelos más simples de n-gramas incluyen la capacidad de capturar relaciones más complejas y la habilidad de manejar una gran cantidad de palabras mediante embeddings, que reducen significativamente la dimensionalidad. Sin embargo, este enfoque aún enfrenta desafíos, como el tamaño limitado de la ventana de contexto y el aprendizaje redundante de patrones para cada posición de la ventana.

![[Pasted image 20231202160627.png]]

![[Pasted image 20231202160635.png]]
