# python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Page(Base):
    __tablename__ = 'page'

    id = Column(Integer, primary_key=True)
    url = Column(String(200))
    urlmd5 = Column(String(32))
    title = Column(String(200))
    category = Column(Integer)
    date = Column(Date)
    content = Column(Text)
    create = Column(Integer)

