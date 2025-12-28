from quality_check import Check, ZeroError, LimitError

import unittest



class Test_Quality_Check(unittest.TestCase):

    def test_check_type(self):
        # test the check_type method to see if it can raise a type Error
        pos_value = 'A string'
        pos_type = 'string'

        # Check to see that it can pass given correct values
        neg_value = 1
        neg_type = 'int'

        with self.assertRaises(TypeError) as context:
            Check.check_type(pos_value, pos_type)

        self.assertFalse(self.checker.check_type(neg_value,neg_type))
    def test_check_zero(self):
        pos_value = 0

        neg_value = 1


        with self.assertRaises(ZeroError) as context:
            Check.check_zero(pos_value)

        self.assertTrue(Check.check_zero(neg_value))

    def test_sanity(self):
        upper_bound = 10
        lower_bound = 5

        with self.assertRaises(LimitError) as context:
            Check.check_sanity(2,upper_bound,lower_bound,'number')
            Check.check_sanity(11,upper_bound,lower_bound,'number')

        self.assertTrue(Check.check_sanity(8,upper_bound,lower_bound,'number'))


if __name__ == '__main__':
    unittest.main()




