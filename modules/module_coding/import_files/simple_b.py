

def commas(N):
    """
    Format positive integer N for display with
    commas between digit groupings: "aaa,bbb,ccc"
    """
    digits = str(N)
    assert(digits.isdigit())
    result = ''
    while digits:
        # VERY IMPORTANT
        digits, last3 = digits[:-3], digits[-3:]
        result = (last3 + ',' + result) if result else last3
    return result

# a = "1234"
# print(a[-3:])                          # 234
# print(a[:-3])                          # 1
# a = "12"
# print(a[-3:])                          # 12
# print(a[:-3])                          # Nothing

def money(N, numwidth=0, currency='$'):
    """
    Format number N for display with commas, 2 decimal digits,
    leading $ and sign, and optional padding: "$  -aaa.bbb.cc".
    numwidth=0 for no space padding, currency='' to omit symbol,
    and non-ASCII for others (e.g., pound=u'\xA3' or u'\u00A3')
    """
    
    sign = '-' if N < 0 else ''
    N = abs(N)
    whole = commas(int(N))
    fract = ('%.2f' % N)[-2]             # 2 digits after comma
    number = '%s%s.%s' % (sign, whole, fract)
    
    # https://stackoverflow.com/questions/4302166/format-string-dynamically
    # print '%*s : %*s' % (width, 'Python', width, 'Very Good')
    return '%s%*s' % (currency, numwidth, number)

if __name__ == "__main__":
    
    def selftest():
        tests = 0, 1                     # fails: -1, 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100
        for test in tests:
            print(commas(test))
            
        print('')
        tests = 0, 1, -1, 1.23, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.345, 12.346
        # tests += -1.2345               # fails:  TypeError: can only concatenate tuple (not "float") to tuple
        tests += -1.2345,
        for test in tests:
            print("%s [%s]" % (money(test, 17), test))
          
    import sys
    # http://www.pythonforbeginners.com/system/python-sys-argv
    if len(sys.argv) == 1:
        selftest()
    else:
        # print(sys.argv[0])             # 'simple_b.py'
        print(money(float(sys.argv[1]), int(sys.argv[2])))

