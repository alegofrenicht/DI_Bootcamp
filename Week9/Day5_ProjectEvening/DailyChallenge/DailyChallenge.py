import datetime



class Airline:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.planes = []


class Airplane:
    def __init__(self, id_plane: int, company):
        self.id = id_plane
        self.company = company
        self.next_flights = []

    def fly(self, flight):
        self.next_flights.append(flight)


    def location_on_date(self, date):
        for flight in self.next_flights:
            if date == flight.date:
                return flight.destination


    def available_on_date(self, date, location):
        return self.location_on_date(date) == location




class Flight:
    def __init__(self, destination, origin, plane, date):
        self.date = datetime.datetime.strptime(date, "%d/%m/%Y")
        self.destination = destination
        self.origin = origin
        self.plane = plane
        self.id = f"{self.destination}/{self.plane.id}/{self.date}"

    def take_off(self):
        return True

    def land(self):
        return True


class Airport:
    def __init__(self, city):
        self.city = city
        self.planes = []
        self.scheduled_departures = []
        self.scheduled_arrivals = []


    def schedule_flight(self, destination, datetime):


    def info(self, start_date, end_date):





