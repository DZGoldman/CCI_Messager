import requests, re, base64, csv
import pandas as pd
from IPython import embed

# TODO fix this - .apply?

def transform_columns (i_data, new_data, fn, columns ):
    if isinstance(columns, str):
        columns = [columns]

    for column in columns:
        data[column] = data[column].map(fn)
    return data


def filter_empty_rows(data, columns):
    for column in columns :
        data = data[data[column].notnull()]
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

def extract_alpha_num_digits (string):
    string = str(string)
    return re.sub('[\W_]', '', string)


def send_to_api(encoded_csv):
    pass

def import_csv():
    with open('mock.csv', 'rt') as r:


        i_data = csv.DictReader(r)

        fieldnames = i_data.fieldnames
        with open('new.csv', 'w') as w:
            new_csv = csv.DictWriter(w, fieldnames = fieldnames)
            return (i_data, new_csv)

def finished_message(success_csv, fail_csv, contats):
    pass


def set_language(lang_string, default = 'english'):
    if lang_string.lower() == 'spanish':
        return 'spanish'
    else:
        return default

def encode_csv (data):
    csv_bytes = data.to_csv().encode('utf8')
    return base64.b64encode(csv_bytes)
