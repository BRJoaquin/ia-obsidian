## Definición

El Pruning, o poda en español, es una técnica de optimización de modelos de redes neuronales. Su objetivo es reducir la complejidad del modelo eliminando pesos (conexiones neuronales) que tienen poco o ningún impacto en el rendimiento del modelo.

### Proceso de Pruning

- **Identificación de pesos no esenciales**: Se evalúan los pesos de las conexiones neuronales para determinar su importancia.
- **Eliminación de pesos**: Los pesos menos importantes (por ejemplo, aquellos cercanos a cero) se eliminan o se establecen en cero.
- **Re-entrenamiento**: Opcionalmente, el modelo puede ser re-entrenado para ajustar los pesos restantes y recuperar cualquier pérdida de rendimiento.

### Tipos de Pruning

1. **Pruning Estructural**: Elimina entidades estructurales completas como neuronas o capas.
2. **Pruning No Estructural**: Elimina pesos individuales, manteniendo la arquitectura original.

## Ventajas y Desventajas

### Ventajas

1. **Reducción del Tamaño del Modelo**: Menor uso de memoria y almacenamiento.
2. **Aumento de la Eficiencia**: Puede mejorar el tiempo de inferencia en dispositivos con recursos limitados.
3. **Regularización**: Ayuda a prevenir el [[Sobreajuste (Overfitting)|sobreajuste]] al eliminar conexiones redundantes.

### Desventajas

1. **Complejidad de Implementación**: Requiere un enfoque cuidadoso para no degradar el rendimiento del modelo.
2. **Posible Pérdida de Precisión**: Si se elimina demasiado, puede afectar negativamente la precisión del modelo.
3. **Dependencia de la Tarea**: El éxito del pruning puede variar según la tarea y la arquitectura del modelo.

## Aplicaciones

- **Dispositivos Móviles y Embebidos**: Ideal para modelos que deben ejecutarse en hardware con recursos limitados.
- **Optimización de Modelos Grandes**: Utilizado para hacer que grandes redes neuronales sean más manejables y eficientes.
- **Investigación en Eficiencia de Modelos**: Herramienta clave en la búsqueda de arquitecturas de red más eficientes y compactas.


![[Pasted image 20231128151912.png]]
