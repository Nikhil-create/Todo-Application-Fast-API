from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://nikhil:UvLTBU1TyloRMMZmxfJp3dwvj6HEbs2a@dpg-d00le18dl3ps73e4j7s0-a.virginia-postgres.render.com/todoapp_xx9g'
# SQLALCHEMY_DATABASE_URL = 'sqlite:///./todosapp.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = sessionmaker(autoflush=False,bind=engine,autocommit=False)

Base = declarative_base()

