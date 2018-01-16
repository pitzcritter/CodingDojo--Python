#Assignment: Call Center
#You're creating a program for a call center. Every time a call comes in you need a way to track that call. One of your program's requirements is to store calls in a queue while callers wait to speak with a call center employee.
#You will create two classes. One class should be Call, the other CallCenter.
#Call Class
#- Create your call class with an init method. Each instance of Call() should have:
#Attributes:
#- unique id
#- caller name
#- caller phone number
#- time of call
#- reason for call
#Methods:
#- display: that prints all Call attributes.

#CallCenter Class
#- Create your call center class with an init method. Each instance of CallCenter() should have the following attributes:
#Attributes:
#- calls: should be a list of call objects
#- queue size: should be the length of the call list
#Methods:
#- add: adds a new call to the end of the call list
#- remove: removes the call from the beginning of the list (index 0).
#- info: prints the name and phone number for each call in the queue as well as the length of the queue.
#You should be able to test your code to prove that it works. Remember to build one piece at a time and test as you go for easier debugging!
#Ninja Level: add a method to call center class that can find and remove a call from the queue according to the phone number of the caller.
#Hacker Level: If everything is working properly, your queue should be sorted by time, but what if your calls get out of order? Add a method to the call center class that sorts the calls in the queue according to time of call in ascending order.
#import time
import datetime
from operator import itemgetter, attrgetter # for sorting 

class Call(object):
    def __init__(self,unique_id, caller_name, phone_number, time_of_call, reason_for_call):
        self.unique_id=unique_id
        self.caller_name=caller_name
        self.phone_number=phone_number
        self.time_of_call=time_of_call
        self.timeValue_of_call=datetime.datetime.strptime(time_of_call,'%d/%m/%Y %I:%M %p')
        self.reason_for_call=reason_for_call
    def display(self):
        print "unique_id: ",  self.unique_id
        print "caller_name: ", self.caller_name
        print "phone_number: ",  self.phone_number
        print "time_of_call: ", self.time_of_call
        print "reason_for_call: ", self.reason_for_call
        print " "
        return self
    def printthis(self,this_string):
        print "print: ", this_string
        return self

class CallCenter(object):
    def __init__(self, *thesecalls):
        self.calls = []
        for this_call in thesecalls:
            self.calls.append(this_call)
    def add(self, call):
        self.calls.append(call)
        queue_size = len(self.calls)
        return self
    def remove(self):
        self.calls.pop(0)
        queue_size = len(self.calls)
        return self
    def info(self):
        for this_call in self.calls:
            print "unique_id: ",  this_call.unique_id
            print "caller_name: ", this_call.caller_name
            print "phone_number: ",  this_call.phone_number
            print "time_of_call: ", this_call.time_of_call
            print "reason_for_call: ", this_call.reason_for_call
            print " "
    def drop_byPhone(self, drop_call):        
        for k in range(len(self.calls)):
            if self.calls[k].phone_number == drop_call:
                #print "action"
                self.calls.pop(k)
                print "removed: ", self.calls[k].caller_name
                return self
        return self
    def printthis(self,this_string):
        print "print: ", this_string
        return self
    def sort_byTime(self):        
        self.calls = sorted(self.calls, key=attrgetter('timeValue_of_call'))


call = Call("331", "Harry", "319-555-4333", "1/8/2017 4:53 PM", "crabby")
#call.printthis("1:")
#call.display() #works

call.printthis("2:")
callcenter = CallCenter(Call("33", "Harry", "319-555-4333", "1/8/2017 4:55 PM", "crabby"), Call("34", "Barry", "319-555-4334", "1/9/2017 4:56 PM", "crabbier"), Call("35", "Larry", "319-555-4335", "1/8/2017 4:56 PM", "crabbiest"))
#callcenter.info()#works

callcenter.printthis("3:")
callcenter.add(Call("36", "Garry", "319-555-4336", "1/8/2017 4:57 PM", "way past crabby")) #works
#callcenter.info()#works

#call.printthis("4:")
callcenter.remove()#works
#callcenter.info()#works

#call.printthis("5:")
callcenter.add(Call("37", "Darry", "319-555-4337", "1/8/2017 4:58 PM", "lost control, call 911")) #works
#callcenter.info()#works

#call.printthis("6:")
callcenter.drop_byPhone("319-555-4336")
#callcenter.info()

callcenter.printthis("7:")
callcenter.sort_byTime()
callcenter.info()