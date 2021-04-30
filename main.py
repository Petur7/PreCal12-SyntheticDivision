import Element


def inputData():

    dividendString = input("Devidend: ")
    dividendElements = Element.splitElement(dividendString)

    divisorString = input("Divisor: ")
    divisorElements = Element.splitElement(divisorString)

    print()
    del dividendString, divisorString
    return dividendElements, divisorElements


def output(element):
    if element.base == 0:
        return ''
    if element.exponent == 0:
        return f'{element.sign}{abs(element.base)}'
    return f'{element.sign}{abs(element.base)}{element.unknow}^{element.exponent}'


def checkExponent(dividendElements, divisorElements):
    # check if the first dividend element's exponent is larger or equal the first divisor element's exponent
    if dividendElements[0].exponent >= divisorElements[0].exponent:
        # check if both of those 2 element have unknow variables
        if dividendElements[0].unknow == divisorElements[0].unknow:
            # return True if the synthesis division is not finish
            # print()
            # print(f'Check exponent: {output(dividendElements[0])} and {output(divisorElements[0])}')
            return True
    # if the function is not return True then their will be no more work to do
    return False


def minusExponent(lastResult, dividendElements, divisorElements):
    # lastResult times divisor elements
    divisorElementsPosition = 1
    while divisorElementsPosition <= len(divisorElements)-1:
        # init value for tempResult
        if lastResult.sign == divisorElements[divisorElementsPosition].sign:
            tempResultSign = '+'
        else:
            tempResultSign = '-'
        tempResultBase = lastResult.base * divisorElements[divisorElementsPosition].base
        if lastResult.unknow != '':
            tempResultUnknow = lastResult.unknow
        else:
            tempResultUnknow = divisorElements[divisorElementsPosition].unknow
        tempResultExponent = lastResult.exponent + divisorElements[divisorElementsPosition].exponent

        # create class for tempResult
        tempResult = Element.Element()
        tempResult.inputElement(sign=tempResultSign, base=tempResultBase, unknow=tempResultUnknow, exponent=tempResultExponent)
        # print(f'Create minus exponent: {output(tempResult)}')

        # minus to dividend
        elementExist = False
        for eachDividendElement in dividendElements:
            if eachDividendElement.unknow == tempResult.unknow and eachDividendElement.exponent == tempResult.exponent:
                # print(f'Minus: {output(eachDividendElement)} and {output(tempResult)}')
                elementExist = True
                eachDividendElement.base = eachDividendElement.base - tempResult.base
                if eachDividendElement.base < 0:
                    eachDividendElement.sign = '-'
                else:
                    eachDividendElement.sign = '+'
        # if element not exist
        if not elementExist:
            tempResult.base *= -1
            if tempResult.base < 0:
                tempResult.sign = '-'
            else:
                tempResult.sign = '+'
            # add tempResult to dividendElements
            dividendElements.append(tempResult)
            # print(f'Add minus: {output(tempResult)}')
            # sort dividendElements
            dividendElements = Element.sortElement(dividendElements)

        divisorElementsPosition += 1

    return dividendElements


def divideHandling(dividendElements, divisorElements):
    # result element list
    resultElements = []

    # keep working if the synthesis division is not finish
    while checkExponent(dividendElements, divisorElements):

        firstDividendElement = dividendElements[0]
        firstDivisorElement = divisorElements[0]

        # create the result when 1st dividend element divide to 1st divisor element
        result = Element.Element()
        if firstDividendElement.sign == firstDivisorElement.sign:
            resultSign = '+'
        else:
            resultSign = '-'
        resultBase = firstDividendElement.base / firstDivisorElement.base
        resultUnknow = firstDividendElement.unknow
        resultExponent = firstDividendElement.exponent - firstDivisorElement.exponent
        if resultExponent == 0: resultUnknow = ''
        # input variable to class
        result.inputElement(sign=resultSign, base=resultBase, unknow=resultUnknow, exponent=resultExponent)
        # add current result to result element list
        resultElements.append(result)
        # print(f'Add result: {output(result)}')

        # erase first element in dividend
        # print(f'Delete element: {output(dividendElements[0])}')
        dividendElements.pop(0)

        dividendElements = minusExponent(result, dividendElements, divisorElements)

    return resultElements, dividendElements

dividendElements, divisorElements = inputData()
resultElements, dividendElements = divideHandling(dividendElements, divisorElements)

print()
resultString = ''
for eachResult in resultElements:
    tempResultString = f'{output(eachResult)} '
    resultString = resultString + tempResultString
print(f'Result: {resultString}')
remainderString = ''
for eachRemainder in dividendElements:
    tempRemainderString = f'{output(eachRemainder)} '
    remainderString = remainderString + tempRemainderString
print(f'Remainder: {remainderString}')