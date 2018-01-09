for i in range(10, 100000):
    found1 = False
    for j in range(2, i):
        if i % j == 0 :
            found1 = True
            break
    if not found1 :
        print  'Foo'
    
    found2 = False
    for j in range(2, i / 2):
        if j * j == i :
            print 'Bar'
            found2 = True
            break
    if found1 == False and found2 == False :
        print 'FooBar'
