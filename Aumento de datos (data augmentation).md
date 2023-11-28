## Definición y Propósito

Data Augmentation, o aumento de datos, es una técnica de [[Regularización|regularización]] que aumenta la diversidad de los datos de entrenamiento mediante la aplicación de transformaciones aleatorias pero realistas. Esta técnica ayuda a mejorar la generalización del modelo y a prevenir el [[Sobreajuste (Overfitting)]].

## Métodos de Data Augmentation

### 1. Transformaciones de Imagen
   - **Rotación**: Girar las imágenes en un rango de ángulos.
   - **Escalado**: Aumentar o disminuir el tamaño de las imágenes.
   - **Recorte**: Recortar partes de la imagen.
   - **Volteo Horizontal/Vertical**: Invertir imágenes horizontal o verticalmente.
   - **Ajustes de Color**: Modificar el brillo, el contraste o la saturación.

### 2. Transformaciones de Audio
   - **Ruido de Fondo**: Añadir sonidos ambientales o ruido.
   - **Cambio de Tono**: Ajustar el tono del audio.
   - **Estiramiento Temporal**: Cambiar la velocidad de reproducción sin alterar el tono.

### 3. Transformaciones de Texto
   - **Sinónimos**: Reemplazar palabras con sinónimos.
   - **Reordenamiento de Frases**: Cambiar el orden de las palabras o frases.

## Implementación en Keras (Ejemplo para Imágenes)

Keras proporciona herramientas para implementar data augmentation directamente en el flujo de entrenamiento.

```python
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Crear un generador con transformaciones específicas
data_gen = ImageDataGenerator(
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Aplicar el generador a los datos de entrenamiento
