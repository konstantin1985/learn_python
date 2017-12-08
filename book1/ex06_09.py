
# Problem 6.9: Write a function that takes two strings representing
# integers, and returns an integer representing their product

import unittest

class BigInt:

    bigInt = ''

    def __init__(self, s=''):
        # Convert str to int
            self.bigInt = s

    # Multiply string s by string with one element integer and return the resulting string
    def MultiplyByInteger(self, s, integer):
        # Strings are immutable so we need to use a list here
        # Careful about this technique for multidimensional arrays
        # https://stackoverflow.com/questions/4056768
        result = [''] * (len(s) + 1)
        carry = 0
        for i in reversed(range(len(s))):
            temp = int(s[i]) * int(integer) + carry
            result[i+1] = str(temp % 10)
            carry = temp // 10
        if carry != 0:
            result[0] = str(carry)
        else:
            result = result[1:]
        return ''.join(result)

    def AddIntegers(self, a, b):
        result = [''] * (max(len(a), len(b)) + 1)
        carry = 0
        if len(a) > len(b):
            b = '0' * (len(a)-len(b)) + b
        else:
            a = '0' * (len(b)-len(a)) + a
        for i in reversed(range(len(a))):
            temp = int(a[i]) + int(b[i]) + carry
            result[i+1] = str(temp % 10)
            carry = temp // 10
        if carry != 0:
            result[0] = str(carry)
        else:
            result = result[1:]
        return ''.join(result)

    def __mul__(self, other):

        # Partial sums
        results = [''] * (len(other.bigInt) + len(self.bigInt))
        loopLen = len(other.bigInt)

        for i in reversed(range(loopLen)):
            results[i] = self.MultiplyByInteger(self.bigInt, other.bigInt[i])
            results[i] = results[i] + '0' * (loopLen - i - 1)

        last = ''
        for result in results:
            last = self.AddIntegers(result, last)

        return BigInt(last)

    def __str__(self):
        return str(self.bigInt)


class Ex6_9Test(unittest.TestCase):

    def test_AuxiliaryFunctions(self):
        b1 = BigInt()

        self.assertEquals(b1.MultiplyByInteger('367', '1'), '367')
        self.assertEquals(b1.MultiplyByInteger('367', '2'), '734')
        self.assertEquals(b1.MultiplyByInteger('367', '3'), '1101')

        self.assertEquals(b1.AddIntegers('367', '1'), '368')
        self.assertEquals(b1.AddIntegers('367', '2935'), '3302')

    def test_MainFunction(self):
        b1 = BigInt('55')
        b2 = BigInt('77')
        b3 = b1 * b2
        self.assertEquals(b3.bigInt, '4235')

        b1 = BigInt('7890')
        b2 = BigInt('78')
        b3 = b1 * b2
        self.assertEquals(b3.bigInt, '615420')


if __name__ == "__main__":
    unittest.main()