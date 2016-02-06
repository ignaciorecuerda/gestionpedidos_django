[![Docker](https://camo.githubusercontent.com/8a4737bc02fcfeb36a2d7cfb9d3e886e9baf37ad/687474703a2f2f693632382e70686f746f6275636b65742e636f6d2f616c62756d732f7575362f726f6d696c67696c646f2f646f636b657269636f6e5f7a7073776a3369667772772e706e67)](https://hub.docker.com/r/ignaciorecuerda2/gestionpedidos_django/)

#Docker

Para crear la imagen lo primero que tengo que hacer es crear el fichero [Dockerfile](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/Dockerfile)

Luego nos vamos a la web [Docker Hub](https://hub.docker.com) y nos registramos.
Pinchamos sobre "Create Automated Build" como se puede ver en la imagen para que nos cree los build automáticamente.

![Create Automated Build](https://www.dropbox.com/s/9dyf2ksjpz6mrkr/hito4.1.png?dl=1)

Damos permisos a Docker Hub para que pueda conectarse a nuestros repositorios de GitHub y así seleccionar el repositorio para el cual queramos crear la imagen.

Ahora docker se encarga de hacer una nueva build a partir del archivo [DockerFile](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/Dockerfile)

![Docker hub success](https://www.dropbox.com/s/d763qfkujfjzk4m/hito4.2.png?dl=1)

Docker Hub, ahora de manera automática, hará un nuevo build cada vez que realicemos algún cambio sobre nuestro código y ejecutemos un `git push`

Para crear el entrono de pruebas basta con ejecutar el comando: 

* `make docker`
* `cd gestionPedidos`
* Ejecutar `make run`

El comando `make docker` hace lo siguiente:

* Instala docker
* Descarga la imagen de de Docker Hub
* Ejecuta la imagen descargada

Solo hay que abrir nuestro navegador, introducir <ip del contenedor>:3000 y tendremos la aplicación ejecutandose.

Pongo una captura de la aplicación corriendo en el contenedor creado

![aplicación funcionando](https://www.dropbox.com/s/p3bbh1x7fqysbiy/ejr10.5.png?dl=1)
