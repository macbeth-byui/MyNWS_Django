from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import requests

def config(request):
    """
    This function will be called when I open http://server/current/config
    """
    if "station_code" in request.session:
        station_code = request.session["station_code"]
    else:
        station_code = ""
    if "units" in request.session:
        units = request.session["units"]
    else:
        units = ""
    values = {'curr_station_code' : station_code,
              'curr_units' : units}
    return render(request, 'current/config.html', values)    

def save_config(request):
    """
    This function processes the GET form from the config page.
    """
    if "station_code" in request.GET:
        request.session["station_code"] = request.GET["station_code"]
    if "units" in request.GET:
        request.session["units"] = request.GET["units"]
    return HttpResponseRedirect(reverse("index"))

def index(request):
    """
    This function will be called when I open http://server/current
    """
    if "station_code" in request.session:
        station_code = request.session["station_code"]
    else:
        station_code = None
    if "units" in request.session:
        units = request.session["units"]
    else:
        units = None

    if station_code is not None:
        req = requests.get("https://api.weather.gov/stations/{}/observations/latest".format(station_code))
        data = req.json()
        if "properties" in data and "temperature" in data["properties"] and "value" in data["properties"]["temperature"]:
            temp = float(data["properties"]["temperature"]["value"])
            if units == "F":
                temp = (temp * 9 / 5) + 32
            values = {'temp' : "{:.2f} {}".format(temp, units), 'station' : station_code}
        else:
            values = {'temp' : "", 'station' : "Need to select valid station."}
    else:
        values = {'temp' : "", 'station' : "Need to select station."}

    return render(request, 'current/index.html', values)
