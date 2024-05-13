# NN - Calculo de parámetros

**Objetivo**: Calcular el número de pesos, sesgos y parámetros totales por capa, así como el número total de parámetros aprendibles en toda la red para cada ejemplo a continuación.

## Ejemplo 1

**Estructura de la Red**:

- **Capa de Entrada**: 128 neuronas
- **Capa Oculta 1**: 64 neuronas
- **Capa de Salida**: 1 neuronas

Activación: ReLU para las capas ocultas, Softmax para la salida.


| Capa    | # de Neuronas de Entrada | # de Neuronas de Salida | # de Pesos | # de Sesgos | # de Parámetros |
| ------- | ------------------------ | ----------------------- | ---------- | ----------- | --------------- |
| **FC1**     | 128                      | 64                      |            |             |                 |
| **FC2**     | 64                       | 1                       |            |             |                 |

**Total de parámetros**: 

## Ejemplo 2

**Estructura de la Red**:

- **Capa de Entrada**: 256 neuronas
- **Capa Oculta 1**: 128 neuronas
- **Capa Oculta 2**: 64 neuronas
- **Capa de Salida**: 10 neuronas

Activación: ReLU para las capas ocultas, Softmax para la salida.

| Capa    | # de Neuronas de Entrada | # de Neuronas de Salida | # de Pesos | # de Sesgos | # de Parámetros |
| ------- | ------------------------ | ----------------------- | ---------- | ----------- | --------------- |
| **FC1**     | 256                      | 128                     |            |             |                 |
| **FC2**     | 128                      | 64                      |            |             |                 |
| **FC3**     | 64                       | 10                      |            |             |                 |

**Total de parámetros**: 

## Ejemplo 3

**Estructura de la Red**:

- **Capa de Entrada**: 512 neuronas
- **Capa Oculta 1**: 256 neuronas
- **Capa Oculta 2**: 128 neuronas
- **Capa Oculta 3**: 64 neuronas
- **Capa de Salida**: 10 neuronas

Activación: ReLU para las capas ocultas, Softmax para la salida.

| Capa    | # de Neuronas de Entrada | # de Neuronas de Salida | # de Pesos | # de Sesgos | # de Parámetros |
| ------- | ------------------------ | ----------------------- | ---------- | ----------- | --------------- |
| **FC1**     | 512                      | 256                     |            |             |                 |
| **FC2**     | 256                      | 128                     |            |             |                 |
| **FC3**     | 128                      | 64                      |            |             |                 |
| **FC4**     | 64                       | 10                      |            |             |                 |

**Total de parámetros**: 

## Ejemplo 4

**Objetivo**: Calcular el número de pesos, sesgos y parámetros totales por capa, así como el shape de salida.

**Estructura de la Red**:

- **Capa de Entrada**: Imágenes de tamaño 32x32 con 3 canales (RGB).
- **CONV1**: Kernel de 5x5, 8 filtros, stride de 1, padding de 2 (zero-padding).
- **POOL1**: Pooling 2x2, stride de 2, tipo 'max'.
- **Flatten**
- **Capa de Salida**: 10 neuronas (clasificación de 10 clases).

Activación: ReLU para la capa convolucional, Softmax para la salida.

| Capa        | Detalle                    | Out Shape | # de Pesos | # de Sesgos | # de Parámetros |
| ----------- | -------------------------- | --------- | ---------- | ----------- | --------------- |
| **Input**   | (32, 32, 3)                | (32,32,3) |            |             |                 |
| **CONV1**   | f=5x5, s=1, p=2, 8 filtros |           |            |             |                 |
| **POOL1**   | 2x2, s=2, max              |           |            |             |                 |
| **Flatten** |                            |           |            |             |                 |
| **FC**      | Softmax, 10 clases         | (10,1)    |            |             |                 |

**Total de parámetros**: 

## Ejemplo 5

**Objetivo**: Calcular el número de pesos, sesgos y parámetros totales por capa, así como el shape de salida de cada capa (activation shape).

**Estructura de la Red**:

- **Capa de Entrada**: Imágenes de tamaño 32x32 con 3 canales (RGB).
- **CONV1**: Kernel de 3x3, 16 filtros, stride de 1, padding de 1 (zero-padding).
- **POOL1**: Pooling 2x2, stride de 2, tipo 'max'.
- **CONV2**: Kernel de 3x3, 32 filtros, stride de 1, padding de 1 (zero-padding).
- **POOL2**: Pooling 2x2, stride de 2, tipo 'max'.
- **Flatten**
- **FC1**: 128 neuronas.
- **FC2**: 10 neuronas (clasificación de 10 clases).

Activación: ReLU para las capas convolucionales y FC1, Softmax para la salida de FC2.

| Capa        | Detalle                     | Out Shape   | # de Pesos | # de Sesgos | # de Parámetros |
| ----------- | --------------------------- | ----------- | ---------- | ----------- | --------------- |
| **Input**   | (32, 32, 3)                 | (32, 32, 3) |            |             |                 |
| **CONV1**   | f=3x3, s=1, p=1, 16 filtros |             |            |             |                 |
| **POOL1**   | 2x2, s=2,max                |             |            |             |                 |
| **CONV2**   | f=3x3, s=1, p=1, 32 filtros |             |            |             |                 |
| **POOL2**   | 2x2, s=2,max                |             |            |             |                 |
| **Flatten** |                             |             |            |             |                 |
| **FC1**     | 128 neuronas                |             |            |             |                 |
| **FC2**     | Softmax, 10 clases          | (10, 1)     |            |             |                 |

**Total de parámetros**: 
