# Computes
az ml compute create -f ./compute/create-cluster.yml

# Data
az ml data create -f ./data/create-data.yml

# Envionrments
az ml environment create -f ./environment/create-environment.yml
az ml environment create -f ./environment/create-environment-inference.yml