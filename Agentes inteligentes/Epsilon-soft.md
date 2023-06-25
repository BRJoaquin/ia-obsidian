
Una política ε-soft es un poco diferente. En lugar de seleccionar aleatoriamente cualquier acción con probabilidad ε, como en ε-greedy, una política ε-soft requiere que todas las acciones tengan al menos una probabilidad ε de ser seleccionadas. En otras palabras, la política ε-soft es una política en la que la probabilidad de seleccionar cualquier acción en cualquier estado no es cero. Esto significa que todas las acciones tienen la oportunidad de ser exploradas, no importa cuán poco prometedoras parezcan en un principio. 


```python
import numpy as np

def e_soft_policy(Q, epsilon, nA):
    """
    Crea una política epsilon-soft a partir de una tabla Q y un valor epsilon.

    Args:
    Q: Una tabla Q [número de estados, número de acciones] 
    epsilon: Probabilidad de seleccionar una acción aleatoria (float entre 0 y 1)
    nA: Número de acciones en el entorno

    Returns:
    Una función que toma el estado de observación como entrada y devuelve una política para ese estado
    """
    def policy_fn(observation):
        A = np.ones(nA, dtype=float) * epsilon / nA
        best_action = np.argmax(Q[observation])
        A[best_action] += (1.0 - epsilon)
        return A
    return policy_fn


```