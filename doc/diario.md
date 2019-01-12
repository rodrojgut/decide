# Diario del grupo Decide-Ortosia-Votación

En este documento se detalla el trabajo realizado por todos los integrantes del grupo Decide-Ortosia-Votación ordenado cronológicamente.

## Integrantes del grupo
* Lozano Pineda, José Ángel
* Pérez Llorente, Ángel
* Sánchez Montiel, José Luis
* Valero García, Luis

## Descripción cronológica
* 25 de octubre
  * *30 minutos* - **Ángel Pérez Llorente** contacta con todos los grupos para la creación de un grupo de Whatsapp con los mánager de cada módulo.
* 16 de noviembre
  * *6 horas* - **Ángel Pérez Llorente** crea, configura y sube una máquina virtual de Ubuntu para que todo el grupo trabaje con la misma configuración. Además, incluye un tutorial de cómo desplegar el proyecto.
* 17 de noviembre
  * *30 minutos* - **Ángel Pérez Llorente** descarga el proyecto del repositorio y realiza la configuración inicial.
  * *2 horas* - **Luis Valero García** toma el primer contacto con la máquina virtual para familiarse con ella.
  * *1 hora* - **José Ángel Lozano Pineda** configura el proyecto en la máquina virtual.
* 18 de noviembre
  * *2 horas* - **Ángel Pérez Llorente** toma el primer contacto con el proyecto para familiarizarse con el entorno de Decide.
* 19 de noviembre
  * *2 horas* - **Luis Valero García** toma el primer contacto con el uso de la plataforma Git a través de comandos por terminal.
  * *5 horas* - **José Ángel Lozano Pineda** toma el primer contacto con el proyecto para familiarizarse con el entorno de Decide.
* 20 de noviembre
  * *30 minutos* - **Luis Valero García** realiza la primera versión del archivo travis.yml.
* 21 de noviembre
  * *30 minutos* - **Luis Valero García** analiza el proyecto de decide para proponer mejoras en nuestro módulo.
* 23 de noviembre
  * *2 horas* - **Todos los integrantes de este grupo** tienen una reunión para preparar el repositorio propio, la gestión de incidencias y definir los cambios a implementar.
  * *30 minutos* - **Ángel Pérez Llorente** y **José Luis Sánchez Montiel** tienen una reunión con el resto de grupos para definir la gestión del código y de las incidencias.
* 26 de noviembre
  * *2 horas* - **Todos los integrantes de este grupo** tienen una reunión para preparar el Milestone 1.
  * *2 horas* - **Ángel Pérez Llorente** reinicia el módulo de votación por incongruencias en las modificaciones realizadas en el modelado, avanza en sus funcionalidades e integra la funcionalidad de preguntas por peso solicitada por el grupo de postprocesado.
* 27 de noviembre
  * *2 horas* - **Todos los integrantes de este grupo** tienen una reunión para analizar la revisión del Milestone 1 y aplicar los cambios sugeridos.
* 28 de noviembre
  * *30 minutos* - **José Ángel Lozano Pineda** crea la rama ortosia-votacion-develop.
* 7 de diciembre
  * *1 hora* - **Luis Valero García** toma el primer contacto con el código del módulo votación para implementar la funcionalidad de soportar varias preguntas en una votación.
* 11 de diciembre
  * *2 horas* - **Ángel Pérez Llorente** investiga sobre Heroku y configura el proyecto para desplegar la rama del módulo de este grupo.
  * *30 minutos* - **Luis Valero García** avanza en la funcionalidad de soportar varias preguntas en una votación.
* 12 de diciembre
  * *2 horas* - **José Ángel Lozano Pineda** empieza a implementar la funcionalidad de votaciones con importancia.
  * *30 minutos* - **Luis Valero García** crea el formulario para crear votaciones con varias preguntas.
  * *2 horas* - **Luis Valero García** tiene una reunión con el grupo de cabina para tratar posibles modificaciones que se puedieran realizar entre ambos módulos.
* 13 de diciembre
  * *4 horas* - **Luis Valero García** concluye la funcionalidad de votaciones con varias preguntas.
* 14 de diciembre
  * *3 horas* - **Ángel Pérez Llorente** investiga sobre errores de persistencia en la base de datos, lo corrige e informa al resto de integrantes de este grupo sobre cómo resolverlo.
* 14 de diciembre
  * *4 horas* - **José Ángel Lozano Pineda** investiga sobre errores de persistencia en la base de datos.
