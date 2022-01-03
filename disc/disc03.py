def multiply(m, n):
    """ Takes two positive integers and returns their product using recursion.
    >>> multiply(5, 3)
    15
    """
    "*** YOUR CODE HERE ***"
    if m == 1:
        return n

    return n + multiply(m-1, n)

def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2 or n == 1: #Bug line
        return n
    else:
        return n * skip_mul(n - 2)

def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    "*** YOUR CODE HERE ***"
    
    def n_has_no_proper_divisor_less_than(d): 
        """Determining whether n has proper divisors less than or equal to d, 
        proper divisor is defined to be a divisor less than n and not equal to one""" 
        if d == 1 or n == 1:           
            return True
        elif n%d == 0:
            return False
        else:
            return n_has_no_proper_divisor_less_than(d-1)

    return n_has_no_proper_divisor_less_than(n-1)

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    print(n)
    if n == 1:
        return 1

    if n%2 == 0:
        return 1 + hailstone(n//2)
    else:
        return 1 + hailstone(3*n +1)

def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31) 
    3211
    """
    "*** YOUR CODE HERE ***"
    #Base case:
    if n1 == 0:
        return n2
    elif n2 == 0:
        return n1
    
    #Inductive case:
    if n1%10 < n2%10:
        return n1%10 + 10 * merge(n1//10, n2)
    else:
        return n2%10 + 10 * merge(n1, n2//10)    

