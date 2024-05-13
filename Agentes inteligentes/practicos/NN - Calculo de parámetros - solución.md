¡Claro! Aquí tienes un resumen con solo las fórmulas utilizadas para cada cálculo:

### Resumen de Fórmulas

1. **Cálculo del Shape de Salida para Convolución**:
   $$
   H_{\text{out}} = \frac{(H_{\text{in}} - \text{kernel} + 2 \cdot \text{padding})}{\text{stride}} + 1
   $$

2. **Cálculo del Shape de Salida para Pooling**:
   $$
   H_{\text{out}} = \frac{H_{\text{in}} - \text{kernel}}{\text{stride}} + 1
   $$

3. **Número de Pesos para Convolución**:
   $$
   \text{Número de Pesos} = \text{kernel} \times \text{kernel} \times \text{canales de entrada} \times \text{número de filtros}
   $$

4. **Número de Sesgos para Convolución**:
   $$
   \text{Número de Sesgos} = \text{número de filtros}
   $$

5. **Total de Parámetros para Convolución**:
   $$
   \text{Total de Parámetros} = \text{Número de Pesos} + \text{Número de Sesgos}
   $$

6. **Shape de Salida para Flatten**:
   $$
   \text{Shape de Salida} = H_{\text{out}} \times W_{\text{out}} \times \text{número de filtros}
   $$

7. **Número de Pesos para Capa Fully Connected**:
   $$
   \text{Número de Pesos} = \text{neuronas de entrada} \times \text{neuronas de salida}
   $$

8. **Número de Sesgos para Capa Fully Connected**:
   $$
   \text{Número de Sesgos} = \text{neuronas de salida}
   $$

9. **Total de Parámetros para Capa Fully Connected**:
   $$
   \text{Total de Parámetros} = \text{Número de Pesos} + \text{Número de Sesgos}
   $$

Estas fórmulas son aplicables a las capas convolucionales, de pooling, y fully connected en la estructura de la red neuronal descrita.

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

Claro, vamos a desglosar cada paso para calcular el número de pesos, sesgos y parámetros totales por capa, así como el shape de salida.

### Detalles del cálculo

1. **Capa de Entrada**:
   - **Shape de Entrada**: (32, 32, 3)

2. **CONV1**:
   - **Kernel**: 5x5
   - **Número de Filtros**: 8
   - **Stride**: 1
   - **Padding**: 2 (zero-padding)

   **Cálculo del Shape de Salida**:
   $$
   H_{\text{out}} = \frac{(H_{\text{in}} - \text{kernel} + 2 \cdot \text{padding})}{\text{stride}} + 1
   $$
   Donde $H_{\text{in}}$ es la altura y anchura de entrada.

   Para **altura** y **anchura**:
   $$
   H_{\text{out}} = \frac{(32 - 5 + 2 \cdot 2)}{1} + 1 = 32
   $$

   - **Shape de Salida**: (32, 32, 8)

   **Número de Pesos**:
   $$
   \text{Número de Pesos} = \text{kernel} \times \text{kernel} \times \text{canales de entrada} \times \text{número de filtros}
   $$
   $$
   \text{Número de Pesos} = 5 \times 5 \times 3 \times 8 = 600
   $$

   **Número de Sesgos**:
   $$
   \text{Número de Sesgos} = \text{número de filtros} = 8
   $$

   **Total de Parámetros**:
   $$
   \text{Total de Parámetros} = \text{Número de Pesos} + \text{Número de Sesgos} = 600 + 8 = 608
   $$

3. **POOL1**:
   - **Kernel de Pooling**: 2x2
   - **Stride**: 2
   - **Tipo**: max

   **Cálculo del Shape de Salida**:
   $$
   H_{\text{out}} = \frac{H_{\text{in}} - \text{kernel}}{\text{stride}} + 1
   $$
   $$
   H_{\text{out}} = \frac{32 - 2}{2} + 1 = 16
   $$

   - **Shape de Salida**: (16, 16, 8)

4. **Flatten**:
   - **Shape de Entrada**: (16, 16, 8)
   - **Shape de Salida**: 16 \times 16 \times 8 = 2048

5. **Capa de Salida**:
   - **Número de Neuronas**: 10

   **Número de Pesos**:
   $$
   \text{Número de Pesos} = \text{neuronas de entrada} \times \text{neuronas de salida} = 2048 \times 10 = 20480
   $$

   **Número de Sesgos**:
   $$
   \text{Número de Sesgos} = \text{neuronas de salida} = 10
   $$

   **Total de Parámetros**:
   $$
   \text{Total de Parámetros} = \text{Número de Pesos} + \text{Número de Sesgos} = 20480 + 10 = 20490
   $$

### Resumen en la Tabla


| Capa        | Detalle                    | Out Shape   | # de Pesos | # de Sesgos | # de Parámetros |
| ----------- | -------------------------- | ----------- | ---------- | ----------- | --------------- |
| **Input**   | (32, 32, 3)                | (32, 32, 3) |            |             |                 |
| **CONV1**   | f=5x5, s=1, p=2, 8 filtros | (32, 32, 8) | 600        | 8           | 608             |
| **POOL1**   | 2x2, s=2, max              | (16, 16, 8) | 0          | 0           | 0               |
| **Flatten** |                            | (2048, )    | 0          | 0           | 0               |
| **FC**      | Softmax, 10 clases         | (10, )      | 20480      | 10          | 20490           |

**Total de parámetros**: **21098**

### Ejemplo 5

Vamos a calcular los detalles para cada capa de la red propuesta.

### Detalles del cálculo

1. **Capa de Entrada**:
   - **Shape de Entrada**: (32, 32, 3)

