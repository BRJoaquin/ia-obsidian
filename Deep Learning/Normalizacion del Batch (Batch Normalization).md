## Concepto y Función

Batch Normalization (BN) es una técnica utilizada en redes neuronales para estabilizar y acelerar el entrenamiento. Propuesta por Sergey Ioffe y Christian Szegedy en 2015, esta técnica normaliza las entradas de cada capa en un mini-batch, es decir, ajusta y escala las activaciones para mantener una distribución más consistente a lo largo de la red.

### Mecanismo Básico

1. **Normalización**: Cada mini-batch de entradas se normaliza para tener una media cercana a cero y una varianza de uno.
2. **Escalado y Desplazamiento**: Se introducen dos parámetros entrenables por capa, que permiten escalar y desplazar las activaciones normalizadas.

## ¿Es Batch Normalization una Técnica de Regularización?

Aunque el propósito principal de Batch Normalization es mejorar la estabilidad y velocidad del entrenamiento, también tiene efectos de regularización:

- **Reducción del Sobreajuste**: Al normalizar las activaciones en cada capa, BN puede reducir la necesidad de regularizadores como [[Dropout]].
- **Ruido Implícito**: Cada mini-batch tiene diferentes estadísticas, lo que introduce una forma de ruido en el entrenamiento y puede ayudar a prevenir el sobreajuste. ver [[Ruido (regularizacion)]]

## Beneficios de Batch Normalization

1. **Estabilidad del Entrenamiento**: Reduce problemas como el [[Desvanecimiento de gradiente|desvanecimiento]] y [[Gradiente Explosivo|explosión]] de gradientes.
2. **Permite Tasas de Aprendizaje Más Altas**: La normalización reduce la dependencia del gradiente en la escala de parámetros o su inicialización.
3. **Reduce la Necesidad de Inicialización Cuidadosa**: Al normalizar las activaciones, se atenúan los efectos de malas inicializaciones.
4. **Actúa como Regularizador**: Aunque no es su función principal, ayuda a reducir el sobreajuste.

## Aplicaciones y Limitaciones

- **Aplicaciones Amplias**: Muy utilizada en casi todo tipo de redes neuronales, especialmente en redes profundas.
- **Limitaciones en RNNs**: Su implementación en redes recurrentes es menos directa y puede ser menos efectiva.

## Implementación en Keras

En Keras, Batch Normalization se implementa fácilmente como una capa que se puede añadir a cualquier modelo secuencial o funcional.

```python
from tensorflow.keras.layers import BatchNormalization

# Ejemplo: Añadir Batch Normalization después de una capa densa
modelo.add(Dense(64, activation='relu'))
modelo.add(BatchNormalization())
```

En resumen, Batch Normalization es una técnica fundamental en el entrenamiento de redes neuronales modernas. No solo facilita y estabiliza el proceso de aprendizaje, sino que también ofrece beneficios de regularización, contribuyendo a la construcción de modelos más rápidos, estables y generalizables.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dXB-KQYkzNU?si=cqFVcJv2x8Coe_Oy" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
