
from src.bus_stop import BusStop


class Bus:
    def __init__(self,route_no,destination):
        self.route_number = route_no
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self,person):
        self.passengers.append(person)

    def drop_off(self,person):
        self.passengers.remove(person)

    def empty(self):
        self.passengers.clear()

    def pick_up_from_stop(self, bus_stop_1):
        for passenger in bus_stop_1.queue:
            self.passengers.append(passenger)
        bus_stop_1.clear()