2. **CONV1**:
   - **Kernel**: 3x3
   - **Número de Filtros**: 16
   - **Stride**: 1
   - **Padding**: 1 (zero-padding)

   **Cálculo del Shape de Salida**:
   $$
   H_{\text{out}} = \frac{(H_{\text{in}} - \text{kernel} + 2 \cdot \text{padding})}{\text{stride}} + 1
   $$
   Donde $H_{\text{in}}$ es la altura y anchura de entrada.

   Para **altura** y **anchura**:
   $$
   H_{\text{out}} = \frac{(32 - 3 + 2 \cdot 1)}{1} + 1 = 32
   $$

   - **Shape de Salida**: (32, 32, 16)

   **Número de Pesos**:
   $$
   \text{Número de Pesos} = \text{kernel} \times \text{kernel} \times \text{canales de entrada} \times \text{número de filtros}
   $$
   $$
   \text{Número de Pesos} = 3 \times 3 \times 3 \times 16 = 432
   $$

   **Número de Sesgos**:
   $$
   \text{Número de Sesgos} = \text{número de filtros} = 16
   $$

   **Total de Parámetros**:
   $$
   \text{Total de Parámetros} = \text{Número de Pesos} + \text{Número de Sesgos} = 432 + 16 = 448
   $$

3. **POOL1**:
   - **Kernel de Pooling**: 2x2
   - **Stride**: 2
   - **Tipo**: max

   **Cálculo del Shape de Salida**:
   $$
   H_{\text{out}} = \frac{H_{\text{in}} - \text{kernel}}{\text{stride}} + 1
   $$
   $$
   H_{\text{out}} = \frac{32 - 2}{2} + 1 = 16
   $$

   - **Shape de Salida**: (16, 16, 16)

4. **CONV2**:
   - **Kernel**: 3x3
   - **Número de Filtros**: 32
   - **Stride**: 1
   - **Padding**: 1 (zero-padding)

   **Cálculo del Shape de Salida**:
   $$
   H_{\text{out}} = \frac{(H_{\text{in}} - \text{kernel} + 2 \cdot \text{padding})}{\text{stride}} + 1
   $$
   $$
   H_{\text{out}} = \frac{(16 - 3 + 2 \cdot 1)}{1} + 1 = 16
   $$

   - **Shape de Salida**: (16, 16, 32)

   **Número de Pesos**:
   $$
   \text{Número de Pesos} = \text{kernel} \times \text{kernel} \times \text{canales de entrada} \times \text{número de filtros}
   $$
   $$
   \text{Número de Pesos} = 3 \times 3 \times 16 \times 32 = 4608
   $$

   **Número de Sesgos**:
   $$
   \text{Número de Sesgos} = \text{número de filtros} = 32
   $$

   **Total de Parámetros**:
   $$
   \text{Total de Parámetros} = \text{Número de Pesos} + \text{Número de Sesgos} = 4608 + 32 = 4640
   $$

5. **POOL2**:
   - **Kernel de Pooling**: 2x2
   - **Stride**: 2
   - **Tipo**: max

   **Cálculo del Shape de Salida**:
   $$
   H_{\text{out}} = \frac{H_{\text{in}} - \text{kernel}}{\text{stride}} + 1
   $$
   $$
   H_{\text{out}} = \frac{16 - 2}{2} + 1 = 8
   $$

   - **Shape de Salida**: (8, 8, 32)

6. **Flatten**:
   - **Shape de Entrada**: (8, 8, 32)
   - **Shape de Salida**: 8 \times 8 \times 32 = 2048

7. **FC1**:
   - **Número de Neuronas**: 128

   **Número de Pesos**:
   $
   \text{Número de Pesos} = \text{neuronas de entrada} \times \text{neuronas de salida} = 2048 \times 128 = 262144
   $

   **Número de Sesgos**:
   $
   \text{Número de Sesgos} = \text{neuronas de salida} = 128
   $

   **Total de Parámetros**:
   $$
   \text{Total de Parámetros} = \text{Número de Pesos} + \text{Número de Sesgos} = 262144 + 128 = 262272
   $$

8. **FC2**:
   - **Número de Neuronas**: 10

   **Número de Pesos**:
   $
   \text{Número de Pesos} = \text{neuronas de entrada} \times \text{neuronas de salida} = 128 \times 10 = 1280
   $

   **Número de Sesgos**:
   $$
   \text{Número de Sesgos} = \text{neuronas de salida} = 10
   $$

   **Total de Parámetros**:
   $$
   \text{Total de Parámetros} = \text{Número de Pesos} + \text{Número de Sesgos} = 1280 + 10 = 1290
   $$

### Resumen en la Tabla


| Capa        | Detalle                     | Out Shape    | # de Pesos | # de Sesgos | # de Parámetros |
| ----------- | --------------------------- | ------------ | ---------- | ----------- | --------------- |
| **Input**   | (32, 32, 3)                 | (32, 32, 3)  |            |             |                 |
| **CONV1**   | f=3x3, s=1, p=1, 16 filtros | (32, 32, 16) | 432        | 16          | 448             |
| **POOL1**   | 2x2, s=2,max                | (16, 16, 16) | 0          | 0           | 0               |
| **CONV2**   | f=3x3, s=1, p=1, 32 filtros | (16, 16, 32) | 4608       | 32          | 4640            |
| **POOL2**   | 2x2, s=2,max                | (8, 8, 32)   | 0          | 0           | 0               |
| **Flatten** |                             | (2048, )     | 0          | 0           | 0               |
| **FC1**     | 128 neuronas                | (128, )      | 262144     | 128         | 262272          |
| **FC2**     | Softmax, 10 clases          | (10, )       | 1280       | 10          | 1290            |
| **Total**   |                             |              |            |             | 268650          |

- **Total de parámetros en la red**: $448 + 4640 + 262272 + 1290 = 267650$
