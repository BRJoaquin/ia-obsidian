## Introducción

Los optimizadores son un componente crítico en el entrenamiento de modelos de deep learning. Ayudan a minimizar (o maximizar) una función objetivo, generalmente una [[Función de pérdida|función de pérdida]], ajustando los [[Parametros aprendibles (Learnable Parameters)|pesos de la red]]. Dos de los optimizadores más comunes son Adam y Stochastic Gradient Descent (SGD).

## Stochastic Gradient Descent (SGD)

### Concepto

- **SGD** es una variante del método de descenso de gradiente.
- Utiliza un subconjunto (batch) de los datos en lugar del conjunto completo para actualizar los pesos, lo que hace que el proceso sea más rápido y menos intensivo en términos de memoria.

### Características

- **Tasa de Aprendizaje Fija**: La tasa de aprendizaje generalmente se establece de forma fija y no cambia durante el entrenamiento.
- **Actualización de Pesos**: Los pesos se actualizan en la dirección opuesta al gradiente de la función de pérdida.

### Ventajas y Desventajas

- **Simple y Efectivo**: En muchos casos, SGD funciona bien, especialmente con tasas de aprendizaje adecuadamente ajustadas.
- **Sensibilidad a la Tasa de Aprendizaje**: Puede ser sensible a la elección de la tasa de aprendizaje y a menudo requiere ajustes manuales.

## Adam (Adaptive Moment Estimation)

### Concepto

- **Adam** combina ideas de dos otros optimizadores: Momentum y RMSprop.
- Ajusta la tasa de aprendizaje durante el entrenamiento, lo que lo hace más flexible que el SGD tradicional.

### Características

- **Momentos de Primer y Segundo Orden**: Calcula las medias móviles del gradiente y el cuadrado del gradiente.
- **Tasa de Aprendizaje Adaptativa**: La tasa de aprendizaje se ajusta para cada parámetro.

### Ventajas y Desventajas

- **Eficiente y Efectivo en Práctica**: Adam suele funcionar bien en la práctica y requiere menos ajustes manuales que SGD.
- **Uso de Memoria**: Utiliza más memoria que SGD debido al almacenamiento de momentos para cada parámetro.