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
      "personEmail": "levi.r.ingersoll@gmail.com",
      "created": "2022-01-27T00:45:58.468Z",
      "updated": "2022-01-27T00:50:16.145Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMTAwOTk3NjAtN2YwOS0xMWVjLTg3ZmMtMDM2OGYyM2M0YWJk",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "hola ",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zODUzNGQ4YS04NjFiLTRiOGUtYmZkNi01NTlhZjQxMzAwYWI",
      "personEmail": "callcenterext110@gmail.com",
      "created": "2022-01-27T00:35:44.214Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZDI3NTkwMTEtN2VmNS0xMWVjLTlmNzUtNjk0MmYzZjUzYWNm",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "I found out in the SDWAN API, that these two URIs get the same information. It is assumed that when I make the call with the first URI it brings me all the devices and with the second URI I should get ONLY the devices associated with (policyid). But when I put the {policyId} to filter the devices associated with this policy it doesn't do it, it keeps getting all the devices on the network, could this be an API failure?",
      "files": [
        "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvZDI3NTkwMTEtN2VmNS0xMWVjLTlmNzUtNjk0MmYzZjUzYWNmLzA"
      ],
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lYmEwOWEzYy0xMDk5LTRjMGYtOGYzNC01OTU4ODcxMDkxNDc",
      "personEmail": "Randy.ROZO@LA.LOGICALIS.COM",
      "created": "2022-01-26T22:18:00.465Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTU0NjZlYTAtN2VlZS0xMWVjLThhNWMtODc1ZTA1ZTZkYTUx",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Hi everyone,\n\nMake the following call /template/device/object/{templateId} to the SDWAN API to get all the Features that the Device Template has, but in the additional Templae I don't get the Policy Template. How can I get it and know which Device Template is using it?",
      "files": [
        "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvOTU0NjZlYTAtN2VlZS0xMWVjLThhNWMtODc1ZTA1ZTZkYTUxLzA",
        "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvOTU0NjZlYTAtN2VlZS0xMWVjLThhNWMtODc1ZTA1ZTZkYTUxLzE"
      ],
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lYmEwOWEzYy0xMDk5LTRjMGYtOGYzNC01OTU4ODcxMDkxNDc",
      "personEmail": "Randy.ROZO@LA.LOGICALIS.COM",
      "created": "2022-01-26T21:26:11.338Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTU3ZjRiMzAtN2VlOS0xMWVjLWFhODYtN2I0MTQ3NTQ0N2Fj",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "the customer would need to expose the Remedy DB via a REST API, the UCCX script would just use REST calls to retrieve data, but it's not a \"database\" from the uccx script point of view, it's just a web api",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNmRlMWNlYS1mNjRmLTQ4NTEtODk0ZC1mZDhiZTJkM2E4Yzc",
      "personEmail": "sascha@ateasystems.com",
      "created": "2022-01-26T20:50:24.227Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZmQzYjU4MDAtN2VlOC0xMWVjLWIzZGMtYWJjMWRiMzdmODEz"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZmQzYjU4MDAtN2VlOC0xMWVjLWIzZGMtYWJjMWRiMzdmODEz",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "I saw this, however, there is no reference to any requirement to configure anything in the UCCX to connect to the Database.  Just to clarify, all I need are the REST commands in this script step.  No Database drivers, No DB read, no DB get, because this step provides fields to capture the data.  I will get with the customer and if I have any issues I will submit more inquiries.  Thank you very much.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yYjAwZDljMC00ZjE4LTRiOTQtYTBkMi0zOTg2NDg1NmEyNzQ",
      "personEmail": "rguenther@skyline-ats.com",
      "html": "<p>I saw this, however, there is no reference to any requirement to configure anything in the UCCX to connect to the Database.  Just to clarify, all I need are the REST commands in this script step.  No Database drivers, No DB read, no DB get, because this step provides fields to capture the data.  I will get with the customer and if I have any issues I will submit more inquiries.  Thank you very much.</p>",
      "created": "2022-01-26T20:46:08.768Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZTU4MjFjNTAtN2VlNi0xMWVjLWJhMWYtMTNhZGFhODRjMzJh",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "see the link I replied earlier..",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNmRlMWNlYS1mNjRmLTQ4NTEtODk0ZC1mZDhiZTJkM2E4Yzc",
      "personEmail": "sascha@ateasystems.com",
      "created": "2022-01-26T20:31:09.973Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYmYwNjFlZjAtN2VlNi0xMWVjLWI2MWYtMzUwZmQ1YTY3MjQ2"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYmYwNjFlZjAtN2VlNi0xMWVjLWI2MWYtMzUwZmQ1YTY3MjQ2",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Yes.  I need to do this from a script.  The customer calls in and the script requests the ticket number.  The UCCX then retrieves the information about the case from the Remedy Database.  Then presents that information to the Finesse desktop.  I have it working perfectly using the JDBC.  But, the customer wants to use REST commands.  I need to know what script step accepts REST commands and learn the syntax of the REST commands.  Thank you",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yYjAwZDljMC00ZjE4LTRiOTQtYTBkMi0zOTg2NDg1NmEyNzQ",
      "personEmail": "rguenther@skyline-ats.com",
      "html": "<p>Yes.  I need to do this from a script.  The customer calls in and the script requests the ticket number.  The UCCX then retrieves the information about the case from the Remedy Database.  Then presents that information to the Finesse desktop.  I have it working perfectly using the JDBC.  But, the customer wants to use REST commands.  I need to know what script step accepts REST commands and learn the syntax of the REST commands.  Thank you</p>",
      "created": "2022-01-26T20:30:05.407Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOTViZTdiNDAtN2VlMi0xMWVjLWE3YmQtYjUwNzNhYjkxMWUx",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Please refer to page 2-189",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mYjc5ZDAwZS1jMThhLTQ4OTEtYjMwMi1lNTMwZTQyZDAyOGQ",
      "personEmail": "rticer@team-sos.com",
      "created": "2022-01-26T20:00:18.164Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNzgwNGUxZDAtN2VlMS0xMWVjLTkyZDMtMGY3YzM4MmIwMmRi"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNjM3ODliYzAtN2VlMi0xMWVjLTk3NDEtYzliYmUwMGUzN2Qw",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "https://www.cisco.com/c/dam/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_11_0/programming/guide/EditorSeriesVol2.pdf",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mYjc5ZDAwZS1jMThhLTQ4OTEtYjMwMi1lNTMwZTQyZDAyOGQ",
      "personEmail": "rticer@team-sos.com",
      "created": "2022-01-26T19:58:53.820Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNzgwNGUxZDAtN2VlMS0xMWVjLTkyZDMtMGY3YzM4MmIwMmRi"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMmFlMTRkYzAtN2VlMi0xMWVjLTliNzQtODVjYTA5YWY4OTM1",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Please refer to \"Provision of Database Subsystem\" on page 151",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mYjc5ZDAwZS1jMThhLTQ4OTEtYjMwMi1lNTMwZTQyZDAyOGQ",
      "personEmail": "rticer@team-sos.com",
      "created": "2022-01-26T19:57:18.876Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNzgwNGUxZDAtN2VlMS0xMWVjLTkyZDMtMGY3YzM4MmIwMmRi"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjBkZDVlOTAtN2VlMi0xMWVjLWIyOTMtYmJhNzY3Y2ExMTBk",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "https://www.cisco.com/c/en/us/td/docs/voice_ip_comm/cust_contact/contact_center/crs/express_12_5/maintain_and_operate/guide/uccx_b_uccx-125admin-and-operations-guide.pdf",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9mYjc5ZDAwZS1jMThhLTQ4OTEtYjMwMi1lNTMwZTQyZDAyOGQ",
      "personEmail": "rticer@team-sos.com",
      "created": "2022-01-26T19:57:02.073Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNzgwNGUxZDAtN2VlMS0xMWVjLTkyZDMtMGY3YzM4MmIwMmRi"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYzEwZmVhZjAtN2VlMS0xMWVjLTlkYmItZjlkZWNiYjBlZDk0",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "do you need to use it from a ccx script?",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNmRlMWNlYS1mNjRmLTQ4NTEtODk0ZC1mZDhiZTJkM2E4Yzc",
      "personEmail": "sascha@ateasystems.com",
      "created": "2022-01-26T19:54:21.343Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNzgwNGUxZDAtN2VlMS0xMWVjLTkyZDMtMGY3YzM4MmIwMmRi"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOWI2M2U3YzAtN2VlMS0xMWVjLWFkZGUtNDc1ZjhkOWQxYzEy",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "https://developer.cisco.com/docs/contact-center-express/#!make-rest-call/make-rest-call-properties",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yNmRlMWNlYS1mNjRmLTQ4NTEtODk0ZC1mZDhiZTJkM2E4Yzc",
      "personEmail": "sascha@ateasystems.com",
      "created": "2022-01-26T19:53:18.140Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNzgwNGUxZDAtN2VlMS0xMWVjLTkyZDMtMGY3YzM4MmIwMmRi"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNzgwNGUxZDAtN2VlMS0xMWVjLTkyZDMtMGY3YzM4MmIwMmRi",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Hello, onsite at a customer with a UCCX application.  They are using Remedy as their ticketing application.  The UCCX needs to retrieve ticket information from the Remedy Database using REST commands.  I have researched the UCCX development documents, REST API documents, forums, Cisco community, and all the information pertains to sending REST API commands TO the UCCX.  Nothing talks about sending REST API commands FROM the UCCX.  Also, all Database references are for JDBC drivers.  Could someone direct me to some examples or documents explaining how the UCCX can use REST API commands to retrieve data from an external Database.  Thank you",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8yYjAwZDljMC00ZjE4LTRiOTQtYTBkMi0zOTg2NDg1NmEyNzQ",
      "personEmail": "rguenther@skyline-ats.com",
      "html": "<p>Hello, onsite at a customer with a UCCX application.  They are using Remedy as their ticketing application.  The UCCX needs to retrieve ticket information from the Remedy Database using REST commands.  I have researched the UCCX development documents, REST API documents, forums, Cisco community, and all the information pertains to sending REST API commands TO the UCCX.  Nothing talks about sending REST API commands FROM the UCCX.  Also, all Database references are for JDBC drivers.  Could someone direct me to some examples or documents explaining how the UCCX can use REST API commands to retrieve data from an external Database.  Thank you</p>",
      "created": "2022-01-26T19:52:18.797Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNGY4MDdkMzAtN2VkNC0xMWVjLTg3ZWItNDVkN2ZlZjdlZWVl",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "On Windows, I believe it's possible to configure Jabber to use the user's Windows login credentials to sign into Jabber automatically when it is started; however that won't really solve your UE metrics requirements.  The Jabber client itself does not have an API for automating its operations/UI, AFAIK.  If this is for testing/QA, then one of several tools for automating/scripting Windows UI testing would probably work, e..g this Stack Overflow thread.  Not sure if such a solution would work for end-user desktops - opening a whole new can of worms 😉",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9lMzg2NTNmYS02NTYxLTRlMjctYWVkNS1mMmM5ZWE1OTAzYTI",
      "personEmail": "dstaudt@cisco.com",
      "html": "<p>On Windows, I believe it&apos;s possible to configure Jabber to use the user&apos;s Windows login credentials to sign into Jabber automatically when it is started; however that won&apos;t really solve your UE metrics requirements.  The Jabber client itself does not have an API for automating its operations/UI, AFAIK.  If this is for testing/QA, then one of several tools for automating/scripting Windows UI testing would probably work, e..g this <a href=\"https://stackoverflow.com/questions/9698512/driving-a-windows-gui-program-from-a-script\" alt=\"https://stackoverflow.com/questions/9698512/driving-a-windows-gui-program-from-a-script\" onclick=\"return sparkBase.clickEventHandler(event);\">Stack Overflow thread</a>.  Not sure if such a solution would work for end-user desktops - opening a whole new can of worms 😉</p>",
      "created": "2022-01-26T18:18:07.363Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNGRlMDU3MzAtN2VkMy0xMWVjLWE2ZWQtNGI1OTM0MjYxNDg4"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNGRlMDU3MzAtN2VkMy0xMWVjLWE2ZWQtNGI1OTM0MjYxNDg4",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Hello there, Is there a way (automate via API or other similar means) to remotely control a Jabber phone for login? Customer is looking to have some way to run a macro that launches Jabber and signs into it. Possibly record how long it takes and if it passes or fails?",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xZThkYWM2Yi0wMzQxLTRkYjctYTBjOS05ZjhmZjZlMTI0NGE",
      "personEmail": "agaur1@cisco.com",
      "created": "2022-01-26T18:10:55.139Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYThmZmM2NjEtN2VjMy0xMWVjLTlmOTEtYjM1Mjg3OGY5MDkw",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "👍",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iMTdlNWRiNS03OWJhLTRlM2MtYmU1ZC1kNGU0YTk2OTUxODc",
      "personEmail": "rosacket@cisco.com",
      "html": "<h1><p>👍</p></h1>",
      "created": "2022-01-26T16:18:56.070Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMTNlMzhhNjAtNzk3MC0xMWVjLTk0ZDAtYzE0NTkxMjIwMDNm"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMzQ2MTMwZjAtN2VjMy0xMWVjLTlmZjMtZDcxODAzYTJmMjYx",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Rob Sackett reaching out to you one to one. ",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hMjg1ZDgzNS0wYzYzLTQ0NGQtOWYzMy0zZGNmOTFiYzM4ZTI",
      "personEmail": "jfloriol@cisco.com",
      "html": "<p><spark-mention data-object-type=\"person\" data-object-id=\"Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iMTdlNWRiNS03OWJhLTRlM2MtYmU1ZC1kNGU0YTk2OTUxODc\">Rob Sackett</spark-mention> reaching out to you one to one. </p>",
      "mentionedPeople": [
        "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iMTdlNWRiNS03OWJhLTRlM2MtYmU1ZC1kNGU0YTk2OTUxODc"
      ],
      "created": "2022-01-26T16:15:40.415Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMTNlMzhhNjAtNzk3MC0xMWVjLTk0ZDAtYzE0NTkxMjIwMDNm"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNjkzYjUxNTAtN2UzZS0xMWVjLWExNmQtNzcxMTVhNDE5NzA2",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Hi James Floriolli. Do you have an update on the status of the new ticket you created (106638)? I'll be meeting with partner AT&T Wednesday, and they'll be asking about this one as the customer originally went to them before being directed to Developer Support per the Help documentation. ",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iMTdlNWRiNS03OWJhLTRlM2MtYmU1ZC1kNGU0YTk2OTUxODc",
      "personEmail": "rosacket@cisco.com",
      "html": "<p>Hi <spark-mention data-object-type=\"person\" data-object-id=\"Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hMjg1ZDgzNS0wYzYzLTQ0NGQtOWYzMy0zZGNmOTFiYzM4ZTI\">James Floriolli</spark-mention>. Do you have an update on the status of the new ticket you created (106638)? I&apos;ll be meeting with partner AT&amp;T Wednesday, and they&apos;ll be asking about this one as the customer originally went to them before being directed to Developer Support per the Help documentation. </p>",
      "mentionedPeople": [
        "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hMjg1ZDgzNS0wYzYzLTQ0NGQtOWYzMy0zZGNmOTFiYzM4ZTI"
      ],
      "created": "2022-01-26T00:25:06.021Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMTNlMzhhNjAtNzk3MC0xMWVjLTk0ZDAtYzE0NTkxMjIwMDNm"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYmEyMjcyODAtN2UzYy0xMWVjLWFlZTEtMjUwZjQ4ZjY4OGNk",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "I did it! and woks fine. Thank you👍",
      "files": [
        "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvYmEyMjcyODAtN2UzYy0xMWVjLWFlZTEtMjUwZjQ4ZjY4OGNkLzA"
      ],
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hM2RiOTgyMS03ODY4LTQ3YjktYTRiMy00MGM2YThmNjNiMDg",
      "personEmail": "tkawagm@gmail.com",
      "created": "2022-01-26T00:13:02.760Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMzBmYmJiYjAtN2RmYi0xMWVjLWFiYWItMGI5YWRiNzBlMWE2",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Thank you, the issue is reported to the appropriate engineers. They say sandboxdnac.cisco.com is fine and will not fail for this so please go ahead.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8xZjkxMDAzZS0zNjdhLTRjZmEtYmI5Yy1kMDFlYjZmNjYxZmU",
      "personEmail": "alexstev@cisco.com",
      "created": "2022-01-25T16:23:55.371Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYjgwNTFmMjAtN2RlYy0xMWVjLWI3M2EtMjE5YjdmNTY5N2Y3",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "The other sandbox, sandboxdnac has a more recent version of DNA Center (2.2.2.3), which uses DNA Center REST API bundle with version (1.7.1). The sandboxdnac has the same credentials for devnetuser as  sandboxdnac2. The client-health API works there as expected.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jNzU4MDUxMS00YTE2LTRiMzgtYjJjNS03Y2JkZWI2YzIxMTE",
      "personEmail": "wastorga@altus.cr",
      "created": "2022-01-25T14:40:19.474Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYjFhYzg0YjAtN2RlYy0xMWVjLWFjYzUtYTM2Y2UzYWFjZDBm",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "I noticed that for sandboxdnac2.cisco, the UI assurance client health calls are also falling. Additionally, it displays the pop-up message \"No issue site hierarchy information found, please reach out to Administrator or try again.\". So it's fair to say that 'the API isn't working properly on sandboxdnac2.cisco.com'.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jNzU4MDUxMS00YTE2LTRiMzgtYjJjNS03Y2JkZWI2YzIxMTE",
      "personEmail": "wastorga@altus.cr",
      "created": "2022-01-25T14:40:08.827Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNjE2ZTVlNzAtN2RkMi0xMWVjLWJkMGYtNmZiMmUyMzkyYmNh",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "No worries, you will find a few folks in their on the same journey as yourself for the exam. Good luck!",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zNjBjOTgwYi1iMzBiLTQ0YzctODI4OS0zNGI4ODc4ZmVhMmI",
      "personEmail": "stuaclar@cisco.com",
      "created": "2022-01-25T11:31:47.287Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMzNhMTVjZTAtN2RkMi0xMWVjLTk5NDQtMzc0MWQyYTJkNWY5",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Oh, kindly thank you!\nI'll look for a similar issue👍",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hM2RiOTgyMS03ODY4LTQ3YjktYTRiMy00MGM2YThmNjNiMDg",
      "personEmail": "tkawagm@gmail.com",
      "created": "2022-01-25T11:30:30.446Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYWQwMmM3MDAtN2RkMS0xMWVjLWExM2YtMDMzNzdkNzU2Y2Ux",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "You could also check/ask in the DevNet Certifications Community https://learningnetwork.cisco.com/s/topic/0TO3i0000008jY5GAI/devnet-certifications-community to see if anyone studying for the exam has ran into this issue too.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zNjBjOTgwYi1iMzBiLTQ0YzctODI4OS0zNGI4ODc4ZmVhMmI",
      "personEmail": "stuaclar@cisco.com",
      "html": "<p>You could also check/ask in the DevNet Certifications Community <code class=\"language-none\">https://learningnetwork.cisco.com/s/topic/0TO3i0000008jY5GAI/devnet-certifications-community</code> to see if anyone studying for the exam has ran into this issue too.</p>",
      "created": "2022-01-25T11:26:44.592Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYjZlMWU1OTAtN2RkMC0xMWVjLWFkZGUtNDc1ZjhkOWQxYzEy",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Yeah. Thank you for your reply😊",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hM2RiOTgyMS03ODY4LTQ3YjktYTRiMy00MGM2YThmNjNiMDg",
      "personEmail": "tkawagm@gmail.com",
      "created": "2022-01-25T11:19:51.657Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMmFhNGRkODAtN2RkMC0xMWVjLWFjMmQtNDVmYmFhYzY2ODY0",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "I do not have enough experience with DNA Centre assurance or the ask in the OCG. As you noted all other API calls are ok.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zNjBjOTgwYi1iMzBiLTQ0YzctODI4OS0zNGI4ODc4ZmVhMmI",
      "personEmail": "stuaclar@cisco.com",
      "created": "2022-01-25T11:15:56.376Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZWZlYmI2NjAtN2RjZS0xMWVjLThhNWMtODc1ZTA1ZTZkYTUx",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Well... is it okay to understand that this API isn't working properly on sandboxdnac2.cisco.com?\nI just tried the example in the Cisco Certified DevNet Associate Official Cert Guide.\n\nBy the way, this API works fine...\nhttps://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device",
      "files": [
        "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvNTc2ZWJjNjAtN2RjZi0xMWVjLWJlOTAtNzU0YWIyNWE0ZWFlLzA"
      ],
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hM2RiOTgyMS03ODY4LTQ3YjktYTRiMy00MGM2YThmNjNiMDg",
      "personEmail": "tkawagm@gmail.com",
      "html": "<p>Well... is it okay to understand that this API isn&apos;t working properly on <a href=\"https://sandboxdnac2.cisco.com\">sandboxdnac2.cisco.com</a>?<br/>I just tried the example in the Cisco Certified DevNet Associate Official Cert Guide.<br/><br>By the way, this API works fine...<br/>https://sandboxdnac2.cisco.com/dna/intent/api/v1/network-device</p>",
      "created": "2022-01-25T11:07:08.358Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh",
      "updated": "2022-01-25T11:10:02.022Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvN2E4YTIzNDAtN2RjNy0xMWVjLTk2MzctYTE4YzhiOTk4NjQ2",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "I tried your example on sandboxdnac.cisco.com which run code Cisco DNA Center AO 2.2 and got\n\n{\n    \"errorMessage\": \"Timestamp is invalid. Please provide a valid timestamp in milliseconds\"\n}\n\nI then tried the other sandbox with the following and this is ok.\n\nhttps://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology\nhttps://{{dnac}}:{{port}}/dna/intent/api/v1/client-health?timestamp=1539408888000\n",
      "files": [
        "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvN2E4YTIzNDAtN2RjNy0xMWVjLTk2MzctYTE4YzhiOTk4NjQ2LzA"
      ],
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zNjBjOTgwYi1iMzBiLTQ0YzctODI4OS0zNGI4ODc4ZmVhMmI",
      "personEmail": "stuaclar@cisco.com",
      "html": "<p>I tried your example on <code class=\"language-none\">sandboxdnac.cisco.com</code> which run code Cisco DNA Center AO 2.2 and got</p><pre><code class=\"language-none\">{\n    &quot;errorMessage&quot;: &quot;Timestamp is invalid. Please provide a valid timestamp in milliseconds&quot;\n}\n</code></pre><p>I then tried the other sandbox with the following and this is ok.</p><blockquote><p>https://devnetsandbox.cisco.com/RM/Diagram/Index/c3c949dc-30af-498b-9d77-4f1c07d835f9?diagramType=Topology</p></blockquote><pre><code class=\"language-none\">https://{{dnac}}:{{port}}/dna/intent/api/v1/client-health?timestamp=1539408888000\n</code></pre>",
      "created": "2022-01-25T10:13:44.948Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjUwOWMyNTAtN2RiMi0xMWVjLThhMDctMWQwZWZmMmJhMjZh",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Please help me.\nI'm currently experimenting with the DNA Center API using Postman in the DevNet Sandbox.  \nThe following API Request does not work.  \nWhy?  \nhttps://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health?timestamp=1566506489000  \n  \nThe response is below.  \n{  \n  \"response\": {  \n   \"errorCode\": 5000,  \n   \"message\": \"An internal has error occurred while processing this request.\",  \n   \"detail\": \"An internal has error occurred while processing this request.\"  \n  }  \n}  \n  \nX-Auth-Token is set in Headers.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9hM2RiOTgyMS03ODY4LTQ3YjktYTRiMy00MGM2YThmNjNiMDg",
      "personEmail": "tkawagm@gmail.com",
      "html": "<p>Please help me.<br/>I&apos;m currently experimenting with the DNA Center API using Postman in the DevNet Sandbox.  <br/>The following API Request does not work.  <br/>Why?  <br/><a href=\"https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health?timestamp=1566506489000\">https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health?timestamp=1566506489000</a>  <br/>  <br/>The response is below.  <br/>{  <br/>  &quot;response&quot;: {  <br/>   &quot;errorCode&quot;: 5000,  <br/>   &quot;message&quot;: &quot;An internal has error occurred while processing this request.&quot;,  <br/>   &quot;detail&quot;: &quot;An internal has error occurred while processing this request.&quot;  <br/>  }  <br/>}  <br/>  <br/>X-Auth-Token is set in Headers.</p>",
      "created": "2022-01-25T07:41:02.069Z",
      "updated": "2022-01-25T09:54:15.190Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYjM3YmM5ODAtN2QwNy0xMWVjLTkxMDMtZDU4MzhhMzk5OWY2",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "have replied to the ticket.. ",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iZDA4NTliMy04NWIwLTQ0MWYtYWRmMi1lNWMwNTExYzNlYWE",
      "personEmail": "gcheria@cisco.com",
      "created": "2022-01-24T11:20:57.112Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYTA1OTNhZjAtNzlmYS0xMWVjLWE4ZWItMmZhOTM2ZmIwNzJj"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNjMxMWQ5ODAtN2QwNy0xMWVjLWJkOTUtODViMzhjNmY4YTk0",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Would it be possible to make a call about this problem? Maybe you could debug it live?",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YzgwNWUwNS02ZmUyLTQ2NDItODE2NS0wYzU3ZTBjODVkZDg",
      "personEmail": "zygmunt.szefel@tenfold.com",
      "created": "2022-01-24T11:18:42.200Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYTA1OTNhZjAtNzlmYS0xMWVjLWE4ZWItMmZhOTM2ZmIwNzJj"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMWJlM2NkYzAtN2QwNy0xMWVjLTljOTUtMDViZTVmMzcxZTQy",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "no we got your ticket ",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iZDA4NTliMy04NWIwLTQ0MWYtYWRmMi1lNWMwNTExYzNlYWE",
      "personEmail": "gcheria@cisco.com",
      "created": "2022-01-24T11:16:42.780Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYTA1OTNhZjAtNzlmYS0xMWVjLWE4ZWItMmZhOTM2ZmIwNzJj"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMTg3ZjFlZjAtN2QwNy0xMWVjLWFkZGUtNDc1ZjhkOWQxYzEy",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "https://devnetsupport.cisco.com/hc/en-us/requests/5705",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YzgwNWUwNS02ZmUyLTQ2NDItODE2NS0wYzU3ZTBjODVkZDg",
      "personEmail": "zygmunt.szefel@tenfold.com",
      "created": "2022-01-24T11:16:37.087Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYTA1OTNhZjAtNzlmYS0xMWVjLWE4ZWItMmZhOTM2ZmIwNzJj"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMGQ2ZTdhYjAtN2QwNy0xMWVjLWFkZGUtNDc1ZjhkOWQxYzEy",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "hmm, no, it is ok, I see it after logging in again.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YzgwNWUwNS02ZmUyLTQ2NDItODE2NS0wYzU3ZTBjODVkZDg",
      "personEmail": "zygmunt.szefel@tenfold.com",
      "created": "2022-01-24T11:16:18.523Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYTA1OTNhZjAtNzlmYS0xMWVjLWE4ZWItMmZhOTM2ZmIwNzJj"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZWZlOTY5NTAtN2QwNi0xMWVjLTk2MzctYTE4YzhiOTk4NjQ2",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "I posted it but unfortunately I wasn't logged in so I think I will lose track of this issue ;/",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YzgwNWUwNS02ZmUyLTQ2NDItODE2NS0wYzU3ZTBjODVkZDg",
      "personEmail": "zygmunt.szefel@tenfold.com",
      "created": "2022-01-24T11:15:28.997Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYTA1OTNhZjAtNzlmYS0xMWVjLWE4ZWItMmZhOTM2ZmIwNzJj"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZDNjNmMzOTAtN2QwNS0xMWVjLWFlZTEtMjUwZjQ4ZjY4OGNk",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Can you click on the button report a sandbox issue and open a ticket using this community forum url -https://community.cisco.com/t5/devnet-sandbox/bd-p/4426j-disc-dev-devnet-sandbox",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iZDA4NTliMy04NWIwLTQ0MWYtYWRmMi1lNWMwNTExYzNlYWE",
      "personEmail": "gcheria@cisco.com",
      "created": "2022-01-24T11:07:32.297Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYTA1OTNhZjAtNzlmYS0xMWVjLWE4ZWItMmZhOTM2ZmIwNzJj"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNzFjYzM2YzAtN2QwNS0xMWVjLWFiM2UtNTk3YjBkODU3NWIy",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "This is not useful for me. I would like to change from CLI the password of Application User who is not an Web admin.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YzgwNWUwNS02ZmUyLTQ2NDItODE2NS0wYzU3ZTBjODVkZDg",
      "personEmail": "zygmunt.szefel@tenfold.com",
      "created": "2022-01-24T11:04:47.916Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvZDU3NmJjYzAtN2EwMC0xMWVjLWFkNmItMWQ1NTkwMzlhYmQ0"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjQ3MzU3NTAtN2QwNS0xMWVjLTg3NGMtMDUyMjZiZjM0YjVm",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "the password that I am trying to set on this sandbox is I think not trivial...:\nCisco123123@#sksdankdls\nI am attaching Default Credential Policy.\n",
      "files": [
        "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvMjQ3MzU3NTAtN2QwNS0xMWVjLTg3NGMtMDUyMjZiZjM0YjVmLzA"
      ],
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80YzgwNWUwNS02ZmUyLTQ2NDItODE2NS0wYzU3ZTBjODVkZDg",
      "personEmail": "zygmunt.szefel@tenfold.com",
      "created": "2022-01-24T11:02:38.149Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvYTA1OTNhZjAtNzlmYS0xMWVjLWE4ZWItMmZhOTM2ZmIwNzJj"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNDg2ZDBlZTAtN2NiZS0xMWVjLWExMjctMzdkOTExNjQ1ZDg5",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Thank you.   I have opened a case.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZThkYjM4ZS00ZjA0LTQwYTItYWQ4ZS1hYjljMTg0NmI5ODk",
      "personEmail": "doyler@cisco.com",
      "created": "2022-01-24T02:35:24.238Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjFiYjExZDAtN2MxOC0xMWVjLWJmMDItZGJmYmQzMzlhMzUw"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMDU4MDE1MzAtN2MyZi0xMWVjLTgxMmYtZTk1YzM1MjRkZjU2",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Hey David Oyler there was some issues with the licence on this sandbox. I would suggest opening a support ticket for this and see if the team can provide you with a estimate this will be places back in the reservation pod. HERE is the link.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS8zNjBjOTgwYi1iMzBiLTQ0YzctODI4OS0zNGI4ODc4ZmVhMmI",
      "personEmail": "stuaclar@cisco.com",
      "html": "<p>Hey <spark-mention data-object-type=\"person\" data-object-id=\"Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZThkYjM4ZS00ZjA0LTQwYTItYWQ4ZS1hYjljMTg0NmI5ODk\">David Oyler</spark-mention> there was some issues with the licence on this sandbox. I would suggest opening a support ticket for this and see if the team can provide you with a estimate this will be places back in the reservation pod. <a href=\"https://devnetsupport.cisco.com/hc/en-us/requests/new?ticket_form_id=1500002825161\" alt=\"https://devnetsupport.cisco.com/hc/en-us/requests/new?ticket_form_id=1500002825161\" onclick=\"return sparkBase.clickEventHandler(event);\">HERE</a> is the link.</p>",
      "mentionedPeople": [
        "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZThkYjM4ZS00ZjA0LTQwYTItYWQ4ZS1hYjljMTg0NmI5ODk"
      ],
      "created": "2022-01-23T09:29:53.923Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjFiYjExZDAtN2MxOC0xMWVjLWJmMDItZGJmYmQzMzlhMzUw"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNmYyY2QwNzAtN2MxOC0xMWVjLWFlZTEtNGYzNGQ1ZWM2ZGZj",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Anyone know if this sandbox setup for pyATS is going to be restored?",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZThkYjM4ZS00ZjA0LTQwYTItYWQ4ZS1hYjljMTg0NmI5ODk",
      "personEmail": "doyler@cisco.com",
      "created": "2022-01-23T06:48:12.791Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjFiYjExZDAtN2MxOC0xMWVjLWJmMDItZGJmYmQzMzlhMzUw"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNTk3YmFlZTAtN2MxOC0xMWVjLWE3ZTctZGRjNDcwZTkxOGFh",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "files": [
        "https://webexapis.com/v1/contents/Y2lzY29zcGFyazovL3VzL0NPTlRFTlQvNTk3YmFlZTAtN2MxOC0xMWVjLWE3ZTctZGRjNDcwZTkxOGFhLzA"
      ],
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZThkYjM4ZS00ZjA0LTQwYTItYWQ4ZS1hYjljMTg0NmI5ODk",
      "personEmail": "doyler@cisco.com",
      "created": "2022-01-23T06:47:36.398Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjFiYjExZDAtN2MxOC0xMWVjLWJmMDItZGJmYmQzMzlhMzUw"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvM2ViODJlODAtN2MxOC0xMWVjLThhZWQtYjlhNTM3ZWMxYzEx",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "The sandbox is coming back as invalid.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZThkYjM4ZS00ZjA0LTQwYTItYWQ4ZS1hYjljMTg0NmI5ODk",
      "personEmail": "doyler@cisco.com",
      "created": "2022-01-23T06:46:51.496Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjFiYjExZDAtN2MxOC0xMWVjLWJmMDItZGJmYmQzMzlhMzUw"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMzY3YjFjYTAtN2MxOC0xMWVjLWE3ZGYtNGQ3ODIyZjdjYjcy",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "https://devnetsandbox.cisco.com/RM/Diagram/Index/756b58ba-15aa-4228-8a41-f94f684330e7?diagramType=Topology",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZThkYjM4ZS00ZjA0LTQwYTItYWQ4ZS1hYjljMTg0NmI5ODk",
      "personEmail": "doyler@cisco.com",
      "created": "2022-01-23T06:46:37.674Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjFiYjExZDAtN2MxOC0xMWVjLWJmMDItZGJmYmQzMzlhMzUw"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjZmMzZmMzAtN2MxOC0xMWVjLTlmMmItNDc0MjQyNjRkOTRl",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "https://developer.cisco.com/docs/pyats/#!hands-on-learning/devnet-sandbox",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZThkYjM4ZS00ZjA0LTQwYTItYWQ4ZS1hYjljMTg0NmI5ODk",
      "personEmail": "doyler@cisco.com",
      "created": "2022-01-23T06:46:11.619Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjFiYjExZDAtN2MxOC0xMWVjLWJmMDItZGJmYmQzMzlhMzUw"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvMjFiYjExZDAtN2MxOC0xMWVjLWJmMDItZGJmYmQzMzlhMzUw",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Regarding pyATS Sandbox support",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS80ZThkYjM4ZS00ZjA0LTQwYTItYWQ4ZS1hYjljMTg0NmI5ODk",
      "personEmail": "doyler@cisco.com",
      "created": "2022-01-23T06:46:02.861Z"
    },
    {
      "id": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNWU1ODM2NzAtN2JiMS0xMWVjLTlmZDktMTNhZGFhODRjMzJh",
      "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vNGZlOTQ2MTAtZjA2MS0xMWU1LWI4Y2UtMTEzZjhkZmMxNGJl",
      "roomType": "group",
      "text": "Thanks a lot Hakan for explaining and clarifying. Much appreciated.",
      "personId": "Y2lzY29zcGFyazovL3VzL1BFT1BMRS81YTRjYTUxNi00YTg1LTRkMjUtYjUwYy1iOTE0ZTkzMzYzM2U",
      "personEmail": "qamber.ali10@gmail.com",
      "created": "2022-01-22T18:30:26.391Z",
      "parentId": "Y2lzY29zcGFyazovL3VzL01FU1NBR0UvNWQwZDM2NTAtN2JhNS0xMWVjLThhYzktMzc0MWQyYTJkNWY5"
    }
  ]
}
```


