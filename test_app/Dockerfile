FROM redhat/ubi9-minimal:9.5-1731604394

RUN microdnf -y install python3.11 python3.11-pip
RUN microdnf install -y gcc gcc-c++ python3.11-devel -y


RUN mkdir test_app
WORKDIR /test_app
COPY . /test_app

RUN pip3.11 install -U pip

RUN pip3.11 install -r requirements.txt --default-timeout=200

CMD [ "python3.11", "server.py" ]

