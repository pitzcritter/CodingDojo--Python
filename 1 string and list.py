words = "It's thanksgiving day. It's my birthday,too!"

print words.find('day')
print words.replace('day','month,')

x = [2,54,-2,7,12,98]

print 'min:' + str(min(x))
print 'max:' + str(max(x))

x = ["hello",2,54,-2,7,12,98,"world"]

print 'first: ' + x[0]
print 'last: ' + x[len(x)-1]

x = [19,2,54,-2,7,12,98,32,10,-3,6]

s = sorted(x)

enums = enumerate(s)
lower = []
upper = []
for i, val in enums:
    if i < len(s)/2:
        lower.append(val)
    else:
        upper.append(val)

print 'lowerarray ' + str(lower)
print 'upperarray ' + str(upper)

upper.insert(0, lower)
print upper

