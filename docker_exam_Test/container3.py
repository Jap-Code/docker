import os
import requests
import json

api = "fastapi"
port = "8000"

#sentences = ["life is beautiful", "that sucks"]

with open('sentences.json', 'r') as f:
    sentences = json.load(f)

with open('/app/logs/authorised.json', 'r') as f:
    authorised = json.load(f)

for nr, sentence in sentences.items():
    for name, password in authorised.items():

        # requête
        rv1 = requests.get(
            url=f"http://{api}:{port}/v1/sentiment?username={name}&password={password}&sentence={sentence}" 
        )

        rv2 = requests.get(
            url=f"http://{api}:{port}/v2/sentiment?username={name}&password={password}&sentence={sentence}"
        )

        output = '''
        ============================
                Content test
        ============================
        request done at "v1 and v2"
        | username = {name}
        | sentence = {sentence}
        | score V1 = {scoreV1}
        | score V2 = {scoreV2}
        ============================

        '''
        logPath = "/app/logs/api_test.log"

        scoreV1 = rv1.json()["score"]
        scoreV2 = rv2.json()["score"]

        print(output.format(name=name, sentence=sentence, scoreV1=scoreV1, scoreV2=scoreV2))

        with open(logPath, 'a') as file:
            file.write(output.format(name=name, sentence=sentence, scoreV1=scoreV1, scoreV2=scoreV2))

