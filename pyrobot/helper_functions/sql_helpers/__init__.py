# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-


# import logging
# from pymongo import MongoClient
# from pyrobot.sample_config import Config

# cli = MongoClient(Config.MONGO_URI)


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from pyrobot import DB_URI


def start() -> scoped_session:
    engine = create_engine(DB_URI)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()
