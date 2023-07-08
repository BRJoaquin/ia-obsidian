La matriz de confusión, también conocida como tabla de contingencia, es una herramienta que permite visualizar el rendimiento de un algoritmo de aprendizaje automático, específicamente en tareas de clasificación. Proporciona un resumen de las predicciones correctas e incorrectas divididas por cada clase. La estructura básica de una matriz de confusión para una tarea de clasificación binaria se muestra a continuación:

|  | Prediccion positiva | Prediccion negativa |  
| -------- | -------- | -------- |  
| Clase positiva | Verdaderos Positivos (TP) | Falsos Negativos (FN) |  
| Clase negativa | Falsos Positivos (FP) | Verdaderos Negativos (TN) |

Aquí está el significado de cada término:

- Verdaderos Positivos (TP): El modelo predijo correctamente que la clase era positiva.
- Verdaderos Negativos (TN): El modelo predijo correctamente que la clase era negativa.
- Falsos Positivos (FP): El modelo predijo incorrectamente que la clase era positiva (cuando en realidad era negativa).
- Falsos Negativos (FN): El modelo predijo incorrectamente que la clase era negativa (cuando en realidad era positiva).

Estos cuatro valores se utilizan para calcular métricas que evalúan el rendimiento del modelo, como la [[Precisión]], el [[Recall]], el [[F1-score]] y el [[AUC-ROC]].

<iframe width="560" height="315" src="https://www.youtube.com/embed/07dtryhNGms" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>