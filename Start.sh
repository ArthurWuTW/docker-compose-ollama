docker-compose up --build --detach

echo "Sleep 5 sec"
sleep 5

docker-compose exec ollama-app /bin/sh -c "ollama pull llama3:8b-instruct-q8_0"

echo "Sleep 5 sec"
sleep 5

echo "Health test"
curl http://localhost:11434/api/generate -d '{"model": "llama3:8b-instruct-q8_0", "stream": false, "prompt": "hello"}'
