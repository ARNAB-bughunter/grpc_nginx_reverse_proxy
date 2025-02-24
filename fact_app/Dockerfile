# FROM python:3.6-slim
# FROM redhat/ubi8:8.9-1028
FROM redhat/ubi9-minimal:9.4



RUN mkdir app
WORKDIR /app
COPY . /app

RUN microdnf -y install python3.11 python3.11-pip

RUN pip3.11 install --upgrade pip
RUN pip3.11 install -r requirements.txt --default-timeout=300


CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7001"]