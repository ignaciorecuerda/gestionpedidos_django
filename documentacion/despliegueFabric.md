#Despliegue automático con Fabric

Para subir la aplicación de manera automática a mi máquina creada en azure he usado Fabric. 

Para ello en primer lugar he tenido que instalarlo con el comando: `sudo pip install fabric`

He creado el archivo que fabric usa para todo ello, este archivo es [fabfile.py](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/fabfile.py). En el se encuentran todas las ordenes a realizar. Para realizar estas ordenes hay que usar comandos como el siguiente:

`fab -H usuario@nombreMaquina metodo`

por ejemplo para descargarme la imagen de docker uso:

`fab -H vagrant@gestion-pedidos-service-ruwzh.cloudapp.net descargar_imagen_docker`

Una imagen de la aplicación corriendo en mi máquina de **azure** con el despliegue de docker:

![aplicacion](https://www.dropbox.com/s/0qjil56m7mpjsbv/despliegueFabric.png?dl=1)