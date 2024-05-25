from fastapi import FastAPI, Request
from generic_helpers import intents_mapping


app = FastAPI()

@app.post("/")
async def QuestionRequest(request:Request):
    payload = await request.json()
    intent = payload['queryResult']['intent']['displayName']
    return intents_mapping[intent](payload)

