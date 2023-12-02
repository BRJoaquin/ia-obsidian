## Función del Decoder
- **Inicialización**: El estado oculto del decoder se inicializa con los valores finales del [[Encoder|encoder]], proporcionando el contexto necesario para generar la salida.
- **Generación de Secuencias**: El decoder traduce el vector de contexto en una secuencia de salida, palabra por palabra.

![[Pasted image 20231202164534.png]]
## Proceso Durante el Entrenamiento
- **Input con SOS**: Al comienzo de la secuencia, el decoder recibe un token especial de inicio de secuencia (SOS).
- **Observación y Predicción**: En cada paso, el decoder observa el contexto y la palabra anterior para predecir la siguiente palabra.
- **Solución a Secuencias de Distintos Largos**: Este método permite al decoder manejar secuencias de salida de diferentes longitudes.

## Proceso Durante la Inferencia
- **Inicio con SOS**: El decoder comienza con el token de SOS.
- **Autoregresión**: Utiliza sus propias predicciones (outputs) como entrada para el siguiente paso temporal.
- **Finalización con EOS**: Continúa generando palabras hasta que produce un token de fin de secuencia (EOS) o alcanza un límite de longitud predefinido.

## Diagrama del Decoder Durante el Entrenamiento

![[Pasted image 20231202164604.png]]

- **Secuencia de Salida**: Ejemplo con la frase "the cat is black" y el token de EOS al final.
- **Vector de Contexto**: El contexto proviene del encoder y se usa para cada paso de predicción.
- **Transformación de Tokens a Salida**:
  - **Input**: El decoder recibe el token actual y el estado oculto previo.
  - **Embedding y Relu**: Transforma el token en un vector denso y aplica una función de activación (ReLU).
  - **GRU**: La unidad recurrente (GRU) procesa el input y actualiza el estado oculto.
  - **Softmax**: La capa de salida aplica softmax para obtener una distribución de probabilidad sobre el vocabulario.
  - **Predicción de la Palabra Siguiente**: Selecciona el token con la mayor probabilidad como la siguiente palabra.

## Importancia del Decoder
- **Generación Coherente**: La habilidad del decoder para generar una secuencia coherente y relevante es esencial para la efectividad del modelo Seq2Seq.
- **Interacción con el Contexto**: Debe ser capaz de interpretar correctamente el vector de contexto proporcionado por el encoder.

## Conclusiones
- **Interdependencia Encoder-Decoder**: El éxito de la decodificación está directamente vinculado a la calidad del contexto proporcionado por el encoder.
- **Adaptabilidad**: La estructura del decoder permite que sea entrenado y utilizado en una variedad de tareas de generación de lenguaje.

