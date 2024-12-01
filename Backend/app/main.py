from fastapi import FastAPI
from database import cur_obj
app=FastAPI()

@app.get("/")
def something():
    cur_obj.execute("select * from images")
    data = cur_obj.fetchall()
    print(data)
    return {"msg" : data }

@app.get("/")
def thing():
    cur_obj.execute("select * from images")
    data = cur_obj.fetchall()
    print(data)
    return {"msg" : data }


