# Use Alpine Linux as the base image
FROM alpine:latest

# Install Python3, pip3 and other dependencies
RUN apk add --update python3 py3-pip py3-dnspython py3-pysocks py3-validators py3-flask py3-flask-restx

# Copy the current directory contents into the container at /app
COPY . /app
WORKDIR /app

# Start the flask server
ENTRYPOINT ["python3"]
CMD ["server.py"]
