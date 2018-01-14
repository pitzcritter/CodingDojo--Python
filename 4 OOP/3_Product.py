class product(object):
    def __init__(self, price,item_name,weight,brand,status):
        self.Price = price
        self.Item_Name =  item_name
        self.Weight = weight
        self.Brand = brand
        self.Status = "for sale"
    def Display_All(self):
        print "Price: ", '${:,.2f}'.format(self.Price)
        print "Item Name: ", self.Item_Name
        print "Weight(lbs): ", self.Weight
        print "Brand: ", self.Brand
        print "Status: ", self.Status
        return self
    def Sell(self):
        self.Status = "sold"
        self.Display_All()
        return self
    def AddTaxinDecimal(self,tax):
        return (1 + tax) * self.Price
    def Return(self, reason):
        if reason == "defective":
            self.Status = reason
        elif reason == "in box":
            self.Status = "for sale"
        elif reason == "opened box":
            self.Status = "used"
            self.Price = 0.8 * self.Price
        else:
            self.Status = "for sale"
        self.Display_All()

CofeePot = product(26.30,"PerkoGand",2.9,"Ronco","for sale")

CofeePot.Display_All()
print " "
CofeePot.Sell()
print " "
CofeePot.Return("defective")
print " "
CofeePot.Return("in box")
print " "
CofeePot.Return("opened box")
print " "
CofeePot.Return("opened box")
print " "
CofeePot.Return("unsure")
print " "
CofeePot.AddTaxinDecimal(0.10)
CofeePot.Weight = 3.1
print " "
CofeePot.Display_All()