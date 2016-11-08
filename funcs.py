import requests, re, base64
import pandas as pd

# TODO fix this
def filter_empty_rows(data, rows):
    for row in rows:
        data = data[data[row].notnull()]
    return data

def extract_digits (string):
    digit_list = re.findall(r'\d+', string)
    return ''.join( digit_list)
def validate_phone_number(phone_number):
    # coerce into string, in case dataframe feeds it an int
    phone_number = str(phone_number)
    digits = extract_digits(phone_number)
    digit_count = len(digits)
    if digit_count == 11 and digits[0] =='1':
        return digits
    if digit_count == 10:
        return '1'+digits
    else:
        return ''
def validate_all_phone_nums(data, phone_num_column='Cell number'):
    new_phone_num_column = data[phone_num_column].map(validate_phone_number)
    data[phone_num_column] = new_phone_num_column
    return data

def get_alpha_num_digits (string):
    pass

def send_to_api(encoded_csv):
    pass

def import_csv():
    return pd.read_excel('test_file.xlsx')
def finished_message(success_csv, fail_csv, contats):
    pass

def set_all_languages(data, language_column = '@@cci_language@@'):
    new_language_column = data[language_column].map(set_language)
    data[language_column] = new_language_column
    return data
def set_language(lang_string, default = 'english'):
    if lang_string.lower() == 'spanish':
        return 'spanish'
    else:
        return default

def encode_csv (data):
    csv_bytes = data.to_csv().encode('utf8')
    return base64.b64encode(csv_bytes)
