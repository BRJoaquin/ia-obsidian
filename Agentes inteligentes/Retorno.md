
El retorno, también conocido como ganancia, es la suma total de las recompensas descontadas que un agente espera obtener en el futuro. **La meta del agente es maximizar el retorno esperado.**

En un [[Episodio]] específico, el retorno $G_t$ a partir del paso de tiempo $t$ se calcula como la suma de las recompensas futuras que el agente recibe, cada una de las cuales está multiplicada por una potencia del factor de descuento $\gamma$ para reflejar el hecho de que las recompensas futuras se consideran menos valiosas que las recompensas inmediatas. 

En notación formal, esto se expresa como:

$$
G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \gamma^3 R_{t+4} + \ldots
$$

donde $R_{t+1}$, $R_{t+2}$, etc., son las recompensas obtenidas en los pasos de tiempo $t+1$, $t+2$, etc., y $\gamma$ es el factor de descuento. 

El [[Factor de descuento]] $\gamma$ es un número entre 0 y 1 que determina cuánto "valora" el agente las recompensas futuras en comparación con las recompensas presentes. Si $\gamma$ es cercano a 0, el agente valora las recompensas inmediatas y tiende a ser cortoplacista en sus decisiones. Si $\gamma$ es cercano a 1, el agente valora las recompensas futuras casi tanto como las inmediatas y tiende a ser más bien de largo plazo en sus decisiones.
