import string

class Passenger:
    def __init__(self, name, pid, f_code, seat):
        self.name = string(name) 
        # Name; e.g.: Vu Quoc Thai
        self.pid = string(pid) 
        # Personal ID; e.g.: 001202001264

        self.f_code = string(f_code)
        # Flight code; e.g: VN457
        self.seat = string(seat)
        # Seat number; e.g.: F3, F5, F6

    def validatePID(self, pid):
        if len(pid) < 13:
            return True
        else:
            return False
    # Validate function for personal ID, makes sure it follows Vietnam's ID

    def validateSeat(self, seat):
        tempnum = int(seat[1])
        for x in range(0, len(string.ascii_uppercase)):
            tempchar = string.ascii_uppercase[x]
            if seat[0] == tempchar:
                if tempnum in range(1, 9):
                    return True
    # Validate function for seat, the first letter in range A to Z, and seat number from 1 to 9


    ###
    # Setter and getters
    ###
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setPID(self, pid):
        self.pid = pid
    def getPID(self):
        return self.pid

    def setCode(self, code):
        self.f_code = code
    def getCode(self):
        return self.f_code
    def setSeat(self, seat):
        self.seat = seat
    def getSeat(self):
        return self.seat

        

class Plane:
    def __init__(self, name, f_code):
        self.name = string(name)
        # Name; e.g.: Boeing 757

        self.f_code = string(f_code)
        ###
        # Flight code; e.g: VN457
        # To be sychronised with Passenger through Flight class
        ###

    ###
    # Setter and getters
    ###
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setCode(self, code):
        self.f_code = code
    def getCode(self):
        return self.f_code



class Flight:
    def __init__(self, f_code, 
    n_passenger, list_passenger, 
    plane,
    t_depart, t_arrive, 
    p_depart, p_arrive,
    ):
        
        self.f_code = string(f_code)
        ###
        # Flight code; e.g: VN457
        # To be sychronised with Passenger and Plane
        ###

        self.plane = plane
        ###
        # Import plane name from f_code
        # Used for printing out information about flight
        ###

        self.n_passenger = int(n_passenger)
        self.list_passenger = list_passenger
        ###
        # Variables to manage passenger
        # n_passenger for number of passenger
        # list_passenger is Dict/List/Array type for seats and passengers
        ###

        self.t_depart = int(t_depart)
        self.t_arrive = int(t_arrive)
        ###
        # Variables for depart and arrive time
        # Use 24hr format
        ###

        self.p_depart = string(p_depart)
        self.p_arrive = string(p_arrive)
        ###
        # Variables for depart and arrive location
        # Use format: City, Country
        ###

    def validateTime(self, t):
        if t in range(0, 24):
            return True
        else:
            return False
    # Validate function for time, used for both depart and arrive
    
    def seatlimit(self, n_passenger):
        if n_passenger in range(0, 234):
            return True
        else:
            return False
    # Used to check to avoid overbooking

    ###
    # Setter and getters
    ###
    def setCode(self, code):
        self.f_code = code
    def getCode(self):
        return self.f_code

    def set_npass(self, n):
        self.n_passenger = n
    def get_npass(self):
        return self.n_passenger
    def set_lpass(self, l):
        self.list_passenger = l
    def get_lpass(self):
        return self.list_passenger

    def setPlane(self, plane):
        self.plane = plane
    def getPlane(self):
        return self.plane

    def setTD(self, td):
        self.t_depart = td
    def getTD(self):
        return self.t_depart 
    def setTA(self, ta):
        self.t_arrive = ta
    def getTA(self):
        return self.t_arrive

    def setPD(self, pd):
        self.p_depart = pd
    def getPD(self):
        return self.p_depart
    def setPA(self, pa):
        self.p_arrive = pa
    def getPA(self):
        return self.p_arrive   
    
    

    





