# Django
from django.http import HttpResponse

# Utilities
from datetime import datetime
import json


def hello_world(request):
    return HttpResponse("Oh Hi! current server time is {now}".format(
        now=datetime.now().strftime("%b %dth, %Y - %H:%M hrs ")))

def say_hi(request, name, age):
    if age < 12:
        message = "Sorry {}, you are not allowed here".format(name)
    else:
        message = "Hellom {}!, Welcome to Platzigram".format(name)
    return HttpResponse(message)

def sorted(request):
    """Hi"""
    numbers = sorted([int(i) for i in request.GET["numbers"].split(",")])
    data = {
        "status": "ok",
        "numbers": numbers,
        "message": "Imtegers sorted successfully"
    }
    return HttpResponse(json.dumps(data, indent=4), content_type="application/json")

