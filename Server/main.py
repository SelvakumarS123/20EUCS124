from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

sample_trains = [
    {
        "trainName": "Chennai Express",
        "trainNumber": "2344",
        "departureTime": {
            "Hours": 21,
            "Minutes": 35,
            "Seconds": 0
        },
        "seatsAvailable": {
            "sleeper": 3,
            "AC": 1
        },
        "price": {
            "sleeper": 2,
            "AC": 5
        },
        "delayedBy": 15
    },
    {
        "trainName": "Hyderabad Express",
        "trainNumber": "2341",
        "departureTime": {
            "Hours": 23,
            "Minutes": 55,
            "Seconds": 0
        },
        "seatsAvailable": {
            "sleeper": 6,
            "AC": 7
        },
        "price": {
            "sleeper": 554,
            "AC": 1854
        },
        "delayedBy": 5
    },
    {
        "trainName": "Delhi Door Hai Express",
        "trainNumber": "2345",
        "departureTime": {
            "Hours": 9,
            "Minutes": 45,
            "Seconds": 0
        },
        "seatsAvailable": {
            "sleeper": 32,
            "AC": 1
        },
        "price": {
            "sleeper": 1,
            "AC": 723
        },
        "delayedBy": 3
    }
]

@app.get("/trains", response_model=List[dict])
async def get_all_trains():
    return sample_trains

@app.get("/trains/{train_number}", response_model=dict)
async def get_train_by_number(train_number: str):
    train = next((t for t in sample_trains if t["trainNumber"] == train_number), None)
    if train is None:
        return JSONResponse(content={"message": "Train not found"}, status_code=404)
    return train



