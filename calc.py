# Author : Sean Nolan
# Email : seannolan85@gmail.com
# Phone : 0863811508


class Bmi():
    """@DESC main class for handling the units and inputs,
       converting and calculating the output to be returned """

    def __init__(self):
        self.weight = None
        self.height = None
        self.bmi = None
        self.advice = None


    def calculate(self,height,weight):
        self.height = height
        self.weight = weight

        try:

            bmi = self.weight / (self.height * self.height)

        except ZeroDivisionError: # final check for zero division errors
            return None

        self.bmi = round(bmi, 2)

        return self.bmi

    def band(self):
        if self.bmi < 18.5:
            self.band = 'Underweight'
        elif 18.5 < self.bmi < 24.9:
            self.band = 'Healthy Weight'
        elif 25 <= self.bmi <= 29.9:
            self.band = 'Overweight'
        elif 30 <= self.bmi <= 39.9:
            self.band = 'Obese'




        self.advice = "Your Report\n\nYou have a BMI of {0} This puts you in the {1} category \n\n ".format(self.bmi
                                                                                                           ,self.band)

        return self.advice


if __name__ == '__main__':
        my_obj = Bmi()
        my_obj.calculate(1.94,125)
        print(my_obj.bmi)
