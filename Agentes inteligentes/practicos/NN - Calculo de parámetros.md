Entendido, comenzaremos con tres ejemplos de redes feedforward con una complejidad creciente y luego pasaremos a las redes convolucionales.

### Ejemplo 1: Red Feedforward Simple
**Objetivo**: Calcular el número de pesos, sesgos y parámetros totales por capa, así como el número total de parámetros aprendibles en toda la red.

**Estructura de la Red**:
- **Capa de Entrada**: 128 neuronas
- **Capa Oculta 1**: 64 neuronas
- **Capa de Salida**: 10 neuronas

**Activación**: ReLU para las capas ocultas, Softmax para la salida.

```markdown
| Capa | # de Neuronas de Entrada | # de Neuronas de Salida | # de Pesos | # de Sesgos | # de Parámetros |
|------|---------------------------|-------------------------|------------|-------------|----------------|
| FC1  | 128                       | 64                      |            |             |                |
| FC2  | 64                        | 10                      |            |             |                |
|      |                           |                         | **Total**  |             |                |
```

### Ejemplo 2: Red Feedforward con Dos Capas Ocultas
**Objetivo**: Calcular el número de pesos, sesgos y parámetros totales por capa, así como el número total de parámetros aprendibles en toda la red.

**Estructura de la Red**:
- **Capa de Entrada**: 256 neuronas
- **Capa Oculta 1**: 128 neuronas
- **Capa Oculta 2**: 64 neuronas
- **Capa de Salida**: 10 neuronas

**Activación**: ReLU para las capas ocultas, Softmax para la salida.

| Capa | # de Neuronas de Entrada | # de Neuronas de Salida | # de Pesos | # de Sesgos | # de Parámetros |
|------|---------------------------|-------------------------|------------|-------------|----------------|
| FC1  | 256                       | 128                     |            |             |                |
| FC2  | 128                       | 64                      |            |             |                |
| FC3  | 64                        | 10                      |            |             |                |
|      |                           |                         | **Total**  |             |                |


### Ejemplo 3: Red Feedforward con Tres Capas Ocultas
**Objetivo**: Calcular el número de pesos, sesgos y parámetros totales por capa, así como el número total de parámetros aprendibles en toda la red.

**Estructura de la Red**:
- **Capa de Entrada**: 512 neuronas
- **Capa Oculta 1**: 256 neuronas
- **Capa Oculta 2**: 128 neuronas
- **Capa Oculta 3**: 64 neuronas
- **Capa de Salida**: 10 neuronas

**Activación**: ReLU para las capas ocultas, Softmax para la salida.


| Capa | # de Neuronas de Entrada | # de Neuronas de Salida | # de Pesos | # de Sesgos | # de Parámetros |
|------|---------------------------|-------------------------|------------|-------------|----------------|
| FC1  | 512                       | 256                     |            |             |                |
| FC2  | 256                       | 128                     |            |             |                |
| FC3  | 128                       | 64                      |            |             |                |
| FC4  | 64                        | 10                      |            |             |                |
|      |                           |                         | **Total**  |             |                |


Estos ejemplos te permitirán desarrollar ejercicios de cálculo de parámetros para diferentes configuraciones de redes feedforward. Una vez que completes estos, podemos proceder con los ejemplos de redes convolucionales.