from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

class Settings:

    Engine = create_engine('postgresql+psycopg2://olist:olist123@localhost:5460/postgres_ts', echo=False)
    Base = declarative_base()