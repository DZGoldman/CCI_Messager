## Test Message Reminder Application

This application inputs a csv file, an ID of a template from the Whispir API, a list of email contacts, and a file name; it sanitizes the CSV file, sends the data to the template on Whispir, and sends emails notifications to all contacts on the inputed list.

#### Install Python:

Check python version:
```
python -V
```

If version is below 3.5.1, install python as follows (for Ubuntu/linux).

Install:
```
cd ~/usr/src &&
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
```

Extract package:
```
sudo tar xzf Python-3.5.2.tgz

```

Compile Python source:  
```
cd ~/Python-3.5.2 &&
sudo ./configure &&
sudo make altinstall
```

##### Install requirements:

Install pip:
```
sudo apt-get install -y python3-pip
```

Install requirements: (Requests module version 2.8.1)
```
  pip install --upgrade -r requirements.txt
```

#### Set Environmental Variables:

From the app's root directory, run the following command:

```
cp inputs_template.py inputs.py &&
cp secrets_template.py secrets.py
```

In the secrets.py file, input your information (as strings).

#### Run Program:
```
python3 main.py appt_template email_list_1 default_file
```
The command line arguments (after main.py) refer to variables defined in the inputs.py file:

1st (string): ID of template on the Whisipr API.

2nd (list of strings): Email addresses to receive notification email.

3rd (string): Name of new CSV file to be created

See the inputs.py file for examples. Additional variables for any of the 3 arguments can be added to that file; just make sure each of the command line arguments corresponds to a variable in inputs.py when the application is run.




#### File Structure:
Methods are defined in the modules in the Functions directory.

The program's methods are all called in the main.py file.

The lowest level methods (string/integer functions) are defined in the data_funcs.py file.

These two files (main.py and data_funcs.py) are the files in which any additional modifications would most likely take place.

#### Testing:
Tests are defined in the tests.py file.

Run all tests:
```
  python tests.py
```
Run one class of tests:
```
  python tests.py DataTests

```
Run single tests:
```
python tests.py DataTests.test_validate_phone_number
```

#### Python modules used:
 **External:**
- requests

**Standard Library:**
- re
- smtplib
- email
- csv
- base64
- json
- unittest
- random
