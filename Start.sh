docker-compose up --build --detach

echo "Sleep 5 sec"
sleep 5

docker-compose exec ollama-app /bin/sh -c "ollama pull llama3:8b-instruct-q8_0"
