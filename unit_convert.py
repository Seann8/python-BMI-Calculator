# Author : Sean Nolan
# Email : seannolan85@gmail.com
# Phone : 0863811508


class UnitConversion:
    def __init__(self):
        pass

    def feet_to_inch(self, feet, inch=0):
        return int(feet) * 12 + int(inch)

    def cm_to_inch(self, height_in_cm):
        return float(height_in_cm) / 2.54

    def inch_to_cm(self, height_in_inch):
        return float(height_in_inch) * 2.54

    def cm_to_meter(self, height_in_cm):
        return float(height_in_cm) * 0.01

    def kg_to_lb(self, kg):
        return float(kg) * 2.20462

    def lb_to_kg(self, lb):

        return float(lb) * 0.453592

    def stone_to_lb(self,stone,lb=0):

        return float(stone) * 14 + float(lb)

