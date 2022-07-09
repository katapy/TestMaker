
APP_NAME=test-maker

POD_NAME=`kubectl get pod --namespace=$APP_NAME | grep $APP_NAME | awk '{print $1}'`
kubectl logs $POD_NAME -c $APP_NAME --namespace=$APP_NAME
