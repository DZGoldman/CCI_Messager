'''
Main program file where where methods in the 'Functions' directory are called.

Imports CSV, converts it to JSON-style format, sanitizes data, removed invallid records, sends data to Whispir, and sends notification emails.
'''
from Functions.csv_funcs import *
from Functions.app_funcs import *
from Functions.data_funcs import *

# Import data, and convert it to list of dictionaries format:
csv_file = import_csv()
data, columns =  jsonify(csv_file)

# Set variables...
# ...file names,
new_file = 'CSV_Files/sucesses.csv'
fail_file = 'CSV_Files/failures.csv'
# ...recipients of notification emails,
email_recipients = ['dzgoldman@wesleyan.edu','dannyg9917@gmail.com']
# ...and column names
phone_number_col, \
language_col,   \
location_col,  \
start_time_col, \
last_name_col, \
end_time_col = get_column_names(data)

# Sanitize data:
transform_columns(data,
                    fn= first_word,
                    target_columns = last_name_col)

transform_columns (data,
                    fn= validate_phone_number,
                    target_columns = phone_number_col)
transform_columns (data,
                    fn= set_language,
                    target_columns= language_col)
transform_columns (data,
                    extract_alpha_num_digits,
                    target_columns= [location_col, start_time_col, end_time_col])

# Remove records with invalid data
removed_rows = filter_out_rows(data,
                test_fn= is_null,
                target_columns= [location_col,start_time_col, end_time_col, phone_number_col] )

# Create new CSV files (successes and failures)
generate_csv(new_file, data, columns)
generate_csv(fail_file ,removed_rows, columns)
# Send data to Whispir API:
response = send_to_api(new_file, encode_json(data))

# Send notification emails:
send_with_attachments(
    email_recipients,
    len(i_data), len(removed_rows),
    success =response.ok,
    api_response = response,
    success_file = new_file,
    fail_file =fail_file)
