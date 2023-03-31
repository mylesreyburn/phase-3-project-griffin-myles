from db.models import User, Location, Appointment
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from tabulate import tabulate

engine = create_engine("sqlite:///database.db")
Session = sessionmaker(bind=engine)

# Users class can see its Appointments
# Location class can see its Appointments and its Users
# Appointments class can create itself??

current_user_id = 0

def sign_in():
    initialize_locations()
    print("")
    print("Welcome to AppointMan!")
    print("")
    full_name = input("Please enter your full name \n")
    # creates new User with full_name if one doesn't already exist, tosses that into Users table 

    current_user_id = log_in_user(full_name)
    print("ID:", current_user_id)
    

    password = input("Please enter your password (hint: it's ''orange'')\n")
    # password is just a formality
    while password != "orange":
        password = input("Wrong password. Please try again. (hint: it's ''orange'') \n")
    print(f"Logged in! Welcome, {full_name}.")
    menu(current_user_id)

def menu(current_user_id):
    print("")
    print("What would you like to do today?")
    direct = input("Press 1 to book a new Appointment" + 
                   "\nPress 2 to view your current appointments" + 
                   "\nPress ENTER if Business Owner\n")
    
    if direct == "1":
        print("Cool!")
        date = input("Enter date (MM/DD/YYYY): \n")
        time = input("Enter time (24 hour time) (ex: 15:00 rather than 3:00 PM): \n")
        print_locations_table()
        location_id = int(input("Enter the ID of the location you wish to book at. \n"))
        book_new(date, time, current_user_id, location_id)
    elif direct == "2":
        view_appointments(current_user_id)
    elif direct == "":
        business_menu(current_user_id)
    else:
        print("Invalid selection.")

def done(current_user_id):
    cont = input("Would you like to continue? (Y/n) \n")
    done = False
    while not done:
        if cont.lower() == "y":
            done = True
            menu(current_user_id)
        elif cont.lower() == "n":
            done = True
            print("Have a nice day.")
            exit()
        else:
            cont = input("Invalid entry. It's one letter dude, come on. \n")

def book_new(date, time, user_id, location_id):
    active_id = location_id
    while active_id > 5 or active_id < 1:
        active_id = int(input("Invalid ID. Please try again. \n"))

    session = Session()
    new_appointment = Appointment(date=date, time=time, user_id=user_id, location_id=active_id)
    session.add(new_appointment)
    session.commit()

    user = session.query(User).filter_by(id=user_id).first()
    user_name = user.name
    current_user_id = user.id

    location = session.query(Location).filter_by(id=active_id).first()
    location_name = location.location


    session.close()

    print(f"Appointment booked at {location_name} for {user_name} on {date} at {time}.")
    done(current_user_id)


    

def print_locations_table():
    session = Session()

    locations = session.query(Location).all()

    data = [[l.id, l.location] for l in locations]

    headers = ["IDS", "LOCATIONS"]
    print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

    session.close()

def view_appointments(user_id):
    session = Session()

    appointments = session.query(Appointment).filter_by(user_id=user_id).all()

    data = [[a.date, a.time, get_location_name_from_id(a.location_id)] for a in appointments]

    headers = ["DATES", "TIMES", "LOCATIONS"]
    if len(data) > 0:
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No appointments found! Please make one.")

    session.close()
    done(user_id)

def get_location_name_from_id(id):
    session = Session()
    location = session.query(Location).filter_by(id=id).first()
    location_name = location.location
    session.close()
    return location_name


def business_menu(user_id):
    password = input("Please enter your password (hint: it's ''orange'')\n")
    while password != "orange":
        password = input("Wrong password. Please try again. (hint: it's ''orange'') \n")
    print("Welcome! Which business is yours?\n------------------------------------")

def log_in_user(name):
    session = Session()

    try:
        user = session.query(User).filter_by(name=name).one_or_none()
        if user is None:
            user = User(name=name)
            session.add(user)
            session.commit()
        user_id = user.id
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()

    return user_id

def initialize_locations():
    # Locations: Dentist, Doctor, DMV, Hair Stylist, Vet
    session = Session()
    session.query(Location).delete()

    dentist = Location(location="Dentist")
    session.add(dentist)
    doctor = Location(location="Doctor")
    session.add(doctor)
    dmv = Location(location="DMV")
    session.add(dmv)
    hair_stylist = Location(location="Hair Stylist")
    session.add(hair_stylist)
    vet = Location(location="Vet")
    session.add(vet)

    session.commit()
    session.close()
