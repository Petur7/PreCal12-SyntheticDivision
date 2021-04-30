from operator import attrgetter

class Element():
    def __init__(self):
        self.sign = '+'
        self.base = 0
        self.unknow = ''
        self.exponent = 0

    def createElementFromString(self, element):
        self.__element__ = element

        # sign detecting
        if not '-' in self.__element__:
            self.sign = '+'
            self.__element__ = self.__element__.replace('+', '')
        else: 
            self.sign = '-'
            self.__element__ = self.__element__.replace('-', '')

        # exponent detecting
        if '^' in self.__element__:
            power_position = self.__element__.find('^')
            self.exponent = int(self.__element__[power_position+1:])
            self.__element__ = self.__element__.replace(self.__element__[power_position:], '')
        else:
            self.exponent = 1

        # get unknow variable
        if self.__element__[len(self.__element__)-1:].isalpha():
            self.unknow = self.__element__[len(self.__element__)-1:]
            self.__element__ = self.__element__.replace(self.unknow, '')
        else:
            self.unknow = ""
            self.exponent = 0

        # get value of the base number
        if '' != self.__element__:
            self.base = int(self.__element__)
        else:
            self.base = 1
        if self.sign == '-': self.base *= -1

        self.raw = element

    def inputElement(self, sign, base, unknow, exponent):
        self.sign = sign
        self.base = base
        self.unknow = unknow
        self.exponent = exponent


def splitElement(polynomial):
    elementList = []
    head_position = 0
    for tail_position in range(1, len(polynomial)+1):
        if '+' == polynomial[tail_position-1] or '-' == polynomial[tail_position-1]:
            if polynomial[head_position:tail_position-1] != '':
                temp_create_element = Element()
                temp_create_element.createElementFromString(polynomial[head_position:tail_position-1])
                elementList.append(temp_create_element)
                head_position = tail_position-1

    # add the last element into list
    temp_create_element = Element()
    temp_create_element.createElementFromString(polynomial[head_position:])
    elementList.append(temp_create_element)

    # sort base on exponent and unknow variable
    elementList = sortElement(elementList)

    return elementList

def sortElement(elementList):
    elementList = sorted(elementList, key=attrgetter('exponent', 'unknow'), reverse=True)
    return elementList