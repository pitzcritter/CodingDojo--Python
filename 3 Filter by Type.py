
given = 2
print type(given) is int


thisObj = {"sI" : 45,
"mI" : 100,
"bI" : 455,
"eI" : 0,
"spI" : -23,
"sS" : "Rubber baby buggy bumpers",
"mS" : "Experience is simply the name we give our mistakes",
"bS" : "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
"eS" : "",
"aL" : [1,7,4,21],
"mL" : [3,5,7,34,3,2,113,65,8,89],
"lL" : [4,34,22,68,9,13,3,5,7,9,2,12,45,923],
"eL" : [],
"spL" : ['name','address','phone number','social security number']
}
print ""
print "types: "
print "bS" + str(thisObj["bS"])
vv = enumerate(thisObj)
#print vv[1]
for i,key in vv:
    print str(i) + " key:  " + key + "   type: " + str(type(thisObj[key])) + "    value: "  + str(thisObj[key])
    if type(thisObj[key]) is int:
        if i >= 100:
            print "    That's big:   " + str(thisObj[key])
        else:
            print "    That's small: " + str(thisObj[key])
    if type(thisObj[key]) is str:
        if len(thisObj[key]) >= 50:
            print "    Long Sentence: " + str(thisObj[key]) 
        else:
            print "    Short Sentence: " + str(thisObj[key]) 
    if type(thisObj[key]) is list:        
        if len(thisObj[key]) > 10:
            print "    Big List: " + str(thisObj[key]) 
        else:
            print "    Small List: " + str(thisObj[key]) 
    if type(thisObj[key]) is list:
        for i in thisObj[key]:
            if type(i) is int:
                if i >= 100:
                    print "        That's big:   " + str(i)
                else:
                    print "        That's small: " + str(i)
            if type(i) is str:
                if len(i) > 50:
                    print "        Long Sentence: " + str(i) 
                else:
                    print "        Short Sentence: " + str(i) 
