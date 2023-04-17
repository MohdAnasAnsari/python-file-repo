try:
    import math
    print(math.exp(10))
except OverflowError:
    print("Value is to big, Overflow the memory.")
else:
    print("Success")

try:
    a=int(input("enter a \n"))
    b=int(input("enter b \n"))
    
    assert a==b
except AssertionError:
    print("give right value")

import sys
while True:
    try:
        a=int(input("enter an integer"))
        r=1/a
        break
    except:
        print("the error is ",sys.exc_info()[0],"occured")
        print("pls try again")
print("the value is ",r)


