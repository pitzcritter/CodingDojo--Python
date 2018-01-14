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

class Store(object):
    def __init__(self, products, location, owner):
        self.Products = [products]
        self.Location = location
        self.Owner = owner
        self.display_all()
    def display_all(self):
        print 'Products: ' + str(self.Products)
        print 'Location: ' + str(self.Location)
        print 'Owner: ' + self.Owner
    def Add_Products(self,thisProduct):
        self.Products.append(thisProduct)
        self.display_all()
    def Remove_Product(self,thisProduct):
        self.Products.remove(thisProduct)
        self.display_all()

        