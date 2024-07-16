# Use the official Redis image as a base image
FROM redis:latest

# Set the maintainer label (optional)
LABEL maintainer="your-email@example.com"

# Expose the default Redis port
EXPOSE 6379

# Copy the custom configuration file
COPY redis.conf /usr/local/etc/redis/redis.conf

# Start Redis server with the custom configuration
CMD ["redis-server", "/usr/local/etc/redis/redis.conf"]
