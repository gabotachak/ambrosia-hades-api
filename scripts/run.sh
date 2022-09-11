docker run --name ambrosia-hades-api -p 4000:5000 ambrosia-hades-api
docker run --name ambrosia-hades-db -p 3308:3306 -e MYSQL_ROOT_PASSWORD=ambrosia -d mysql
