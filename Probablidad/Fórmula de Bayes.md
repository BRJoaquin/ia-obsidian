La fórmula de Bayes es un teorema fundamental en la teoría de la probabilidad que relaciona las probabilidades condicionales de dos eventos. La fórmula es la siguiente:

$$\Large
P(A | B) = \frac{P(B | A) \cdot P(A)}{P(B)}
$$

En esta fórmula:

-   $P(A | B)$ es la probabilidad condicional de que el evento $A$ ocurra, dado que el evento $B$ ya ha ocurrido.
-   $P(B | A)$ es la probabilidad condicional de que el evento $B$ ocurra, dado que el evento $A$ ya ha ocurrido.
-   $P(A)$ es la probabilidad marginal de que el evento $A$ ocurra.
-   $P(B)$ es la probabilidad marginal de que el evento $B$ ocurra.


# Ejemplo 

Supongamos que una empresa tiene dos máquinas (M1 y M2) que producen cierto tipo de componentes. La máquina M1 produce el 70% de los componentes, y la máquina M2 produce el 30% restante. Desafortunadamente, ambos tipos de máquinas tienen una tasa de defectos en su producción: M1 produce el 1% de componentes defectuosos, mientras que M2 produce el 3% de componentes defectuosos.

Ahora, si seleccionamos un componente al azar y resulta ser defectuoso, queremos calcular la probabilidad de que haya sido producido por la máquina M1.

Definimos los eventos:

-   A: el componente es defectuoso
-   B1: el componente fue producido por M1
-   B2: el componente fue producido por M2

Podemos calcular la probabilidad de que un componente defectuoso haya sido producido por la máquina M1. En este caso, utilizaremos el teorema de Bayes y la fórmula de probabilidad total para encontrar P(B1|A).

Recordemos que el teorema de Bayes nos dice:

$$
\\ P(B_1 \mid A) = \frac{P(A \mid B_1) P(B_1)}{P(A)}$$

Podemos reemplazar P(A) usando la fórmula de probabilidad total:

$$P(A) = P(A \mid B_1) P(B_1) + P(A \mid B_2) P(B_2)$$

Entonces, la fórmula del teorema de Bayes se convierte en:

$$P(B_1 \mid A) = \frac{P(A \mid B_1) P(B_1)}{P(A \mid B_1) P(B_1) + P(A \mid B_2) P(B_2)}$$

Usando la información proporcionada:

-   P(B1) = 0.7
-   P(B2) = 0.3
-   P(A|B1) = 0.01
-   P(A|B2) = 0.03


Sustituimos estos valores en la fórmula modificada:

$$P(B_1 \mid A) = \frac{(0.01)(0.7)}{(0.01)(0.7) + (0.03)(0.3)}$$
$$P(B_1 \mid A) \approx 0.4375$$

Entonces, si un componente seleccionado al azar resulta ser defectuoso, hay aproximadamente un 43.75% de probabilidad de que haya sido producido por la máquina M1.