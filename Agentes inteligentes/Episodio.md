Se refiere a una **secuencia completa** de interacciones de un [[Agente]] con su [[Entorno]], desde un estado inicial hasta un estado terminal. (vease [[Estado]]) 

Un episodio se compone de una secuencia de pasos, en cada uno de los cuales el agente observa el estado actual, elige y realiza una acción, y luego recibe una recompensa y observa el nuevo estado. 

Al final de cada episodio, el agente puede actualizar sus estimaciones de la función de valor y/o de la política basándose en las recompensas que ha recibido y los estados y acciones que ha observado.

En contraste, en tareas continuas, no hay un concepto claro de episodio porque el agente continúa interactuando con el entorno indefinidamente.
