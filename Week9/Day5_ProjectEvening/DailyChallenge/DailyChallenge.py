import datetime


class Airline:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.planes = []


class Airplane:
    def __init__(self, id: int, company):
        self.id = id
        self.company = company
        self.next_flights = []

    def fly(self, destination):


    def location_on_date(self, date):

    def available_on_date(self, date, location):


class Flight:
    def __init__(self, destination, origin, plane):
        self.date = datetime.date
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f"{self.destination}/{self.plane.id}/{self.date}"

    def take_off(self):
        return True

    def land(self):
        return True


class Airport:
    def __init__(self):
        self.city = None
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []


    def schedule_flight(self, destination, datetime):


    def info(self, start_date, end_date):





