Una función de activación en una [[Redes Neuronales Artificiales]] es una función matemática que transforma la suma ponderada de las entradas de una neurona en una salida, generalmente para ser usada como entrada para la siguiente [[Capa (DL)|capa]] de la red. Se usan para introducir la no linealidad en el modelo, permitiendo así que la red aprenda y generalice patrones más complejos.

La elección de la función de activación puede afectar significativamente el rendimiento del modelo. Aquí te dejo algunas de las funciones de activación más utilizadas:

- [[Función Sigmoide]]
- [[Función ReLu]]
- [[Función Leaky ReLU]]
- Función Tanh
- [[Función Softmax]] 

Si no se usa una función de activación, entonces la red neuronal solo estaría compuesta de combinaciones lineales de sus entradas, y por lo tanto, sólo podría aprender relaciones lineales entre las entradas y las salidas. Esto limitaría severamente la complejidad de los patrones que la red puede aprender.

Los conceptos clave en torno a las funciones de activación incluyen:

- **No linealidad**: Las funciones de activación son en su mayoría no lineales. Esto permite a las redes neuronales aprender de los datos que son intrínsecamente no lineales.
    
- **Diferenciables**: Para que la [[Retropropagación del error]] funcione, que es el algoritmo que las redes neuronales usan para aprender de los errores que están cometiendo, las funciones de activación deben ser diferenciables.
    
- **Rango de activación**: El rango de la función de activación (es decir, los valores que puede tomar la salida) también puede afectar al aprendizaje de la red. Funciones como la sigmoide y tanh tienen un rango limitado (entre 0 y 1, y -1 y 1 respectivamente), mientras que funciones como ReLU pueden producir valores en un rango más amplio.