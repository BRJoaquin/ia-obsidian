
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

![[Pasted image 20231202120147.png]]
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

# Modelos Word2Vec: Preentrenados vs Entrenamiento Propio

## Modelos Preentrenados
- **Cuándo usar**: Para prototipos rápidos, tareas generales de NLP, o cuando se carece de recursos computacionales.
- **Ventajas**: Ahorro de tiempo, calidad probada, entrenados en corpus grandes.

## Entrenamiento Propio
- **Cuándo usar**: Para textos de dominios específicos, datos actualizados o cuando se manejan términos especializados.
- **Ventajas**: Personalización para necesidades específicas, actualización con lenguaje y términos recientes.

## Decisión
- **Basada en**: Naturaleza del texto, recursos disponibles, y especificidad del dominio.

# Ejemplo en Python utilizando la biblioteca Gensim para entrenar un modelo Word2Vec


```python
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')

# Supongamos que tenemos el siguiente corpus de texto
corpus = [
    "The quick brown fox jumps over the lazy dog",
    "Word2Vec will convert words to vectors",
    "Gensim is a great library for Word2Vec"
]

# Tokenizamos las frases del corpus
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in corpus]

# Entrenamos el modelo Word2Vec
# size: dimensionality of the word vectors
# window: maximum distance between the current and predicted word within a sentence
# min_count: ignores all words with total frequency lower than this
# workers: use these many worker threads to train the model
model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Usamos el modelo para obtener el vector de una palabra
vector = model.wv['word2vec']  # Obtener el vector de la palabra 'word2vec'

# Encontramos las palabras más similares a 'word2vec'
similar_words = model.wv.most_similar('word2vec')

# Imprimimos el vector y palabras similares
print(vector)
print(similar_words)
```

# Ejemplo en Python utilizando un modelo Word2Vec preentrenado con la biblioteca Gensim

```python
from gensim.models import KeyedVectors

# Cargamos el modelo preentrenado de Word2Vec. Este ejemplo utiliza el modelo 'word2vec-google-news-300' que es grande y puede demorar en cargarse.
# Asegúrese de tenerlo descargado previamente o ajuste el siguiente código para descargarlo automáticamente si es necesario.
model = KeyedVectors.load_word2vec_format('word2vec-google-news-300.bin', binary=True)

# Obtenemos el vector para una palabra específica
vector = model['computer']  # Reemplazar 'computer' con la palabra de su elección

# Calculamos palabras similares al término 'computer'
similar_words = model.most_similar('computer', topn=5)  # Obtener las 5 palabras más similares

# Imprimimos el vector y las palabras similares
print(vector)
print(similar_words)
```