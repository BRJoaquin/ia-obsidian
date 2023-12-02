
- **Incorporación de Información Secuencial**: Los Transformers no tienen en cuenta la posición de las palabras en la secuencia de entrada de manera inherente. El positional encoding agrega información sobre la posición de cada palabra.

## Cómo Funciona
- **Vectores Únicos para Posiciones**: Se generan vectores únicos para cada posición en la secuencia y se suman a los vectores de embedding de las palabras correspondientes.
- **Uso de Funciones Trigonométricas**: Comúnmente, las funciones seno y coseno se utilizan para calcular estos vectores, asegurando que cada posición tenga una representación distintiva.

## Importancia en el Modelo Transformer
- **Diferenciación de Palabras**: Permite al modelo diferenciar entre palabras basándose en su posición en la secuencia, una dimensión crucial de la información en el lenguaje.
- **Conservación de Secuencialidad**: Mantiene la secuencialidad en una arquitectura que procesa la entrada en paralelo.

## Conclusión
El positional encoding es crucial en los modelos Transformer para mantener la noción de orden de las palabras, lo que es esencial para el procesamiento del lenguaje natural.


<iframe width="560" height="315" src="https://www.youtube.com/embed/xi94v_jl26U?si=6Aa0rqd8NQkyXcMF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
