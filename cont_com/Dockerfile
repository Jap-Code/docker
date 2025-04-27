FROM python:3.12-slim

# Arbeitsverzeichnis
WORKDIR /

# Abhängigkeiten installieren
COPY requirements.txt .
RUN pip install -r requirements.txt

# Kopiere den gesamten Python-Code in das Arbeitsverzeichnis
COPY . .

# Befehl zum Starten des Skripts
CMD ["python", "container1.py"]  # Container1 starten, für andere Container ändern

