### WARING
### If you cannot start pod, please check below.
### https://qiita.com/hakatakinoco/items/6fbcfbc833aaecee3bea

APP_NAME=test-maker

cd ..
eval $(minikube docker-env)
docker build -t $APP_NAME:v1 .

minikube start

(
    kubectl create namespace $APP_NAME

    # Create secret
    kubectl create secret generic my-env-file-secret --from-env-file=./.env --namespace=$APP_NAME
    kubectl describe secrets/my-env-file-secret --namespace=$APP_NAME
)

(
    cd k8s

    # Run k8s app
    kubectl apply -f test-maker-pod.yaml --namespace=$APP_NAME
    # kubectl apply -f test-maker-psql-service.yaml --namespace=$APP_NAME
    kubectl apply -f test-maker-service.yaml --namespace=$APP_NAME
    kubectl expose deployment $APP_NAME --type=NodePort --port=5000 --namespace=$APP_NAME
)
(
    cd tools

    # Wait for running k8s.
    echo "Please wait for 15 seconds"
    sleep 15

    # Initialize RDB
    echo "Initailize RDB"
    # Allow permission
    chmod +x create_table.sh
    chmod +x insert_master_table.sh
    ./create_table.sh
    ./insert_master_table.sh

    # Set env data if exist
    if [ -e "env/insert_env_data.sh" ]; then
        echo "File exists."
        chmod +x env/insert_env_data.sh
        ./env/insert_env_data.sh
    fi

    # Open brower
    URL=`minikube service $APP_NAME --url --namespace=$APP_NAME`
    open $URL/testmaker/login

    # Wait for input
    read -p "Input if you want to end."
    # Delete
    kubectl delete service $APP_NAME --namespace=$APP_NAME
    kubectl delete deployment $APP_NAME --namespace=$APP_NAME
    kubectl delete namespace $APP_NAME
    # minikube stop
)

docker rmi -f `docker images | grep $APP_NAME:v1 | awk '{print $1}'`
