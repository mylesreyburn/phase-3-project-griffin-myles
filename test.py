
import sqlite3


class Location:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.appointments = {}

class Appointment:
    def __init__(self, date, time, user, location):
        self.date = date
        self._time = time
        self.user = user
        self.user.appointments.append(self)
        self.user_name = user.name

        self.location = location
        self.location.users.append(user)
        self.location.appointments[self.time] = self

    def get_time(self):
        return self._time

    def set_time(self, time):
        if type(time) == str and len(time) == 5:
            self._name = time
        else:
            raise Exception("Can't be done!")

    time = property(get_time, set_time,)

class User:
    def __init__(self, name):
        self.name = name
        self.appointments = []


guy = User("Kennedy")
location = Location("Dentist")
new_appointment = Appointment("10/05/2023", "10:00 PM", guy, location)

new_appointment = Appointment("10/05/2023", "10:00 PM", User("Kennedy"), Location("Dentist"))

class Customer:
    def __init__(self, name):
        self._name = name
        self._orders = []
        self._coffees = []

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if type(name) == str and 1 <= len(name) <= 15 and hasattr(self, "name"):
            self._name = name
        
    name = property(get_name, set_name)