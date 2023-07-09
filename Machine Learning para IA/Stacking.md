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

<iframe width="560" height="315" src="https://www.youtube.com/embed/8T2emza6g80" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>