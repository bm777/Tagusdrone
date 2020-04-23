#!/bin/bash

echo "------ Intalling -> update and upgrade---------- "
#sudo apt-get update && sudo apt-get upgrade -y
echo "------ creating DIRECTORY -> .virt---------- "
mkdir .vir

echo "------ Intalling -> pip3 virtualenv virtualenvwrapper---------- "
sudo apt install python3-pip -y
pip install virtualenv
which virtualenv
pip install virtualenvwrapper
echo "------ Updating -> .bashrc---------- "

echo "#Virtualenvwrapper settings:
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export WORKON_HOME=$HOME/.virt
export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh" >> ~/.bashrc
source ~/.bashrc

echo "------ creating virtualenv wrapper -> virt---------- "
mkvirtualenv vir

workon vir

echo "------ Intalling -> flask---------- "
pip install flask
echo "------ VIRTUAL ENVIRONMENT -> DONE ---------- "
