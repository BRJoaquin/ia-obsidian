
En el [[Procesamiento del Lenguaje Natural (NLP)|procesamiento del lenguaje natural (NLP)]], representar palabras como vectores numéricos es un enfoque fundamental que facilita a los algoritmos de machine learning y las redes neuronales trabajar con texto. Este enfoque se conoce como *word embedding* o incrustación de palabras.

## Representación Vectorial de Palabras

- **Necesidad**: Los modelos de machine learning no pueden trabajar directamente con texto crudo; necesitan una representación numérica.
- **Vectores de Palabras**: Son representaciones densas y de baja dimensión en un espacio vectorial continuo.

## Aplicaciones de los Word Embeddings

- **Cálculo de Similitud**: Los vectores permiten medir la similitud coseno entre palabras, ayudando a identificar palabras con significados similares.
- **Clusterización**: Al agrupar palabras con embeddings similares, se pueden descubrir patrones semánticos o sintácticos en el texto.
- **Extracción de Features**: Los embeddings pueden servir como un conjunto robusto de características para tareas de NLP.
- **Clasificación de Texto**: En tareas como la detección de spam o la clasificación de sentimientos, los embeddings proporcionan una representación rica para los clasificadores.

## Métodos de Word Embedding

- **One-Hot Encoding**: Representación más simple pero ineficiente, donde cada palabra se representa como un vector con un "1" en la posición correspondiente a la palabra y "0" en todas las demás. ve [[One-hot encoding]] y [[One-hot (NLP)]]
- **TF-IDF**: Pondera la frecuencia de una palabra en un documento contra su frecuencia inversa en el corpus, proporcionando importancia relativa. ver [[Term Frequency - Inverse Document Frequency (TF - IDF)]]
- **Word2Vec**: Utiliza redes neuronales para aprender representaciones de palabras a partir de grandes corpus de texto. ver [[Word2Vec]]
- **GloVe**: Combina la factorización de la matriz de co-ocurrencia de palabras con el aprendizaje contextual de Word2Vec.
- **BERT y ELMo**: Modelos de lenguaje contextuales que generan embeddings dinámicos basados en el uso específico de las palabras en un contexto.

Estos vectores no solo capturan la frecuencia de las palabras, sino también patrones semánticos y sintácticos, lo que permite que los modelos de NLP manejen tareas complejas como el entendimiento del lenguaje natural y la generación de texto.


![[Pasted image 20231202111104.png]]