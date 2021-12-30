def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    assert k >= 0, "Depth must not smaller than zero."
    
    count = 0
    result = 1
    while count < k:
        result, n, count = result * n, n-1, count+1

    return result
        



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    assert y>=0, "Sum_digits function can only take nonegative function."
    result = 0
    while y // 10 > 0:
        result, y = result + y%10, y//10

    result = y + result 
    return result


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    flag = False

    curr_digit, next_digit = 0, 0
    while n//10 >0:
        curr_digit, n = n%10, n//10
        next_digit = n%10
        if curr_digit == 8 and next_digit == 8:
            flag = True
    
    return flag

def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    "*** YOUR CODE HERE ***"
    if n%3 == 0 and n%5 == 0:
        print('fizzbuzz')
    elif n%3 == 0:
        print('fizz')
    elif n%5 == 0:
        print('buzz')
    else:
        print(n)
    return None