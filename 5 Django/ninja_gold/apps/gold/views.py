from __future__ import unicode_literals
from django.urls import reverse
from django.shortcuts import render, redirect
from random import randrange
from time import gmtime, strftime

class gotoBuilding:
    def __init__(self, location, earned, request):
        self.location = location
        self.earned = earned
        
        if 'grand_total' in request.session:
            request.session['grand_total'] += earned
        else:
            request.session['grand_total'] = earned
        
        self.grand_total = request.session['grand_total']

        if earned >= 0:
            self.comment = "Entered a {0} and earned {1} golds! {2}".format(location,earned, strftime('%Y-%m-%d %H:%M %p', gmtime()))
            self.color = 'green'
        else:
            self.comment = "Entered a {0} and lost {1} golds! {2}".format(location,earned, strftime('%Y-%m-%d %H:%M %p', gmtime()))
            self.color = 'red'

        self.this_record = {'earned': earned, 'grand_total': self.grand_total, 'comment': self.comment, 'color': self.color}
        #return this_record
        print "this_record: ",self.this_record

    def appendThisRecord(self, request):
        request.session['data'].append(self.this_record)
        print "Appended new record"
        return request.session['data']

    #def calcGrandTotal(self, earned, request):
    #    request.session['grand_total'] += earned
    #    print "New grand_total: ", 
    #    return request.session['grand_total']=request.session['grand_total']
    


def index(request):     
    if not 'data' in request.session:
        request.session['data'] = []#[{'earned': '10', 'grand_total': '10', 'comment': 'dummy comment', 'color': 'red'}]
        grand_total = 0
        print "initialize"
    #data = request.session['data']
    print "data in index: ", request.session['data']
    print "goto index"
    context = {"data": request.session['data']}    
    return render(request, 'gold/index.html', context)    


def farm(request):
    earned = randrange(10,20)
    goto = gotoBuilding('farm', earned, request)
    print "goto: ", goto
    data = goto.appendThisRecord(request)    
    print "farm data: ", data
    context = {"data": request.session['data']}
    #return render(request, 'gold/index.html',context)
    return redirect('/',request, context)

def cave(request):
    earned = randrange(5,10)
    goto = gotoBuilding('cave', earned, request)
    datacontext = goto.appendThisRecord(request)    
    context = {"data": request.session['data']}
    return redirect('/',request, context)
    #return render(request, 'gold/index.html', context)

def house(request):
    earned = randrange(2,5)
    goto = gotoBuilding('house', earned, request)
    data = goto.appendThisRecord(request)    
    context = {"data": request.session['data']}
    return redirect('/',request, context)
    #return render(request, 'gold/index.html', context)

def casino(request):
    earned = randrange(-50,50)
    goto = gotoBuilding('casino', earned, request)
    data = goto.appendThisRecord(request)    
    context = {"data": request.session['data']}
    return redirect('/',request, context)
    #return render(request, 'gold/index.html', context)

def clear(request):
    for key in request.session.keys():
        del request.session[key]
    return redirect( reverse('index'))