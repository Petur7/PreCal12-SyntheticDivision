import unittest
from Element import splitElement

class TestElementSplit(unittest.TestCase):
    
    def test_basic_1(self):
        # 2x^3-x^2-2x+1
        test_resultList = splitElement('1-2x-x^2+2x^3')

        self.assertEqual(test_resultList[0].sign, '+')
        self.assertEqual(test_resultList[0].base, 2)
        self.assertEqual(test_resultList[0].unknow, 'x')
        self.assertEqual(test_resultList[0].exponent, 3)
        
        self.assertEqual(test_resultList[1].sign, '-')
        self.assertEqual(test_resultList[1].base, -1)
        self.assertEqual(test_resultList[1].unknow, 'x')
        self.assertEqual(test_resultList[1].exponent, 2)

        self.assertEqual(test_resultList[2].sign, '-')
        self.assertEqual(test_resultList[2].base, -2)
        self.assertEqual(test_resultList[2].unknow, 'x')
        self.assertEqual(test_resultList[2].exponent, 1)

        self.assertEqual(test_resultList[3].sign, '+')
        self.assertEqual(test_resultList[3].base, 1)
        self.assertEqual(test_resultList[3].unknow, '')
        self.assertEqual(test_resultList[3].exponent, 0)

    def test_basic_2(self):
        # 2x^4+13x^3+29x^2+15x+7
        test_resultList = splitElement('2x^4+13x^3+29x^2+15x+7')

        self.assertEqual(test_resultList[0].sign, '+')
        self.assertEqual(test_resultList[0].base, 2)
        self.assertEqual(test_resultList[0].unknow, 'x')
        self.assertEqual(test_resultList[0].exponent, 4)

        self.assertEqual(test_resultList[1].sign, '+')
        self.assertEqual(test_resultList[1].base, 13)
        self.assertEqual(test_resultList[1].unknow, 'x')
        self.assertEqual(test_resultList[1].exponent, 3)

        self.assertEqual(test_resultList[2].sign, '+')
        self.assertEqual(test_resultList[2].base, 29)
        self.assertEqual(test_resultList[2].unknow, 'x')
        self.assertEqual(test_resultList[2].exponent, 2)

        self.assertEqual(test_resultList[3].sign, '+')
        self.assertEqual(test_resultList[3].base, 15)
        self.assertEqual(test_resultList[3].unknow, 'x')
        self.assertEqual(test_resultList[3].exponent, 1)

        self.assertEqual(test_resultList[4].sign, '+')
        self.assertEqual(test_resultList[4].base, 7)
        self.assertEqual(test_resultList[4].unknow, '')
        self.assertEqual(test_resultList[4].exponent, 0)

unittest.main()