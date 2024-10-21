from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from .models import *
from datetime import datetime
import pytz
from .utils import *
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', block=True)
def landingpage(request):
    if request.method == "POST":
        code = request.POST["code"]
        usrLat = request.POST["latitude"]  # will return wgs84 coordinates
        usrLng = request.POST["longitude"]
        # print("coordinates: ", usrLat, usrLng) #debugging purposes
        if usrLat == "" or usrLng == "":
            return render(
                request,
                "html/intro.html",
                {
                    "msg": "Error: Please enable location services or contact a PR member for help"
                },
            )
        try:
            fastLat = 24.8568301094953  # wgs84 coordinates
            fastLng = 67.2641877044029
            # these are the coordinates b/w CS and EE building
            distance = WGS84_Distance_Calc(fastLat, fastLng, usrLat, usrLng)
            record = DevDayAttendance.objects.get(att_code=code)
            try:
                currentTime = datetime.now()
                eventDetails = Event.objects.get(competitionName=record.Competition)
                currentDate = currentTime.strftime("%Y-%m-%d")
                currentTime = currentTime.strftime("%H:%M:%S")
                event_start_time = eventDetails.start_time.strftime("%H:%M:%S")
                event_end_time = eventDetails.end_time.strftime("%H:%M:%S")
                eventDate = eventDetails.start_time.strftime("%Y-%m-%d")
                if(eventDate != currentDate):
                    return render(
                        request,
                        "html/intro.html",
                        {"msg": "Error: Competition has not started yet"},
                    )
                if currentTime < event_start_time:
                    return render(
                        request,
                        "html/intro.html",
                        {"msg": "Error: Competition has not started yet"},
                    )
                elif currentTime > event_end_time:
                    return render(
                        request,
                        "html/intro.html",
                        {"msg": "Error: Competition has ended"},
                    )
            except:
                return render(
                    request,
                    "html/intro.html",
                    {"msg": "Error: Competition details not found"},
                )
            if distance > 1000:  # a kilometer
                return render(
                    request,
                    "html/intro.html",
                    {"msg": "Error: You are not in the vicinity of the event"},
                )
                
            try: 
                if record.attendance:
                    msg = "Your attendance has already been marked"
                else:
                    msg = "Your attendance has been marked."
                    record.attendance = True
                    record.save()

                return render(
                    request,
                    "html/success.html",
                    {"msg": msg, "teamName": record.Team_Name},
                )
            except: 
                return render(
                    request, "html/intro.html", {"msg": "Error: Oops an error occurred. Please try again or contact a PR member for help."}
                )
        except:
            return render(request, "html/intro.html", {"msg": "Error: Incorrect code"})

    return render(request, "html/intro.html", {"msg": ""})


def page_not_found_404(request, exception=404):
    return render(
        request,
        "html/404.html",
        status=404,
    )

def limit_exceed_403(request, exception=403):
    return render(
        request,
        "html/403.html",
        status=403,
    )