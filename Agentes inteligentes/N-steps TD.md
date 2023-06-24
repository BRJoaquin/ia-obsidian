
El aprendizaje de Diferencias Temporales de n pasos, o n-Steps TD Learning, es una extensión de [[TD(0)]] que combina ideas de [[Métodos Monte Carlo]] y TD(0) **para hacer una actualización basada en múltiples pasos en lugar de un solo paso**.

En TD(0), solo miramos la recompensa inmediata y el siguiente estado para hacer una actualización. Sin embargo, en n-Steps TD Learning, miramos las `n` próximas recompensas y estados para hacer la actualización.

La idea básica es estimar el retorno `Gt` no solo en función de la recompensa inmediata y la próxima estimación de valor del estado (como en TD(0)), sino también en función de las `n` próximas recompensas y la estimación del estado después de `n` pasos.

La ecuación para el retorno en n-Steps TD Learning es la siguiente:

$$G_{t:t+n} = R_{t+1} + \gamma R_{t+2} + ... + \gamma^{n-1}R_{t+n} + \gamma^nV(S_{t+n})$$

Y la regla de actualización de valor se convierte en:

$$V(S_t) = V(S_t) + \alpha[G_{t:t+n} - V(S_t)]$$

Aquí, `n` es un parámetro que puedes elegir ([[Hiperparámetros]]). Cuando `n=1`, obtienes TD(0). Cuando `n` es igual a la longitud del episodio, obtienes el método de Monte Carlo. Así que puedes ver n-Steps TD Learning como un compromiso entre TD(0) y el método de Monte Carlo.

**Una ventaja de n-Steps TD Learning es que te permite ajustar el equilibrio entre sesgo y varianza. Con un `n` más pequeño, tienes más sesgo pero menos varianza. Con un `n` más grande, tienes menos sesgo pero más varianza.**

# Algoritmo

![[Pasted image 20230624195645.png]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/AJiG3ykOxmY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
