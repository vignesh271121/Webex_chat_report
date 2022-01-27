# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import datetime
import xlsxwriter

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

def web_chat(url_val,bear_auth,month_check,room_data_get,year_val_get):

    get_date_list = []
    get_Id_list = []
    get_parentID_list = []

    response = requests.get(url_val, auth=BearerAuth(bear_auth))
    print(response.status_code)

    if response.status_code == 401:
        message = 'Fail_server'
        return message
    else:
        data = response.json()
        #print(data['items'])

        for i in range(len(data['items'])):
            k = str(data['items'][i]['created'])
            month_val = k.split('-')
            if month_val[1] == str(month_check):
                get_date_list.append(data['items'][i]['created'])
                get_Id_list.append(data['items'][i]['id'])
                if "parentId" in data['items'][i]:
                    get_parentID_list.append(data['items'][i]['parentId'])

        get_date_list.reverse()
        get_parentID_list.reverse()
        get_Id_list.reverse()

        month_number = str(month_check)
        datetime_object = datetime.datetime.strptime(month_number, "%m")
        month_name = datetime_object.strftime("%b")

        workbook = xlsxwriter.Workbook(
            'folder_path/' + room_data_get + "_" + month_name + str(
                year_val_get) + '.xlsx')
        worksheet = workbook.add_worksheet(month_name + str(year_val_get))

        row = 0
        col = 0
        heading_list = ['Date', 'Email of question', 'Domain', 'Question asked', 'Room', 'Answered by', 'Answer Given']
        count = 0
        for title in (heading_list):
            worksheet.write(row, col + count, title)
            count = count + 1
        row += 1

        for k in get_Id_list:
            for j in range(len(data['items'])):
                if k == data['items'][j]['id']:
                    print("=============================================================")
                    print("------------------Question------------------------")
                    print(data['items'][j]['created'])
                    split_date = str(data['items'][j]['created'])
                    date_val = split_date.split('T')
                    print(date_val[0])
                    worksheet.write(row, col, date_val[0])
                    print(data['items'][j]['personEmail'])
                    worksheet.write(row, col + 1, data['items'][j]['personEmail'])
                    worksheet.write(row, col + 2, " ")
                    if "text" in data['items'][j]:
                        print(data['items'][j]['text'])
                        worksheet.write(row, col + 3, data['items'][j]['text'])
                    worksheet.write(row, col + 4, room_data_get)
                    for l in range(len(data['items'])):
                        if "parentId" in data['items'][l]:
                            if data['items'][l]['parentId'] == k:
                                print("------------------Answer------------------------")
                                print(data['items'][l]['personEmail'])
                                worksheet.write(row, col + 5, data['items'][l]['personEmail'])
                                if "text" in data['items'][l]:
                                    print(data['items'][l]['text'])
                                    worksheet.write(row, col + 6, data['items'][l]['text'])
                                row += 1
        workbook.close()

        get_date_list.clear()
        get_Id_list.clear()
        get_parentID_list.clear()

        filename_val = room_data_get + "_" + month_name + str(year_val_get)
        return filename_val


def download(room_get_data,get_date,get_bear_token):
    room_data = room_get_data
    date = get_date+'-01'
    print(date)
    datee = datetime.datetime.strptime(date, "%Y-%m-%d")
    month_change = datee.replace(month=int(datee.month) + 1)
    dat_str = str(month_change)
    final_date = dat_str.split(" ")
    month = int(datee.month)
    year_val = int(datee.year)
    if month<10:
        month="0"+str(month)
    if month=="00":
        month="12"
    print(month)
    url_get_data = ''
    date_format_value = final_date[0]+'T00:00:00.000Z'
    print(date_format_value)
    bear_token = get_bear_token
    if room_data == "support":
        url_get_data ='https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl&before='+date_format_value+'&max=1000'
    elif room_data == "program":
        url_get_data ='https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYzQ2OTk3NTAtZGIyNy0xMWU1LWI0ZjQtZmJmMjI3Y2ZmYWYz&before='+date_format_value+'&max=1000'
    file_list_name = web_chat(url_get_data,bear_token,month,room_data,year_val)

    if file_list_name == 'Fail_server':
        alert_msg = 'false'
        return alert_msg
    else:
        return file_list_name
