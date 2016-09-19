FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y build-essential python-dev python-pip
COPY . /app
WORKDIR /app
RUN pip install pip --upgrade
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["server.py"]