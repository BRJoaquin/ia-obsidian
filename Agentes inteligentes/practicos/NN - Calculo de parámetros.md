
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

## Ejemplo 4

**Objetivo**: Calcular el número de pesos, sesgos y parámetros totales por capa, así como el shape de salida.

**Estructura de la Red**:
- **Capa de Entrada**: Imágenes de tamaño 32x32 con 3 canales (RGB).
- **CONV1**: Kernel de 5x5, 8 filtros, stride de 1, padding de 2 (zero-padding).
- **POOL1**: Pooling 2x2, stride de 2, tipo 'max'.
- **Capa de Salida**: 10 neuronas (clasificación de 10 clases).

**Activación**: ReLU para la capa convolucional, Softmax para la salida.

| Capa  | Detalle                    | Out<br>Shape | # de Pesos | # de Sesgos | # de Parámetros |
| ----- | -------------------------- | ------------ | ---------- | ----------- | --------------- |
| Input |                            | (32,32,3)    |            |             |                 |
| CONV1 | f=5x5, s=1, p=2, 8 filtros |              |            |             |                 |
| POOL1 | 2x2, s=2, max              |              |            |             |                 |
| FC    | Softmax, 10 clases         | (10,1)       |            |             |                 |

Total de parámetros: 

Excelente, vamos a crear un ejemplo un poco más complejo con dos capas convolucionales, dos capas de pooling y dos capas completamente conectadas. Este tipo de estructura nos permite profundizar en el análisis de cómo las capas interactúan y transforman los datos a través de la red.

### Ejemplo 5: CNN con Múltiples Capas Conv y Pooling

**Objetivo**: Calcular el número de pesos, sesgos y parámetros totales por capa, así como el shape de salida de cada capa (activation shape).

**Estructura de la Red**:
- **Capa de Entrada**: Imágenes de tamaño 32x32 con 3 canales (RGB).
- **CONV1**: Kernel de 3x3, 16 filtros, stride de 1, padding de 1 (zero-padding).
- **POOL1**: Pooling 2x2, stride de 2, tipo 'max'.
- **CONV2**: Kernel de 3x3, 32 filtros, stride de 1, padding de 1 (zero-padding).
- **POOL2**: Pooling 2x2, stride de 2, tipo 'max'.
- **FC1**: 128 neuronas.
- **FC2**: 10 neuronas (clasificación de 10 clases).

**Activación**: ReLU para las capas convolucionales y FC1, Softmax para la salida de FC2.

```markdown
| Capa  | Detalle                       | Activation Shape | # de Pesos  | # de Sesgos | # de Parámetros |
| ----- | ----------------------------- | ---------------- | ----------- | ----------- | --------------- |
| Input |                               | (32, 32, 3)      | 0           | 0           | 0               |
| CONV1 | f=3x3, s=1, p=1, 16 filtros   | (32, 32, 16)     | 3x3x3x16    | 16          | 3x3x3x16 + 16   |
| POOL1 | 2x2, s=2, max                 | (16, 16, 16)     | 0           | 0           | 0               |
| CONV2 | f=3x3, s=1, p=1, 32 filtros   | (16, 16, 32)     | 3x3x16x32   | 32          | 3x3x16x32 + 32  |
| POOL2 | 2x2, s=2, max                 | (8, 8, 32)       | 0           | 0           | 0               |
| FC1   | 128 neuronas                  | (128, 1)         | 8x8x32x128  | 128         | 8x8x32x128 + 128|
| FC2   | Softmax, 10 clases            | (10, 1)          | 128x10      | 10          | 128x10 + 10     |

Total de parámetros: \[CALCULAR AQUÍ\]
```

Esta tabla resume cada capa, mostrando la forma de activación después de cada operación, junto con el cálculo del número de pesos, sesgos y parámetros totales para cada capa. En el total de parámetros, simplemente sumarías los parámetros de todas las capas que contienen parámetros. Esta estructura proporciona una visión completa y permite entender cómo las dimensiones y parámetros cambian a través de la red. Si necesitas más detalles o un ajuste en los números, dime para adaptarlo a tus necesidades.