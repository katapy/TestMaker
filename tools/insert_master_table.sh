
APP_NAME=test-maker
POD_NAME=`kubectl get pod --namespace=$APP_NAME | grep $APP_NAME | awk '{print $1}'`

# Get Secret value
POSTGRES_DB=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_DB | awk '{print $2}' | base64 --decode`
POSTGRES_PASSWORD=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_PASSWORD | awk '{print $2}' | base64 --decode`
POSTGRES_USER=`kubectl get secret my-env-file-secret -o yaml | grep POSTGRES_USER | awk '{print $2}' | base64 --decode`

kubectl exec -i $POD_NAME -c postgres --namespace=$APP_NAME -- bash <<'EOC'
PSQL_URI="postgresql://localhost/$POSTGRES_DB?user=$POSTGRES_USER"
echo "Connect RDB"
psql $PSQL_URI

insert into table_header(
    table_name,
    column_name,
    display_name)
    values(
        'person',
        'id',
        'ID');

insert into table_header(
    table_name,
    column_name,
    display_name)
    values(
        'person',
        'name',
        'User name');

SELECT * FROM table_header;

EOC
