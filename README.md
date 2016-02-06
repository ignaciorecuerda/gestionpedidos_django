# gestionpedidos_django
aplicación de gestión de clientes y pedidos hecha con django

[![Build Status](https://travis-ci.org/ignaciorecuerda/gestionpedidos_django.svg?branch=master)](https://travis-ci.org/ignaciorecuerda/gestionpedidos_django)

[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://gestionpedidos.herokuapp.com/gestionpedidos/)

[![Docker](https://camo.githubusercontent.com/8a4737bc02fcfeb36a2d7cfb9d3e886e9baf37ad/687474703a2f2f693632382e70686f746f6275636b65742e636f6d2f616c62756d732f7575362f726f6d696c67696c646f2f646f636b657269636f6e5f7a7073776a3369667772772e706e67)](https://hub.docker.com/r/ignaciorecuerda2/gestionpedidos_django/)

[![Azure](https://camo.githubusercontent.com/0a0a0d99a96e23a0af8b612b45cf0e204080ad6c/68747470733a2f2f7777772e64726f70626f782e636f6d2f732f6f717572366b3730706f797363786a2f617a7572652e706e673f646c3d31)](http://gestion-pedidos-service-ruwzh.cloudapp.net/gestionpedidos/)

#Integración continua

Para la integración continua de mi proyecto he usado Travis.

[Más detalle]()


#Creando entorno de pruebas

Como entorno de pruebas voy a usar Docker. 

Docker es una plataforma que se encarga de automatizar el despliegue de aplicaciones en contenedores de software similares a donde se ejecutará, dando así la opción de probar la aplicación antes de que pase a producción.

La imagen de mi aplicación en Docker está en este [enlace](https://hub.docker.com/r/ignaciorecuerda2/gestionpedidos/)

Para crear el entrono de pruebas basta con ejecutar los siguientes comandos: 

* `make docker`
* `cd gestionPedidos`
* `make run`

[Más detalle](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/documentacion/documentacionDocker.md)


#Desplegando en el PaaS Heroku
He escogido el PaaS Heroku. Lo he escogido porque es muy sencillo de usar, ya que se puede enlazar directamente con un repositorio de gitHub y gestionar de una manera muy fácil con unos comandos de terminal.

[Más detalle](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/documentacion/despliegueHeroku.md)