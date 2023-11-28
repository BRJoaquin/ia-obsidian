  
El "pooling" es una técnica comúnmente utilizada en el procesamiento de imágenes, particularmente dentro de las redes neuronales convolucionales (CNNs). Su principal objetivo es reducir la dimensionalidad espacial (altura y ancho) de la representación de entrada, para disminuir la cantidad de parámetros y cálculos en la red, y por lo tanto, controlar el sobreajuste.

Hay varios métodos de pooling, pero los más comunes son el max pooling y el average pooling.

- **Max pooling**: Toma el valor máximo de la región de la imagen cubierta por el kernel de pooling. Por ejemplo, si el tamaño del kernel es 2x2, entonces para cada 2x2 sección de la imagen, el max pooling toma el valor máximo de esos 4 píxeles y lo utiliza para representar esa región en la próxima capa de la red.

- **Average pooling**: Toma el valor promedio de la región de la imagen cubierta por el kernel de pooling. Al igual que con el max pooling, si el tamaño del kernel es 2x2, entonces para cada 2x2 sección de la imagen, el average pooling calcula el promedio de esos 4 píxeles.

![[Pasted image 20230704092715.png]]

El proceso de pooling ayuda a hacer que la representación sea invariante a pequeñas traslaciones, lo que hace que la red sea más robusta a variaciones en la posición de las características en la imagen de entrada.

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZjM_XQa5s6s?si=UcWBazYCiFXb77Ku" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
