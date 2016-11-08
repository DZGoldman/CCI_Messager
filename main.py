from funcs import *
import pandas as pd

i_data = import_csv()

clean_data = validate_all_phone_nums (i_data)

clean_data = filter_empty_rows(clean_data, ['@@cci_location@@','@@cci_start_time@@', '@@cci_end_time@@'])

clean_data = transform_columns (clean_data, set_language, columns= '@@cci_language@@')

clean_data = transform_columns (clean_data, extract_alpha_num_digits, columns= ['@@cci_location@@', '@@cci_start_time@@', '@@cci_end_time@@'])

print(clean_data)
# print(type(i_data) == pd.DataFrame)
