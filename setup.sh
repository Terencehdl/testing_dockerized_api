#!/bin/bash
# Définir le chemin de logs en fonction du système d'exploitation
if [[ "$OSTYPE" == "msys" ]]; then
    LOGS_PATH="$(pwd)/logs"
else
    LOGS_PATH="/home/terenceh/Documents/Datascientest-Devops/Docker/examHilderal/app/logs"  # Remplacez par le chemin correct sur votre machine
fi

export LOGS_PATH
# Script de configuration pour la construction d'images et le lancement des conteneurs
# Attention a bien lancer ce script dans le dossier du projet
sudo docker pull datascientest/fastapi:1.0.0

# Construire les images individuellement en fonction du dossier dans lequel se trouve les fichiers de configuration
echo "Construction des images..."
sudo docker build -t authentication_image:latest ./authentication
sudo docker build -t authorization_image:latest ./authorization
sudo docker build -t content_image:latest ./content

# Afficher un message lorsque la construction des images est terminée
echo "Construction des images terminée."

# Lancer les conteneurs en arrière-plan
echo "Lancement des conteneurs..."
sudo docker compose up 

# Afficher un message lorsque le lancement des conteneurs est terminé
echo "Lancement des conteneurs terminé."
