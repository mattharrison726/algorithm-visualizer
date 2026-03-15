# Stage 1: build the React app
FROM node:24-alpine AS builder

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci --silent

COPY public/ ./public/
COPY src/ ./src/
COPY tsconfig.json ./

RUN npm run build

# Stage 2: serve with nginx
FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
