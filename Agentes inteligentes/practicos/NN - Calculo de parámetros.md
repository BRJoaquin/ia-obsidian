
**Objetivo**: Calcular el número de pesos, sesgos y parámetros totales por capa, así como el número total de parámetros aprendibles en toda la red para cada ejemplo a continuación
## Ejemplo 1

**Estructura de la Red**:
- **Capa de Entrada**: 128 neuronas
- **Capa Oculta 1**: 64 neuronas
- **Capa de Salida**: 1 neuronas

**Activación**: ReLU para las capas ocultas, Softmax para la salida.

| Capa | # de Neuronas de Entrada | # de Neuronas de Salida | # de Pesos | # de Sesgos | # de Parámetros |
| ---- | ------------------------ | ----------------------- | ---------- | ----------- | --------------- |
| FC1  | 128                      | 64                      |            |             |                 |
| FC2  | 64                       | 1                       |            |             |                 |

Total de parámetros: 

## Ejemplo 2

**Estructura de la Red**:
- **Capa de Entrada**: 256 neuronas
- **Capa Oculta 1**: 128 neuronas
- **Capa Oculta 2**: 64 neuronas
- **Capa de Salida**: 10 neuronas

**Activación**: ReLU para las capas ocultas, Softmax para la salida.

| Capa | # de Neuronas de Entrada | # de Neuronas de Salida | # de Pesos | # de Sesgos | # de Parámetros |
| ---- | ------------------------ | ----------------------- | ---------- | ----------- | --------------- |
| FC1  | 256                      | 128                     |            |             |                 |
| FC2  | 128                      | 64                      |            |             |                 |
| FC3  | 64                       | 10                      |            |             |                 |

Total de parámetros: 

## Ejemplo 3

**Estructura de la Red**:
- **Capa de Entrada**: 512 neuronas
- **Capa Oculta 1**: 256 neuronas
- **Capa Oculta 2**: 128 neuronas
- **Capa Oculta 3**: 64 neuronas
- **Capa de Salida**: 10 neuronas

**Activación**: ReLU para las capas ocultas, Softmax para la salida.

| Capa | # de Neuronas de Entrada | # de Neuronas de Salida | # de Pesos | # de Sesgos | # de Parámetros |
| ---- | ------------------------ | ----------------------- | ---------- | ----------- | --------------- |
| FC1  | 512                      | 256                     |            |             |                 |
| FC2  | 256                      | 128                     |            |             |                 |
| FC3  | 128                      | 64                      |            |             |                 |
| FC4  | 64                       | 10                      |            |             |                 |

Total de parámetros: 


**Ejemplo 4**

* **Capa de Entrada**: 3 color channels (RGB), tamaño 28x28
* **Capa Convolutional 1**: 32 filters, kernel size 5x5, stride 2x2
* **Capa Convolutional 2**: 64 filters, kernel size 3x3, stride 1x1
* **Capa de Salida**: 10 neurons

| Capa   | # de Filas  | # de Columnas  | # de Filas en la Entrada  | # de Columnas en la Entrada  | # de Pesos  | # de Sesgos  | # de Parámetros |
| -----  | -----------  |  -------------  |  ------------------------  |  -------------------------  | ----------  | -----------  |  ---------------  |
| Conv1   | 32          | 28x28           | 3                         | 28                         | (5*5*3+1)*32 = 4800  | 32             | 4832            |
| Conv2   | 64          | 14x14           | 32                        | 14                        | (3*3*32+1)*64 = 9216 | 64             | 9280             |
| FC      | 1           | 10               | 256                       | 10                         | (256*10) + 10 = 2570  | 10             | 2580              |
Total de parámetros: 4832 + 9280 + 2580 = **16692**

**Ejemplo 5**

* **Capa de Entrada**: 1 color channel, tamaño 32x32
* **Capa Convolutional 1**: 16 filters, kernel size 7x7, stride 3x3
* **Capa Convolutional 2**: 32 filters, kernel size 5x5, stride 2x2
* **Capa de Salida**: 20 neurons

| Capa   | # de Filas  | # de Columnas  | # de Filas en la Entrada  | # de Columnas en la Entrada  | # de Pesos  | # de Sesgos  | # de Parámetros |
| -----  | -----------  |  -------------  |  ------------------------  |  -------------------------  | ----------  | -----------  |  ---------------  |
| Conv1   | 16          | 32x32           | 1                         | 32                         | (7*7+1)*16 = 1120  | 16             | 1136            |
| Conv2   | 32          | 16x16           | 16                        | 16                        | (5*5*16+1)*32 = 5120 | 32             | 5152             |
| FC      | 1           | 20               | 320                       | 20                         | (320*20) + 20 = 6640  | 20             | 6660              |
Total de parámetros: 1136 + 5152 + 6660 = **12988**

**Ejemplo 6**

* **Capa de Entrada**: 3 color channels (RGB), tamaño 224x224
* **Capa Convolutional 1**: 64 filters, kernel size 11x11, stride 4x4
* **Capa Convolutional 2**: 128 filters, kernel size 9x9, stride 2x2
* **Capa de Salida**: 30 neurons

| Capa   | # de Filas  | # de Columnas  | # de Filas en la Entrada  | # de Columnas en la Entrada  | # de Pesos  | # de Sesgos  | # de Parámetros |
| -----  | -----------  |  -------------  |  ------------------------  |  -------------------------  | ----------  | -----------  |  ---------------  |
| Conv1   | 64          | 224x224         | 3                         | 224                         | (11*11+1)*64 = 7040  | 64             | 7104            |
| Conv2   | 128         | 112x112        | 64                        | 112                       | (9*9*64+1)*128 = 12288 | 128            | 12516              |
| FC      | 1           | 30               | 1792                      | 30                         | (1792*30) + 30 = 53760  | 30             | 53890              |
Total de parámetros: 7104 + 12516 + 53890 = **65110**

Espero que estos ejercicios te ayuden a calcular el número total de parámetros en redes neuronales convolucionales. ¡Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en preguntar!