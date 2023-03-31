from sqlalchemy import create_engine, func
from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
import sqlite3

Base = declarative_base()
engine = create_engine("sqlite:///db/database.db")

class User(Base):

    __tablename__ = "Users"
    id = Column(Integer(), primary_key=True)
    name = Column(String())

    Appointment = relationship("Appointment", backref=backref("Users"))

    def __repr__(self):
        return f"Users(id={self.id}, name={self.name})"
    
class Location(Base):

    __tablename__ = "Locations"
    id = Column(Integer(), primary_key=True)
    location = Column(String())

    Appointment = relationship("Appointment", backref=backref("Locations"))

    def __repr__(self):
        return f"Locations(id={self.id}, location={self.location}, user_id={self.user_id})"

class Appointment(Base):

    __tablename__ = "Appointments"
    id = Column(Integer(), primary_key=True)
    date = Column(String())
    time = Column(String())
    user_id = Column(Integer(), ForeignKey(User.id))
    location_id = Column(Integer(), ForeignKey(Location.id))

    def __repr__(self):
        return f"Appointments(id={self.id}, date={self.date}, time={self.time}, user_id={self.user_id}), location_id={self.location_id}"