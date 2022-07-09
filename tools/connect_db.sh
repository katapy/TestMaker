
APP_NAME=test-maker

cd ..

(
    kubectl create namespace $APP_NAME

    # Create secret
    kubectl create secret generic my-env-file-secret --from-env-file=./.env --namespace=$APP_NAME
    kubectl describe secrets/my-env-file-secret --namespace=$APP_NAME
)

(
    cd k8s
    
    # Create DB
    kubectl apply -f psql.yaml --namespace=$APP_NAME

    # Get Secret value
    POSTGRES_DB=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_DB | awk '{print $2}' | base64 --decode`
    POSTGRES_PASSWORD=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_PASSWORD | awk '{print $2}' | base64 --decode`
    POSTGRES_USER=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_USER | awk '{print $2}' | base64 --decode`

    echo "Please wait 20 seconds"
    sleep 20

    URL=`minikube service postgresserver --url --namespace=$APP_NAME`
    echo "PSQL URL: $URL"
    # Connect DB
    psql "postgresql://${URL##*/}/$POSTGRES_DB?user=$POSTGRES_USER&password=$POSTGRES_PASSWORD"

    # Delete
    kubectl delete namespace $APP_NAME
)
