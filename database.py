from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv


load_dotenv()

DB_USER = os.environ.get('DB_USER', 'test_user')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'test1234')
DB_HOST = os.environ.get('DB_HOST', 'localhost')
DB_PORT = os.environ.get('DB_PORT', '3306')
DB_NAME = os.environ.get('DB_NAME', 'dashboard')



SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./myapi.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, )

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_db() :
    db = SessionLocal()
    try :
        yield db
    finally :
        db.close()


    