
Los Modelos de Lenguaje (LM) son modelos estadísticos o de aprendizaje profundo que calculan la probabilidad de secuencias de palabras en un idioma. Son fundamentales en muchas tareas de procesamiento del lenguaje natural (NLP).

![[Pasted image 20231202155334.png]]

![[Pasted image 20231202155402.png]]

## Propósito de los Modelos de Lenguaje

- **Generación de Texto**: Producir texto coherente y contextualmente relevante.
- **Estimación de Probabilidad**: Determinar la probabilidad de una secuencia de palabras o la siguiente palabra en una secuencia.
- **Entendimiento del Contexto**: Captar el significado contextual de las palabras dentro de una frase.

## Tipos de Modelos de Lenguaje

### Modelos Estadísticos
- **N-gramas**: Modelos simples basados en la frecuencia y proximidad de grupos de n palabras.
  ![[Pasted image 20231202155508.png]]
  ![[Pasted image 20231202155538.png]]
  ![[Pasted image 20231202155554.png]]
- **Modelos Ocultos de Markov (HMM)**: Modelos basados en estados y transiciones para secuencias de texto.

### Modelos Neuronales
- **RNNs (Redes Neuronales Recurrentes)**: Modelos secuenciales para manejar dependencias a largo plazo. ver [[Redes Neuronales Recurrentes (RNN)]]
- **LSTM/GRU (Long Short-Term Memory/Gated Recurrent Units)**: Variantes de RNN diseñadas para recordar información a lo largo de intervalos de tiempo más largos.
- **Transformers**: Arquitecturas basadas en atención que capturan contextos globales y relaciones entre palabras en secuencias largas. ver [[Transformers]]

## Modelos de Lenguaje Preentrenados
- **BERT (Bidirectional Encoder Representations from Transformers)**: Entiende el contexto en ambas direcciones (izquierda-derecha y derecha-izquierda).
- **GPT (Generative Pretrained Transformer)**: Modelo autoregresivo que predice la siguiente palabra en una secuencia.
- **XLNet, RoBERTa, T5**: Mejoras y variaciones de modelos basados en Transformers para tareas específicas.

## Aplicaciones de Modelos de Lenguaje

- **Traducción Automática**: Traducir texto de un idioma a otro.
- **Autocompletado y Predicción de Texto**: Sugerir la siguiente palabra o completar frases en interfaces de usuario.
- **Reconocimiento de Voz**: Convertir señales de audio en texto escrito.
- **Análisis de Sentimientos**: Determinar la polaridad del sentimiento en el texto.
- **Generación de Respuestas**: Usados en chatbots y asistentes virtuales para generar respuestas.

## Desafíos en Modelos de Lenguaje

- **Ambigüedad Lingüística**: Diferentes significados de palabras o frases en contextos variados.
- **Requerimiento de Gran Cantidad de Datos**: Los modelos neuronales, especialmente los Transformers, requieren grandes datasets para entrenamiento.
- **Sesgos en el Modelo**: Los modelos pueden perpetuar o amplificar sesgos presentes en los datos de entrenamiento.

Los Modelos de Lenguaje son una parte integral del avance en la inteligencia artificial, permitiendo que las máquinas procesen y generen lenguaje humano de manera más efectiva.
