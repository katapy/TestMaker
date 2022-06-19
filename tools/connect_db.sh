
APP_NAME=test-maker

cd ..

(
    cd k8s
    kubectl create namespace $APP_NAME
    kubectl apply -f psql.yaml --namespace=$APP_NAME

    URL=`minikube service postgresserver --url --namespace=$APP_NAME`
    # Connect DB
    psql "postgresql://${URL##*/}/mydb?user=admin&password=P@ssw0rd"
)
