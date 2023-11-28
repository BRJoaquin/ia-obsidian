El Early Stopping (ES) es una técnica de [[Regularización|regularización]] para prevenir el [[Sobreajuste (Overfitting)|sobreajuste]] del modelo en los datos de prueba. El ES se basa en **monitorizar** la pertenencia del **error de validación** **durante** el entrenamiento y **detener** el entrenamiento cuando el error de validación comienza a aumentar.

El ES funciona de la siguiente manera:

1. Se divide el conjunto de datos en dos partes: el set entrenamiento y el set validación.
2. El modelo se entrena sobre el set entrenamiento.
3. Durante el entrenamiento, se monitorea la pertenencia del error de validación.
4. Cuando el error de validación comienza a aumentar, se detiene el entrenamiento y se utiliza el modelo más reciente para hacer predicciones en el set prueba.

![[Pasted image 20231128153910.png]]

El ES tiene varios beneficios:

* Previene el sobreajuste del modelo en los datos de prueba.
* Reduce la cantidad de tiempo y computación requerida para entrenar un buen modelo.
* Mejora la generalización del modelo, ya que evita que el modelo sea demasiado complejo y se adapte solo al conjunto entrenamiento.

El ES también tiene varios desafíos:

* Se deben elegir las condiciones para detener el entrenamiento, lo cual puede ser difícil y depende del problema específico.
* El modelo puede tener una mala generalización incluso con ES si no es buenamente diseñado o si hay demasiados parámetros.

En conclusión, el Early Stopping (ES) es una técnica de optimización para prevenir la sobre-apertura del modelo en los datos de prueba y mejora la generalización del modelo. El ES funciona monitorizando la pertenencia del error de validación durante el entrenamiento y deteniendo el entrenamiento cuando el error de validación comienza a aumentar.

![[Pasted image 20231128154021.png]]

## Configuración

- **Parámetro de Paciencia**: Define el número de [[Epoch|épocas]] para esperar después de un último mejoramiento en la métrica de rendimiento antes de detener el entrenamiento.
- **Restauración del Mejor Modelo**: Generalmente, se restaura el estado del modelo a aquel en el que tenía el mejor rendimiento en la métrica de validación.

## Ejemplo en Python (TensorFlow/Keras)

```python
from tensorflow.keras.callbacks import EarlyStopping

# Configuración del Early Stopping
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Entrenamiento del modelo con Early Stopping
modelo.fit(X_train, Y_train, validation_data=(X_val, Y_val), epochs=100, callbacks=[early_stopping])
```
