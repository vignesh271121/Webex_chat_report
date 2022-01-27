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
#### Get Authentication
Webex REST API, an Authentication HTTP header is used to identify the requesting user. This header must include an access token. This access token may be a personal access token from this site (see below), a Bot token, or an OAuth token from an Integration or Guest Issuer application.

![image](https://user-images.githubusercontent.com/97229745/151295751-095ef3a3-04d1-4360-9a8f-dea174b132d4.png)

### excel_report.html

![image](https://user-images.githubusercontent.com/97229745/151295905-d88a3f66-c385-4a68-a60f-2ebbbf05a324.png)

### .#css
```sh
<style media="screen">
      *,
*:before,
*:after{
    padding: 0;
    margin: 0;
    box-sizing: border-box;
}
body{
    background-color: #080719;
    background-image: url({% static 'images/room_img.png'

}
.background{
    width: 430px;
    height: 520px;
    position: absolute;
    transform: translate(-50%,-50%);
    left: 50%;
    top: 50%;
}
.background .shape{
    height: 200px;
    width: 200px;
    position: absolute;
    border-radius: 50%;
}

form{
    height: 520px;
    width: 400px;
    background-color: rgba(255,255,255,0.13);
    position: absolute;
    transform: translate(-50%,-50%);
    top: 50%;
    left: 50%;
    border-radius: 10px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.1);
    box-shadow: 0 0 40px rgba(8,7,16,0.6);
    padding: 50px 35px;
}
form *{
    font-family: 'Poppins',sans-serif;
    color: #ffffff;
    letter-spacing: 0.5px;
    outline: none;
    border: none;
}
form h3{
    font-size: 32px;
    font-weight: 500;
    line-height: 42px;
    text-align: center;
}

label{
    display: block;
    margin-top: 30px;
    font-size: 16px;
    font-weight: 500;
}
input{
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(255,255,255,0.07);
    border-radius: 3px;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 300;
}
::placeholder{
    color: #e5e5e5;
}
button{
    margin-top: 50px;
    width: 100%;
    background-color: #ffffff;
    color: #080710;
    padding: 15px 0;
    font-size: 18px;
    font-weight: 600;
    border-radius: 5px;
    cursor: pointer;
}
.social{
  margin-top: 30px;
  display: flex;
}
.social div{
  background: red;
  width: 150px;
  border-radius: 3px;
  padding: 5px 10px 10px 5px;
  background-color: rgba(255,255,255,0.27);
  color: #eaf0fb;
  text-align: center;
}
.social div:hover{
  background-color: rgba(255,255,255,0.47);
}
.social .fb{
  margin-left: 25px;
}
.social i{
  margin-right: 4px;
}

.submit {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}

.special {
    display: block;
    height: 50px;
    width: 100%;
    background-color: rgba(255,255,255,0.27);
    color: #fff;
    padding: 0 10px;
    margin-top: 8px;
    font-size: 14px;
    font-weight: 400;

}

.option {
  padding:0 30px 0 10px;
  min-height:40px;
  display:flex;
  align-items:center;
  background:#333;
  border-top:#222 solid 1px;
  position:absolute;
  top:0;
  width: 100%;
  pointer-events:none;
  order:2;
  z-index:1;
  transition:background .4s ease-in-out;
  box-sizing:border-box;
  overflow:hidden;
  white-space:nowrap;

}

.option:hover {
  background:#666;
}


* {
  margin: 0;
  padding: 0;
}

.loader {
  display: none;
  top: 50%;
  left: 50%;
  position: absolute;
  transform: translate(-50%, -50%);
}

.loading {
  border: 16px solid #f3f3f3; /* Light grey */
  border-top: 16px solid #3498db; /* Blue */
  width: 60px;
  height: 60px;
  border-radius: 50%;
  border-top-color: #1ecd97;
  border-left-color: #1ecd97;
  animation: spin 1s infinite ease-in;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

   </style>
   ```
### .#Javascript
```sh
<script type="text/javascript">
        $(document).ready(function() {
            $(function() {
                $( "#alert_flag" ).dialog({
                    modal: true,
                    closeOnEscape: false,
                    dialogClass: "no-close",
                    resizable: false,
                    draggable: false,
                    width: 600,
                    buttons: [
                        {
                            text: "OK",
                            click: function() {
                            $( this ).dialog( "close" );
                            }
                        }
                    ]
                });
            });
        });

    function validateForm() {
         var token_val = document.forms["webex_form"]["token"].value;
         let date_val = document.forms["webex_form"]["date_val"].value;
         if (token_val == "") {
            alert("please find this URL[https://developer.webex.com/docs/getting-started] to get a Token");
            return false;
         }else if (date_val == "") {
            alert("Date must be filled out");
            return false;
         }
         else{
            spinner()

        }
    }

    function spinner() {
        document.getElementsByClassName("loader")[0].style.display = "block";
    }
    </script>
    ```
    
### .Html file

```sh
<body>
    <div class="background">
        <div class="shape"></div>
        <div class="shape"></div>
    </div>

    {% if alert_flag == "True" %}
        <div id="alert_flag" title="alert_flag">
            <script>alert('{{ file_name }}')</script>
        </div>
    {% endif %}
    <form name="webex_form" action = "{% url 'download_data' %}" method = "POST" onsubmit="return validateForm()">
        {% csrf_token %}
        <h3>Webex Chat Report</h3>
        <label for="Token">Authentication Token</label>
        <input type="text" placeholder="Bear Token" id="token" name="token">

        <label for="Date">Date:</label>
        <input type="month" id="date_val" name="date_val">

        <label for="room">Room</label>
        <select name="room_id" id="room_id" class="special" >
            <option value="support" class="option">Devnet support room</option>
            <option value="program" class="option">Devnet program room</option>
        </select>
        <br>
        <input type="submit" value="Download" class="sbtn btn btn-secondary btn-c"  style="background-color: #4CAF50">
        <div class="loader">
            <div class="loading">
        </div>
        </div>
        </br>
    </form>
</body>
```

    
 
   
 



