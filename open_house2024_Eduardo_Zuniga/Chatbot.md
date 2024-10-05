- Funcionalidad principal -< Core Loop
Esperar pregunta
Dar respuesta

- Requisitos Funcionales
Almacenar las respuestas
Almacenar las preguntas
Ciclar el menu


- Variables de Flujo
1. EntradaPregunta: string
2. EntradaMenu: int
3. EntradaMenuInterior: int
4. ProgramaRespuesta: string


- Flujo
1. Mostrar el menu
1.1. Menu de Preguntas sobre la especialidad 
1.2. Menu de Preguntas sobre las areas
1.3. Salir
2. Dar la instruccion al usuario
3. Recibir la entrada y verificar si la pregunta es valida
4: SI -> Responder pregunta
4: NO -> Devuelve que vuelva a formular la pregunta -> Volver al 3
5. Preguntar si el usuario quiere hacer otra pregunta
6: SI -> Devolverse al 3
6: NO -> Devolverse al 1


