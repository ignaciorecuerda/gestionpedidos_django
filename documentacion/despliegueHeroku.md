[![Heroku](https://www.herokucdn.com/deploy/button.png)](http://gestionpedidos.herokuapp.com/gestionpedidos/)


Para el despliegue en Herocu he tenido que modificar varias cosas para poder servir el contenido estático de mi aplicación. 
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