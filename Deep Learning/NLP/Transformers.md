
Los Transformers son un tipo de arquitectura de modelo de deep learning que ha revolucionado el campo del [[Procesamiento del Lenguaje Natural (NLP)|procesamiento del lenguaje natural (NLP)]].

![[Pasted image 20231202195125.png]]
## Características Principales
- **Estructura**: Compuesta por bloques de encoders y decoders apilados.
- **Mecanismo de Atención**: Utiliza una versión avanzada de mecanismos de atención llamada 'self-attention' que permite a los modelos ponderar la importancia de cada parte de la entrada sin la necesidad de secuencialidad.
- **Paralelización**: A diferencia de las RNN, los Transformers no requieren procesamiento secuencial, lo que permite una paralelización masiva y reduce significativamente el tiempo de entrenamiento.

## Funcionamiento
- **Encoders**: Cada encoder procesa la entrada completa y calcula una serie de representaciones que son pasadas al siguiente encoder.
- **Decoders**: Similar a los encoders, pero también utilizan la salida del último encoder para generar la secuencia de salida.

## Ventajas
- **Eficiencia en Secuencias Largas**: Al eliminar la necesidad de procesamiento secuencial, los Transformers manejan mejor las secuencias largas.
- **Mejor Entendimiento del Contexto**: La atención en todas las posiciones permite un mejor entendimiento contextual.
- **Escala**: Diseñados para trabajar con grandes cantidades de datos y modelos, escalan efectivamente con más datos y capacidad computacional.

## Aplicaciones
- **Traducción Automática**: Google y otros servicios de traducción utilizan Transformers para proporcionar traducciones rápidas y precisas.
- **Generación de Texto**: GPT (Generative Pretrained Transformer) es capaz de generar texto coherente y relevante.



# Vectores Query, Key y Value en Transformers

## Conceptos Básicos
En la arquitectura Transformer, los vectores query (consulta), key (clave) y value (valor) son componentes centrales del mecanismo de atención.

### Query
- **Propósito**: Representar la palabra o elemento actual que está buscando información relevante en otras partes de la entrada.
- **Uso**: Se utiliza para calcular la puntuación de atención con cada key.

### Key
- **Propósito**: Representar las palabras o elementos en la entrada que se compararán con el query.
- **Uso**: Las keys interactúan con los queries para determinar el nivel de atención que cada elemento de la entrada debe recibir.

### Value
- **Propósito**: Contener la información real de cada elemento de la entrada que se quiere recuperar una vez que se han calculado las puntuaciones de atención.
- **Uso**: Una vez que se establece la relevancia de las keys con respecto a un query, los corresponding values se ponderan y se combinan para producir la salida del mecanismo de atención.

## Mecanismo de Atención
- **Atención**: Se calcula una puntuación de atención utilizando los vectores query y key. 
- **Ponderación de Values**: La puntuación de atención determina cómo se ponderan los values.
- **Salida**: La combinación de los values ponderados se convierte en la salida de la capa de atención para ese query específico.

## Importancia en Transformers
- **Captura de Relaciones Contextuales**: Este sistema de vectores permite que el modelo capture relaciones complejas y dependencias a larga distancia entre palabras o subunidades en una secuencia.
- **Dinamismo**: Los vectores query, key y value permiten un enfoque dinámico para extraer y resaltar información relevante de la entrada.

## Conclusión
Los vectores query, key y value son fundamentales para el funcionamiento de los mecanismos de atención en los Transformers, proporcionando una forma poderosa y flexible de modelar interacciones entre diferentes partes de la entrada.




ver ademas:
- [[Positional Encoding]]


<iframe width="560" height="315" src="https://www.youtube.com/embed/aL-EmKuB078?si=0ogLWCOCQ9kSaenr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/xi94v_jl26U?si=6Aa0rqd8NQkyXcMF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
