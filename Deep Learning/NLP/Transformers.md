
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

## Conclusiones
Los Transformers son actualmente el estándar de oro en muchas tareas de NLP y continúan impulsando avances en el campo.


ver ademas:
- [[Positional Encoding]]


<iframe width="560" height="315" src="https://www.youtube.com/embed/aL-EmKuB078?si=0ogLWCOCQ9kSaenr" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/xi94v_jl26U?si=6Aa0rqd8NQkyXcMF" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
