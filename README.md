# Webex Chat Report
#### Webex_data_generate
This repo is used for generating the WebEx Chat report from two DevNet public rooms namely Support and Program rooms in Excel format

## Requirements
- Python
- Django framework

## How to Install and Run This App
### _Step 1:_
- Make sure Python is installed on your workstation
- If you dont have it, you can get it here ---> [https://www.python.org/downloads/]
### _Step 2:_
- Start by making sure you're logged into GitHub. 
- click the Fork button in the upper-right hand corner of this page [https://github.com/vignesh271121/Webex_chat_report] and follow the prompts.
### _Step 3:_
- Clone this repo. Click the green code button and copy the URL listed under 'HTTPS'.
- Now go to you IDE, such as VS Code, PyCharm or Atom, find a place to clone it and type 'git clone' plus the URL you just copied. 
- For example 'git clone https://github.com/vignesh271121/Webex_chat_report
### _Step 4:_
- Create a virtual environment. cd into the Webex_data_generate folder. Type 'python -m venv venv' or 'python3 -m venv venv' and then 'source venv/bin/activate' for Mac and Linix or 'source venv/scripts/activate' on Windows. 
- You'll know it worked when you see '(venv)' at the beginning of your command prompt.
### _Step 5:_
- Install the requirements. Type 'pip intall -r requirements.txt' or 'pip3 intall -r requirements.txt'

### Requirements.txt

```sh
asgiref==3.4.1
certifi==2021.10.8
charset-normalizer==2.0.10
cycler==0.11.0
Django==4.0.1
et-xmlfile==1.1.0
fonttools==4.28.5
idna==3.3
kiwisolver==1.3.2
matplotlib==3.5.1
numpy==1.22.1
openpyxl==3.0.9
packaging==21.3
requests==2.7.0
six==1.16.0
sqlparse==0.4.2
tzdata==2021.5
urllib3==1.26.7
XlsxWriter==3.0.2
```
### _Step 6:_
- Edit the download location. Open the file report_App/report_download.py and on around line 47, replace 'Enter your Path folder' with the folder of your choice for the Excel report to be placed.
- Make sure that folder is created and present with full path.
```sh
workbook = xlsxwriter.Workbook(
            'folder_path/' + room_data_get + "_" + month_name + str(
                year_val_get) + '.xlsx')
        worksheet = workbook.add_worksheet(month_name + str(year_val_get))
```

### report_App/report_download.py
```sh
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
```

### _Step 7:_
- Run the app. From the Webex_data_generate folder, run the command 'python manage.py runserver' or 'python3 manage.py runserver' and use your web browser go to the URL presented in the terminal, such as http://127.0.0.1:8000/. 
- You'll find your authentication token here (https://developer.webex.com/docs/getting-started). 

```sh
url_get_data ='https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl&before='+date_format_value+'&max=1000'
url_get_data ='https://webexapis.com/v1/messages?roomId=Y2lzY29zcGFyazovL3VzL1JPT00vYzQ2OTk3NTAtZGIyNy0xMWU1LWI0ZjQtZmJmMjI3Y2ZmYWYz&before='+date_format_value+'&max=1000'
```

### Get data Json response

```sh
{
  "items": [
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvN2UyOTUwNDAtN2YwYS0xMWVjLWFlZTEtMjUwZjQ4ZjY4OGNk",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Hello. I'm trying to utilize capabilities from the IOS-XE 17.3 YANG schema but I'm running a Cisco 3850 IOS 16.9. How can I utilize the 17.3 schema if the latest IOS for the 3850 is 16.12?",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iMjI2NWJlNS03ZGY4LTQzNTEtYjYyMC1kOGJkZTYxM2FiNTc",
      "personEmail": "#############",
      "created": "2022-01-27T00:45:58.468Z",
      "updated": "2022-01-27T00:50:16.145Z"
    }
   
```


