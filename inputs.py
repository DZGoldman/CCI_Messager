'''
Define variables to use as command line arguments for template, email contacts, and file name
'''
import sys

# Add new variables below:

# Whispir API templatees
appt_template = '6DBC01BE80705741'
my_other_template = 'FAKEFAKEFAKE@#$@#$@#$'

#  Contact lists (to receieve notification email)
email_list_1 = ['dannyg9917@gmail.com', 'dzgoldman@wesleyan.edu']
alternative_email_list = ['dude@fake.com', 'person@whatever.gov']

# File names (for new CSV_file)
default_file = 'success.csv'





# Don't touch anything below!!!
# Catches missing/undefined command line arguments
try:
    current_template = eval(sys.argv[1])
except:
    sys.exit('Invalid template command line argument (arg 1)')
try:
    current_email_recs = eval(sys.argv[2])
except:
    sys.exit('Invalid email-list command line argument (arg 2)')
try:
    current_file_name = eval(sys.argv[3])
except:
    sys.exit('Invalid file-name command line argument (arg 3)' )
