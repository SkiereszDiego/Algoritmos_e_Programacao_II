class Tower:

    def __init__(self, id, name, adress):
        self.id = id 
        self.name = name
        self.adress = adress
    
    def print_out(self):
         print('\nID: {} \nTower: {} \nAdress: {}\n'.format (self.id, self.name, self.adress))

    def register(self):
        print('')