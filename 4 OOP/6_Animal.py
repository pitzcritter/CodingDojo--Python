class animal(object):
    def __init__(self, name, health=100): 
        self.Name = name
        self.Health = health
    def Walk(self): 
        self.Health -= 1
        return self
    def Run(self): 
        self.Health -= 5
        return self
    def DisplayHealth(self): 
        print (self.Name+ ": "+ str(self.Health))

Animal1 = animal("Lemming")
Animal1.Walk().Walk().Walk().Run().Run().DisplayHealth()
Animal = animal("Vole",1000).DisplayHealth()

class dog(animal):	
    def __init__(self, name, health=150):
        super(dog, self).__init__(name, health)        
        #self.Name = name
        #self.Health = health
        #return self
    def Pet(self): 
        self.Health += 5
        return self

Dog = dog('Fido')
Dog.Walk().Walk().Walk().Run().Run().Pet().DisplayHealth()

class dragon(animal):
    def __init__(self, name, health=170):
        super(dragon, self).__init__(name, health)        

    def Fly(self):
        self.Health -=10
        return self
        
    def DisplayHealth(self):
        super(dragon, self).DisplayHealth()
        print "I am a dragon"
        return self

Dragon = dragon('Burpless')
Dragon.Walk().Walk().Walk().Run().Run().Fly().Fly().DisplayHealth()

class ardvark(animal):
    def __init__(self, name, health=110):
        super(ardvark, self).__init__(name, health)        

Ardvark = ardvark('Nosy')
#Ardvark.Fly()
#Ardvark.Pet()
Ardvark.DisplayHealth()
#Dog.Fly()