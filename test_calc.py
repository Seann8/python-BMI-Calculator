import calc
import unittest

class Test_Bmi_Calc (unittest.Testcase):
    def test_height_convert(self):
        pass

    def test_bmi_calc(self):
        self.assertEqual(calc.calculate(1.93,130),34.9)

    def test_inputs(self):
        pass


if __name__ == '__main__':
    unittest.main()
