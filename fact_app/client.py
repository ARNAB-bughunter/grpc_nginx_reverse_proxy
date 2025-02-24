import json
import requests

headers = {
    "Content-Type": "application/json"
}

json_data = {"number":15}

print(requests.post(url="https://test.arnab.in/", data=json_data,verify="/home/user/workspace/my_test/grpc_nginx/grpc_nginx_reverse_proxy/server.crt"))

# print(requests.post(url="http://test.arnab.in/", json=json_data, headers=headers))