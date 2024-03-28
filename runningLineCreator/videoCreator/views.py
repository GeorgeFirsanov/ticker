from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from videoCreator.creator.ticker import create_running_line
import os
# Create your views here.
def index(request):
    return HttpResponse("<h2>Видео будет в разрешении 512x512 пикселей и длительностью 3 секунды</h2>")

def vsend(request, message):
    create_running_line(message)
    path = './/videoCreator//creator//videos//'
    fullname = path + message +'.mp4'
    file = FileWrapper( open( fullname, 'rb') )
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
    os.remove(fullname)
    return response

    return HttpResponse("Видео [" + message + ".mp4] будет в разрешении 512x512 пикселей и длительностью 3 секунды")
