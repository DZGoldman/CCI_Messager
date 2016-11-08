import unittest, random, string
from funcs import *

class Tests(unittest.TestCase):

    def test_validate_phone_number (self):
            self.assertFalse(validate_phone_number(''))
            self.assertEqual(validate_phone_number(
            '1-555-123-4567'), '15551234567')
            self.assertEqual(validate_phone_number(
            ' 555 123 4567  '), '15551234567')
            self.assertEqual(validate_phone_number(
            '555-123---4567'), '15551234567')
            self.assertEqual(validate_phone_number(
            '!11@2#3$4%5^&6*7(8)9:0;'),'11234567890')
            for _ in range(10):
                rand_digit_string = str(random.randint(1000000000,9999999999))
                self.assertEqual(validate_phone_number(
                rand_digit_string), '1' +rand_digit_string )
    def test_get_alpha_num_digits(self):
        self.assertEqual(get_alpha_num_digits(
        'usa56.'),'usa' )

    def test_set_language(self):
        self.assertEqual(set_language   (''),'english')
        self.assertEqual( set_language  ('spanish'), 'spanish')
        self.assertEqual(set_language   ('SPANISH'),'spanish')
        for _ in range(10):
            self.assertEqual( set_language(
            self.randomstring(8)),'english' )

    def randomstring(self, length):
        return ''.join(random.choice(string.ascii_letters) for i in range(length))
        # random string test

unittest.main()
