from funcs import *
import pandas as pd

i_data, clean_data = import_csv()


clean_data = transform_columns (i_data, clean_data, validate_phone_number, columns = 'Cell number')
#
# clean_data = transform_columns (clean_data, set_language, columns= '@@cci_language@@')
#
# clean_data = transform_columns (clean_data, extract_alpha_num_digits, columns= ['@@cci_location@@', '@@cci_start_time@@', '@@cci_end_time@@'])
#
# clean_data = filter_empty_rows(clean_data, ['@@cci_location@@','@@cci_start_time@@', '@@cci_end_time@@', 'Cell number'])

print(i_data)
# print(type(i_data) == pd.DataFrame)
