
# Modele el problema con un grafo con transiciones de probabilidad

```mermaid
graph TD
    A[Piso 1] -->|Subir, 3 min| B[Piso 2]
    A -->|Esperar, 2 min, 0.5 prob| A
    A -->|Esperar, 2 min, 0.5 prob| D[Piso 4]
    B -->|Subir, 1 min| C[Piso 3]
    B -->|Esperar, 2 min, 0.5 prob| C
    B -->|Esperar, 2 min, 0.5 prob| D
    C -->|Esperar, 1.5 min, 0.5 prob| A
    C -->|Esperar, 1.5 min, 0.5 prob| D
```
> El piso 4 se considera una estado terminal


# Cálculos analíticos

> Nota: Se considera (gamma) $\gamma$ = 1 para todos los ejercicios

## Calcule la utilidad esperada de la política “siempre esperar"

$$\large v_\pi(1) = 0.5[-2 + 1 \times v_\pi(1) + 0.5[-2 + 1 \times v_\pi(4)] $$
