El **Error de Generalización** es una medida de cómo de bien un [[Modelo (Hipotesis)]] de Machine Learning es capaz de realizar predicciones en nuevos datos, es decir, en datos que no se utilizaron durante el entrenamiento del modelo. 

En términos más formales, el error de generalización de un modelo es la expectativa de su error en una nueva muestra aleatoria de datos. Si consideramos un modelo de hipótesis $h$, una función de pérdida $L$ y una distribución de datos $D$, el error de generalización $E$ se define como:

$$\Large E(h) = E_{(x, y) \sim D}[L(h(x), y)]$$

En otras palabras, es el error promedio que esperaríamos ver si aplicáramos nuestro modelo a nuevos datos extraídos de la misma distribución que nuestros datos de entrenamiento.

Idealmente, queremos que nuestro modelo tenga un error de generalización bajo, lo que significa que es capaz de hacer predicciones precisas en datos nuevos y no vistos. Sin embargo, es importante mencionar que no podemos calcular el error de generalización directamente porque no tenemos acceso a la distribución de datos completa. En su lugar, a menudo estimamos el error de generalización utilizando técnicas como la validación cruzada o conjuntos de validación y pruebas separados.

# Ejemplo
![[Pasted image 20230707114423.png]]
![[Pasted image 20230707114336.png]]
![[Pasted image 20230707114356.png]]