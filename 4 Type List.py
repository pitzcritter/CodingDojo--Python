# input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
#"The list you entered is of mixed type"
#"String: magical unicorns hello world"
#"Sum: 117.98"
t=""
thisStr = ""
thisSum = 0
theseTypes = []
for val in l:
    if not type(val) in theseTypes:
        theseTypes.append(type(val))
    if type(val) is int or type(val) is float:
        thisSum += val
    if type(val) is str:
        thisStr += " " + val
    if type(val) is str:
        print ""

print l
if len(theseTypes) == 1:
    if theseTypes[0] is "<type 'int'>" or theseTypes[0] is int:
        t = "integer"
    if theseTypes[0] is "<type 'str'>" or theseTypes[0] is str:
        t = "string"
    if theseTypes[0] is "<type 'float'>" or theseTypes[0] is float:
        t = "float"
    if theseTypes[0] is "<type 'list'>" or theseTypes[0] is list:
        t = "list"
    
    print "The list you entered is " + t + " type"
else:
    print "The list you entered is of mixed type"

if thisSum >0:
    print "Sum " + str(thisSum)

if str in theseTypes:
    print "String: " + thisStr
print " "


# input
l = [2,3,1,7,4,12]
#output
#"The list you entered is of integer type"
#"Sum: 29"

t=""
thisStr = ""
thisSum = 0
theseTypes = []
for val in l:
    if not type(val) in theseTypes:
        theseTypes.append(type(val))
    if type(val) is int or type(val) is float:
        thisSum += val
    if type(val) is str:
        thisStr += " " + val
    if type(val) is str:
        print ""

print l

if len(theseTypes) == 1:
    if theseTypes[0] is "<type 'int'>" or theseTypes[0] is int:
        t = "integer"
    if theseTypes[0] is "<type 'str'>" or theseTypes[0] is str:
        t = "string"
    if theseTypes[0] is "<type 'float'>" or theseTypes[0] is float:
        t = "float"
    if theseTypes[0] is "<type 'list'>" or theseTypes[0] is list:
        t = "list"
    
    print "The list you entered is " + t + " type"
else:
    print "The list you entered is of mixed type"

if thisSum >0:
    print "Sum " + str(thisSum)

if str in theseTypes:
    print "String: " + thisStr
print " "


# input
l = ['magical','unicorns']
#output
#"The list you entered is of string type"
#3"String: magical unicorns"

t=""
thisStr = ""
thisSum = 0
theseTypes = []
for val in l:
    if not type(val) in theseTypes:
        theseTypes.append(type(val))
    if type(val) is int or type(val) is float:
        thisSum += val
    if type(val) is str:
        thisStr += " " + val
    if type(val) is str:
        print ""

print l
if len(theseTypes) == 1:
    if theseTypes[0] is "<type 'int'>" or theseTypes[0] is int:
        t = "integer"
    if theseTypes[0] is "<type 'str'>" or theseTypes[0] is str:
        t = "string"
    if theseTypes[0] is "<type 'float'>" or theseTypes[0] is float:
        t = "float"
    if theseTypes[0] is "<type 'list'>" or theseTypes[0] is list:
        t = "list"
    
    print "The list you entered is " + t + " type"
else:
    print "The list you entered is of mixed type"

if thisSum >0:
    print "Sum " + str(thisSum)

if str in theseTypes:
    print "String: " + thisStr
print " "
