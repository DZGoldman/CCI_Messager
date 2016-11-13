from Functions.csv_funcs import *
from Functions.app_funcs import *
from Functions.data_funcs import *

csv_file = import_csv()
i_data, columns =  jsonify(csv_file)

transform_columns (i_data, validate_phone_number, target_columns = 'Cell number')
transform_columns (i_data, set_language, target_columns= '@@cci_language@@')

transform_columns (i_data, extract_alpha_num_digits,
                    target_columns= ['@@cci_location@@', '@@cci_start_time@@', '@@cci_end_time@@'])

removed_rows = filter_out_rows(i_data, is_null, ['@@cci_location@@','@@cci_start_time@@', '@@cci_end_time@@', 'Cell number'] )
# make conditional
new_file = 'CSV_Files/sucesses.csv'

generate_csv(new_file, i_data, columns)
generate_csv('CSV_Files/failures.csv', removed_rows, columns)


# print(send_to_api.__doc__)

send_to_api(new_file,
    # encode_csv(new_file)
    encode_json(i_data)
)


# send_with_attachments(['dzgoldman@wesleyan.edu', 'dannyg9917@gmail.com'],new_file,len(i_data), len(removed_rows))


# send to api
# send emails
# print(type(i_data) == pd.DataFrame)
