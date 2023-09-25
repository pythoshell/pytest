#import pytest
import random
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def test_01():
    var = 503
    print("test1 -------------------")
    try:
        print(var +'entered' )
    except TypeError:
        print("Here you cannot append integer with string")
    assert var == 503, "Value is not True"

def test_02():
    print("test2 -------------------")
    """
    Multiplying list using a number just repeat the number of time the original list and stores in new variable
    """
    num = [1, 2, 3]
    print(num * 2)



def test_03():
    """
    split will output list based on the device
    """
    print("test3 -------------------" )
    import re
    Stmt1 = "Raj:x:1231:raj_01"
    a = re.split(':', Stmt1)
    print(a)
    print(type(a))


def test_04():
    """
    Both string can be attached together
    """
    print("test4 -------------------")
    var = 'python'
    print(var + 'entered')


def test_05():
    print("test5 -------------------")
    """ below code will identify how many count of number of 23 available in the list """
    score = [23, 33, 44, 55 , 66]
    print(score.count(23))

def test_06():
    """
    Floor will covert floating value to integer
    """
    print("test6 -------------------")
    import math
    val = 5.7
    print(type(val))
    new = math.floor(val)
    print( new)
    print(type(new))


def test_07():
    """
    seperator string can be used for print statements

    """
    print("test7 -------------------")
    a = 'infy'
    b = 123
    print(a,b, sep=":")
    #print(b)


def test_08():
    """
    & opertor returns set results
    """
    print("test8 ---------------------------------")
    temp1 = {11, 12, 13, 14}
    temp2 = {11, 12}
    print(temp1 & temp2)
    print(type(temp1 & temp2))

def test_09():
    """
    The random.randrange() function generates a
    random integer within a specified range. The function takes three arguments:

    start (inclusive): The lower bound of the range.
    stop (exclusive): The upper bound of the range.
    step (optional): The step size, which determines the
    spacing between possible values in the range.
    If not provided, the default step is 1.
    """
    print("test9 ---------------------------------")
    print(random.randrange(4, 5, 7))

    print('stefan salvatore'[5:])

def test_10():
    x = 'abcdef'
    i = 'a'
    while i in x:

        x = x[:-1]
        print(i,end=" ")

    for i in range(10):
        if i ==5:
            break
        else:
            print(i, end=" ")
    else:
        print("end")

def test_11():
    print("\ntest11 ---------------------------------")
    # Example 1: Using range(stop)
    for i in range(5):
        print(i)
    # Output: 0, 1, 2, 3, 4

    # Example 2: Using range(start, stop)
    for i in range(2, 5):
        print(i)
    # Output: 2, 3, 4

    # Example 3: Using range(start, stop, step)
    for i in range(1, 10, 2):
        print(i)
    # Output: 1, 3, 5, 7, 9


def test_12():
    print("test 12 ---------------------------------")
    """
    lstrip removes leading space 
    """
    a = " python program "
    print(a.lstrip('p'))

def test_13():
    print("\ntest 13 ---------------------------------\n")
    """
    
    """
    import re
    name1 = "Ram_09ati798@gmail.com"
    # print(re.findall('[\w]+',name1))
    # Using re.findall() to find all words in the string
    words = re.findall(r'[\w]+', name1)
    print(words)


def test_14():
    print("\ntest 14 ---------------------------------\n")
    """
    this functions only replaces number of string based on the count
    
    """
    xyz = ('apple', "applet ", 'app')
    abc = "assassinationssss"
    print(abc.replace('s', "S", len(max(xyz))))

def test_15():
    print("\ntest 15 ---------------------------------\n")
    """
    this functions only replaces number of string based on the count

    """
    names1 = ['a', 'b', 'c', 'd']
    names2 = names1
    names3 = names1[:]