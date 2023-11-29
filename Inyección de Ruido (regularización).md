## Concepto y Objetivo

La inyección de ruido en las etiquetas de salida es una técnica de [[Regularización|regularización]] en deep learning que consiste en modificar intencionalmente las etiquetas de los datos de entrenamiento. Esta modificación se realiza asumiendo que algunas etiquetas pueden contener errores o no ser completamente precisas. El objetivo es prevenir el [[Sobreajuste (Overfitting)|sobreajuste]], especialmente en situaciones donde la maximización del logaritmo de la [[Probabilidad condicional|probabilidad condicional]] $\log p(y | x)$ puede ser perjudicial debido a etiquetas incorrectas.

## Mecanismo y Ejemplo: Label Smoothing

### Label Smoothing

- **Definición**: Regulariza modelos basados en [[Función Softmax|softmax]] suavizando las etiquetas de clasificación.
- **Implementación**: En lugar de utilizar etiquetas "duras" (0 o 1), se emplean objetivos "suaves", es decir, valores ligeramente ajustados hacia una distribución más uniforme.
- **Ejemplo**: Para una clasificación con \( k \) categorías y una pequeña constante \( \epsilon \), una etiqueta correcta de 1 se reemplaza por \( 1 - \epsilon \), y una etiqueta incorrecta de 0 se reemplaza por \( \frac{\epsilon}{k - 1} \).

### Aplicación en la Función de Pérdida

- **Función de Pérdida con Cross-Entropy**: Se utiliza con estos objetivos suaves, lo que evita la búsqueda de probabilidades extremas (0 o 1) por parte del modelo.

## Beneficios del Ruido en Etiquetas

1. **Previene el Sobreajuste**: Al suavizar las etiquetas, el modelo se vuelve menos propenso a aprender patrones erróneos de etiquetas ruidosas o incorrectas.
2. **Robustez en la Clasificación**: Evita que el modelo persiga probabilidades extremadamente altas o bajas, lo que puede conducir a un mejor rendimiento en datos no vistos.
3. **Convergencia Estable**: Previene la divergencia del modelo que puede ocurrir al intentar predecir probabilidades absolutas (0 o 1) en la clasificación.

## Consideraciones Importantes

- **Selección del Valor de \( \epsilon \)**: Elegir un valor adecuado para \( \epsilon \) es crucial; un valor muy alto puede dañar la capacidad del modelo para aprender las etiquetas correctas, mientras que un valor muy bajo puede no tener un efecto significativo.
- **Aplicabilidad**: Aunque es una técnica poderosa, su aplicación y efectividad pueden variar dependiendo del tipo de tarea y la naturaleza de los datos.

## Historia y Uso Actual

- **Uso Histórico**: Esta estrategia se ha utilizado desde la década de 1980 y continúa siendo una técnica importante en las redes neuronales modernas.
- **Ejemplos en la Práctica**: Empresas y proyectos de investigación han aplicado label smoothing en sistemas de clasificación avanzados, demostrando su eficacia en mejorar la generalización y la robustez de los modelos.

En resumen, la inyección de ruido en las etiquetas de salida, y en particular el label smoothing, es una técnica de regularización sutil pero poderosa que ayuda a mejorar la robustez y la generalización de los modelos de deep learning al suavizar las etiquetas duras y prevenir el sobreajuste debido a etiquetas potencialmente incorrectas o ruidosas.
