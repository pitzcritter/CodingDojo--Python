print "odds:"
i = 1
while i <= 1000:
    if not i % 2 == 0:
        print i
    i += 1
i = 5

print "fives:"
while i <= 1000000:
    if i % 5 == 0:
        print i
    i += 1

print "Sum of list:"
a = [1, 2, 5, 10, 255, 3]
b = sum(a)
print b

print "average1:"
a = [1, 2, 5, 10, 255, 3]
print reduce(lambda x, y: x + y, a) / float(len(a))

print "average2:"
a = [1, 2, 5, 10, 255, 3]
print sum(a) / float(len(a))

