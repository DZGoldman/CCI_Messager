import unittest, random, string
from Functions.data_funcs import *

class Tests(unittest.TestCase):

    def test_validate_phone_number (self):

            self.assertEqual(validate_phone_number  ('1-555-123-4567'), '15551234567')
            self.assertEqual(validate_phone_number  (' 555  123/4567  '), '15551234567')
            self.assertEqual(validate_phone_number  ('555-123---4567'), '15551234567')

            self.assertFalse(validate_phone_number(''))
            self.assertFalse(validate_phone_number('123-4567'))
            self.assertFalse(validate_phone_number('555-5555-55555'))
            for _ in range(10):
                rand_digit_string = str(random.randint(1000000000,9999999999))
                self.assertEqual(validate_phone_number(rand_digit_string), '1' +rand_digit_string )

    def test_extract_alpha_num_digits(self):
        self.assertFalse('')
        self.assertEqual(extract_alpha_num_digits   ('1234567890!@#$%^&*()'), '1234567890' )
        self.assertEqual(extract_alpha_num_digits   ('{}|:"<>?"asdfghjkl'), 'asdfghjkl' )
    def test_set_language(self):
        self.assertEqual(set_language   (''),'english')
        self.assertEqual( set_language  ('spanish'), 'spanish')
        self.assertEqual(set_language   ('SPANISH'),'spanish')
        for _ in range(10):
            self.assertEqual( set_language  (self.randomstring(8)),'english' )
    def test_is_null(self):
        self.assertTrue(is_null(''))
        self.assertTrue(is_null(None))
        self.assertFalse(is_null(0))
    def randomstring(self, length):
        return ''.join(random.choice(string.ascii_letters) for i in range(length))
        # random string test

unittest.main()
