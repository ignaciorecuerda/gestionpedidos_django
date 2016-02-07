docker:
	sudo apt-get update
	sudo apt-get install -y docker.io
	sudo docker pull ignaciorecuerda2/gestionpedidos_django
	sudo docker run -t -i ignaciorecuerda2/gestionpedidos_django  /bin/bash

azure:
	sudo vagrant provision
	fab -H vagrant@gestion-pedidos-service-ruwzh.cloudapp.net lanzar_app_azure

test:
	python manage.py test

run:
	sudo python manage.py runserver 0.0.0.0:80