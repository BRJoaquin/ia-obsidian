
El desvanecimiento de gradiente (Gradient Vanishing) es un problema común que se puede encontrar en el entrenamiento de modelos profundos, especialmente cuando los modelos tienen muchos parámetros. El desvanecimiento de gradiente se produce cuando el gradiente de error de predicción se hace muy pequeño o negativo durante el entrenamiento, lo que impide al modelo aprender a minimizar el error de predicción.

El desvanecimiento de gradiente se produce por varias razones:

1. El gradiente se multiplica por una cantidad muy grande en cada capa del modelo. Este efecto se llama "múltiples de activación".
2. El gradiente se añade a un valor muy pequeño en cada capa del modelo, lo que se produce cuando el valor de los parámetros se hace demasiado grande o pequeño.
3. El gradiente se divide por un valor muy grande en cada capa del modelo, lo que se produce cuando el valor de los parámetros se hace mucho más pequeño que el valor de los inputs en cada capa del modelo.
4. El desvanecimiento de gradiente también puede producirse debido a la inversión del signo del gradiente durante la propagación de lasgradientes en el modelo.

️


<iframe width="560" height="315" src="https://www.youtube.com/embed/qO_NLVjD6zE?si=qM4lnKvPi1OCVzxg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>