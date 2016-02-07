# Gestion de pedidos: Proyecto para Infraestructura Virtual

####Aplicación para llevar la gestión de clientes y pedidos 
####Realizado por: **Jose Ignacio Recuerda Cambil**

[![Build Status](https://travis-ci.org/ignaciorecuerda/gestionpedidos_django.svg?branch=master)](https://travis-ci.org/ignaciorecuerda/gestionpedidos_django)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://gestionpedidos.herokuapp.com/gestionpedidos/)

[![Docker](https://camo.githubusercontent.com/8a4737bc02fcfeb36a2d7cfb9d3e886e9baf37ad/687474703a2f2f693632382e70686f746f6275636b65742e636f6d2f616c62756d732f7575362f726f6d696c67696c646f2f646f636b657269636f6e5f7a7073776a3369667772772e706e67)](https://hub.docker.com/r/ignaciorecuerda2/gestionpedidos_django/)

[![Azure](https://camo.githubusercontent.com/0a0a0d99a96e23a0af8b612b45cf0e204080ad6c/68747470733a2f2f7777772e64726f70626f782e636f6d2f732f6f717572366b3730706f797363786a2f617a7572652e706e673f646c3d31)](http://gestion-pedidos-service-ruwzh.cloudapp.net/gestionpedidos/)

##Introducción

Con este proyecto se consigue la creación y aprovisionamiento de las máquinas de prueba y de producción. Se utilizará como PaaS (Heroku) y como IaaS (Azure).

La aplicación lleva un seguimiento de los clientes y de los pedidos de cada cliente. En la página inicial muestra una gráfica con el número de pedidos de todos los clientes que se encuentran en la base de datos. Se pueden dar de alta nuevos clientes rellenando un formulario con sus datos, y por otro lado, añadir pedidos individuales para cada uno de las clientes, introduciendo la fecha de compra, enlace del producto y el precio. 

**La aplicacion esta despegada en:**

* [Heroku (PaaS)](http://gestionpedidos.herokuapp.com/gestionpedidos/)

* [Azure (IaaS)](http://gestion-pedidos-service-ruwzh.cloudapp.net/gestionpedidos/)

##Herramientas usadas

* **Travis** (Integración continua)

* **Docker** (Entorno de pruebas)

* **Fabric** (Despliegue automático)

* **Vagrant** (Crear máquinas)

* **Ansible** (Aprovisionar máquinas)

* **Heroku** (PaaS)

* **Azure**(IaaS)

* **Sqlite** (Base de Datos) 

* **Django** (Aplicación)


##Integración continua

Para la integración continua de mi proyecto he usado **Travis**. Cada actualización que haga en el repositorio automáticamente travis se encargará de pasar los test para asegurarse que la aplicación funciona correctamente.

[Más detalle](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/documentacion/integracionContinua.md)


##Creando entorno de pruebas con Docker

Como entorno de pruebas voy a usar **Docker**. 

Docker es una plataforma que se encarga de automatizar el despliegue de aplicaciones en contenedores de software similares a donde se ejecutará, dando así la opción de probar la aplicación antes de que pase a producción.

La imagen de mi aplicación en Docker está en este [enlace](https://hub.docker.com/r/ignaciorecuerda2/gestionpedidos_django/)

[Más detalle](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/documentacion/documentacionDocker.md)


##Despliegue en el PaaS Heroku

He escogido el PaaS **Heroku**. Lo he escogido porque es muy sencillo de usar, ya que se puede enlazar directamente con un repositorio de gitHub y gestionar de una manera muy fácil con unos comandos de terminal.

[Más detalle](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/documentacion/despliegueHeroku.md)


##Despliegue automático con Fabric

Para automatizar el despliegue he hecho uso de la herramienta **Fabric** .
Con ayuda de Fabric puedo desplegar mi entorno de pruebas creado anteriormente con Docker, o el que comentaré a continuación con Ansible y Vagrant en Azure. 
Para todo esto he creado un archivo llamado [fabfile.py](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/fabfile.py) en el que defino ordenes paara automatizar.

[Más detalle](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/documentacion/despliegueFabric.md)

##Despliegue en el IaaS Azure

Para desplegar mi infraestructura he usado el IaaS de Azure, haciendo uso de una suscripción gratuita.

Para tener la aplicación funcionando en Azure con la ayuda de Vagrant y Ansible hay que ejecutar:

`make azure`

[Más detalle](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/documentacion/despliegueAzure.md)


#Comandos para usar este repositorio

##Para ejecutar los test

```
fab -H vagrant@gestion-pedidos-service-ruwzh.cloudapp.net ejecutar_tests
```

##Descargar repositorio

```
fab -H vagrant@gestion-pedidos-service-ruwzh.cloudapp.net descargar_repositorio
```

##Para aprovisionar la máquina de azure y lanzar la aplicacion

```
make azure
```
