[![Build Status](https://travis-ci.org/ignaciorecuerda/gestionpedidos_django.svg?branch=master)](https://travis-ci.org/ignaciorecuerda/gestionpedidos_django)

#Integración contínua con travis

Para empezar tenemos que registrarnos en la página desde el mismo git. Le damos permisos para que pueda acceder a nuestros proyectos de git y así lanzar la aplicación. Una vez hecho esto creo el fichero llamado [.travis.yml](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/.travis.yml) y lo añado a la carpeta raiz del repositorio.

Cada vez que haga un push a mi repositorio travis, de manera automática, hará de nuevo los test de la aplicación.

![travis](https://www.dropbox.com/s/ewlkdvw65xhne5x/travis.png?dl=1)