* 17 de diciembre
  * *30 minutos* - **José Ángel Lozano Pineda** realiza un merge de la rama votacion-develop con la rama master de este módulo.
  * *1 hora* - **José Ángel Lozano Pineda** modifica el archivo .gitignore para evitar conflictos de persistencia en la base de datos.
  * *5 horas* - **Ángel Pérez Llorente** investiga sobre errores de persistencia que vuelven a aparecer. Investiga comandos de django y postgres para resolverlo. Una vez solucionado, informa al resto de integrantes de este grupo para que no suban al repositorio archivos relacionados con las migraciones de la base de datos.
  * *30 minutos* - **Ángel Pérez Llorente** continúa con la funcionalidad de crear preguntas relacionadas con opciones de preguntas anteriores y realiza un merge de la rama ortosia-votacion-develop a ortosia-votacion.
* 18 de diciembre
  * *3 horas* - **José Ángel Lozano Pineda** reinstala y configura la máquina virtual debido a errores con la misma.
  * *5 horas* - **Ángel Pérez Llorente** investiga sobre cómo referenciar en un formulario de un objeto con dos *foreign key* hacia una misma tabla a causa de un error en django. Además, finaliza la funcionalidad de crear preguntas relacionadas con opciones de preguntas anteriores.
* 19 de diciembre
  * *2 horas* - **José Ángel Lozano Pineda** añade la fecha inicial en la creación de una votación.
  * *3 horas* - **Ángel Pérez Llorente** investiga sobre cómo ejecutar los tests debido a un error de permisos en la base de datos de pruebas. Además, arregla los tests adaptándolos a las nuevas funcionalidades.
  * *3 horas* - **Ángel Pérez Llorente** investiga fallo en el fichero travis.yml y lo arregla para la rama ortosia-votacion-develop.
  * *1 hora* - **Luis Valero García** modifica el archivo tests.py para arreglar un error debido al cambio de multiplicidad entre los modelos de preguntas y votaciones.
  * *3 horas* - **Luis Valero García** modifica el archivo testvoting.py para probar los cambios realizados en el modelo por las nuevas implementaciones.
* 20 de diciembre
  * *12 horas* - **Ángel Pérez Llorente** investiga sobre cómo fusionar Heroku y Travis e introduce cambios para la automatización del despliegue en la rama ortosia-votacion.
  * *30 minutos* - **Todos los integrantes de este grupo** tienen una reunión para preparar el Milestone 2.
* 21 de diciembre
  * *1 hora* - **Ángel Pérez Llorente** realiza un merge y resuelve conflictos.
* 26 de diciembre
  * *2 horas* - **José Ángel Lozano Pineda** modifica los archivos de serializers y modelos para que sean coherentes entre sí.
  * *2 horas* - **Luis Valero García** investiga el despliegue en Heroku y Docker.
  * *4 horas* - **Luis Valero García** crea una guía de comandos y tutoriales para las distintas herramientas utilizadas a lo largo del proyecto.
* 27 de diciembre
  * *2 horas* - **José Ángel Lozano Pineda** crea los test para la API.
* 28 de diciembre
  * *3 horas* - **José Ángel Lozano Pineda** investiga el funcionamiento de la API y crea los métodos para la misma.
* 29 de diciembre
  * *2 horas* - **José Ángel Lozano Pineda** añade la petición a la API para crear votaciones de tipo referéndum con los tests correspondientes.
* 2 de enero
  * *1 hora* - **José Ángel Lozano Pineda** gestiona los errores en el método tally para que enviara un error en peticiones incorrectas.
  * *1 hora* - **José Ángel Lozano Pineda** tiene una reunión con el grupo del módulo mixnet.
* 4 de enero
  * *3 horas* - **Todos los integrantes de este grupo** tienen una reunión para estructurar una primera versión de la memoria colectiva del trabajo.
  * *4 horas* - **Ángel Pérez Llorente** crea una nueva rama llamada ortosia-votacion-prepro con una versión anterior de ortosia-votacion debido a numerosos errores y el rechazo del *pull request* a ortosia-prepro. En la nueva rama se realiza el *pull request*.
* 7 de enero
  * *4 horas* - **José Ángel Lozano Pineda** modifica el método tally para evitar que se pueda realizar tally dos veces en una misma votación.
* 10 de enero
  * *3 horas* - **José Ángel Lozano Pineda** realiza un control de excepciones para los fallos en las peticiones de la API de mixnet que fallaban al enviar votaciones con votos vacíos.
  * *30 minutos* - **José Ángel Lozano Pineda** tiene una reunión con el grupo del módulo mixnet.
  * *4 horas* - **Ángel Pérez Llorente** arregla un *warning* y realiza una funcionalidad solicitada por el módulo cabina para poder crear votaciones con múltiples preguntas con el método POST.
* 12 de enero
  * *6 horas* - **Todos los integrantes de este grupo** tienen una reunión para escribir la documentación del proyecto.
 