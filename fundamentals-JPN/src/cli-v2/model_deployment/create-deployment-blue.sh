deployment_flag=$(az ml online-deployment list --endpoint-name ftalive-demo --query "[].name | contains(@,'blue')")
if [ $deployment_flag == "true" ]; then
    az ml online-deployment delete --name blue --endpoint-name ftalive-demo --yes
else
    echo "Deployment ftalive-demo-blue doesn't exist."
fi
az ml online-deployment create --name blue --endpoint-name ftalive-demo -f blue-deployment.yml --all-traffic