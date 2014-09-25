# chart3/app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import app


engine = create_engine(app.config['DATABASE_URI'], convert_unicode = True, **app.config['DATABASE_CONNECT_OPTIONS'])
db_session = scoped_session(sessionmaker(autocommit = False, autoflush = False, bind = engine))

Model = declarative_base(name = 'Model')
Model.query = db_session.query_property()

def init_db():
    import models
    Model.metadata.create_all(bind = engine)

