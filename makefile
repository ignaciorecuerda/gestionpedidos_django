docker:
	sudo apt-get update
	sudo apt-get install -y docker.io
	sudo docker pull ignaciorecuerda2/gestionpedidos_django
	sudo docker run -t -i ignaciorecuerda2/gestionpedidos_django  /bin/bash

azure:
	# sudo apt-get update
	# sudo apt-get install -y vagrant
	# sudo apt-get install -y npm
	# sudo npm install -g azure-cli
	# sudo apt-get install -y ruby-dev
	# sudo apt-get install make
	vagrant plugin install vagrant-azure
	sudo vagrant up 
	sudo vagrant provision

test:
	python manage.py test