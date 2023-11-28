![[Pasted image 20231128105430.png]]

El Feedforward es un proceso fundamental en las redes neuronales profundas (CNN, RNN, etc.) que describe cómo las entradas fluyen a través de la red y cómo se propagan los valores a lo largo de las capas. En este proceso, las entradas se propagan en una sola dirección, de la capa de entrada hacia adelante a través de todas las capas ocultas hasta la capa de salida (capa output).

## Ejemplo de Código en Python

```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Ejemplo de una red feedforward simple
pesos = np.array([0.5, -0.5])  # Ejemplo de pesos
sesgo = 0.0                    # Ejemplo de sesgo

# Función de feedforward
def feedforward(entradas):
    return sigmoid(np.dot(entradas, pesos) + sesgo)

# Datos de entrada de ejemplo
entradas = np.array([2, 3])

# Resultado de feedforward
resultado = feedforward(entradas)
print("Resultado de Feedforward:", resultado)
```