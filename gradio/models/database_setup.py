# database_setup.py
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建 SQLite 数据库引擎
engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()


# 定义 User 模型
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


# 创建表
Base.metadata.create_all(engine)

# 创建数据库会话
Session = sessionmaker(bind=engine)
session = Session()
