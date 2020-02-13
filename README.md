1. docker build -t spacecraftserver4flask:default .
2. docker run --name spacecraftserver4flask --publish 9000:9000 spacecraftserver4flask:default 

pip3 freeze > requirements.txt