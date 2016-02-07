#Despliegue en Azure

En primer lugar instalo los plugin necesarios para que vagrant pueda conectarse con azure. Para ello ejecuto el comando `vagrant plugin install vagrant-azure`

![plugin vagrant azure](https://www.dropbox.com/s/4uvf6ayptn1lmyd/ejr8.1.png?dl=1)

Nos logeamos en azure con `azure login` y después ejecutamos el comando `azure account download` que nos dará un enlace que cuando abramos desde el navegador nos descargará un archivo

![descargando archivo de suscripción azure](https://www.dropbox.com/s/sm1v2mie3l913en/ejr8.2.png?dl=1)

Importo el archivo de suscripción que se me acaba de descargar con el comando `azure account import /media/psf/Google\ Drive/universidad/4INFORMATICA/DAI/Practicas/practica4/practica4MAC/Pase\ para\ Azure-1-17-2016-credentials.publishsettings`

![importado archivo de suscripción azure](https://www.dropbox.com/s/z619fddeduqups4/ejr8.3.png?dl=1)

Ahora voy a generar un certificado que tendré que subir a Azure para poder interaccionar con el más adelante. Este lo genero ejecutando los siguientes comandos: 

* `openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout ~/.ssh/azurevagrant.key -out ~/.ssh/azurevagrant.key`

* `chmod 600 ~/.ssh/azurevagrant.key`

* `openssl x509 -inform pem -in ~/.ssh/azurevagrant.key -outform der -out ~/.ssh/azurevagrant.cer`

Para subir el certificado tenemos que entrar en el [portal de azure](https://manage.windowsazure.com/) ir al menú "Setting" y a conticuación en la pestaña "Management certificates". Ahora pulsamos la opción "upload" y buscamos el certificado creado anteriormente 

![subo certificado a azure](https://www.dropbox.com/s/nkrbfh2b8uevvla/ejr8.4.png?dl=1)

![certificado subido](https://www.dropbox.com/s/8ahvbwb1oy2v6wz/ejr8.5.png?dl=1)

Ahora necesito un archivo .pem para autenticar la máquina de azure desde nuestro fichero Vagrantfile, para ello ejecutamos estos dos comandos:

* `openssl req -x509 -key ~/.ssh/id_rsa -nodes -days 365 -newkey rsa:2048 -out azurevagrant.pem` Generamos el archivo .pem `cat ~/.ssh/azurevagrant.key > ~/azurevagrant.pem` Concatenamos la clave primaria con el certificado en el archivo .pem

Ahora es el momento de crear mi archivo [Vagrantfile](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/Vagrantfile). 


En el archivo ansible_hosts tengo:


	[localhost]
	192.168.56.10


Y a continuación defino la variable de entorno necesaria para Ansible

`export ANSIBLE_HOSTS=/media/psf/Google\ Drive/universidad/4INFORMATICA/DAI/Practicas/practica4/practica4MAC/gestionpedidos_django/ansible_host`

Creo mi archivo [vagrant.yml](https://github.com/ignaciorecuerda/gestionpedidos_django/blob/master/vagrant.yml) con todos los comandos necesarios para preparar el entorno donde se ejecutará mi aplicación. 

Una vez tengo el archivo preparado creo una box con una imagen de azure con el siguiente comando:

`vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box`
Para eliminar la maquina: vagrant box remove azure

![añado box azure](https://www.dropbox.com/s/4bjx309j8cafc9q/ejr8.6.png?dl=1)


Ahora crearemos la máquina con el comando `vagrant up --provider=azure`

Si por el contrario ya tenemos la máquina creada y lo único que queremos es realizar el despliegue tendremos que usar el comando `vagrant provision`

![aplicación ejecutandose con ansible y vagrant](https://www.dropbox.com/s/8y1d1dw48xdlmgz/ejr8.7.png?dl=1)