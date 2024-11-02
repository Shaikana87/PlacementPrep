from django.shortcuts import render
import json

# Create your views here.

def career(request):
    with open('scripts/portal.json') as f:
        portals = json.load(f)
    return render(request, 'career.html', {'portals':portals})