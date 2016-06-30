# python
# -*- coding: utf-8 -*-
from sqlalchemy import Column, String, Integer, Text, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    pid = Column(Integer)
    url = Column(String(500))
    status = Column(Integer)