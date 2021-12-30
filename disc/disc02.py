def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    def make_keeper_cond(cond):
        i = 1
        while i<=n:
            if cond(i):
                print(i)            
            i += 1
    return make_keeper_cond

def curry2(f):
    """Curry a function with 2 elements.

    >>> def pow(x,y):
    ...     return x**y
    >>> curry2(pow)(2)(3)
    8
    >>> curry2(pow)(3)(2)
    9
    """   
    return lambda x: lambda y: f(x,y)

def make_keeper_redux(n):
    """Returns a function. This function takes one parameter <cond>
    and prints out all integers 1..i..n where calling cond(i)
    returns True. The returned function returns another function
    with the exact same behavior.

    >>> def multiple_of_4(x):
    ...     return x % 4 == 0
    >>> def ends_with_1(x):
    ...     return x % 10 == 1
    >>> k = make_keeper_redux(11)(multiple_of_4)
    4
    8
    >>> k = k(ends_with_1)
    1
    11
    """
    # Paste your code for make_keeper here!
    def do_keeper(cond):
        i = 1
        while i<=n:
            if cond(i):
                print(i)            
            i += 1
        
        return make_keeper_redux(n)

    return do_keeper

def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)("first")("second")("third")
    first
    done
    done
    """
    def inner_print(x):
        if n == 0:
            print("done")
            return print_n(0)
        else:
            print(x)
            return print_n(n-1)
    return inner_print

def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def do_match_k(digit):
        while digit//(10**k) > 0:
            last_digit, k_aprat_digit  = digit%10, (digit//(10**k))%10
            if last_digit != k_aprat_digit:
                return False
            digit = digit // 10
        return True
    return do_match_k

def three_memory(n):
    """
    >>> f = three_memory('first')
    >>> f = f('first')
    Not found
    >>> f = f('second')
    Not found
    >>> f = f('third')
    Not found
    >>> f = f('second') # 'second' was not input three calls ago
    Not found
    >>> f = f('second') # 'second' was input three calls ago
    Found
    >>> f = f('third') # 'third' was input three calls ago
    Found
    >>> f = f('third') # 'third' was not input three calls ago
    Not found
    """
    def f(x, y, z):
        def g(i):
            if x == i:
                print("Found")
            else:
                print("Not found")
            return f(y, z, i)
        return g
    return f(None, None, n)  

def chain_function():
    """
    >>> tester = chain_function()
    >>> x = tester(1)(2)(4)(5) # Expected 3 but got 4, so print 3. 1st chain break, so print 1 too.
    3 1
    >>> x = x(2) # 6 should've followed 5 from above, so print 6. 2nd chain break, so print 2
    6 2
    >>> x = x(8) # The chain restarted at 2 from the previous line, but we got 8. 3rd chain break.
    3 3
    >>> x = x(3)(4)(5) # Chain restarted at 8 in the previous line, but we got 3 instead. 4th break
    9 4
    >>> x = x(9) # Similar logic to the above line
    6 5
    >>> x = x(10) # Nothing is printed because 10 follows 9.
    >>> y = tester(4)(5)(8) # New chain, starting at 4, break at 6, first chain break
    6 1
    >>> y = y(2)(3)(10) # Chain expected 9 next, and 4 after 10. Break 2 and 3.
    9 2
    4 3
    """
    def g(curr, next_n, count_breaks):
        if not(curr == 0 or next_n == curr + 1):
            count_breaks += 1
            print(curr+1, count_breaks)
        return lambda n: g(next_n, n, count_breaks)
    return lambda first: g(0, first, 0)  