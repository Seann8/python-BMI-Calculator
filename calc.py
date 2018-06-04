## main class for calculating bmi


class Bmi():
    """@DESC main class for handling the units and inputs, converting and calculating the output to be returned """

    def __init__(self,weight,height,unit_weight,unit_height):
        self.weight = weight
        self.height = height
        self.negerror = ValueError('Please enter positive values only')
        self.valerror = TypeError('Please enter an integer or float only')




    def calculate(self):


        if isinstance(self.weight,int):
            pass
        elif isinstance(self.height,int):
            pass

        else:
            raise self.valerror


        if self.weight < 0 :
            raise self.negerror
        elif  self.height < 0 :
            raise self.negerror

        try:

            bmi =(self.weight / self.height ** 2)

        except ZeroDivisionError:

            bmi = 0

        return round(bmi,2)


  


