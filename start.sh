docker build --tag ambrosia-hades-api .
docker run --name ambrosia-hades-api -d -p 4000:5000 ambrosia-hades-api