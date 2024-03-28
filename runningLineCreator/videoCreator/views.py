from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from videoCreator.creator.ticker import create_running_line
from .models import TextQuery

import os

# Create your views here.
def index(request):
    all_messages = TextQuery.objects.values_list("name", flat=True)
    data = {"allTexts": all_messages}
    #return HttpResponse("<h2>Видео будет в разрешении 512x512 пикселей и длительностью 3 секунды</h2>")
    return render(request, "index.html", context=data)

def vsend(request, message):
    create_running_line(message)
    TextQuery.objects.create(name=message)

    path = './/videoCreator//creator//videos//'
    fullname = path + message +'.mp4'
    file = FileWrapper( open( fullname, 'rb') )
    response = HttpResponse(file, content_type='video/mp4')
    response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
    os.remove(fullname)
    return response

def postuser(request):
    # получаем из данных запроса POST отправленные через форму данные
    message = request.POST.get("name", "Undefined")
    response = vsend(request=request, message=message)
    return response