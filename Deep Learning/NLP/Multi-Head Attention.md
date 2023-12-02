
Multi-Head Attention es una técnica en la arquitectura [[Transformers]] que permite al modelo dirigir su atención a diferentes partes de la secuencia de entrada en paralelo.

### Query
- **Propósito**: Representar la palabra o elemento actual que está buscando información relevante en otras partes de la entrada.
- **Uso**: Se utiliza para calcular la puntuación de atención con cada key.

### Key
- **Propósito**: Representar las palabras o elementos en la entrada que se compararán con el query.
- **Uso**: Las keys interactúan con los queries para determinar el nivel de atención que cada elemento de la entrada debe recibir.

### Value
- **Propósito**: Contener la información real de cada elemento de la entrada que se quiere recuperar una vez que se han calculado las puntuaciones de atención.
- **Uso**: Una vez que se establece la relevancia de las keys con respecto a un query, los corresponding values se ponderan y se combinan para producir la salida del mecanismo de atención.

## Funcionamiento
- **Múltiples Cabezas**: La atención se calcula varias veces en paralelo, cada una con un conjunto diferente de matrices de pesos (query, key y value), conocidas como 'cabezas'.
- **Diversificación**: Cada cabeza aprende a atender a diferentes partes de la secuencia, lo que permite que el modelo capture una variedad de características contextuales y dependencias a distintas escalas.
- **Concatenación y Proyección**: Las salidas de todas las cabezas se concatenan y luego se proyectan a través de otra matriz de pesos para formar la salida final.

## Beneficios
- **Captura de Múltiples Relaciones**: Permite al modelo procesar información de manera más rica y capturar múltiples dependencias a la vez.
- **Paralelización Mejorada**: Al operar en paralelo, los Multi-Head Attention aumentan la eficiencia del entrenamiento y la inferencia.

## Uso en Encoder y Decoder
- **Encoder**: Utiliza Multi-Head Attention para auto-relacionar la secuencia de entrada, lo que permite que cada posición de la secuencia tome en cuenta la información de todas las otras posiciones.
- **Decoder**: Aplica Multi-Head Attention dos veces; primero para la auto-atención, asegurándose de que las predicciones futuras no influyan en las actuales, y luego para la atención entre el output del encoder y el estado actual del decoder.

## 
