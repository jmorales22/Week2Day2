class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def print_info(self):
        print(self.make + " " + self.model + " " + str(self.year))
    
car = Vehicle('Volkswagen', 'Passat', 2018)
car.print_info()
