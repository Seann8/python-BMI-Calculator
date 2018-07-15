class LimitError(Exception):
    pass


class ZeroError(Exception):
    pass


class Check():
    def __init__(self):
        pass

    @staticmethod
    def check_type(value, type):
        if isinstance(value, type):
            raise TypeError
        else:
            return False

    @staticmethod
    def check_zero(value):
        if value <= 0:
            raise ZeroError('Please enter a value greater than Zero')
        else:
            return value

    @staticmethod
    def check_sanity(value, upper, lower, unit):
        if not lower <= value <= upper and value != 0:
            raise LimitError('Please enter a value that falls inisde the range of {0} and {1} {2}\'s'.format(lower,
                                                                                                             upper,
                                                                                                             unit))
        else:
            return value

## DONE: Write unit tests for this Class
