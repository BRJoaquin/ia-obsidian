El método Actor-Crítico es un paradigma central en el aprendizaje por refuerzo que busca combinar las ventajas de los métodos basados en la política (ver [[Gradiente de Política]]) y los basados en el valor. Este enfoque híbrido consiste en dos componentes principales: un "actor" que decide qué acción tomar, y un "crítico" que evalúa la decisión del actor proporcionando una estimación de la función de valor.

![[Pasted image 20230706151612.png]]

# Actor-Crítico

El actor es una función parametrizada $\pi(a|s, \theta)$ que representa la política del agente, donde $s$ es el estado, $a$ es la acción, y $\theta$ son los parámetros de la política. Por otro lado, el crítico es una función parametrizada $V(s, w)$ que intenta estimar la función de valor de estado, donde $w$ son los parámetros del crítico.

El objetivo del crítico es aprender a predecir el retorno esperado $V^\pi(s)$ en un estado dado $s$ bajo la política $\pi$. Esto se realiza a través de técnicas como el Aprendizaje Temporal Diferencial (TD Learning), que se basa en la actualización de los valores estimados en base a las recompensas reales recibidas y las próximas estimaciones del valor del estado.

Por otro lado, el actor busca mejorar la política de selección de acciones utilizando las señales del crítico. Esto implica ajustar los parámetros $\theta$ de la política en dirección al gradiente de la política ponderado por la ventaja, que es la diferencia entre la recompensa recibida y la estimación del valor del crítico.

El pseudocódigo del algoritmo Actor-Crítico se puede ver a continuación:

```
Inicializar parámetros de política θ y función de valor V arbitrariamente
Para cada episodio:
    Inicializar estado S
    Para cada paso del episodio:
        Elegir una acción A siguiendo π(·|S, θ)
        Tomar la acción A, obtener recompensa R y próximo estado S'
        δ ← R + γV(S', w) - V(S, w)
        w ← w + α δ ∇w V(S, w)
        θ ← θ + α γ^t δ ∇θ log π(A|S, θ)
        S ← S'
```

# Ventajas de Actor-Crítico

Al mantener explícitamente tanto una política como una función de valor, los métodos de Actor-Crítico pueden explotar la guía de la función de valor para buscar de manera más eficiente en el espacio de la política.

Además, los métodos de Actor-Crítico permiten aprender políticas estocásticas y pueden aplicarse a problemas con espacios de acción contínuos o altamente dimensionales donde los métodos basados en valor pueden ser ineficientes.

Aunque la implementación de los métodos de Actor-Crítico puede ser más compleja debido a la necesidad de mantener y actualizar dos conjuntos de parámetros, la capacidad de estos métodos para combinar los beneficios de los métodos de aprendizaje basados en política y en valor hace que sean un enfoque muy utilizado en el aprendizaje por refuerzo.

# Extensiones de Actor-Crítico

Hay muchas variantes y extensiones de los métodos de Actor-Crítico, que buscan abordar algunas de las limitaciones y mejorar la eficiencia de la idea básica.

Por ejemplo, los métodos de Actor-Crítico de Diferencia Temporal de N-pasos buscan balancear el sesgo y la varianza de las estimaciones de la función de valor al considerar las recompensas de múltiples pasos futuros.

Otra extensión popular es la Política de Gradiente Determinista (DPG), que se aplica a problemas con espacios de acción continuos. En lugar de aprender una política estocástica, DPG aprende una política determinista parametrizada y un crítico que estima la función de valor acción-estado.

Finalmente, el Aprendizaje Profundo ha permitido la aplicación de los métodos de Actor-Crítico a problemas con espacios de estado y/o acción de alta dimensión, dando lugar a métodos como el Actor-Crítico Profundo Determinista (DDPG), la Política de Gradiente Profundo (DPG) y la Ventaja del Actor-Crítico (A2C/A3C).

# Conclusión

Los métodos de Actor-Crítico representan un enfoque muy poderoso en el aprendizaje por refuerzo que combina las ventajas de los métodos basados en política y en valor. Aunque la implementación puede ser más compleja, la flexibilidad y eficiencia de estos métodos los han hecho muy populares en una amplia gama de aplicaciones.