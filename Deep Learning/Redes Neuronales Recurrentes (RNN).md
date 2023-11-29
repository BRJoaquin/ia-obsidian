## Introducción a las RNN

### Definición
- **Redes Neuronales Recurrentes (RNN)**: Tipo de red neuronal artificial diseñada para reconocer patrones en **secuencias de datos** como texto, genomas, series temporales, etc.
- **Característica Principal**: Capacidad de mantener información en 'memoria' a corto plazo utilizando nodos de bucle.

![[What-is-Recurrent-Neural-Network.webp]]

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

![[Pasted image 20231129184110.png]]
### LSTM (Long Short-Term Memory)
- **Estructura Mejorada**: Resuelve el problema del desvanecimiento del gradiente.
- **Puertas de Memoria**: Controlan el flujo de información, permitiendo retener o descartar datos.

### GRU (Gated Recurrent Unit)
- **Variante de LSTM**: Más simple y a menudo tan efectiva como LSTM.
- **Menos Puertas**: Facilita y acelera el entrenamiento.

## Variantes de RNN 
## Variantes de RNN 
### One-to-Many 
- **Aplicaciones**: Generación de música, imágenes a partir de descripciones. 
- **Funcionamiento**: Una única entrada produce una secuencia de salidas. 

### Many-to-One 
- **Aplicaciones**: Análisis de sentimiento, clasificación de texto. 
- **Funcionamiento**: Secuencia de entrada produce una única salida. 
 
### Many-to-Many 
- **Aplicaciones**: Traducción de idiomas, transcripción de voz a texto. 
- **Funcionamiento**: Secuencia de entrada se mapea a secuencia de salida de longitud potencialmente diferente.

## Desafíos y Mejoras

### Problemas Comunes
- **Desvanecimiento y Explosión del Gradiente**: Afecta la capacidad de aprendizaje.

### Técnicas de Mejora
- **Recorte del Gradiente**: Mitiga la explosión del gradiente.
- **Incorporación de Atención**: Mejora el manejo de secuencias largas.

## Conclusión

Las RNN son una herramienta poderosa en el ámbito del aprendizaje automático, especialmente útil para datos secuenciales. Aunque enfrentan desafíos como el desvanecimiento del gradiente, las innovaciones como LSTM y GRU ofrecen soluciones efectivas. Su aplicación en campos como NLP y series temporales demuestra su versatilidad y potencial.

---

