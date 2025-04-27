FROM node:20-alpine3.21.3

WORKDIR /server/

COPY server.js .

EXPOSE 3000

CMD ["node", "server.js", "--host", "0.0.0.0", "--port", "3000"]
