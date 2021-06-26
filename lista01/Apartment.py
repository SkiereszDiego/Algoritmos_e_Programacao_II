from Tower import Tower
apartments= []

class Apartment(Tower):
    def __init__(self, id, name, adress, apt_number, tower, parking_space_number):
        Tower.__init__(self, id, name, adress)
        self.apt_number = apt_number
        self.tower = tower
        self.parking_space_number = parking_space_number

    def print_out(self):
         print('\nTower: {} \nAdress: {} \nApt: {}\nParking number: {}'.format (self.name, self.adress, self.apt_number, self.parking_space_number))
        # for obj in apartments:
        #print( obj.id, obj.name, obj.adress, obj.apt_number, obj.tower, obj.parking_space_number, sep =' ' )

    def register(self, id, name, adress, apt_number, tower, parking_space_number):
        apartments.append(Apartment(id, name, adress, apt_number, tower, parking_space_number))

