#Assignment: Dictionary in, tuples out
#Write a function that takes in a dictionary and returns a list of tuples where the first tuple item is the key and the second is the value. Here's an example:

### function input
#my_dict = {
#  "Speros": "(555) 555-5555",
##  "Michael": "(999) 999-9999",
##  "Jay": "(777) 777-7777"
#}
#function output
#[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

myDict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def toTuple(dic):
    order = ['Speros','Michael', 'Jay']
    print tuple([myDict[field] for field in order])
    print [(k, v) for k, v in myDict.iteritems()]

    this = []
    for k,v in myDict.items():
        this.append((k,v))
    print this



toTuple(myDict)