# before executing this shell sript, you have to configure environment variable `jobname` that created model to register.
export jobname=$jobname
echo $jobname
az ml model create -f ./register-model.yml -p "azureml://jobs/${jobname}/outputs/artifacts/paths/model" 