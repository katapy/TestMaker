### WARING
### If you cannot start pod, please check below.
### https://qiita.com/hakatakinoco/items/6fbcfbc833aaecee3bea

APP_NAME=test-maker

cd ..

# Start minikube if it is not running.
(
    MINIKUBE_STATUS=`minikube status | grep host | awk '{print $2}'`
    echo "minikube host is $MINIKUBE_STATUS"
    if [ $MINIKUBE_STATUS != "Running" ]; then
        minikube start
    fi
)

eval $(minikube docker-env)

# Build docker.
(
    start_time=`date +%s`
    docker build -t $APP_NAME:v1 .
    end_time=`date +%s`
    echo "Docker build time: $((end_time - start_time))"
)

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

    # Allow permission
    chmod +x wait_db_connection.sh
    chmod +x create_table.sh
    chmod +x insert_master_table.sh

    # Waiting for connecting DB.
    ./wait_db_connection.sh

    # Initialize RDB
    echo "Initailize RDB"
    # Allow permission
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
