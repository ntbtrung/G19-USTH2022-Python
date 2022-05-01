from asyncio import constants
from email.policy import default
import domains
import string

###
# This class exists only to export a location String for p_depart and p_arrive variables
###
class Location:
    def __init__(self, ct, pays):
        self.ct = string(ct)
        # City
        self.pays = string(pays)
        # French for country

    EligibleCT = ("Hanoi", "Saigon")
    EligiblePays = ("Vietnam")

    def validateCT(self, ct_list, ct):
        for x in range(0, len(ct_list)):
            tempct = ct_list[x]
            if ct == tempct:
                return True

    def validatePays(self, pays_list, pays):
        for x in range(0, len(pays_list)):
            tempp = pays_list[x]
            if pays == tempp:
                return True

    ###
    # Setter and getters
    ###    
    def setCT(self, ct):
        self.ct = ct
    def getCT(self):
        return self.ct
    def setPays(self, pays):
        self.pays = pays
    def getPays(self):
        return self.pays

    def export(self):
        return (self.ct +', ' + self.pays)
    # Somehow the most important function