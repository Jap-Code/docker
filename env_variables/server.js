const http = require('http');

const PORT = process.env.PORT || 3000;
const MESSAGE = process.env.MESSAGE || "Hallo Welt!";

const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end(`Message: ${MESSAGE}\n`);
});

server.listen(PORT, () => {
    console.log(`Server läuft auf Port ${PORT}`);
});
