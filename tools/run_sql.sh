(
    cd ..
    cd sql

    if [ ! -e $1 ]; then
        echo "File does not exist."
        exit 0
    fi

    APP_NAME=test-maker
    POD_NAME=`kubectl get pod --namespace=$APP_NAME | grep $APP_NAME | awk '{print $1}'`

    # Get Secret value
    POSTGRES_DB=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_DB | awk '{print $2}' | base64 --decode`
    POSTGRES_PASSWORD=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_PASSWORD | awk '{print $2}' | base64 --decode`
    POSTGRES_USER=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_USER | awk '{print $2}' | base64 --decode`
    
    SQL_CODE=`cat $1`

    kubectl exec -i $POD_NAME -c postgres --namespace=$APP_NAME -- \
        psql postgresql://localhost/$POSTGRES_DB?user=$POSTGRES_USER -c "$SQL_CODE"
)
