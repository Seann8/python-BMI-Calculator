=
from unit_convert import UnitConversion

from quality_check import Check

from quality_check import LimitError, ZeroError


class Sanaitze():
    def __init__(self):
        pass

    @staticmethod
    def sanitize_imperial_inputs(inputs):
        if inputs.endswith("\'"):
            inputs += '0'

        elif "'" not in inputs:
            inputs += "'0"

        return inputs


class DataInput():

    ''' @DESC a class to control handle user inputs '''
    height: str
    unit: str

    def __init__(self):
        self.input_wght_msg = 'Enter you weight in kg\n'
        self.input_hght_msg = 'Enter your height in meters\n'
        self.input_wght_stone_msg = " Enter your weight in stones and pounds seperated by a \'\n"
        self.unit = 'M'
        self.height = 0
        self.weight = 0
        self.converter = UnitConversion()
        self.checker = Check() # class to check variables
        self.cleaner = Sanaitze() # class to sanatize imperial inputs
        self.choice = None

    @staticmethod
    def splash_screen(message):

        return (message)

    def input_units(self,message='Hello'):
        """
        @DESC Method to ask the user which type of units they want to use
        """
        unit = int(input(message))

        while True:
            try:
                int(unit)
            except ValueError:
                print(message)
                continue
            if int(unit) not in (1, 2):
                unit = int(input('please select an option, 1 for metric 2 for imperial'))

            elif int(unit) in (1, 2):
                break

        if unit == 1:
            self.unit = 'M'
            return self.unit
        elif unit == 2:
            self.unit = 'I'
            return self.unit

    def input_metric_height(self,message='how tall are you?'):
        check = self.checker

        while True:
            print(message)

            self.height = input(self.input_hght_msg)

            try:
                self.height = float(self.height)

            except ValueError:
                print('Please enter your height in number format')
                continue

            try:
                check.check_sanity(self.height, 2.72, 0.696, 'Meters')
                check.check_zero(self.height)
            except (LimitError, ZeroError) as e:
                print(e)
                continue

            else:
                break

        return self.height

    def input_imp_height(self, message='how heavy are you?'):
        check = self.checker
        cleaner = self.cleaner
        while True:
            print(message)
            try:
                self.height = input('input your height in feet and inches: eg 5\'8')

                self.height = cleaner.sanitize_imperial_inputs(self.height)
                feet, inches = self.height.split("\'")

            except ValueError:
                print('Please enter your height in inches and feet separated by \'')
                continue
            try:
                self.height = self.converter.feet_to_inch(feet, inches)
                check.check_sanity(self.height, 96, 24, 'Feet')
                check.check_zero(self.height)

            except (ValueError, TypeError):
                print('Please enter your height in inches and feet separated by \'')
                continue

            except (ZeroError,LimitError) as e:
                print(e)
                continue

            else:
                break
        self.height = self.converter.inch_to_cm(self.height) / 100
        return self.height

    def input_metric_weight(self,message='how heavy are you?'):
        check = self.checker


        while True:
            print(message)
            self.weight = input('Please Enter your weight in Kgs')

            try:
                self.weight = float(self.weight)
                check.check_sanity(self.weight, 500, 30, 'Kilograms')
                check.check_zero(self.weight)
                # test to see if the string inputs can be converted to a float

            except ValueError:
                print('Please Enter your weight in number format')
                continue

            except (LimitError, ZeroError) as e:
                print(e)
                continue

            else:
                break

        return self.weight

    def input_imp_weight(self):
        check = self.checker
        cleaner = self.cleaner


        while True:
            try:
                self.weight = input('input your weight in stones and pounds: eg 15\'12')
                # if the user enters a single digit format , or forgets pounds the the system will correct
                self.weight = cleaner.sanitize_imperial_inputs(self.weight)

            except (ValueError, TypeError):
                # Handle Value/ Type Errors with a reset of the loop

                print('please enter your weight in stones and pounds seperate by a \'')

                continue
            try:
                stones, pounds = self.weight.split("\'")  # breaks the user input into two variables
                self.weight = self.converter.stone_to_lb(stones, pounds)  # convert user input into single unit
                self.checker.check_sanity(self.weight, 881, 36, 'stone')  # check user input falls into acceptable range


            except LimitError:
                # Custom Exception that handles weights outside normal ranges

                print('Please enter a weight between 3 and 28 stone')

                continue


            except ZeroError as e:
                # Custom Exception that handles zero entered as a value

                print(e)
                continue
            else:
                break

        self.weight = self.converter.lb_to_kg(self.weight)  # Convert final weight to Metric

        return self.weight

    @staticmethod
    def quit():

        """
        @DESC method to ask the user if they want to exit the program or if they want to go again
        returns a Boolean depending on user choice.
        """
        while True:
            try:
                choice = input('press q to quit \n r to restart')
                choice = choice.lower() # sanitize inputs before comparision

            except TypeError:
                print('Please enter q to quit or r to restart')
                if choice not in ('q', 'r'):
                    continue
                else:
                    break
            if choice == 'q':
                return True
            elif choice == 'r':
                return False


if __name__ == '__main__':
    obj = DataInput()
    obj.input_units()
    obj.input_height()
    obj.input_weight()


    print(obj.height)


