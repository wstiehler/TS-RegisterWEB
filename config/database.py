from sqlalchemy.orm import session
from sqlalchemy.orm.session import Session, sessionmaker
from config.settings import Settings

class Database:

    def __enter__(self):

        base = Settings.Base
        engine = Settings.Engine
        base.metadata.create_all(engine, checkfirst=True)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        return self.session

    def __exit__(self):

        self.session.close()


