APP_NAME=test-maker

cd ..
eval $(minikube docker-env)
docker build -t $APP_NAME:v1 .

(
    kubectl create namespace $APP_NAME

    # Create secret
    kubectl create secret generic my-env-file-secret --from-env-file=./.env --namespace=$APP_NAME
    kubectl describe secrets/my-env-file-secret --namespace=$APP_NAME
)

(
    cd k8s
    minikube start

    # Run k8s app
    kubectl apply -f test-maker-pod.yaml --namespace=$APP_NAME
    # kubectl apply -f test-maker-psql-service.yaml --namespace=$APP_NAME
    kubectl apply -f test-maker-service.yaml --namespace=$APP_NAME
    kubectl expose deployment $APP_NAME --type=NodePort --port=5000 --namespace=$APP_NAME
    
    # Open brower
    echo "Please wait 20 seconds"
    sleep 20
    URL=`minikube service $APP_NAME --url --namespace=$APP_NAME`
    open $URL/testmaker

    # Wait for input
    read -p "Input if you want to end."
    # Delete
    kubectl delete service $APP_NAME --namespace=$APP_NAME
    kubectl delete deployment $APP_NAME --namespace=$APP_NAME
    kubectl delete namespace $APP_NAME
    # minikube stop
)

docker rmi -f `docker images | grep $APP_NAME:v1 | awk '{print $1}'`
