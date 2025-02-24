from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import socket
import time

app = FastAPI()

# Define the request body model
class FactorialRequest(BaseModel):
    number: int

# Helper function to calculate factorial
def calculate_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
            time.sleep(0.5)
        return result

# POST endpoint to calculate factorial
@app.post("/")
async def factorial(request: FactorialRequest):
    try:
        result = calculate_factorial(request.number)
        container_id  = socket.gethostname()
        return {"number": request.number, "factorial": result, "container_name":  container_id}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))