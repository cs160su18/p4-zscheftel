from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

def custom(request):
    return render(request, 'custom/index.html', {})
 
def ingredientSelect(request):
    return render(request, 'custom/ingredientSelect.html', {})
  
def processSelect(request):
    return render(request, 'custom/processSelect.html', {})
  
def finalDetails(request):
    return render(request, 'custom/finalDetails.html', {})
  
def submissionConfirmation(request):
    return render(request, 'custom/submissionConfirmation.html', {})
  
def room(request, room_name):
    return render(request, 'draw/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })