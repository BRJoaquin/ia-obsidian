## Definición
La extracción de características (Feature Extraction) es un proceso fundamental en el campo de la [[Visión por Computadora|visión por computadora]]. Implica identificar y seleccionar las partes más relevantes de los datos visuales (como imágenes o secuencias de video) para su uso posterior en tareas de análisis como clasificación, detección y seguimiento de objetos.

## Tipos de Características

### Bajo Nivel
- **Bordes**: Contornos que definen la forma y estructura de los objetos en una imagen.
- **Esquinas**: Puntos en la imagen donde dos bordes se cruzan, indicando cambios significativos en la intensidad.
- **"Blobs"**: Regiones de la imagen que difieren en propiedades como intensidad o color con respecto a su entorno.
- **SIFT (Scale-Invariant Feature Transform)**: Algoritmo para detectar y describir características locales en imágenes. Las características detectadas son invariantes a escala y rotación.

### Alto Nivel
- **Thresholding (Umbralización)**: Proceso de segmentación de imágenes que separa los objetos del fondo mediante un umbral de intensidad.
- **Template Matching**: Técnica para encontrar áreas de una imagen que coinciden con una plantilla dada.
- **Hough Transform**: Método para la detección de formas geométricas simples como líneas, círculos y elipses.

#### Formas Detectadas por la Transformada de Hough
- **Líneas**: Identificación de líneas rectas en la imagen.
- **Círculos y Elipses**: Detección de formas curvas y su localización precisa.
- **Formas Generalizadas**: Extensión del método para detectar formas más complejas.

## Aplicaciones
- **Reconocimiento de patrones**: Identificar y clasificar patrones visuales.
- **Navegación de robots**: Interpretar el entorno visual para la navegación autónoma.
- **Interfaz hombre-máquina**: Facilitar la interacción con las computadoras mediante la interpretación de gestos o movimientos.
- **Seguridad y vigilancia**: Detección automática de actividades o entidades sospechosas.

# Links
https://distill.pub/2017/feature-visualization/
