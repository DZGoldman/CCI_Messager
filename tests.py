'''Testing suite'''
import unittest, random, string
from Functions.data_funcs import *
from Functions.csv_funcs import *

class DataTests(unittest.TestCase):
    def test_first_word(self):
        self.assertFalse('')
        self.assertTrue(first_word('Daniel'),'Daniel')
        self.assertTrue(first_word(' Daniel AKA Batman  '), 'Daniel')
    def test_validate_phone_number (self):
        self.assertEqual(validate_phone_number  ('1.555.123.4567'), '15551234567')
        self.assertEqual(validate_phone_number  (' 555  123---4567  '), '15551234567')
        self.assertFalse(validate_phone_number(''))
        self.assertFalse(validate_phone_number('123-4567'))
        for _ in range(10):
            rand_digit_string = str(random.randint(1000000000,9999999999))
            self.assertEqual(validate_phone_number(rand_digit_string), '1' +rand_digit_string )

    def test_extract_alpha_num_digits(self):
        self.assertFalse('')
        self.assertEqual(extract_alpha_num_digits   ('1234567890!@#$%^&*()'), '1234567890' )
        self.assertEqual(extract_alpha_num_digits   ('{}|:"<>?"asdfghjkl'), 'asdfghjkl' )
        self.assertEqual(extract_alpha_num_digits('2123 sstreet street'), '2123 sstreet street')
    def test_set_language(self):
        self.assertEqual(set_language   (''),'english')
        self.assertEqual(set_language   ('SPANISH'),'spanish')
        self.assertEqual(set_language   ('ES'),'spanish')
        for _ in range(10):
            self.assertEqual( set_language  (self.randomstring(8)),'english' )

    def test_is_null(self):
        self.assertTrue(is_null(''))
        self.assertTrue(is_null(None))
        self.assertFalse(is_null(0))
    def test_validate_email(self):
        for bad_email in ['dan, dan@@aol.com, danny.aol@com, dan@gmail']:
            self.assertFalse(validate_email(bad_email))
        for good_email in ['dan@gmail.com', 'dan234@nycourts.edu', 'dan12345@aol.com']:
            self.assertEqual( validate_email(good_email), good_email)
    def randomstring(self, length):
        return ''.join(random.choice(string.ascii_letters) for i in range(length))


class CSVTests(unittest.TestCase):
    def test_transform_columns(self):
        test_json = [{'col_1': 10,'col_2': 20}]
        result = transform_columns(test_json, lambda x: x+1, 'col_1')
        self.assertEqual(result, [{'col_1': 11,'col_2': 20}])

    def test_filter_out_rows(self):
        test_json = [{'col_1': 10,'col_2': 20},{'col_1': 1,'col_2': 2} ]
        result = filter_out_rows(test_json, lambda x: x==1, 'col_1')
        self.assertEqual(result,[{'col_1': 1,'col_2': 2} ])
        self.assertEqual(test_json, [{'col_1': 10,'col_2': 20}])
unittest.main()
