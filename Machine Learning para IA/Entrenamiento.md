El entrenamiento es una etapa clave en el proceso de [[Machine Learning]], en la que un modelo ajusta sus parámetros internos para aprender a realizar una tarea específica, como [[Clasificación]], [[Regresión lineal]] o [[Clustering]]. Durante el entrenamiento, el modelo utiliza un conjunto de datos de entrenamiento, que contiene ejemplos de entradas y, en el caso del [[Aprendizaje supervisado]], las salidas correspondientes.

El proceso de entrenamiento generalmente involucra los siguientes pasos:

1.  **Inicialización**: Los parámetros del modelo se inicializan, a menudo con valores aleatorios o utilizando algún método específico.

2.  **Paso de avance (forward pass)**: El modelo procesa los datos de entrada y genera una salida (predicción). En el caso de las redes neuronales, esto implica propagar la información a través de las capas y aplicar funciones de activación.

3.  **Cálculo de la pérdida**: Se compara la salida del modelo con las salidas reales o etiquetas del conjunto de datos de entrenamiento utilizando una [[Función de pérdida]] (también llamada función de costo o error). La función de pérdida cuantifica la diferencia entre las predicciones del modelo y los valores reales, y el objetivo es minimizar esta diferencia durante el entrenamiento.

4.  **Retropropagación (backpropagation)**: En el caso de las redes neuronales, se utiliza el algoritmo de retropropagación para calcular el gradiente de la función de pérdida con respecto a cada uno de los parámetros del modelo. Este paso es esencial para la actualización de los parámetros en función del error cometido por el modelo.

5.  **Actualización de parámetros**: Los parámetros del modelo se actualizan utilizando un algoritmo de optimización, como el descenso de gradiente estocástico (SGD) o variantes más avanzadas como Adam y RMSProp. La actualización de parámetros implica ajustar los valores de los parámetros en función del gradiente calculado en el paso de retropropagación, con el objetivo de minimizar la función de pérdida.

6.  **Iteraciones**: El proceso de avance, cálculo de pérdida, retropropagación y actualización de parámetros se repite a lo largo de múltiples iteraciones (también llamadas epochs), hasta que el modelo alcance un rendimiento aceptable o se cumpla un criterio de parada específico.

Una vez que el modelo ha sido entrenado, se puede evaluar en un conjunto de datos de validación o prueba para medir su capacidad de generalizar a datos no vistos. **Es importante tener en cuenta que un buen rendimiento en el conjunto de entrenamiento no garantiza necesariamente un buen rendimiento en datos nuevos, ya que el modelo puede haber [[Sobreajuste (Overfitting)]] los datos de entrenamiento** (aprendiendo el ruido o las peculiaridades de los datos en lugar de las características generales). Para evitar esto, se utilizan técnicas como la [[Validación cruzada (Cross-validation)]], la [[Regularización]] y la [[Selección de modelo]]