#handles database connection
print("Loading app.database module")
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

######### YOU CAN USE THIS WHEN YOU ARE WORKING WITH DATABASE DRIVER "PSYCOPG" #########
######### YOU PUT IT IN THE MAIN CLASS ##########
#import psycopg
#from psycopg.rows import dict_row
#import time
# while True:
#     try:
#         conn = psycopg.connect(
#             host='localhost',
#             dbname='fastapi',
#             user='postgres',
#             password='2022AmrSharkawi',
#             row_factory=dict_row 
#         )
#         cursor=conn.cursor()
#         print("Connection was successful!")
#         break

#     except Exception as error:
#         print(f"An error occurred: {error}")
#         time.sleep(10)