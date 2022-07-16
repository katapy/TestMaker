
APP_NAME=test-maker
POD_NAME=`kubectl get pod --namespace=$APP_NAME | grep $APP_NAME | awk '{print $1}'`

# Get Secret value
POSTGRES_DB=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_DB | awk '{print $2}' | base64 --decode`
POSTGRES_PASSWORD=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_PASSWORD | awk '{print $2}' | base64 --decode`
POSTGRES_USER=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_USER | awk '{print $2}' | base64 --decode`

# Wait for running k8s pod.
POD_NAME=`kubectl get pod --namespace=$APP_NAME | grep $APP_NAME | awk '{print $1}'`
while true 
do
    POD_STATUS=`kubectl get pods --namespace=$APP_NAME | grep $POD_NAME | awk '{print $3}'`
    echo "Pod status is $POD_STATUS"
    [ $POD_STATUS == "Running" ] && break
    sleep 1
done

# Waiting for connecting DB.
kubectl exec -i $POD_NAME -c postgres --namespace=$APP_NAME -- bash <<'EOC'
PSQL_URI="postgresql://localhost/$POSTGRES_DB?user=$POSTGRES_USER"
while true 
do
    psql $PSQL_URI -c "\dt" 2>/dev/null
    [ $? -eq 0 ] && break # Break if exit code is 0.
    echo "Waiting for connect db."
    sleep 1
done
EOC

echo "Connected DB."
