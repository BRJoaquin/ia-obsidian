
El preprocesamiento en NLP es un conjunto de técnicas utilizadas para preparar los datos de texto para su análisis y modelado. Es un paso crítico que afecta directamente la eficacia de las tareas de NLP.

## Pasos Claves del Preprocesamiento

### Eliminación de Caracteres No Deseados
- **Limpieza**: Remoción de caracteres que no aportan significado al texto como tags HTML, caracteres especiales o números, dependiendo del contexto.

### Tokenización
- **Definición**: Proceso de dividir el texto en unidades significativas llamadas tokens, que pueden ser palabras, frases o símbolos.
- **Importancia**: Es fundamental para convertir el texto en una forma que las máquinas puedan procesar.

### Eliminación de Stop Words
- **Stop Words**: Son palabras que aparecen frecuentemente en el lenguaje pero portan poco significado para el análisis, como artículos, pronombres y preposiciones.
- **Objetivo**: Simplificar el texto y enfocarse en las palabras que aportan más significado al contenido.

### Normalización
- **Conversión a Minúsculas**: Uniformizar el texto para que palabras como "Hola" y "hola" sean tratadas como iguales.
- **Stemming**: Reducción de palabras a su raíz o forma base, lo que puede resultar en palabras que no son léxicamente correctas pero tienen un significado similar.
- **Lematización**: Proceso más sofisticado que el stemming, que convierte una palabra a su forma de diccionario (lema), teniendo en cuenta su rol gramatical.

## Ejemplo de Flujo de Preprocesamiento

```plaintext
Input Text: "Cats, running along the beach on a sunny day."
1. Limpieza: Remover puntuación y otros caracteres no alfabéticos.
2. Tokenización: ["Cats", "running", "along", "the", "beach", "on", "a", "sunny", "day"]
3. Eliminación de Stop Words: ["Cats", "running", "beach", "sunny", "day"]
4. Normalización:
    - Conversión a Minúsculas: ["cats", "running", "beach", "sunny", "day"]
    - Stemming: ["cat", "run", "beach", "sun", "day"]
    - Lematización: ["cat", "run", "beach", "sunny", "day"]
```
