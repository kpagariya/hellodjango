from django.shortcuts import render

from django.http import HttpResponse
from .models import Drivers
def clientsListing(request):
    #return HttpResponse('<h1>Hello, I am learning Django!</h1>')
    # logic to 
    # 1) retrieve the client data from DB 
    # 2) pass it to clients.html for display
    # 3) Display clients on UI
    # select * from Drivers.
    clientlistings = Drivers.objects.all()
    print("Recevied driver records",len(clientlistings))
    context = {
    	'driverList' : clientlistings
    }
    return render(request,'clients/clients.html',context)