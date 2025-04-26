FROM node:10-alpine

WORKDIR /server/

COPY server.js .

EXPOSE 3000

CDM ["node", "server.js", "--host", "0.0.0.0", "--port", "3000"]
