import time
import datetime
import calendar
print("time.asctime(time.localtime(time.time()))",time.asctime(time.localtime(time.time())))
print("datetime.datetime.now()",datetime.datetime.now())
print("time.localtime",time.localtime)
print("datetime.datetime(2020,5,4)",datetime.datetime(2020,5,4))
print(datetime.datetime(2020,5,4,14,15,10))
calendar.prcal(2020)
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.year)
print(x.strftime("%a"))

x=datetime.datetime(2018,6,1)
print(x.strftime("%B"))
x=datetime.datetime(2018,6,1)
print(x.strftime("%b"))

print("==========================")
def between(l1,low,high):
    l2=[]
    for i in l1:
        if i>low and i<high :
            l2.append(i)
    return l2
l=[1,2,3,4,3,3,2,1]
print(between(l,2,5))

num = int(input("enter number: "))
fact=1
if num<0 or num==0:
    print(1)
else:
    for i in range(1,num+1):
        fact=fact*i
    print("The factorial of",num,"is",fact)    
