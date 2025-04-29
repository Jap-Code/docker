
import os
import requests
import json

api = "fastapi"
port = "8000"

with open('/app/logs/authenticated.json', 'r') as f:
    authenticated = json.load(f)

authorised = {}

for name, password in authenticated.items():
    # requête
    rv1 = requests.get(
        url=f"http://{api}:{port}/v1/sentiment?username={name}&password={password}&sentence=stentence" 
    )

    rv2 = requests.get(
        url=f"http://{api}:{port}/v2/sentiment?username={name}&password={password}&sentence=stentence"
    )

    output = '''
    ============================
        Authorisation test
    ============================
    request done at "/sentinents"
    | username = {name}
    | v1 status = {v1_status_code}
    | v2 status = {v2_status_code}
    ============================
    '''

    logPath = "/app/logs/api_test.log"

    v1_status_code = rv1.status_code
    v2_status_code = rv2.status_code

    print(output.format(name=name, password=password, v1_status_code=v1_status_code, v2_status_code=v2_status_code))
    
    if os.environ.get('T2LOG') == '1':
        with open(logPath, 'a') as file:
            file.write(output.format(name=name, password=password, v1_status_code=v1_status_code, v2_status_code=v2_status_code))

    if v1_status_code == 200 and v2_status_code == 200:
        authorised.update({name: password})

with open('/app/logs/authorised.json', 'w') as aufile:
    json.dump(authorised, aufile, indent=4)
