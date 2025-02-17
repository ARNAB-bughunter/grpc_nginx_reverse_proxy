import grpc
from grpc_generated_file import test_pb2, test_pb2_grpc
import asyncio
import json


async def run():    
    data_str = "ARNAB NAHA"
    async with grpc.aio.insecure_channel("0.0.0.0:7000") as channel:
        stub = test_pb2_grpc.TestStub(channel)
        data = test_pb2.InputJson(data=data_str)
        response = await stub.Hello(data)
    return response.data


print(asyncio.run(run()))