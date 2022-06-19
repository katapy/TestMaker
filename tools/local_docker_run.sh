
cd ..

CONTAINER_NAME="test-maker"

docker build -t $CONTAINER_NAME .
docker run -p 5000:5000 -it $CONTAINER_NAME

# Delete continer & image after test
docker rm -f `docker ps -a | grep $CONTAINER_NAME | awk '{print $1}'`
docker rmi -f `docker images | grep $CONTAINER_NAME | awk '{print $1}'`
