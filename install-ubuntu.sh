#!/bin/zsh

if which python3 >/dev/null 2>&1 ; then
    echo "Python ya se encuentra instalado"
else 
    echo "Iniciando instalacion de python..."
    sudo apt-get -y install python3
fi

if which nmap >/dev/null 2>&1 ; then
    echo "Nmap ya se encuentra instalado"
else 
    echo "Iniciando instalacion de nmap..."
    sudo apt-get -y install nmap
fi

echo 'Instalando comandos necesarios...'

sudo cp Scripts/* /usr/local/bin

echo 'Definiendo los comandos...'

alias wnscan="/usr/local/bin/wnscan"
sudo chmod +x /usr/local/bin/wnscan