endpoint_flag=$(az ml online-endpoint list --query "[].name | contains(@,'ftalive-demo')")
if [ $endpoint_flag == "true" ]; then
    az ml online-endpoint delete --name ftalive-demo --yes
else
    echo "Endpoint ftalivedemo doesn't exist."
fi
az ml online-endpoint create --name ftalive-demo