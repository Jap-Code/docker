#!/bin/bash

docker image build . -t js_server_response:latest

docker run --name my_server -p 3000:3000 -d --rm js_server_response:latest

echo "waiting for server to get out of bed.."
until curl -s http://localhost:3000 > /dev/null; do
	echo "Server is still not outa bed.."
	sleep 1
done

echo "there he is, let's go!"
curl -X GET -i http://localhost:3000

docker stop my_server
