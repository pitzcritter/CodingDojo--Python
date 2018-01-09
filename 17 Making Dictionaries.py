#Assignment: Making Dictionaries
#Create a function that takes in two lists and creates a single dictionary. The first list contains keys and the second list contains the values. Assume the lists will be of equal length.

#Your first function will take in two lists containing some strings. Here are two example lists:

#3name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
#favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]
#Copy
#Here's some help starting your function.

#def make_dict(list1, list2):
#  new_dict = {}
#  # your code here
#  return new_dict
#Copy
#Hacker Challenge:
#If the lists are of unequal length, the longer list should be used for the keys, the shorter for the values.

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    new_dict = dict(zip(list1, list2))
  # your code here
    return new_dict

print make_dict(name, favorite_animal)

name.append("Earl")
name.append("Don")

def make_dict2(list1,list2):
    index = 0
    ziplist = []
    if len(list1) > len(list2):
        for val in list1:
            if index < len(list2):
                ziplist.append((val,list2[index]))
                index += 1
            else:
                ziplist.append((val,""))
            
    else:
        for val in list2:
            if index <= len(list2):
                ziplist.append((val,list1[index]))
                index += 1
            else:
                ziplist.append((val,""))
            
    return ziplist;    


print " "
print make_dict2(name, favorite_animal)