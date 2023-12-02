
La lematización es un proceso de preprocesamiento de texto en [[Procesamiento del Lenguaje Natural (NLP)|NLP]] que consiste en transformar una palabra a su forma de diccionario (lema). A diferencia del [[Stemming|stemming]], que simplemente recorta los sufijos de las palabras, la lematización considera el análisis morfológico de las palabras para devolver su base o raíz léxica correcta según el idioma.

## Características de la Lematización

- **Análisis Morfológico**: Requiere comprender la estructura de la palabra, incluyendo su raíz y afijos (prefijos y sufijos), así como su categoría gramatical (parte del discurso).
- **Contexto Gramatical**: Toma en cuenta el contexto y el uso de la palabra dentro de una frase para determinar su lema.
- **Precisión**: Produce resultados más precisos y palabras lematizadas que existen en el idioma.

## Ejemplo

Considere la palabra "running":

- **Stemming**: Puede resultar en "runn" o "run", dependiendo del algoritmo.
- **Lematización**: Devolverá "run" si "running" se usa como verbo en el contexto de una oración.

La lematización es preferida sobre el stemming en aplicaciones donde se requiere precisión semántica y gramatical, como en sistemas de recuperación de información y análisis de texto avanzado.


![[Pasted image 20231202110948.png]]