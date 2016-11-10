from Functions.csv_funcs import *
from Functions.app_funcs import *
from Functions.data_funcs import *

i_data, columns =  import_csv()

transform_columns (i_data, validate_phone_number, target_columns = 'Cell number')
transform_columns (i_data, set_language, target_columns= '@@cci_language@@')

transform_columns (i_data, extract_alpha_num_digits,
                    target_columns= ['@@cci_location@@', '@@cci_start_time@@', '@@cci_end_time@@'])

removed_rows = filter_out_rows(i_data, is_null, ['@@cci_location@@','@@cci_start_time@@', '@@cci_end_time@@', 'Cell number'] )

# make conditional
generate_csv('successes.csv', i_data, columns)
generate_csv('failures.csv', removed_rows, columns)

b64_encoded_csv = encode_csv('successes.csv')

# send to api
# send emails
# print(type(i_data) == pd.DataFrame)
