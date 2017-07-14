from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime as dt
import time

engine = create_engine("sqlite:///test.db", echo=True)
Base = declarative_base(bind=engine)

class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True)
    ts = Column(DateTime)
    create_date = Column(DateTime)
    name = Column(String)

    def __init__(self, name):
        self.name = name
        self.create_date = dt.now()
        return


Base.metadata.create_all()
Session = sessionmaker(bind=engine)

s = Session()

ivan = Student("Ivan")

#s.add_all([ivan, ])
#s.commit()

while True:
    for student in s.query(Student):
        print("name = {} id = {} created = {}".format(student.name, student.id, student.create_date))
    time.sleep(5)
