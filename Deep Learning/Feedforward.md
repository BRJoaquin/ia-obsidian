![[Pasted image 20231128105430.png]]

## Definición y Conceptos Básicos
- **Definición**: Feedforward es el proceso por el cual una red neuronal artificial procesa la información de entrada hacia adelante, desde la capa de entrada hasta la capa de salida.
- **Funcionamiento**: En una red neuronal feedforward, las señales viajan en una sola dirección: de entrada a salida. No hay ciclos o bucles en este tipo de redes.
  
## Características Principales
- **Capas de la Red**: 
  - **Capa de Entrada**: Recibe los datos de entrada.
  - **Capas Ocultas**: Realizan cálculos y transformaciones en los datos.
  - **Capa de Salida**: Produce el resultado final de la red.
- **Conexiones**: Cada neurona en una capa está conectada a todas las neuronas en la capa siguiente.
- **Pesos y Sesgos**: Cada conexión tiene un peso, y cada neurona, un sesgo, que se ajustan durante el entrenamiento.
- **Funciones de Activación**: Se utilizan para introducir no linealidades en el modelo, permitiendo a la red aprender patrones complejos.

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