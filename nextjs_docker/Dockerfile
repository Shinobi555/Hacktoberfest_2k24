FROM node:20-slim

COPY  package.json .

run npm install --only=production

COPY src/app src/app

CMD ["npm", "run","dev"]

