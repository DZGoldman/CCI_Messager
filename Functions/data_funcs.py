'''Low level raw data manipulation functions - string manipulation and format converison.'''
import re

def set_language(lang_string, default_language = 'english'):
    ''' Convert language string into "spanish" or a default language ("english" by default)'''
    if lang_string.lower() in ['spanish', 'es']:
        return 'spanish'
    else:
        return default_language
def validate_email(email_str):
    ''' Input email as string, return empty string if email format is improper'''
    if re.match(r"[^@]+@[^@]+\.[^@]+", email_str):
        return email_str
    else:
        return ''

def extract_digits (string):
    ''' Stript all characters except digits 0-9 from string'''
    digit_list = re.findall(r'\d+', string)
    return ''.join( digit_list)

def validate_phone_number(phone_number):
    '''Input phone_number (string) in any format and return string in '1-XXXXXXXXXX' format.

    Note: Uses 'extract_digits' function
    '''
    digits = extract_digits(phone_number)
    digit_count = len(digits)
    if digit_count == 11 and digits[0] =='1':
        return digits
    if digit_count == 10:
        return '1'+digits
    else:
        return ''

def extract_alpha_num_digits (string):
    ''' Strip all characters except alhpha numeric characeters (0-9, a-z) and spaces from a string.'''
    return re.sub('([^\s\w]|_)+', '', string)

def first_word(string):
    ''' Get substring until the first space'''
    return string.split(' ')[0]

def strip_white_space(string):
    return string.strip()

def is_null(x):
    '''Determines if input value is null, returns Boolean'''
    return True if (not x) and (x !=0) else False

def remove_final_punctuation(string):
    '''Remove punctuation at end of input, if it exists'''
    if string == '': return ''
    elif string[-1] in ['.', '!', '?']:
        return string[: -1 ]
    else:
        return string
