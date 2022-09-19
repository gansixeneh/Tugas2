from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_html(request):
    data_mywatchlist = MyWatchList.objects.all()

    if(MyWatchList.objects.filter(watched="True").count() >= 
        MyWatchList.objects.filter(watched="False").count()):
    
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"

    context = {
        'list_mywatchlist': data_mywatchlist,
        'final_message': message
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
