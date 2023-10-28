#1
import math
a =  int (input())
b =  int (input())
c= math.sqrt(a*a+b*b)
print(c)

#2
a=int(input())
a=a*45+(a//2)*5+((a+1)//2-1)*15
print(a//60+9, a%60)

#3
a =  int (input())
b =  int (input())
if (a > b):
    print(1)
elif (a < b) :
    print (2)
else :
    print(0)

#4
a =  int (input())
b =  int (input())
c =  int (input())
max = a
if b > max:
  max=b
if  c > max:
  max=c
print(max)

#5
a =  int (input())
b =  int (input())
c =  int (input())
if a==b==c:
   print(3)
elif a==b or b==c or c==a:
    print(2)
else:
    print(0)

 #6
 a = int(input())
b = int(input())
c = int(input())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)




