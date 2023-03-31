from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db.models import Base, User, Location, Appointment
from helpers import sign_in

engine = create_engine("sqlite:///database.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    sign_in()