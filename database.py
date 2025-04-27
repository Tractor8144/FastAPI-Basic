import sqlalchemy as _sqlalchemy
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

DATABASE_URL = "postgresql://postgres:admin@localhost/fastapi_db"

engine = _sqlalchemy.create_engine(DATABASE_URL)

SessionLocal = _orm.sessionmaker(autocommit = False, autoflush=False, bind = engine)

Base = _declarative.declarative_base()

#hello there!
