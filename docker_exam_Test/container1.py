
import os
import requests

print("container1 startet..")

# Request an API
r = requests.get(
    url='http://fastapi:8000/permissions?username=alice&password=wonderland'
)

# Text-Template für die Ausgabe
output = '''
============================
    Authentication test
============================
request done at "/permissions"
| username="alice"
| password="wonderland"
expected result = 200
actual result = {status_code}
==>  {test_status}
'''

# Pfad zur Log-Datei
logPath = "/app/logs/api_test.log"

# Statuscode und Teststatus ermitteln
status_code = r.status_code
if status_code == 200:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

# Ausgabe im Terminal
print(output.format(status_code=status_code, test_status=test_status))

# Ausgabe ins Log-File
with open(logPath, 'a') as file:
    file.write(output.format(status_code=status_code, test_status=test_status))
    file.write("\nthis is a test >>> it worked..\n")
