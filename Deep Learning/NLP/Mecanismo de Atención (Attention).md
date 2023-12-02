
Los mecanismos de atención son una técnica en el procesamiento del lenguaje natural que permite a los modelos [[Sequence to Sequence (Seq2Seq)|Seq2Seq]] enfocarse en diferentes partes de la secuencia de entrada al generar cada palabra de la secuencia de salida.

## Funcionamiento Básico
- **Selección de Información Relevante**: El mecanismo de atención asigna pesos a diferentes partes de la entrada, indicando qué tan relevante es cada parte para la generación de la siguiente palabra.
- **Mejora de la Captura de Contexto**: En lugar de depender de un único vector de contexto, el decoder puede acceder a toda la secuencia de estados ocultos del encoder y seleccionar información relevante en cada paso.

## Solución a Limitaciones
- **Limitaciones de un Solo Vector de Contexto**: Sin atención, el decoder se basa en un solo vector de contexto, lo que puede ser insuficiente para secuencias largas y complejas.
- **Uso Integral de los Outputs del Encoder**: Con atención, el decoder utiliza todos los outputs del encoder, no solo el estado final, lo que proporciona una visión más completa de la entrada.

## Componentes del Mecanismo de Atención
- **Capas Lineales**: Transforman los estados ocultos para prepararlos para la atención.
- **Multiplicación de Matrices**: Calcula la puntuación de atención entre el estado oculto del decoder y los estados ocultos del encoder.
  ![[Pasted image 20231202174624.png]]
- **Ponderación de la Información**: Los pesos de atención determinan la contribución de cada estado oculto del encoder al estado oculto actual del decoder.

![[Pasted image 20231202173233.png]]

## Limitaciones
- **Definición de Tamaño Máximo**: Es necesario establecer un tamaño máximo para las secuencias debido a la naturaleza computacional de la atención.

## Conclusión
El mecanismo de atención es una innovación clave que ha mejorado significativamente la capacidad de los modelos Seq2Seq para manejar secuencias largas y mantener la coherencia y relevancia en la generación de texto.

# Links

- https://medium.com/analytics-vidhya/seq2seq-models-french-to-english-translation-using-encoder-decoder-model-with-attention-9c05b2c09af8

# Videos

<iframe width="560" height="315" src="https://www.youtube.com/embed/fjJOgb-E41w?si=PZpwtxj5s6z3v0VX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
