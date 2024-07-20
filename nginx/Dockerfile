#FROM nginx:alpine
#COPY nginx.conf /etc/nginx/conf.d/default.conf


# Use the official Nginx image from Docker Hub
FROM nginx:alpine

# Copy the custom Nginx configuration file
COPY nginx.conf /etc/nginx/nginx.conf
CMD ["nginx", "-g", "daemon off;"]


# Expose port 80 for Nginx
EXPOSE 80
