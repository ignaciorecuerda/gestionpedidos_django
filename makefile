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