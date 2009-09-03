from django.http import HttpResponse
from django.shortcuts import render_to_response

def home(request):
    # here, I will put a function that will pass a list of posts to the template
        
    return HttpResponse("sup?")
    
def blog(request, year='$none', month='$none', day='$none'):
    print "Check!"
    return render_to_response('sample.html')