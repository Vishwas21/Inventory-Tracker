from django.shortcuts import render
from django.http import HttpResponse
import json

sensorData = [[1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1],
              [1,0,1,0,1,0,1,0],
              [0,1,0,1,0,1,0,1]]

values = [10, 20, 30, 40, 50, 60, 70, 80]

# Create your views here.
def homeView(request, *args, **kwargs):
    print("Inside homeView()")
    context = {}
    return render(request, 'inventoryCheck.html', context)

def gridView(request, *args, **kwargs):
    print("Inside gridView()")
    context = {}
    return render(request, 'grid.html', context)

# Function returns the analysed data about the inventory
def getData(request):
    print("Inside getData()")
    if request.is_ajax() and request.method == "POST":
        send_data = json.dumps({"values" : values})
        return HttpResponse(send_data, content_type="application/json")
    return HttpResponse("")

# Function returns the grid values given by the sensors
def getGridData(request):
    print("Inside getGridData()")
    if request.is_ajax() and request.method == "POST":
        send_data = json.dumps({"gridValues" : sensorData})
        return HttpResponse(send_data, content_type="application/json")
    return HttpResponse("")