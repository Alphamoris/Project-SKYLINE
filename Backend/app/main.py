from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def something():
    return {"msg" : "Here is The First message from me ,HI!!"}