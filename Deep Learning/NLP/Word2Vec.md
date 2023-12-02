
Word2Vec es una técnica de procesamiento de lenguaje natural utilizada para aprender representaciones vectoriales de palabras, llamadas [[Embeding|embeddings]]. Desarrollado por un equipo de investigadores liderados por Tomas Mikolov en Google, Word2Vec captura la esencia semántica de las palabras a través de su contexto en un corpus de texto.

![[Pasted image 20231202115644.png]]

## Fundamentos de Word2Vec

![[Pasted image 20231202115724.png]]

### Modelo Basado en Contexto
- **Idea Central**: Las palabras que ocurren en contextos similares tienden a tener significados similares.
- **Ventana de Contexto**: Word2Vec considera una "ventana" de palabras alrededor de cada palabra objetivo para aprender su representación.

![[Pasted image 20231202115753.png]]

### Dos Arquitecturas Principales
- **CBOW (Continuous Bag of Words)**: Predice la palabra actual basada en el contexto.
- **Skip-Gram**: Predice el contexto a partir de una palabra dada.

![[Pasted image 20231202115835.png]]

### Entrenamiento de Word2Vec
- **Red Neuronal Shallow**: Word2Vec utiliza una red neuronal de una sola capa oculta para el aprendizaje de embeddings.
- **Optimización**: Se utiliza descenso de gradiente estocástico y técnicas como negative sampling o hierarchical softmax para la eficiencia del entrenamiento.

## Características de los Embeddings de Word2Vec

### Relaciones Semánticas
- **Palabras Similares**: Palabras semánticamente similares están cerca en el espacio vectorial.
- **Analogías**: Capaz de capturar analogías (por ejemplo, "rey" es a "hombre" lo que "reina" es a "mujer").

![[Pasted image 20231202115905.png]]

https://projector.tensorflow.org/
### Dimensionalidad
- **Tamaño del Vector**: Los embeddings típicamente tienen entre 100 y 300 dimensiones, dependiendo del tamaño del corpus y la diversidad del vocabulario.

### Ventajas de Word2Vec
- **Representaciones Densas**: A diferencia de one-hot encoding, Word2Vec proporciona representaciones densas y continuas.
- **Desempeño**: Mejora significativamente el rendimiento en varias tareas de NLP como la clasificación de texto, la traducción automática y más.

## Aplicaciones de Word2Vec

- **Extracción de Características**: Como entrada para otros modelos de aprendizaje automático en tareas de NLP.
- **Agrupación de Palabras**: Para descubrir grupos de palabras con significados similares.
- **Búsqueda Semántica**: Mejorar los motores de búsqueda al encontrar resultados relevantes que no contienen la palabra exacta de la consulta pero tienen un significado similar.

## Limitaciones de Word2Vec

- **Palabras con Múltiples Significados**: Word2Vec asigna un único vector a cada palabra, lo que puede ser problemático para palabras con múltiples significados (polisemia).
- **Dependencia del Corpus**: La calidad y el sesgo de los embeddings dependen del corpus utilizado para el entrenamiento.

## Herramientas y Recursos

- **Implementaciones**: Disponibles en bibliotecas como Gensim en Python.
- **Modelos Preentrenados**: Google y otros han publicado modelos Word2Vec preentrenados, que se pueden utilizar para iniciar proyectos de NLP.

Word2Vec ha sido un avance fundamental en NLP, permitiendo avances significativos en la comprensión y modelado del lenguaje natural.
