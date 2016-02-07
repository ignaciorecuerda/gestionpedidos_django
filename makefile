docker:
	sudo apt-get update
	sudo apt-get install -y docker.io
	sudo docker pull ignaciorecuerda2/gestionpedidos_django
	sudo docker run -t -i ignaciorecuerda2/gestionpedidos_django  /bin/bash

crearMaquina:
	sudo apt-get install nodejs-legacy
	sudo apt-get install npm
	sudo npm install -g azure-cli
	sudo pip install paramiko PyYAML jinja2 httplib2 ansible
	sudo dpkg -i vagrant_1.8.1_x86_64.deb
	vagrant plugin install vagrant-azure

azure:
	sudo vagrant provision
	fab -H vagrant@gestion-pedidos-service-ruwzh.cloudapp.net lanzar_app_azure

test:
	python manage.py test

run:
	sudo python manage.py runserver 0.0.0.0:80