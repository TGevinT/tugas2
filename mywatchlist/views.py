from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers
import operator

# Create your views here.
def show_mywatchlist(request):
    data_barang_mywatchlist = MyWatchList.objects.all()
    data_barang_mywatchlist = sorted(data_barang_mywatchlist, key=operator.attrgetter('pk'))
    sudah_nonton = 0
    belum_nonton = 0
    for list in data_barang_mywatchlist:
        if (list.watched) :
            sudah_nonton += 1
        else:
            belum_nonton += 1
    if (sudah_nonton >= belum_nonton):
        kesimpulan = "1"
    else:
        kesimpulan = "0"
            
    context = {
        'list_watch' : data_barang_mywatchlist,
        'nama' : 'Teuku Gevin Taufan',
        'student_id' : '2106750104',
        'kesimpulan' : kesimpulan
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
