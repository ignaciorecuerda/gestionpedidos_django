# gestionpedidos_django
aplicación de gestión de clientes y pedidos hecha con django

[![Build Status](https://travis-ci.org/ignaciorecuerda/gestionpedidos_django.svg?branch=master)](https://travis-ci.org/ignaciorecuerda/gestionpedidos_django)


####################### poner introduccion a herocu con el enlace a la documentacion ######################


#Creando entorno de pruebas

Como entorno de pruebas voy a usar Docker. 

Docker es una plataforma que se encarga de automatizar el despliegue de aplicaciones en contenedores de software similares a donde se ejecutará, dando así la opción de probar la aplicación antes de que pase a producción.

La imagen de mi aplicación en Docker está en este [enlace](https://hub.docker.com/r/ignaciorecuerda2/gestionpedidos/)

Para crear el entrono de pruebas basta con ejecutar los siguientes comandos: 

* `make docker`
* `cd gestionPedidos`
* `make run`

[Más detalle](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/documentacion/documentacionDocker.md)