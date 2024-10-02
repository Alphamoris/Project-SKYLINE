from pydantic import BaseModel, InstanceOf

class db(BaseModel):
    con_obj : object
    cur_obj : object
    counter : int = 0