'''
Main program file where where methods in the 'Functions' directory are called.

Imports CSV, converts it to JSON-style format, sanitizes data, removed invallid records, sends data to Whispir, and sends notification emails.
'''
import os
from inputs import current_template, current_email_recs, current_file_name, imported_file_path
from Functions.csv_funcs import *
from Functions.api_funcs import *
from Functions.data_funcs import *
from Functions.email_funcs import *


# Import data, and convert it to list of dictionaries format:
csv_file = open(imported_file_path, 'rt',  encoding="latin-1")
data, columns =  jsonify(csv_file)

# Set variables...
# ...file names,
new_file = path_prefix + '/CSV_Files/' + current_file_name
fail_file = path_prefix + '/CSV_Files/failures.csv'
# ...recipients of notification emails,
# current_email_recs = ['dannyg9917@gmail.com']
# ...and column names
phone_number_col = 'mobile'
language_col = 'cciLanguage'
location_col = 'cciLocation'
start_time_col = 'cciStartTime'
first_initial_col = 'cciFirstInitial'
last_name_col = 'cciLastName'
end_time_col = 'cciEndTime'
email_col = 'email'

# Sanitize data:
transform_columns(data, fn = strip_white_space,
                        target_columns = [phone_number_col, language_col,location_col, start_time_col,first_initial_col,last_name_col,end_time_col,email_col])
transform_columns(data, fn= first_word,
                    target_columns = last_name_col)
transform_columns (data, fn= validate_phone_number,
                    target_columns = phone_number_col)

transform_columns (data, fn= set_language,
                    target_columns= language_col)

transform_columns (data, fn = extract_alpha_num_digits,
                    target_columns= first_initial_col)
transform_columns(data, fn = remove_final_punctuation,
                    target_columns = location_col)
transform_columns (data, fn = validate_email,
                    target_columns= email_col)

# Remove records with invalid data:
removed_rows = filter_out_rows(data,
                test_fn= is_null,
                target_columns= [location_col,start_time_col, end_time_col, phone_number_col] )

# Create new CSV files (successes and failures)
generate_csv(new_file, data, columns)
generate_csv(fail_file ,removed_rows, columns)

# Send data to Whispir API:
response = send_messages( encode_json(data), current_template)

# Send notification emails:
send_with_attachments( current_email_recs,len(data), len(removed_rows),success =response, api_response = response,success_file = new_file,fail_file =fail_file)
