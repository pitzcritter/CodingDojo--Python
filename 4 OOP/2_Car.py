class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.Price = price
        self.Speed =  speed
        self.Fuel = fuel
        self.Mileage = mileage
        if price > 10000:
            self.Tax = 0.15
        else:
            self.Tax = 0.12    
    def display_all(self):
        print "Price: ", '${:,.2f}'.format(self.Price)
        print "Speed(mph): ", self.Speed
        print "Fuel: ", self.Fuel
        print "Mileage(mpg): ", self.Mileage
        print "Tax: {}%".format(self.Tax * 100)
        return self
    
Corvette = car(70000,210,"full",26)
Yugo = car(5, 10, "near empty",18)

Corvette.display_all()
print " "
Yugo.display_all()