from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from pathlib import Path
from flask_migrate import Migrate

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, './app/config/.env'))

migrate = Migrate()

def configure_database(app):
    POSTGRES_URL = os.environ.get('POSTGRES_URL') 
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PW = os.environ.get('POSTGRES_PW')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')

    print(f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PW}@{POSTGRES_URL}/{POSTGRES_DB}'