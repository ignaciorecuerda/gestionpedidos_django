docker:
	sudo apt-get update
	sudo apt-get install -y docker.io
	sudo docker pull ignaciorecuerda2/gestionpedidos_django
	sudo docker run -t -i ignaciorecuerda2/gestionpedidos_django  /bin/bash

azure:
	sudo vagrant provision

test:
	python manage.py test