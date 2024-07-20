# Use Python37
FROM python:3.7

# Set the working directory
WORKDIR /app

# Copy requirements.txt to the docker image and install packages
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . /app

# Expose port 8080
EXPOSE 8080
ENV PORT 8080

# Run demo_data.py and then start the app with gunicorn
CMD ["sh", "-c", "python chat/demo_data.py && exec gunicorn --bind :$PORT --worker-class eventlet -w 1 chat.app:app"]
