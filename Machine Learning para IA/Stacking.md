El apilamiento o "Stacking" es una técnica de aprendizaje conjunto ([[Ensemble]]) que busca mejorar la precisión de las predicciones al combinar varios modelos de aprendizaje automático.

La idea principal detrás del stacking es utilizar **varios modelos de base (también conocidos como modelos de primer nivel) para generar predicciones, que luego se utilizan como "nuevas características" para un segundo modelo, a menudo llamado meta-modelo o modelo de segundo nivel**. El meta-modelo entonces se entrena para hacer una predicción final basada en las predicciones de los modelos de base.

En términos más concretos, estos son los pasos típicos para implementar el stacking:

1. **Entrenar los modelos de base:** Se eligen varios modelos de aprendizaje automático y se entrenan con el conjunto de datos de entrenamiento.

2. **Generar predicciones de los modelos de base:** Una vez entrenados, cada uno de los modelos de base genera predicciones para el conjunto de validación y el conjunto de prueba.

3. **Crear un nuevo conjunto de datos de entrenamiento para el meta-modelo:** Las predicciones de los modelos de base para el conjunto de validación se utilizan como características (o "metacaracterísticas") para crear un nuevo conjunto de datos de entrenamiento para el meta-modelo. El objetivo (etiqueta) para este nuevo conjunto de datos sigue siendo el mismo que el del conjunto de datos original.

4. **Entrenar el meta-modelo:** El meta-modelo se entrena con el nuevo conjunto de datos de entrenamiento.

5. **Generar la predicción final:** Para hacer predicciones sobre nuevos datos, primero se pasa el conjunto de datos de prueba a través de los modelos de base. Las predicciones resultantes se utilizan como metacaracterísticas para el meta-modelo, que finalmente genera la predicción final.

![[Pasted image 20230708210312.png]]

El apilamiento es una técnica poderosa que permite combinar de manera efectiva una variedad de modelos de aprendizaje automático, aprovechando la diversidad entre ellos para mejorar la precisión de las predicciones. Sin embargo, también puede ser más complejo de implementar que otras técnicas de ensemble como el Bagging o el Boosting, y puede llevar a un sobreajuste si no se maneja con cuidado.

# Cross-validation

Para evitar el sobreajuste y obtener una evaluación más precisa del rendimiento del modelo en el Stacking, se puede utilizar la validación cruzada, también conocida como Cross Validation. A continuación, se muestra una versión simplificada del procedimiento:

1. **Dividir el conjunto de entrenamiento en k pliegues:** Al igual que en la validación cruzada tradicional, el conjunto de entrenamiento se divide en k subconjuntos o "pliegues".

2. **Entrenar y generar metacaracterísticas:** Para cada pliegue, los modelos de base se entrenan en los k-1 pliegues restantes y **se hacen predicciones en el pliegue excluido**. Este proceso se repite para cada pliegue, asegurando que las metacaracterísticas para cada observación se generan en un modelo que no fue entrenado en esa observación. Esto ayuda a prevenir el sobreajuste.

3. **Entrenar el meta-modelo:** Las metacaracterísticas generadas en el paso anterior se utilizan para crear un nuevo conjunto de datos de entrenamiento. El meta-modelo se entrena en este nuevo conjunto de datos.

4. **Generar la predicción final:** Para hacer predicciones sobre nuevos datos, primero se pasa el conjunto de datos de prueba a través de los modelos de base. Las predicciones resultantes se utilizan como metacaracterísticas para el meta-modelo, que finalmente genera la predicción final.


Este proceso se conoce como Stacking con validación cruzada fuera de la bolsa, y puede ser una forma efectiva de evitar el sobreajuste en el Stacking.

Cabe mencionar que este proceso puede ser computacionalmente intensivo, ya que requiere entrenar múltiples modelos de base para cada pliegue de los datos. Sin embargo, es una técnica valiosa para combinar modelos de manera efectiva y puede conducir a mejoras significativas en el rendimiento del modelo.

![[Pasted image 20230713112621.png]]

# Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/8T2emza6g80" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>