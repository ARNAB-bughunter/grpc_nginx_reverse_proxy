# import json


# data =  json.load(open("86c9355b14714714879a06c69c6be080_raw.json"))

import grpc
import asyncio
from grpc_generated_file import test_pb2, test_pb2_grpc

class TestServicer(test_pb2_grpc.TestServicer):
    def Hello(self, request, context):
        response = test_pb2.OutputJson()
        print(f"DATA RECIVED::: {request.data}")
        response.data = "Hello " + request.data
        return response

async def serve():
  server = grpc.aio.server()
  test_pb2_grpc.add_TestServicer_to_server(TestServicer(),server)
  print("\nStarting server, Listing on port 50051...")
  server.add_insecure_port('[::]:50051')
  await server.start()
  await server.wait_for_termination()

if __name__ == "__main__":
   asyncio.run(serve())
