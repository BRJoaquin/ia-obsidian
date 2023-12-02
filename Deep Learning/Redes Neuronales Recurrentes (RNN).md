## Introducción a las RNN

### Definición
- **Redes Neuronales Recurrentes (RNN)**: Tipo de red neuronal artificial diseñada para reconocer patrones en **secuencias de datos** como texto, genomas, series temporales, etc.
- **Característica Principal**: Capacidad de mantener información en 'memoria' a corto plazo utilizando nodos de bucle.

![[What-is-Recurrent-Neural-Network.webp]]

![[Pasted image 20231129201256.png]]
### Aplicaciones
- **Procesamiento del Lenguaje Natural (NLP)**: Traducción automática, generación de texto. ver [[Procesamiento del Lenguaje Natural (NLP)]]
- **Reconocimiento de Voz**: Transcripción de audio a texto.
- **Series Temporales**: Predicción del mercado de valores, análisis climático.

## Fundamentos Técnicos

### Arquitectura Básica
- **Estructura de Bucle**: Permite que la información persista pasando de un paso de la red al siguiente.
- **Células Neuronales**: Unidades básicas que procesan entradas secuenciales.

### Funcionamiento
1. **Entrada Secuencial**: La red recibe y procesa entradas en secuencia.
2. **Estado Oculto**: Almacena información de entradas anteriores, actuando como 'memoria'.
3. **Salida**: Cada paso de tiempo produce una salida basada en la entrada actual y el estado oculto.

### Ventajas
- **Memoria de Corto Plazo**: Capacidad para recordar información reciente.
- **Flexibilidad en Longitud de Entrada**: Maneja secuencias de longitud variable.

### Desventajas
- **Problema de Desvanecimiento del Gradiente**: Dificultad para aprender dependencias a largo plazo debido a la disminución exponencial del gradiente a través de capas.
- **Complejidad Computacional**: Mayor tiempo y recursos necesarios para el entrenamiento.

## Tipos de RNN

![[Pasted image 20231129184037.png]]

### RNN Básicas
- **Modelo Simple**: Adecuado para secuencias cortas.
- **Problema**: Dificultad para conectar información a través de largas secuencias. 
- **Soluciones**: Uso de LSTM o GRU para mejorar la retención de memoria. 

![[Pasted image 20231129184110.png|500]]
### LSTM (Long Short-Term Memory)
- **Estructura Mejorada**: Resuelve el problema del desvanecimiento del gradiente.
- **Puertas de Memoria**: Controlan el flujo de información, permitiendo retener o descartar datos.

![[Pasted image 20231129184706.png|500]]
### GRU (Gated Recurrent Unit)
- **Variante de LSTM**: Más simple y a menudo tan efectiva como LSTM.
- **Menos Puertas**: Facilita y acelera el entrenamiento.

![[Pasted image 20231129184720.png|500]]
## Variantes de RNN 

![[Pasted image 20231129184330.png]]
### One-to-Many 
- **Aplicaciones**: Generación de música, imágenes a partir de descripciones. 
- **Funcionamiento**: Una única entrada produce una secuencia de salidas. 
### Many-to-One 
- **Aplicaciones**: Análisis de sentimiento, clasificación de texto. 
- **Funcionamiento**: Secuencia de entrada produce una única salida. 

![[Pasted image 20231129201421.png]]

### Many-to-Many 
- **Aplicaciones**: Traducción de idiomas, transcripción de voz a texto. 
- **Funcionamiento**: Secuencia de entrada se mapea a secuencia de salida de longitud potencialmente diferente.

![[Pasted image 20231129201435.png]]

![[Pasted image 20231129201511.png]]

## Desafíos y Mejoras

### Problemas Comunes
- **Desvanecimiento y Explosión del Gradiente**: Afecta la capacidad de aprendizaje.
- **Secuencialidad**: Alto costo computacional debido a la naturaleza secuencial del procesamiento.

### Técnicas de Mejora
- **Recorte del Gradiente**: Mitiga la explosión del gradiente. ver [[Clipping del gradiente]]
- **Incorporación de Atención**: Mejora el manejo de secuencias largas.

## Backprop through time

![[Pasted image 20231202121432.png]]

Backpropagation en tiempo real (BPTT) es una técnica para entrenar redes neuronales recurrentes (RNN) que utiliza una versión modificada del algoritmo de backpropagación común. La principal diferencia entre BPTT y el backpropagación común es que en BPTT se actualiza la red neuronal después de cada ejemplo (o cada ciertos steps), mientras que en el backpropagación común se actualiza la red neuronal después de procesar todo el conjunto de datos de entrada.

https://en.wikipedia.org/wiki/Backpropagation_through_time#:~:text=Backpropagation%20through%20time%20(BPTT)%20is,independently%20derived%20by%20numerous%20researchers.

## Conclusión

Las RNN son una herramienta poderosa en el ámbito del aprendizaje automático, especialmente útil para datos secuenciales. Aunque enfrentan desafíos como el desvanecimiento del gradiente, las innovaciones como LSTM y GRU ofrecen soluciones efectivas. Su aplicación en campos como NLP y series temporales demuestra su versatilidad y potencial.


# Links y videos

- http://dprogrammer.org/rnn-lstm-gru
- https://stanford.edu/~shervine/teaching/cs-230/cheatsheet-recurrent-neural-networks#overview


<iframe width="560" height="315" src="https://www.youtube.com/embed/y9PLF2GsD-c?si=MOR8W-6R17sBY4v9" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/6niqTuYFZLQ?si=RWUBofW8ekiT0Zws" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>


