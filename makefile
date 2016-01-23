azure:
	sudo apt-get update
	sudo apt-get install -y vagrant
	sudo npm install -g azure-cli
	vagrant plugin install vagrant-azure
	sudo vagrant up --provider=azure