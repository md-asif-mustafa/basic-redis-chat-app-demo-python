# Use the official Node.js image
FROM node:16 AS build

# Set the working directory
WORKDIR /app

# Copy package.json and yarn.lock
COPY package.json yarn.lock ./

# Install dependencies using Yarn
RUN yarn install

# Copy the rest of the application code
COPY . .

# Build the React app
RUN yarn build

# Use the official Nginx image to serve the build
FROM nginx:alpine

# Copy the build artifacts from the build stage
COPY --from=build /app/build /usr/share/nginx/html

# Expose port 80 for Nginx
EXPOSE 80

# Default command to run Nginx
CMD ["nginx", "-g", "daemon off;"]
