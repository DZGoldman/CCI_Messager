from funcs import *
import pandas as pd

i_data = import_csv()
# print(len(i_data))
# print((i_data['@@cci_lastname@@']) )
# print(i_data['Cell number'])
clean_data = validate_all_phone_nums (i_data)
clean_data = filter_empty_rows(clean_data, ['@@cci_location@@','@@cci_start_time@@', '@@cci_end_time@@'])
set_all_languages
print(clean_data)
# print(type(i_data) == pd.DataFrame)
