FROM nginx:stable-alpine3.21-slim
COPY ./index.html /usr/share/nginx/html/index.html

EXPOSE 80

#nginx -g daemon off sorgt dafür, dass nginx nicht im Hintergrund läuft. Ansonsten stirbt der Container sofort
CMD ["nginx", "-g", "daemon off;"]





