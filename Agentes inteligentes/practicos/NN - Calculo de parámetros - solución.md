### Ejemplo 1

Para las capas totalmente conectadas (FC), la cantidad de pesos es igual al producto del número de neuronas de entrada por el número de neuronas de salida. El número de sesgos es igual al número de neuronas de salida. Los parámetros totales por capa son la suma de pesos y sesgos.

- **Capa FC1**: 
  - **# de Pesos**: $128 \times 64 = 8192$
  - **# de Sesgos**: $64$
  - **# de Parámetros**: $8192 + 64 = 8256$

- **Capa FC2**:
  - **# de Pesos**: $64 \times 1 = 64$
  - **# de Sesgos**: $1$
  - **# de Parámetros**: $64 + 1 = 65$

- **Total de parámetros en la red**: $8256 + 65 = 8321$

### Ejemplo 2

Aplicamos el mismo cálculo para la segunda red:

- **Capa FC1**:
  - **# de Pesos**: $256 \times 128 = 32768$
  - **# de Sesgos**: $128$
  - **# de Parámetros**: $32768 + 128 = 32896$

- **Capa FC2**:
  - **# de Pesos**: $128 \times 64 = 8192$
  - **# de Sesgos**: $64$
  - **# de Parámetros**: $8192 + 64 = 8256$

- **Capa FC3**:
  - **# de Pesos**: $64 \times 10 = 640$
  - **# de Sesgos**: $10$
  - **# de Parámetros**: $640 + 10 = 650$

- **Total de parámetros en la red**: $32896 + 8256 + 650 = 41802$

### Ejemplo 3

Y lo mismo para la tercera red:

- **Capa FC1**:
  - **# de Pesos**: $512 \times 256 = 131072$
  - **# de Sesgos**: $256$
  - **# de Parámetros**: $131072 + 256 = 131328$

- **Capa FC2**:
  - **# de Pesos**: $256 \times 128 = 32768$
  - **# de Sesgos**: $128$
  - **# de Parámetros**: $32768 + 128 = 32896$

- **Capa FC3**:
  - **# de Pesos**: $128 \times 64 = 8192$
  - **# de Sesgos**: $64$
  - **# de Parámetros**: $8192 + 64 = 8256$

- **Capa FC4**:
  - **# de Pesos**: $64 \times 10 = 640$
  - **# de Sesgos**: $10$
  - **# de Parámetros**: $640 + 10 = 650$

- **Total de parámetros en la red**: $131328 + 32896 + 8256 + 650 = 173130$

### Ejemplo 4

**Capas Convolutivas y de Pooling:**
Para capas convolutivas, el número de pesos es el producto del tamaño del kernel por el número de filtros, y el número de sesgos es igual al número de filtros. En capas de pooling no hay pesos ni sesgos.

- **CONV1**:
  - **Tamaño del Kernel**: $5 \times 5$
  - **Número de Filtros**: 8
  - **# de Pesos**: $5 \times 5 \times 3 \times 8 = 600$ (incluyendo los canales de entrada RGB)
  - **# de Sesgos**: $8$
  - **# de Parámetros**: $600 + 8 = 608$
  - **Out Shape**: Con stride de 1 y padding de 2, el output es igual al input, así que $32 \times 32 \times 8$.

- **POOL1**:
  - **Out Shape**: Con un pooling de 2x2 y stride de 2, el tamaño de cada dimensión se reduce a la mitad, así que $16 \times 16 \times 8$.

- **FC**:
  - El output de POOL1 es un tensor de $16 \times 16 \times 8 = 2048$ elementos, que es la entrada de la capa FC.
  - **# de Pesos**: $2048 \times 10 = 20480$
  - **# de Sesgos**: $10$
  - **# de Parámetros**: $20480 + 10 = 20490$

- **Total de parámetros en la red**: $608 + 20490 = 21098$

### Ejemplo 5

En el caso de múltiples capas convolucionales y de pooling, el cálculo sigue un patrón similar, considerando la reducción de dimensiones y el incremento de canales.

- **CONV1**:
  - **# de Pesos**: $3 \times 3 \times 3 \times 16 = 432$
  - **# de Sesgos**: $16$
  - **# de Parámetros**: $432 + 16 = 448$
  - **Out Shape**: Con stride de 1 y padding de 1, mantiene $32 \times 32 \times 16$.

- **POOL1**:
  - **Out Shape**: Reduce a la mitad, $16 \times 16 \times 16$.

- **CONV2**:
  - **# de Pesos**: $3 \times 3 \times 16 \times 32 = 4608$
  - **# de Sesgos**: $32$
  - **# de Parámetros**: $4608 + 32 = 4640$
  - **Out Shape**: Con stride de 1 y padding de 1, $16 \times 16 \times 32$.

- **POOL2**:
  - **Out Shape**: Reduce a la mitad, $8 \times 8 \times 32$.

- **FC1**:
  - **Entrada**: $8 \times 8 \times 32 = 2048$
  - **# de Pesos**: $2048 \times 128 = 262144$
  - **# de Sesgos**: $128$
  - **# de Parámetros**: $262144 + 128 = 262272$

- **FC2**:
  - **# de Pesos**: $128 \times 10 = 1280$
  - **# de Sesgos**: $10$
  - **# de Parámetros**: $1280 + 10 = 1290$

- **Total de parámetros en la red**: $448 + 4640 + 262272 + 1290 = 267650$
