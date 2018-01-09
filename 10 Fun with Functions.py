def odd_even(lower, upper):
    for num in range(lower, upper):
        if num % 2 == 0 :
            print "Number is " + str(num) + ".This is an even number."
        else:
            print "Number is " + str(num) + ".This is an odd number."

def multiply(thislist, factor):
    return [x * factor for x in thislist]

odd_even(1, 200)

print " "
a = [2, 4, 10, 16]
print multiply(a, 5)

#def layered_multiples(arr):
#    
#      newlist = [x * factor for x in thislist]
#3  return new_array
#x = layered_multiples(multiply([2,4,5],3))
#print x

def layered_mult(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(i)
        new_array.append(val_arr)
    return new_array

x = layered_mult(multiply([1,2,3],4))
print x
