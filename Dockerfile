FROM ubuntu:latest

#Autor
MAINTAINER Jose Ignacio Recuerda Cambil <ignacio.recuerda@gmail.com>

#Actualizar
RUN sudo apt-get update

#Descargar aplicación 
RUN sudo apt-get install -y git
RUN sudo  git clone https://github.com/ignaciorecuerda/gestionPedidos.git

#Instalacíon software necesario
RUN sudo apt-get install -y python-setuptools
RUN sudo apt-get -y install python-dev
RUN sudo apt-get -y install build-essential
RUN sudo easy_install pip
RUN sudo pip install --upgrade pip

#Instalo dependencias
RUN ls
RUN cd gestionPedidos/ && sudo pip install -r requirements.txt