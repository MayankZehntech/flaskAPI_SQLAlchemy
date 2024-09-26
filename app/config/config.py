import os
from dotenv import load_dotenv  

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    print(f'DATABASE_URI: {SQLALCHEMY_DATABASE_URI}')
    #SQLALCHEMY_DATABASE_URI = ('postgresql://postgres:!2s6!YEdf6BrmkBf@solved-dev-27-08-2024.c5ixm26kc4nu.us-east-2.rds.amazonaws.com/db_sfsync')
    SQLALCHEMY_TRACK_MODIFICATIONS = False