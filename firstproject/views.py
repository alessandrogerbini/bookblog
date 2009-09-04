from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    # here, I will put a function that will pass a list of posts to the template
        
    return HttpResponse("sup?")
    
#def blog(request, year='$none', month='$none', day='$none'):
    #print "Check!"
    #return render_to_response('sample.html')

#the following three functions catch the incoming requests from the user by
    # day, month, and year, and pass the variables to a template
    # the template assumes that it is recieving all of these variables, it does not have a failsafe in place
def YearArchive(request, year):
    print "got a year request"
    return  render_to_response('sample.html', {
        'year': year,
    })

def MonthArchive(requst, year, month):
    print "got a month request"
    return render_to_response('sample.html', {
        'year': year,
        'month': month,
    })

def ByDay(requst, year, month, day):
    print "got a by day request"
    return render_to_response('sample.html', {
        'year': year,
        'month': month,
        'day': day,
    })