import random
# random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...

def getGrad(score):
    if score < 70:
        return ('D')
    elif score < 80:
        return 'C'
    elif score < 90:
        return 'B'
    else: 
        return 'A'
print 'Scores and Grades'
for v in range(1,10):
    rnd = random.randint(10,100)
    print 'Score: ' + str(rnd) + '; Your grade is ' + getGrad(rnd )
    
print 'End of the program. Bye!'
