
class Passenger:
    def __init__(self, name, pid, f_code, seat):
        self.name = name 
        # Name; e.g.: Vu Quoc Thai
        self.pid = pid 
        # Personal ID; e.g.: 001202001264

        self.f_code = f_code
        # Flight code; e.g: VN457
        self.seat = seat 
        # Seat number; e.g.: F3, F5, F6

class Plane:
    def __init__(self, name, f_code):
        self.name = name
        # Name; e.g.: Boeing 757

        self.f_code = f_code
        ###
        # Flight code; e.g: VN457
        # To be sychronised with Passenger through Flight class
        ###

class Flight:
    def __init__(self, f_code, 
    n_passenger, list_passenger, 
    plane,
    t_depart, t_arrive, 
    p_depart, p_arrive,
    ):
        self.f_code = f_code
        ###
        # Flight code; e.g: VN457
        # To be sychronised with Passenger and Plane
        ###

        self.plane = plane
        ###
        # Import plane name from f_code
        # Used for printing out information about flight
        ###

        self.n_passenger = n_passenger
        self.list_passenger = list_passenger
        ###
        # Variables to manage passenger
        # n_passenger for number of passenger
        # list_passenger is Dict/List/Array type for seats and passengers
        ###

        self.t_depart = t_depart
        self.t_arrive = t_arrive
        ###
        # Variables for depart and arrive time
        # Use 24hr format
        ###

        self.p_depart = p_depart
        self.p_arrive = p_arrive
        ###
        # Variables for depart and arrive location
        # Use format: City, Country
        ###





