class Parking:

    def __init__( self, max_vacancies ):
        self.max_vacancies = max_vacancies
        self.occupied_vacancies = 0

    def max( self ):
        return self.max_vacancies

    def available( self ):
        return self.max_vacancies - self.occupied_vacancies

    def occupied( self ):
        return self.occupied_vacancies

    def enter( self ):
        if( self.occupied_vacancies == self.max_vacancies ):
            raise Exception('Garage is full!')
        self.occupied_vacancies += 1

    def exit( self ):
        if( self.occupied_vacancies == 0 ):
            raise Exception('Garage is empty!')
        self.occupied_vacancies -= 1

n = int(input('Enter the maximum number of vehicles : '))

e = Parking(n)

e.entra()
e.entra()
e.entra()
e.entra()
e.sai()

print( e.maximo() )
print( e.disponiveis() )
print( e.ocupadas() )