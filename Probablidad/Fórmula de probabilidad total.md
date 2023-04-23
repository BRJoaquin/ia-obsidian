La fórmula de la probabilidad total es un concepto fundamental en teoría de probabilidad. Se utiliza cuando se tienen eventos mutuamente excluyentes y colectivamente exhaustivos que forman una partición del espacio muestral. La fórmula establece que la probabilidad de un evento A se puede calcular sumando las probabilidades condicionales de A dado cada evento en la partición, multiplicadas por la probabilidad de cada evento en la partición.

Supongamos que tenemos una partición del espacio muestral formada por eventos mutuamente excluyentes y colectivamente exhaustivos B₁, B₂, ..., Bₙ. La fórmula de la probabilidad total para un evento A es:

$$\Large P(A) = \sum_{i=1}^{n} P(A \mid B_i) P(B_i)$$

> Decimos que un conjunto de eventos es colectivamente exhaustivo si al menos uno de los eventos en el conjunto debe ocurrir cada vez que se realiza el experimento aleatorio. En otras palabras, la unión de todos los eventos en el conjunto abarca todo el espacio muestral. Los eventos colectivamente exhaustivos proporcionan una descripción completa de todas las posibles salidas del experimento.
> 
> Por ejemplo, supongamos que lanzamos un dado justo de seis caras. Podemos considerar los siguientes eventos:
> -   A: el resultado es un número impar (A = {1, 3, 5})
>   -   B: el resultado es un número par (B = {2, 4, 6})
>     Los eventos A y B son colectivamente exhaustivos, ya que cubren todas las posibles salidas del experimento (A ∪ B = {1, 2, 3, 4, 5, 6}). Cada vez que lancemos el dado, el resultado será un número impar (evento A) o un número par (evento B).

# Ejemplo 

Supongamos que una empresa tiene dos máquinas (M1 y M2) que producen cierto tipo de componentes. La máquina M1 produce el 70% de los componentes, y la máquina M2 produce el 30% restante. Desafortunadamente, ambos tipos de máquinas tienen una tasa de defectos en su producción: M1 produce el 1% de componentes defectuosos, mientras que M2 produce el 3% de componentes defectuosos.

Ahora, queremos calcular la probabilidad de que un componente seleccionado al azar sea defectuoso.

Definimos los eventos:

-   A: el componente es defectuoso
-   B1: el componente fue producido por M1
-   B2: el componente fue producido por M2

Sabemos lo siguiente:

-   P(B1) = 0.7 (70% de los componentes son producidos por M1)
-   P(B2) = 0.3 (30% de los componentes son producidos por M2)
-   P(A|B1) = 0.01 (1% de los componentes producidos por M1 son defectuosos)
-   P(A|B2) = 0.03 (3% de los componentes producidos por M2 son defectuosos)

Aplicamos la fórmula de probabilidad total para calcular P(A):

P(A) = P(A|B1)P(B1) + P(A|B2)P(B2) P(A) = (0.01)(0.7) + (0.03)(0.3) P(A) = 0.007 + 0.009 P(A) = 0.016

Entonces, la probabilidad de que un componente seleccionado al azar sea defectuoso es del 1.6%.