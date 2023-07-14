Es la proporción de verdaderos positivos que se identificaron correctamente.

En el contexto de la [[Clasificación]] de datos, el recall (también conocido como sensibilidad o tasa de verdaderos positivos) es una métrica que mide la proporción de casos positivos que fueron correctamente identificados por un modelo o algoritmo. 

El recall se calcula dividiendo el número de verdaderos positivos entre la suma de los verdaderos positivos y los falsos negativos. En otras palabras, es la proporción de casos positivos que fueron correctamente clasificados en relación con todos los casos positivos reales.
   $$\text{Recall} = \frac{\text{TP}}{\text{TP} + \text{FN}}$$

Una alta puntuación de recall indica que el modelo tiene una buena capacidad para identificar correctamente los casos positivos, lo cual es especialmente importante en situaciones donde se busca minimizar los falsos negativos, como en pruebas médicas para detectar enfermedades graves.

Sin embargo, un alto recall puede ir acompañado de un alto número de falsos positivos, lo cual puede ser problemático en ciertos escenarios. Por lo tanto, es importante considerar otras métricas y encontrar un equilibrio entre el recall y la [[Precisión]] (proporción de verdaderos positivos entre la suma de verdaderos positivos y falsos positivos) al evaluar modelos o algoritmos. 

# Ejemplo

Supongamos que tenemos un modelo de clasificación de enfermedades y queremos evaluar su rendimiento utilizando el recall. El modelo se utiliza para detectar una enfermedad grave y se prueba en un conjunto de datos con 100 casos positivos (personas que realmente tienen la enfermedad) y 200 casos negativos (personas sanas).

El modelo identifica correctamente 80 casos positivos y clasifica incorrectamente 20 como falsos negativos. Por lo tanto, el número de verdaderos positivos es 80.

El recall se calcula dividiendo los verdaderos positivos entre la suma de los verdaderos positivos y los falsos negativos:

Recall = Verdaderos Positivos / (Verdaderos Positivos + Falsos Negativos)
        = 80 / (80 + 20)
        = 0.8

Por lo tanto, el recall en este caso es del 80%, lo que indica que el modelo fue capaz de identificar correctamente el 80% de los casos positivos.

Es importante tener en cuenta que el recall no nos proporciona información sobre los falsos positivos, es decir, las personas sanas clasificadas incorrectamente como enfermas. Por lo tanto, al evaluar un modelo o algoritmo, también debemos considerar otras métricas como la precisión para obtener una imagen más completa del rendimiento del modelo.

# Cuando usarlo

El recall es especialmente útil en situaciones donde es importante identificar correctamente los casos positivos y minimizar los falsos negativos. Algunos ejemplos de casos en los que el recall puede ser relevante incluyen:

- Pruebas médicas para detectar enfermedades graves: En este caso, es fundamental identificar correctamente a las personas que realmente tienen la enfermedad para poder proporcionarles el tratamiento adecuado lo antes posible.

- Detección de fraudes: En el ámbito financiero, es importante identificar correctamente las transacciones fraudulentas para evitar pérdidas económicas.

En general, el recall se utiliza cuando se busca minimizar los falsos negativos y se prioriza la detección correcta de los casos positivos. Sin embargo, también es importante considerar otras métricas como la precisión para obtener una evaluación más completa del rendimiento del modelo o algoritmo.