from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_barang_mywatchlist = MyWatchList.objects.all()
    context = {
        'list_watch' : data_barang_mywatchlist,
        'nama' : 'Teuku Gevin Taufan',
        'student_id' : '2106750104',
    }
    return render(request, "mywatchlist.html", context)

# Mengembalikan data dalam bentuk xml
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

# Mengembalikan data dalam bentuk json
def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
