**Webex_data_generate**

**How to Install and Run This App**

**STEP 1:** Make sure Python is installed on your workstation. If you dont have it, you can get it here ---> https://www.python.org/downloads/

**STEP 2:** Fork this repo. Start by making sure you're logged into GitHub. Then click the Fork button in the upper-right hand corner of this page (https://github.com/vignesh271121/Webex_data_generate) and follow the prompts.

**STEP 3:** Clone this repo. Click the green code button and copy the URL listed under 'HTTPS'. Now go to you IDE, such as VS Code, PyCharm or Atom, find a place to clone it and type 'git clone' plus the URL you just copied. For example 'git clone https://github.com/vignesh271121/Webex_data_generate.git'

**STEP 4:** Create a virtual environment. cd into the Webex_data_generate folder. Type 'python -m venv venv' and then 'source venv/bin/activate' for Mac and Linix or 'source venv/scripts/activate' on Windows. You'll know it worked when you see '(venv)' at the beginning of your command prompt.

**STEP 5:** Install the requirements. Type pip intall -r requirements.txt

**STEP 6:** Edit the download location. Open the file report_App/report_download.py and on around line 47, replace 'Enter your Path folder' with the folder of your choice for the Excel report to be placed. Make sure that folder is created and present with full path.

**STEP 7:** Run the app. From the Webex_data_generate folder, run the command 'python manage.py runserver' and use your web browser go to the URL presented in the terminal, such as http://127.0.0.1:8000/. You'll find your authentication token here (https://developer.webex.com/docs/getting-started). Choose a date and room and hit 'Download'. Your results will print.(https://user-images.githubusercontent.com/97229745/150739281-217ac9a0-2d7a-4da8-bc2f-3e1d3228d8fa.png)
![image](https://user-images.githubusercontent.com/97229745/150739612-6f270fd1-d505-425d-867d-4ba276b3afb4.png)
