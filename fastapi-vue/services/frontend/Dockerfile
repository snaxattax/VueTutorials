FROM node:lts-alpine

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@5.0.6 -g
RUN mkdir -p node_modules/.cache && chmod -R 777 node_modules/.cache

COPY package.json .
COPY package-lock.json .
RUN npm install
RUN npm remove @vue/cli-plugin-eslint

CMD ["npm", "run", "serve"]