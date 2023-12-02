## One-Hot Encoding en NLP

- **Definición**: Representa palabras como vectores donde cada palabra se asocia con un vector con un solo valor '1' y el resto '0'.
- **Problema de Dimensionalidad**: Cada palabra única en el vocabulario requiere una dimensión. Esto puede resultar en vectores muy grandes y dispersos, especialmente para grandes corpus de texto.

![[Pasted image 20231202114741.png]]
# Reducción de Dimensionalidad en One-Hot Encoding para NLP

La reducción de dimensionalidad es un proceso clave en NLP para manejar la alta dimensionalidad que resulta del one-hot encoding. En el contexto de NLP, implica convertir la representación de alta dimensión de los datos de texto en un espacio 
de menor dimensión, preservando tanto como sea posible la información relevante.

## Técnicas de Reducción de Dimensionalidad

### Análisis de Componentes Principales (PCA)
- **Uso No Común en Texto**: PCA no es común en one-hot encoding para NLP debido a la dispersión y naturaleza binaria de los datos.

### Descomposición en Valores Singulares (SVD)
- **Popular en NLP**: SVD es una técnica efectiva para reducir la dimensionalidad de matrices dispersas como las creadas por one-hot encoding.
- **Latent Semantic Analysis (LSA)**: Aplica SVD a la matriz de términos por documentos para identificar patrones y relaciones ocultas entre palabras (significados latentes).

### Autoencoders
- **Redes Neuronales**: Un autoencoder es una red neuronal diseñada para aprender una representación comprimida de los datos de entrada.

## Beneficios de la Reducción de Dimensionalidad

- **Mejora del Rendimiento de Cómputo**: Reduce la cantidad de cálculo necesario para procesar los datos.
- **Disminución del Sobreajuste**: Al reducir la cantidad de características, puede ayudar a mejorar la generalización de los modelos.
- **Visualización de Datos**: Permite visualizar datos de alta dimensión en 2D o 3D.

## Proceso de SVD en NLP

1. **Construir la Matriz de Términos por Documentos**: Donde las filas representan palabras únicas y las columnas representan documentos.
2. **Aplicar SVD**: Factoriza la matriz en tres matrices distintas (U, Σ, V^T) que representan los vectores de términos, los valores singulares y los vectores de documentos, respectivamente.
3. **Seleccionar Componentes Principales**: Seleccionar los 'k' valores singulares más grandes y sus correspondientes vectores para formar la nueva representación de espacio reducido.

## Ejemplo de SVD

Dada una matriz término-documento de one-hot encoding:

```plaintext
    S1 S2 S3 S4 S5
dog  1  1  1  0  0
cat  1  1  0  1  0
cow  0  0  1  0  1
```

La aplicación de SVD y la reducción de dimensiones a 'k' componentes daría lugar a nuevas matrices que representan una versión simplificada del espacio original, manteniendo las relaciones semánticas más importantes entre las palabras.