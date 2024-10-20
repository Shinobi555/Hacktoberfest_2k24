from node:20-slim

COPY  package.json .

RUN npm install --omit=dev

COPY /app .

CMD ["node","index.js"]