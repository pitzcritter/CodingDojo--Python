class bike(object):
    def __init__(self, price, max_speed):
        self.Price = price
        self.Max_Speed =  max_speed
        self.miles = 0    
    def displayInfo(self):
        print "Price: ", '${:,.2f}'.format(self.Price.strftime)
        print "Max Speed(mph): ", self.Max_Speed
        print "Miles: ", self.miles
        return self
    def ride(self):
        print "Riding: " , self.miles
        self.miles+=10
        return self
    def reverse(self):
        print "Reversing: " , self.miles
        self.miles-=5
        return self
Stingray = bike(100, 10)
Racer = bike(13300, 35)
Recumbent = bike(2500, 45)

print "Stingray"
print "   price: ", Stingray.Price
print " "
print "Racer"
print Racer.ride().ride().reverse()