
TF-IDF es una técnica de ponderación utilizada en la recuperación de información y en el [[Procesamiento del Lenguaje Natural (NLP)|procesamiento del lenguaje natural]] que refleja la importancia de una palabra en un documento en relación con un corpus. La sigla TF-IDF se compone de dos términos: term frequency (TF) y inverse document frequency (IDF).

## Componentes de TF-IDF

### Term Frequency (TF)
- **Definición**: Mide la frecuencia de una palabra en un documento.
- **Cálculo**: El número de veces que una palabra aparece en un documento dividido por el número total de palabras en el documento.

### Inverse Document Frequency (IDF)
- **Definición**: Mide la importancia de la palabra en el conjunto completo de documentos (corpus).
- **Cálculo**: El logaritmo del número total de documentos en el corpus dividido por el número de documentos que contienen la palabra.
![[Pasted image 20231202112715.png]]

## Fórmula de TF-IDF

La puntuación de TF-IDF para una palabra en un documento se calcula como:

> TF-IDF = TF * IDF

![[Pasted image 20231202112748.png]]
## Aplicaciones de TF-IDF

- **Recuperación de Información**: Para ponderar y recuperar documentos relevantes en respuesta a una consulta.
- **Extracción de Palabras Clave**: Identificar las palabras más representativas de un documento.
- **Clasificación de Documentos**: Como características para algoritmos de clasificación de texto.

## Ventajas de TF-IDF

- **Diferenciación de Palabras**: Palabras comunes que aparecen en muchos documentos reciben una puntuación más baja, mientras que palabras únicas reciben una puntuación más alta.
- **Mejora sobre BOW**: Al tomar en cuenta la frecuencia de documentos, ofrece una mejora significativa sobre la simple bolsa de palabras (BOW).

## Limitaciones de TF-IDF

- **Contexto y Significado**: No capta el contexto ni el significado de las palabras; las palabras con puntuaciones similares de TF-IDF podrían tener significados muy diferentes.
- **Palabras con la Misma Puntuación**: No distingue entre palabras con la misma puntuación de TF-IDF que podrían tener diferentes relevancias para el documento.

TF-IDF sigue siendo una herramienta fundamental en NLP y es comúnmente utilizado como un punto de partida para tareas de procesamiento de texto más complejas.
