
![[Pasted image 20231202131939.jpg]]

Las Redes Generativas Adversarias (GANs, por sus siglas en inglés de Generative Adversarial Networks) son una clase de métodos de aprendizaje automático no supervisado, introducidos por Ian Goodfellow y sus colegas en 2014. Las GANs se componen de dos redes neuronales que se entrenan simultáneamente mediante un proceso competitivo.

## Componentes de una GAN

### Red Generadora (Generator)
- **Función**: Aprende a generar datos que imitan la distribución real de los datos de entrenamiento.
- **Objetivo**: Producir muestras indistinguibles de los datos reales.

### Red Discriminadora (Discriminator)
- **Función**: Evalúa las muestras recibidas y distingue entre las generadas artificialmente y las reales.
- **Objetivo**: Mejorar en la tarea de clasificar si una muestra es real o falsa.

## Entrenamiento de GANs

El entrenamiento de una GAN es un [[Juego de suma cero|juego de suma cero]] entre el generador y el discriminador:

1. **Generador**: Crea muestras.
2. **Discriminador**: Intenta clasificar si son reales o generadas.
3. **Retroalimentación**: El generador usa la retroalimentación del discriminador para mejorar su capacidad de generar muestras realistas.
4. **Convergencia**: Eventualmente, si la GAN está bien diseñada y entrenada adecuadamente, el generador produce muestras que el discriminador ya no puede diferenciar de los datos reales.

## Aplicaciones de GANs

- **Imagen**: Generación de imágenes realistas, superresolución, transferencia de estilo.
- **Texto**: Generación de texto plausible, traducción automática.
- **Audio**: Síntesis de voz, música.
- **Simulación**: Creación de entornos virtuales, modelos de simulación para entrenamiento de agentes de IA.

## Desafíos en el Entrenamiento de GANs

- **Modo de Colapso (Mode Collapse)**: Situación donde el generador produce un rango limitado de respuestas.
- **No Convergencia**: Las GANs pueden ser difíciles de entrenar debido a la dinámica compleja entre el generador y el discriminador.
- **Ajuste de Hiperparámetros**: Requiere una cuidadosa selección de hiperparámetros para estabilizar el entrenamiento.
