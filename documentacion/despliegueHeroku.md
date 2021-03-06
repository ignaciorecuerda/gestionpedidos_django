[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://gestionpedidos.herokuapp.com/gestionpedidos/)

#Despliegue en Heroku

Los pasos que he seguido para tener la aplicación en Heroku son los siguientes:

* En primer lugar creo una aplicación en Heroku, esta aplicación la he llamado "gestionpedidos".
![Creando aplicacion en heroku](https://www.dropbox.com/s/fpm9tfrubpbq5ma/hito1.png?dl=1)

* Una vez creada me voy a la página web de Heroku y verifico que se ha creado correctamente mi aplicación. Podemos comprobarlo en la siguiente captura de pantalla

![verifico creacion app](https://www.dropbox.com/s/r1lrlm91vnhlqt0/hito3.png?dl=1)

* Añado el archivo [Procfile](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/Procfile) que contiene el comando `web: gunicorn tango_with_django_project.wsgi --log-file -` necesario para que Heroku sepa el comando para ejecutar la aplicación.

* Ya solo falta hacer un push de mi repositorio a heroku para subirla y que se lance automáticamente, para ello he usado el comando `git push heroku master`.

* Por último, me voy a la página de Heroku y dentro de la aplicación me voy al menú "Desploy" y selecciono "Enable Automatic Deploy" para que la aplicación se depliegue automáticamente al hacer push en el repositorio. También selecciono la casilla "Wait for CI to pass before deploy" para que pase los test antes de desplegarse (ya que tengo integración continua).

![Seleccionando despliegue automático](https://www.dropbox.com/s/196loe5m7so9l9b/hito6.png?dl=1)


#Sirviendo contenidos estáticos 

Para el despliegue en Heroku he tenido que modificar varias cosas para poder servir el contenido estático de mi aplicación. 
Hay que realizar los siguientes pasos:

* En primer lugar hay que instalar dj-static con el comando:

  * `pip install https://pypi.python.org/packages/source/d/dj-static/dj-static-0.0.6.tar.gz`. 

* En segundo lugar tenemos que añadir tanto dj-static como static3 a nuestro requirements.txt, en concreto las versiones que estoy usando son la 0.0.6 de dj-static y la 0.6.1 de static3 con lo cual añado las lineas:
  * `dj-static==0.0.6`

  * `static3==0.6.1`

* Modifico el archivo[settings.py](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/tango_with_django_project/settings.py) añadiendo lo siguiente:
  * `STATIC_ROOT = 'staticfiles'`

  * `STATIC_URL = '/static/'`

* Modifico el archivo [wsgi.py](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/tango_with_django_project/wsgi.py) de mi proyecto añadiendo lo siguiente: 
  * `from dj_static import Cling`

  * `application = Cling(get_wsgi_application())`

* Modifico mi archivo [base.html](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/templates/base.html)
  * En la primera linea pongo:
    
    * `{% load staticfiles %}`

  * En los link donde usaba la carpeta static los modifico añadiendo `{% static 'nombreDelArchivo' %}`

Una vez hecho esto puedo subir mi aplicación a Heroku y esta servirá los contenidos estáticos correctamente.

El enlace de mi aplicación en Heroku es: [GestionPedidos](http://gestionpedidos.herokuapp.com/gestionpedidos/)