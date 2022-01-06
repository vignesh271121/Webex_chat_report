from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . import report_download


def index(request):
    return render(request,'excel_report.html')

def download_data(request):
    if request.method == "POST":
        token_Get = str(request.POST.get("token"))
        date_Get = str(request.POST.get("date_val"))
        room_id_Get = str(request.POST.get("room_id"))
        report_download.download(room_id_Get,date_Get,token_Get,)
        return render(request, 'excel_report.html')
    else:
        return render(request, 'excel_report.html')