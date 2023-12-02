## Objetivo del Encoder
- **Generar Vector de Contexto**: El encoder toma la secuencia de entrada y la transforma en un vector de contexto. Este vector es una representación condensada de toda la información necesaria para generar la salida.

![[Pasted image 20231202164239.png]]

## Contexto y Estado Oculto
- **Estado Oculto de la Red Recurrente**: El estado oculto es el componente clave que el encoder actualiza a medida que procesa cada elemento de la secuencia de entrada.
- **Uso de Outputs Recurrentes**: Aunque el estado oculto final es esencial, los outputs generados en cada paso de la secuencia también pueden ser utilizados para enriquecer el contexto.

## Diagrama Explicativo
- **Secuencia de Entrada**: Por ejemplo, la frase "le chat est noir" junto con un token de final de secuencia `<EOS>` es convertida en una serie de índices `[02 85 03 12 99]` que representan las palabras en el vocabulario del modelo.
- **Proceso de Codificación**:
  - **Embedding**: Cada índice de palabra se transforma en un vector denso que captura aspectos semánticos de la palabra (embedding).
  - **GRU (Gated Recurrent Unit)**: El modelo procesa secuencialmente los embeddings actualizando su estado oculto (hidden).
  - **Output y Hidden**: Cada paso de la secuencia produce un output y una versión actualizada del estado oculto. El estado oculto final se utiliza como el vector de contexto.

## Importancia del Estado Oculto
- **Representación del Contexto**: El estado oculto encapsula la información de toda la secuencia de entrada y es fundamental para la generación de la secuencia de salida.
- **Transferencia de Información**: Este vector de contexto se pasa al [[Decoder|decoder]] como estado inicial o como parte de su proceso de decodificación en cada paso temporal.


