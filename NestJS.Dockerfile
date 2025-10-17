# Base image
FROM node:20 as build

ENV ENVIRONMENT 'production';

# Application Port
ARG PORT
ENV PORT=$PORT

# Create app directory
WORKDIR /app

# Copy the package json and yarn related files
COPY ./nestjs/barcode_scanner/yarn.lock  ./
COPY ./nestjs/barcode_scanner/package.json  ./

# Install app dependencies
RUN yarn install

# Bundle app source
COPY nestjs/barcode_scanner .

# Creates a "dist" folder with the production build
RUN yarn run build

FROM node:20-alpine as runtime

WORKDIR /dist

#COPY --from=build /app/dist/apps/barcode_scanner .
#COPY ./nestjs/barcode_scanner/yarn.lock  ./
#COPY ./nestjs/barcode_scanner/package.json  ./
#
#RUN yarn workspaces focus --production
#
#EXPOSE $PORT
## Start the server using the production build
#CMD [ "node", "main.js" ]
