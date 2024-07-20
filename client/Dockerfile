# Use an official Node.js runtime as a parent image
FROM node:18 # Consider using a more recent LTS version

# Set the working directory
WORKDIR /app

# Copy package.json and yarn.lock
COPY package.json yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the application code
COPY . .

# Build the client application
RUN yarn build

# Install serve globally
RUN yarn global add serve

# Expose the port that the app runs on
EXPOSE 3000

# Command to serve the built application
CMD ["serve", "-s", "build"]
