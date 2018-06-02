from unit_convert import UnitConversion
import unittest

class Test_unit_conversion(unittest.TestCase):

    def test_feet_to_inch(self):
        self.assertEqual(UnitConversion.feet_to_inch(self,6,4),76)

    def test_inch_to_cm(self):
        self.assertEqual(UnitConversion.inch_to_cm(self,76),193.04)

    def test_m_to_inch(self):
        self.assertEqual(UnitConversion.cm_to_inch(self,193.04),76)

    def test_cm_to_meter(self):
        self.assertEqual(UnitConversion.cm_to_meter(self,193.04),1.9304)

    def test_kg_to_lb(self):
        self.assertEqual(UnitConversion.kg_to_lb(self,130),286.6006)

    def test_lb_to_kg(self):
        self.assertEqual(UnitConversion.lb_to_kg(self,286.6006),130
        )

    def stone_to_kg(self):
        pass


if __name__ == '__main__':
    unittest.main()
     


