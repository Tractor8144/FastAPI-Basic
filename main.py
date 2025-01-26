from fastapi import FastAPI

app2 = FastAPI()

@app2.get("/")
def root():
    return {"Hello":"world"}