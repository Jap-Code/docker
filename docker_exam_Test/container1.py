
import os
import requests
import json

api = "fastapi"
port = "8000"

with open('users.json', 'r') as f:
    userdict = json.load(f)

#userdict -> move to .env after test & COPY via Dockerfile
# userdict = {
#     "alice": "wonderland",
#     "bob": "builder",
#     "clementine": "mandarine"
# }

authenticated = {}

for name, password in userdict.items():
    # requête
    r = requests.get(
        url=f"http://{api}:{port}/permissions?username={name}&password={password}"   
    )

    output = '''
    ============================
        Authentication test
    ============================
    request done at "/permissions"
    | username = {name}
    | password = {password}
    expected result = 200
    actual result = {status_code}
    ==>  {test_status}
    ============================
    '''

    logPath = "/app/logs/api_test.log"
    envPath = "/app/logs/authenticated.json"

    status_code = r.status_code
    if status_code == 200:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'

    print(output.format(name=name, password=password, status_code=status_code, test_status=test_status))

    with open(logPath, 'a') as file:
        file.write(output.format(name=name, password=password, status_code=status_code, test_status=test_status))

    if test_status == 'SUCCESS':
        authenticated.update({name: password})
        
with open(envPath, 'w') as efile:
    json.dump(authenticated, efile, indent=4)