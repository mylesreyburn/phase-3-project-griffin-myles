from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Location, Appointment
from sqlalchemy.dialects import sqlite

if __name__ == "__main__":

    engine = create_engine("sqlite:///database.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Delete users, locations, and appointments upon initiation
    # session.query(User).delete()
    # session.query(Location).delete()
    # session.query(Appointment).delete()

    # Create instances for each class

    user_1 = User(name="Goon")
    session.add(user_1)
    user_2 = User(name="Hank")
    session.add(user_2)
    user_3 = User(name="Lenny")
    session.add(user_3)
    session.commit()

    location_1 = Location(location="Dentist")
    session.add(location_1)
    location_2 = Location(location="Salon")
    session.add(location_2)
    location_3 = Location(location="Masseuse")
    session.add(location_3)
    location_4 = Location(location="Masseuse")
    session.add(location_4)
    session.commit()

    appointment_1 = Appointment(time="13:00", date="04/03/1990", user_id=1, location_id=1)
    session.add(appointment_1)
    appointment_2 = Appointment(time="17:00", date="10/12/2007", user_id=1, location_id=2)
    session.add(appointment_2)
    appointment_3 = Appointment(time="04:00", date="02/24/1980", user_id=2, location_id=2)
    session.add(appointment_3)
    appointment_4 = Appointment(time="13:50", date="01/30/2000", user_id=3, location_id=3)
    session.add(appointment_4)
    appointment_5 = Appointment(time="12:35", date="12/09/2021", user_id=3, location_id=4)
    session.add(appointment_5)
    session.commit()
    
    