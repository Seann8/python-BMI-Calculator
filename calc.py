## main class for calculating bmi


class Bmi(self):
    """@DESC main class for handling the units and inputs, converting and calculating the output to be returned """
    def __init__(self,weight,height,unit_weight,unit_height):
        weight = self.weight
        height = self.height
        unit_height = self.unit_height

    def convert_weight(self):

        if self.unit_height == "pound":
            convert = 0.45359237
        elif self.unit_height == "stone":
            convert = 0.15747

        weight = self.weight/convert

    return weight

   def convert_height(self):
       if self.unit_height == 'feet' :
           convert = .3048
        
    def calculate(self):
        BMI =(weight / height ** 2)
        return BMI


    def convert(self):
        pass
    


