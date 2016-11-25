'''
Define variables to use as command line arguments
'''
import sys

# Whispir API templatees
appt_template = '6DBC01BE80705741'
my_other_template = 'FAKEFAKEFAKE@#$@#$@#$'

#  Contact lists (to receieve notification email)
email_list_1 = ['dannyg9917@gmail.com', 'dzgoldman@wesleyan.edu']
email_list_2 = ['dude@fake.com', 'person@whatever.gov']

# File names (for new CSV_file)
default_file = 'success.csv'







current_template = eval(sys.argv[1])
current_email_recs = eval(sys.argv[2])
current_file_name = eval(sys.argv[3])
