from calc import Bmi
import unittest

class Test_Bmi_Calc (unittest.TestCase):

    def setUp(self):
        self.test_obj_calc = Bmi(130, 1.92, 'kg', 'm')

        self.test_obj_zero = Bmi(0, 0, 'kg', 'm')

        self.test_obj_neg = Bmi(-1, 0, 'kg', 'm')

        self.test_obj_type = Bmi('1', 0, 'kg', 'm')

    def tearDown(self):
        del self.test_obj_calc
        del self.test_obj_zero
        del self.test_obj_neg
        del self.test_obj_type

    def test_bmi_calc(self):

        self.assertEqual(self.test_obj_calc.calculate(), 35.26)

        self.assertEqual(self.test_obj_zero.calculate(), 0)

        with self.assertRaises(ValueError) as context:
            self.assertRaises(self.test_obj_neg.calculate())


if __name__ == '__main__':
    unittest.main()
