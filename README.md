# Organizador de eventos

- Para abrir el programa simplemente ejecutar el fichero vPrincipal.
- Para ver al documentacion ejecutamos el archivo index.html de la carpeta html.
- Para ver el informe generado con el programa se ejecuta el archivo informe.pdf de la carpeta informes.

La nueva versión del programa contiene un menú para dar acceso más directo a algunas acciones importantes. Además se han insertado algunos iconos para ayudar a realizar ciertas acciones. También se ha dispuesto más espaciado entre los elementos de la interfaz.

Se ha hecho la interfaz más intuitiva a la hora de crear, modificar, eliminar o consultar algún dato de la base de datos, como por ejemplo los empleados de un evento. Cada vez que realicemos una de esas acciones se muestra un mensaje de validado. También es fácil identificar los botones y la función que realizan.

Además, el número de acciones que se deben realizar para conseguir lo que se pretende son los mínimos y están muy claros.

Los colores que se han definido para el programa son claros y no realizan una carga visual excesiva.

La estructura general del programa está organizada como la mayoría de programas de este estilo, por ello es fácil entender el esquema que se debe seguir para realizar distintas operaciones pues al no incluir nada innovador el manejo del programa es más directo ya que se conoce un esquema similar de antemano.

##Pruebas de software

**Probar crear un nuevo evento.** Al pulsar el botón de nuevo evento se genera una ventana para introducir los datos del evento. No hay control del tipo de dato que se introduce, de modo que podríamos introducir un texto dentro del campo fecha. Además una vez creado el evento tenemos que abrir otra vez el programa para que se muestren los datos nuevos. Nos muestra un mensaje de información.

**Probar visualizar datos del evento.** Al pulsar el botón del evento que queremos consultar nos aparecen los datos de dicho evento. Sin embargo también aparece una lista con los eventos existentes, esto es redundante ya que esta información aparece en la ventana anterior y no tiene ninguna utilidad en la ventana de un evento.

**Probar botón consultar.** No encuentra los datos introducidos. La consulta de la base de datos es erronea.

**Probar botón crear del evento.** Se ha creado un empleado nuevo en un evento. Se crea correctamente pero tenemos que volver a abrir la ventana para visualizar los datos. Nos muestra un mensaje de información.

**Probar botón editar del evento.** No funciona.

**Probar botón informe del evento.** Realiza un informe con los datos de la tabla seleccionada.

**Probar botón borrar.** Se borra el registros seleccionado y automáticamente se muestra en la tabla.

**Probar botón menú Organizador eventos.** Se muestra una pestaña para poder salir del programa.

**Probar botón evento del menú.** Podemos crear un nuevo evento.
