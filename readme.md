### Clone

```
git clone https://github.com/it63070160/Week9.git
```

### build FastAPI Docker image with docker build 
```
- cd Week9
- docker build -t fastapi-docker_lab5 .
```
### build Frontend Docker image with docker build 
```
- cd Week9/frontend
- docker build -t flask-docker-app .
```

### Run the Docker container by executing the following command:
```
docker run -p 8088:80 fastapi-docker_lab5 
docker run -p 8081:8081 -d --name container_building.jpg  -e APP_COLOR=building.jpg flask-docker-app
```
