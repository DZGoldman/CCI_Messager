import re

def set_language(lang_string, default = 'english'):
    if lang_string.lower() == 'spanish':
        return 'spanish'
    else:
        return default

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

def is_null(x):
    return True if (not x) and (x !=0) else False

def extract_digits (string):
    digit_list = re.findall(r'\d+', string)
    return ''.join( digit_list)


def extract_alpha_num_digits (string):
    string = str(string)
    return re.sub('[\W_]', '', string)
