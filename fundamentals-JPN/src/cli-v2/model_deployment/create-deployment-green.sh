deployment_flag=$(az ml online-deployment list --endpoint-name ftalive-demo --query "[].name | contains(@,'green')")
if [ $deployment_flag == "true" ]; then
    az ml online-deployment delete --name green --endpoint-name ftalive-demo --yes
else
    echo "Deployment ftalive-demo-green doesn't exist."
fi
az ml online-deployment create --name green --endpoint-name ftalive-demo -f green-deployment.yml