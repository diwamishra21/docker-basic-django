from django.http import HttpResponse
import datetime

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>Hello World. <br> It is now %s.</body></html>" % now
    return HttpResponse(html)
