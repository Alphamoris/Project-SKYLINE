from asyncio import exceptions
import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
import time
from schemas import db

database_params : dict = {
    "database" : "simple" ,
    "user" : "postgres" ,
    "password" : "8072052338." ,
    "host" : "localhost" ,
    "port" : "5432" ,
    "cursor_factory" : RealDictCursor
 }

con_obj = psycopg2.connect(**database_params)
print("Connected To The Database Successfully")
cur_obj=con_obj.cursor()
def db_ins():
    return con_obj
           
# def get_db_instance(db_con : db = {}):
#     while db_con.counter == 0: 
#         try:
#             db_con.con_obj = psycopg2.connect(**database_params)
#             db_con.cur_obj=db_con.con_obj.cursor() # type: ignore
#             if db_con.con_obj:
#                 print("Connection was succcessful!!")
#                 db_con.counter=1
#                 return(db_con)
#         except Exception as e:
#             print(e)
#             time.sleep(5)
#     else:
#         return db_con
