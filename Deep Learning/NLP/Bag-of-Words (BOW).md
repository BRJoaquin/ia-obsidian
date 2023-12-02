
Bag-of-Words (BOW) es un modelo de representación textual utilizado en [[Procesamiento del Lenguaje Natural (NLP)|NLP]]. Describe la presencia de palabras dentro de un documento i**gnorando el orden y el contexto en el que aparecen**. Es un enfoque simple pero poderoso para convertir texto en un formato que los algoritmos de machine learning pueden procesar.

## Características de BOW

- **Modelo de Diccionario**: Construye un "diccionario" de todas las palabras únicas en el corpus.
- **Representación Vectorial**: Cada documento se representa como un vector en este espacio de diccionario, donde cada dimensión corresponde a una palabra del diccionario.

## Cómo Funciona BOW

1. **Tokenización**: Divide el texto en palabras o tokens.
2. **Construcción del Diccionario**: Identifica todas las palabras únicas en todos los documentos para formar el diccionario.
3. **Vectorización**: Crea un vector para cada documento, donde el valor en cada dimensión representa la frecuencia (o presencia/ausencia) de la palabra correspondiente en el documento.

## Variantes de BOW

- **Bolsa de Conteo**: Simplemente cuenta cuántas veces aparece cada palabra del diccionario en cada documento.
- **TF-IDF**: Pondera las frecuencias de las palabras por la inversa de su frecuencia en los documentos del corpus para dar más importancia a las palabras menos frecuentes y potencialmente más significativas.

## Limitaciones de BOW

- **Pérdida de Contexto**: Ignora el orden de las palabras, lo que significa que puede perder el contexto y el significado que dependen de la secuencia de palabras.
- **Esparsidad**: Los vectores resultantes son típicamente dispersos (la mayoría de sus elementos son cero), especialmente con diccionarios grandes, lo que es ineficiente en términos de almacenamiento y cálculo.
- **Sinónimos y Polisemia**: No maneja bien los sinónimos (palabras diferentes con significados similares) y la polisemia (una palabra que tiene múltiples significados).

A pesar de sus limitaciones, BOW sigue siendo un método muy utilizado en varias aplicaciones de NLP, especialmente cuando el contexto y el orden de las palabras no son cruciales para la tarea.
