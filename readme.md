## Test Message Reminder Application


#### Install Dependencies:
This app uses Python 3.5; it should work with any version of Python > 3.
```
  pip install --upgrade -r requirements.txt
```
#### Set Environmental Variables:

Environomental variables can be set by creating a file called 'secrets.py' in the application's root directory. The file should define the following string variables:

```python
# secrets.py file:

# API authentication:
key = "<Whispir API Key>"
user = "<Whispir API user-name>"
whispir_password = "<Whispir API password>"

# For sending notification emails:
email = "<Gmail address>"
password = "<Gmail password>"
```

#### Run Program:
```
python main.py appt_template email_list_1
```

#### Modifying/ Expanding:

Modifications should most likely be made in the main.py file or the data_funcs.py

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
-  string
