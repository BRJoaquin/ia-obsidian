# Descenso del Gradiente

## Definición General
El descenso del gradiente es un algoritmo de optimización utilizado principalmente para encontrar el mínimo de una función. Es ampliamente utilizado en el campo del aprendizaje automático y el deep learning para minimizar una función de costo, que mide la diferencia entre la salida prevista del modelo y la salida real.

## Funcionamiento Básico
- **Gradiente:** Representa la dirección de la mayor tasa de aumento de una función. En el descenso del gradiente, se busca la dirección opuesta para minimizar la función.
- **Paso Iterativo:** El algoritmo da pasos iterativos en la dirección opuesta al gradiente.
- **Tamaño del Paso:** Conocido como tasa de aprendizaje, determina la magnitud del paso en cada iteración.

## Aplicación en Deep Learning
- **Función de Costo:** El objetivo es minimizar esta función, que mide el error del modelo.
- **Actualización de Parámetros:** Se ajustan los pesos y sesgos del modelo basándose en el gradiente de la función de costo.
- **Convergencia:** Se busca alcanzar un punto donde el cambio en la función de costo es mínimo o nulo.

## Tipos de Descenso del Gradiente
1. **Descenso del Gradiente por Lote (Batch Gradient Descent):** Utiliza todo el conjunto de datos para calcular el gradiente en cada iteración.
2. **Descenso del Gradiente Estocástico (Stochastic Gradient Descent - SGD):** Utiliza un solo ejemplo de entrenamiento por iteración. [[Descenso de Gradiente Estocástico (Stochastic Gradient Descent, SGD)]]
3. **Descenso del Gradiente Mini-Lote (Mini-batch Gradient Descent):** Utiliza un subconjunto del conjunto de entrenamiento por iteración.

## Ventajas y Desventajas
### Ventajas
- **Universalidad:** Aplicable a una amplia gama de problemas.
- **Simplicidad:** Algoritmo fácil de entender e implementar.

### Desventajas
- **Selección de Tasa de Aprendizaje:** Si es demasiado alta, puede no converger; si es demasiado baja, el proceso es muy lento.
- **Dependencia de Inicialización:** El punto de partida puede afectar la convergencia.
- **Mínimos Locales y Puntos de Silla:** Puede quedar atrapado en mínimos locales o puntos de silla en funciones no convexas.

## Ejemplo en Python
Un ejemplo básico utilizando Python para implementar el descenso del gradiente sería:

```python
def funcion_costo(x):
    return x**2

def gradiente(x):
    return 2*x

def descenso_gradiente(x_inicio, tasa_aprendizaje, n_iteraciones):
    x = x_inicio
    for i in range(n_iteraciones):
        grad = gradiente(x)
        x = x - tasa_aprendizaje * grad
    return x

x_inicio = 10
tasa_aprendizaje = 0.1
n_iteraciones = 100

x_minimo = descenso_gradiente(x_inicio, tasa_aprendizaje, n_iteraciones)
```

https://blog.gopenai.com/understanding-of-gradient-descent-intuition-and-implementation-b1f98b3645ea


<iframe width="560" height="315" src="https://www.youtube.com/embed/A6FiCDoz8_4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe> 
