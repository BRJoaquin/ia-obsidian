## Definición

El dropout es una técnica de [[Regularización|regularización]] utilizada en redes neuronales para prevenir el [[Sobreajuste (Overfitting)|sobreajuste]]. **Esta técnica implica desactivar aleatoriamente un subconjunto de neuronas durante el entrenamiento**.

![[Pasted image 20231128151549.png]]
## Funcionamiento

- **Aleatoriedad**: En cada paso de entrenamiento, cada neurona tiene una probabilidad `p` de ser "eliminada", es decir, su salida se establece en cero.
- **Diversidad de características**: Al eliminar diferentes neuronas en cada iteración, se fomenta que la red aprenda características más robustas y menos dependientes de neuronas específicas.
- **Ensamblado implícito**: Cada paso de entrenamiento utiliza una "subred" diferente, lo que se asemeja a entrenar múltiples modelos y promediar sus predicciones.

### Parámetros

- **Probabilidad de Dropout (`p`)**: Este es el hiperparámetro principal y representa la probabilidad de que una neurona se "apague". Un valor común es 0.5, pero puede ajustarse según la tarea y la arquitectura de la red.

### Implementación en Python con TensorFlow/Keras

```python
import tensorflow as tf
from tensorflow.keras.layers import Dropout

# Ejemplo de cómo añadir una capa de dropout en una red neuronal
modelo = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu'),
    Dropout(0.5),  # Añadir dropout con una probabilidad de 0.5
    tf.keras.layers.Dense(10, activation='softmax')
])
```

## Ventajas y Desventajas

### Ventajas

1. **Prevención de sobreajuste**: Al forzar a la red a no depender de cualquier neurona específica, se reduce el riesgo de memorizar los datos de entrenamiento.
2. **Robustez**: Aumenta la capacidad de generalización del modelo al aprender características más generalizables.
3. **Simplicidad**: Es fácil de implementar y suele ser efectivo con poca configuración.

### Desventajas

1. **Tiempo de entrenamiento**: Puede aumentar el tiempo de entrenamiento, ya que cada iteración utiliza una configuración diferente de neuronas.
2. **Selección de hiperparámetros**: La elección de la probabilidad de dropout puede ser crítica y requiere ajuste fino.

![[Pasted image 20231128154042.png]]