# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Build the client application
RUN npm run build

# Serve the built application using a simple server
RUN npm install -g serve

# Expose the port that the app runs on
EXPOSE 3000

# Command to serve the built application
CMD ["serve", "-s", "build"]
