from django.shortcuts import render
from . import report_download

def index(request):
    return render(request,'excel_report.html')

def download_data(request):
    if request.method == "POST":
        token_Get = str(request.POST.get("token"))
        date_Get = str(request.POST.get("date_val"))
        room_id_Get = str(request.POST.get("room_id"))
        download_file = report_download.download(room_id_Get,date_Get,token_Get,)

        if download_file == 'false':
            return render(request, 'excel_report.html', {'alert_flag': "True", 'file_name': 'please find this URL[https://developer.webex.com/docs/getting-started] to get a valid Token'})
        else:
            return render(request, 'excel_report.html',{'alert_flag': "True",'file_name':download_file})
    else:
        return render(request, 'excel_report.html')
