# Explicación de Regularización en Machine Learning

La regularización es una estrategia fundamental en aprendizaje automático para prevenir el sobreajuste, facilitando que el modelo generalice mejor a nuevos datos. Se implementa añadiendo un término de penalización al coste de la función de pérdida.

## Función de Coste con Regularización

La función de coste con [[Regularización|regularización]] se expresa como:

$$ \tilde{J}(W) = J(W) + \lambda R(W), \quad \lambda > 0 $$

- $J(W)$: [[Función de pérdida|Función de coste]] original sin regularización.
- $\lambda$: Parámetro de regularización que controla la fuerza de la penalización.
- $R(W)$: Término de regularización que añade una penalidad basada en la complejidad del modelo.

## Parámetros de Regularización

- **$\lambda$**: Parámetro de _tuning_ o ajuste.
  - Es un [[Hiperparámetro|hiperparámetro]] que debe ser cuidadosamente seleccionado, típicamente a través de [[Validación cruzada (Cross-validation)|validación cruzada]].
  - Al ser mayor que cero ($\lambda > 0$), asegura que la penalización es efectiva.

## Efectos de Ajustar $\lambda$

- Al incrementar $\lambda$:
  - **Aumenta el sesgo**: Conduce a un modelo menos flexible, pudiendo causar [[Subajuste (Underfitting)|subajuste]].
  - **Disminuye la varianza**: Ayuda a prevenir el [[Sobreajuste (Overfitting)|sobreajuste]], limitando la complejidad del [[Modelo (Hipotesis)|modelo]].

## Visualización del Error Cuadrático Medio

![[Pasted image 20231128143404.png]]

El gráfico adjunto ilustra la relación entre el error cuadrático medio (MSE) y el parámetro de regularización $\lambda$.

- **Eje X**: Escala logarítmica de $\lambda$.
- **Eje Y**: MSE, indicando el error del modelo.
- **Curvas**:
  - **Curva Rosa**: Representa el error de entrenamiento (sesgo + varianza).
  - **Curva negra**: Representa el sesgo.
  - **Curva Verde**: Representa la varianza.

El punto de cruce de las curvas indica un valor de $\lambda$ equilibrado que minimiza tanto el sesgo como la varianza.

## Conclusión

La selección adecuada de $\lambda$ es crucial para el rendimiento del modelo, buscando un balance entre sesgo y varianza para una buena generalización.
