import random

#Part I
def draw_stars(thislist) :
    for i in thislist:
        print '*' * i

x = [4, 6, 1, 3, 5, 7, 25]
draw_stars(x)

print " "

#Part II
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_starsb(thislist) :
    for i in thislist:
        if isinstance(i, basestring):
            print i.lower()[0:1] * len(i)
        else:
            print '*' * i

draw_starsb(x)