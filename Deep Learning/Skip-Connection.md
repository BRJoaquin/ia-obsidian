## Definición

Las skip connections, también conocidas como **conexiones residuales**, son una técnica utilizada en arquitecturas de redes neuronales profundas. Permiten que la salida de una capa anterior sea utilizada como entrada adicional para una capa posterior, generalmente saltándose una o más capas intermedias.

![[Pasted image 20231129202933.png]]
## Funcionamiento y Beneficios

### Facilitación del Flujo de Información

- **Directo**: Permiten que la señal de entrada fluya directamente a capas más profundas.
- **Preservación de Información**: Ayudan a preservar la información original, lo que puede ser crítico en tareas complejas.

### Alivio del Problema de Desvanecimiento de Gradientes
ver [[Desvanecimiento de gradiente]]
- **Gradientes más Fuertes**: Facilitan la propagación de gradientes durante el entrenamiento, lo que es especialmente útil en redes muy profundas.
- **Entrenamiento Eficiente**: Permiten que las redes neuronales profundas se entrenen de manera más efectiva y eficiente.

### Mejora del Aprendizaje de Características

- **Extracción de Características**: Ayudan a las capas profundas a aprender características complementarias a las aprendidas por capas anteriores.
- **Diversidad en Aprendizaje**: Fomentan la diversidad en el aprendizaje de características en diferentes capas de la red.

## Ejemplos en Arquitecturas de Red

### Redes ResNet

- **Uso Extensivo**: Las skip connections son un componente clave en las arquitecturas ResNet, ampliamente utilizadas en visión por computador.
- **Bloques Residuales**: Cada bloque residuo en una ResNet tiene una skip connection que suma la entrada del bloque con su salida.

## Consideraciones y Limitaciones

### Complejidad de la Red

- Aunque mejoran el rendimiento, las skip connections aumentan la complejidad de la red.

### Requerimientos Computacionales

- Pueden incrementar los requerimientos de memoria y tiempo de cómputo, dependiendo de cómo se implementen.

## Conclusión

Las skip connections son una técnica poderosa en deep learning, especialmente útil para construir redes neuronales profundas. Facilitan el entrenamiento y mejoran la capacidad de la red para aprender características complejas y variadas. Su aplicación en arquitecturas como ResNet ha demostrado mejoras significativas en tareas de visión por computador y otras áreas.

# Y si son tan buenas por que no se usan siempre?

<iframe width="560" height="315" src="https://www.youtube.com/embed/de-Oi1kX7is?si=AzmoFPXE1l_3PUb-" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Razones por las que No Siempre se Usan

### 1. Complejidad de la Arquitectura

- **Diseño Más Complejo**: La incorporación de skip connections puede complicar el diseño y la comprensión de la arquitectura de la red.
- **Integración con Otras Componentes**: Puede ser desafiante integrar skip connections con otras características de la red, como normalización por lotes o capas de activación.

### 2. Requerimientos de Recursos

- **Uso de Memoria**: Las skip connections incrementan el uso de memoria, lo que puede ser un problema en dispositivos con recursos limitados.
- **Tiempo de Entrenamiento**: Pueden aumentar el tiempo de entrenamiento debido a la complejidad adicional en el cálculo de los gradientes y la propagación hacia adelante y hacia atrás.

### 3. No Siempre Necesarias

- **Tareas Simples**: En tareas más simples o con conjuntos de datos más pequeños, las skip connections pueden no ser necesarias y una arquitectura más simple podría ser suficiente.
- **Problemas de Ajuste Fino**: En algunos casos, pueden introducir problemas en el ajuste fino de modelos, especialmente cuando se necesita un control más granular de la propagación de los gradientes.

### 4. Elección Basada en el Problema

- **Dependencia del Tipo de Tarea**: Algunas tareas pueden beneficiarse más de las skip connections que otras. Por ejemplo, son muy útiles en tareas de visión por computador, pero pueden ser menos críticas en otros dominios.
- **Experiencia y Experimentación**: La elección de usarlas o no a menudo depende de la experiencia del diseñador del modelo y de la experimentación específica para la tarea en cuestión.



