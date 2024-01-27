#1.Code to demonstrate current date and time
"""import datetime
current_time=datetime.datetime.now()
print("The attributes of nows() are:")
print("Year:",current_time.year)
print("Month",current_time.month)
print("Day",current_time.day)
print("Hour",current_time.hour)
print("Minute",current_time.minute)
print("Second",current_time.second)"""


#2.Write a python program to get the python version you are using
"""import sys
print("Python version")
print(sys.version)
print("Version info")
print(sys.version_info)"""

#3.Write a python program that accepts an integer(n) and the computes the value of n+nn+nnn
"""n=int(input("Enter n value"))
n1=n*10+n
n2=n1*10+n
sum=n+n1+n2
print(sum)"""


#4.Write a python program to read and print various types of variable
"""a= int(input("enter a value"))
print(a)
print(a,"type is",type(a))
b=float(input("Enter the value"))
print(b)
print(b,"type is",type(b))
c=input("Enter a value")
print(c)
print(c,"type is",type(c))
list=[1,2,3,4]
print(type(list))
tuple=(5,6,7,9)
print(type(tuple))
set={11,12,13,14}
print(type(set))
dictionary={"name":"john","rollno":"123"}
print(type(dictionary))"""

#5.To write the program to print the calendar.
'''import calendar
yy=int(input("Enter the year"))
mm=int(input("Enter the month"))
print(calendar.month(yy,mm))'''



#6.Write a program to calculate the sqaure root using sqrt() function from math import sqrt.     #sqrt function is used to find the square root of the number,
"""from math import sqrt
number=int(input("Enter a number"))
square_root=sqrt(number)
print("The square root of the given number ",number," is",square_root)
"""

#7.Write a program to calculate the area and perimeter of triangle and circle
"""import math
pi=3.14
r=float(input("Enter radius"))
circle_area=pi*r*r
print("the area of the circle is",circle_area)
circle_perimeter=2*pi*r
print("The circle perimeter value =",circle_perimeter)
print("Enter sides of triangle")
a=float(input("enter a value"))
b=float(input("enter b value"))
c=float(input("enter c value"))
s=(a+b+c)/2
triangle_area=math.sqrt(s*((s-a)*(s-b)*(s-c)))
print("the area of triangle is",triangle_area)
triangle_perimeter=a+b+c
print("the triangle perimeter value",triangle_perimeter)"""
#10 python program to solve quadratic equation
"""import math
a=int(input("Enter the value of 'a':"))
b=int(input("Enter the value of 'b':"))
c=int(input("Enter the value of 'c':"))
dis=(b*b)-(4*a*c)
sqrtv=math.sqrt(abs(dis))
if a==0:
    print("Input correct quadratic equation")
elif dis>0:
    print("real and different roots")
    print((-b + sqrtv)/(2*a))
    print((-b - sqrtv)/(2*a))
elif dis==0:
    print("real and same roots")
    print(-b/(2*a))
else:
    print("Complex roots")
    print(-b/(2*a),"+ i",sqrtv)
    print(-b/(2*a),"- i",sqrtv)"""
#10 WRITE A PYTHON PROGRAM TO CONVERT CELSIUS TO FAHRENHEIT
"""cel=float(input("Enter the Celsius value:"))
fah=(cel*1.8)+32
print(cel," Celsius is equivalent to ",fah," Fahrenheit")"""

#8.Python program to demonstrate swapping of two variables.
"""x=10
y=50
temp=x
x=y
y=temp
print("Value of x:",x)
print("value of y:2",y)"""

#9. Python program to convert from kilometer to miles
"""kilometers=float(input("Enter the value in kilometers:"))
conv_fac=0.621371
miles=kilometers*conv_fac
print('%dkilometers is equal to %dmiles'%(kilometers,miles))"""
#Week3 
#10. Pythin program to find whether the given number is odd oe even
"""n=int(input("Enter a number"))
if (n%2==0):
    print("The given number is even")

else:
    print("The given number is odd")"""

#11. Write a python progam to get the difference between a given number and 17, if the number is greater than 17 it will return double difference
""""n=int(input("Enter the number "))
difference=17-n
print("the difference",difference)
if(n>17):
    absolute_difference=abs(17-n)
    double_diff=absolute_difference*2
    print("The result",double_diff)
"""
#12.
#13.Write a python program to calculate the sum of three given numbers, if the values are equal then three times of their sum.
"""def sum_thrice(x,y,z):
    sum=x+y+z
    if x==y==z:
        sum=sum*3
        return sum
    return sum
a=int(input("Enter 1 no"))
b=int(input("Enter 2 no"))
c=int(input("Enter 3 no"))
print("sum is:%d"%sum_thrice(a,b,c))"""
#14.write a python to find to factorial of the given number
"""def factorial(n):
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact=1
        while(n>1):
            fact*=n     
            n-=1
        return fact
m=int(input("Enter m value"))
result=factorial(m)
print("The value is ",result)"""
#Fact using reccursion
"""def factorial(n):
    if(n <= 1):
        return 1
    else:
        return(n*factorial(n-1))
n = int(input("Enter number:"))
print("Factorial:")
print(factorial(n))
"""
#15.Python program to print maximum of 3 numbers
""""a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
largest=0
if a>b and a>c:
    largest=a
elif b>a and b>c:
    largest=b
else:
    largest=c
print(largest,"is the largest of three numbers")"""
#16.check whether the given number is a leap year or not
"""year=int(input("Enter year:"))
if(year%4==0 and year%100!=0)or (year%400==0):
    print("The",year,"is a leap year" )
else:
    print(year,"is not a leap year")"""
#17.Wrire a program which will find all numbers which are divisible by 7 but not a multiple of 5 , between 2000 and 3200 (both included).
"""for i in range(2000,3201,1):
    if i%7==0 and i%5!=0:
        print(i,",\t",end="")"""
#18.Write a python program to check whether a number is divisible by 5 and 11 or not.

"""n=int(input("Enter the number"))
if(n%5==0 and n%11==0):
    print("The given number is divisible by 5 and 11")

else:
    print("The given number is not divisible by 11 and 5")

"""                                                                                   #if you end a comment with four double qoutes then you will get EOL error(end line error: interpreter expects a character their wbut we haven't given.)
#19. Write a pthon program to check whether a character is alphabet or not
"""while(True):
    print("do you want to continue press 1 other press 2:")
    a=int(input("enter a value"))
    if(a==1):
        n=input("enter n value")
        if(n.isalpha()):
           print("the enter {0} is a alphabet".format(n))
        else:
            print("The entered {0} is not a alphabet".format(n))"""
    

#20.Write a python program to check whether the given character is alphabet ,digit or special charcter
'''while(True):
    a=int(input("Do you want to continue press 1 or press 2:"))
    if(a==1):
        ch=input("please enter your own character:")
        if((ch>"a" and ch<="z")or (ch>="A" and ch<="Z")):
           print("The given character ",ch , "is a Alphabet")
        elif(ch>="0" and ch<="9"):
            print("The given character ",ch ,"is a digit")
        else:
            print("The given characer ",ch,"is a special character")

    else:
        break'''
#21.Write a python program to check whether the given alphabet is upper case or lowercase
'''while(True):
    print("do you want to continue press 1 other press 2")
    a=int(input("enter a value"))
    if(a==1):
        ch=input("Please enter your own character")
        if(ch.isupper()):
            print("The given chracter {0} is in uppercase".format(ch))
        elif(ch.islower()):
            print("The given character {0} is in lowercase".format(ch))
        else:
        
            print("Wrong input")

    else:
        break'''

#22 Write a python program to input week number and print week day.
'''weekday=int(input("Enter weekday number(1-7):"))
if (weekday==1):
    print("\m Monday")
elif (weekeday==2):
    print("\n Tuesday")
elif weekday==3:
    print("\n Wednesday")
elif weekday==4:
    print("\n Thursday")
elif weekday==5:
    print("\n Friday")
elif weekday==6:
    print("\n Saturday")
elif (weekday==7):
    print("\n Sunday")
'''
#23 Write a python program to print the number of notes
'''notes=[2000,500,200,100,50,20,10,5]
amount=int(input("Enter the amount:"))
for i in range(8):
    print("Rs.",notes[i],"notes will be:",amoount//note[i])
    amount=amount%notes[i]'''


#1Write a python program to print all natural numbers from 1 to n. using while loop.
'''n=int(input("Enter number"))
i=1
while(i<=n):
    print(i,end=" ")
    i=i+1'''

#2.Write a python program to find the sum of all odd numbers between 1 and n
'''n=int(input("Enter a number"))
sum=0
for i in range(1,n+1,2):
    sum=sum+i

print("The odd numbers sum =",sum)'''

#3.write a python to count number of digits in a number
'''n=int(input("enter number"))
count=0
while(n>0):
    n=n//10
    count=count+1
print("The number of digits are",count)'''

#4.Write a python program to find first and last digit of a number
'''num=int(input("enter a number"))
list=[]
while(num!=0):
    rem=num%10
    list.append(rem)
    num=num//10
list.reverse()
len=len(list)
print("first digit is %d and last digit is %d"%(list[0],list[len-1]))'''

#5.Write a python program to calculate sum of digits of number:
'''n=int(input("Enter number"))
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem
    n=n//10
print("The sum of the digits",sum)'''

#6.Write a python program to enter a number and print its reverse .
"""n=int(input("Enter a number"))
reverse=0
while(n>0):
    rem=n%10
    reverse=reverse*10+rem
    n=n//10

print("The reverse of a given number is ",reverse)"""

#24. To print prime numbers 
'''n=int(input("Enter the number "))
i=2
while i<=n:
    count=0
    j=1
    while j<=1:
        if i%j==0:
            count+=1    #wrong corrected
        j+=1

    if count>2:
        pass
    else:
        print("{}".format(i),end=" ")
    i+=1'''

#25. write a program to print the following pattern .
'''n=5
for i in range(1,n+1):
    for  j in range(1,1+i):
        print("*",end=" ")  
    print()'''
    

#26.write a program to print this pattern
'''n=int(input("enter a number"))
for i in range(n,0,-1):
    for  j in range(1,i+1):
        print("*",end=" ")
    print()'''
#27. Write a program to print this pattern
'''n=int(int(input("enter the number")))
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
n=int(input("enter a number"))

for i in range(n,0,-1):
    for j in range(1,n-1):
        print(" ",end=" ",)
    print("*")'''

#28 . Write a python code to check whether a number is amstrong number or perfect number or prime number or magic number or not .
'''num=int(input("enter a number: "))
if num>0:
    # Python program to check if the number is an Armstrong number or not
# initialize sum
    order=len(str(num))
    sum = 0
# find the sum of the cube of each digit
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp//= 10

# display the result
    if num == sum:
       print(num,"is an Armstrong number")
    else:
        print(num,"is not an Armstrong number")
#To check whether the given number is strong number or not
    sum=0
    temp=num  
    while(num):
        i=1   
        fact=1  
        rem=num%10  
        while(i<=rem):  
            fact=fact*i   # Find factorial of each number  
            i=i+1  
        sum=sum+fact  
        num=num//10  
    if(sum==temp):  
        print("Given number is a strong number")  
    else:  
        print("Given number is not a strong number")

#To check whether the given number is prime number
    count=0
    for i in range(2,num//2):
        if num%i==0:
            count=count+1
            break
        if (count==0 and num!=1):
            print("%d is a Prime number"%(num))
        else:
            print("%d is not a prime number"%(num))
#To check the given number is magical or not
    
   
    def digCount(self):
        num=self.num
        c = 0
        while num != 0:
            num = num//10
            c += 1    #how many digits
            return c
#Function to calculate the sum of digits of a number
    def digSum(self):
        num=self.num
        sum = 0
        for i in range(digCount(num)):
            sum+=num%10
            num//=10
        return sum
#Function to check whether a number is a magic number or not
    def magic_check(self):
        while(digCount(num)>1):
            num = digSum(num)
        if num == 1:
            return True
        else:
            return False
#Iterating over the list and using the magic_check function
    if()):
        print(" %d iS a Magic Number"%(num))
    else:
        print(" %d iS NOT a Magic Number"%(num))
        
else:
    print("The given input is invalid")'''

#To find frequency of each digit in a given number or series .eg: 124853398433

'''i=(1,2,4,8,5,3,3,9,8,4,3,3)'''

#To find sum of each digit that the final sum should be single digit

#1.To check whether number is palindrome or not
'''num=int(input("Enter a number"))
temp=num
rev=0
rem=0
while(num>0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
if(temp==rev):
    print("The number is a palindrome")
else:
    print("Not a palindrome")'''
    
#2. To find the frequency of each digit in a given integer.
'''n=int(input("Enter any number"))
print("Digit\tFrequency")
for i in range (1,10):
    count=0;
    temp=n
    while temp>0:
        digit=temp%10
        if digit==i:
            count=count+1
        temp=temp//10
    if count>0:
        print(i,"\t",count)'''

#31.Write a python program to print all the ASCII character with their values
'''i=0
while i<=225:
    print(i,"=",chr(i),end="")
    i+=1'''
#4.Write a python program to find all factors of a number
'''n=int(input("Enter a number "))
print("The factors of",n,"are:")
for i in range(1,n+1):
    if n%i==0:
        print(i,end=' ')'''
#5.Write a python program to calculate factorial of a given number.
'''n=int(input("Enter a number"))
fact=1
if n<0:
    print("Sorry, factorial does not exist for negative numbers ")
elif n==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("The factorial of %d is %d"%(n,fact))'''

#6. Write a python program to print all prime numbers between 1 to n.
'''n=int(input("enter the number:"))
c=0
for i in range (2,n+1):
  for k in range (2,i):
    if i%k==0:
      c=c+1
  if c==0:
    print(i)
  c=0  '''  
#Write a python progrm to print amstrong number, strong number,perfect
#number and magic number
'''print("menu list")
print("_________")
print("1.for checking Amstrong number")
print("2.for checking strong number")
print("3.for checking Prime number")
print("4.for checking Perfect number")
print("5.for checking magic number")
choice=int(input("Enter your choice"))
#Amstrong number
if(choice==1):
    num=int(input("enter any number"))
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**order
        temp=temp//10
    if num==sum:
        print(num,"is an Amstrong number")
    else:
        print(num,"is not an Amstrong number")
#strong number
if (choice==2):
    num=int(input("Enter a number"))
    sum=0
    temp=num
    while(num):
        i=1
        fact=1
        rem=num%10
        while(i<=rem):
            fact=fact*i
            i=i+1
        sum=sum+fact
        num=num//10
    if(sum==temp):
        print("The given number is a strong number")
    else:
        print("not a strong number")

#Prme numberz
if (choice==3):
    num=int(input("Enter a number"))
    count=0
    for i in range(1,num+1):
        if (num%i==0):
            count+=1
        if (count==2):
            print("The given number is a prime number")

        else:
           print("The given number is not a prime number")
#Perfect number
if (choice==4):
    n = int(input("Enter any number: "))
    sum1 = 0
    for i in range(1, n):
        if(n % i == 0):
            sum1 = sum1 + i
    if (sum1 == n):
        print("The number is a Perfect number!")
    else:
        print("The number is not a Perfect number!")

#Magic number
if (choice==5):
    import math
    num = int(input("Enter a Number \n"))
    digitCount = int(math.log10(num))+1
    sumOfDigits = 0

    temp = num 
    while( digitCount > 1):

        sumOfDigits = 0

        while(temp > 0):
            sumOfDigits += temp%10
            temp = temp//10

        temp = sumOfDigits
        digitCount = int(math.log10(sumOfDigits))+1
   
    if(sumOfDigits == 1):
        print("The given number is a Magic number")
    else:
        print("The given number is not a magic number") '''
#8.Write a python to print Fibonacci series up to n terms.

'''nterms = int(input("How many terms? "))

n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")

elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)

else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1'''
#METHOD 2 FOR FIBONACCI
'''xn=int(input("ENTER A NUMBER: "))
f=0
s=1
print("The fibbonacci series upto",n,"is:") #wrongone 
t=f+s
while(1<=n):
    print(t,end=''
        f=s
        s=t
          t=f+s
#36 .Create a list
"""list1=[]
n=int(input("Enter the number of elements into the list "))
for i in range(n):
    ele=int(input("Enter the element in the list "))
    list1.append(ele)
print("The list",list1)"""
#split funtion
#ASSIGNMENT 3

#write a python program to fint th largest number

list1=[10,20,4,99]
          list.sort()
          print("Largest element ,is ")'''

#2.Write a program to find the second largest number in list
'''def second_largest(list):
    list.sort()
    return list[-2]
list=[]
n=int(input("Enter the size of the list"))
for i in range(0,n):
    c=int(input("Enter element of list"))
    list.append(c)
print("second largest in ",list,"is")
print(second_largest(list))'''

#3.Write a python program to put even and odd elements in a list into two different lists
'''def split_list(my_list):
    even_list=[]
    odd_list=[]
    for i in my_list:
        if(i%2==0):
            even_list.append(i)
        else:
            odd_list.append(i)
    print("The list of even numbers are: ",even_list)
    print("The list of odd numbers are: ",odd_list)
my_list=[2,5,13,17,51,62,73,84,95]
print("The list is ")
print(my_list)
split_list(my_list)'''

#Program to print this pattern
'''n=int(input("Enter a number of rows you need: "))   
j=0
for i in range(1,n+1):
    for space in range(1,(n-i)+1):              # *
        print(end=" ")                          #***
    while j!=(2*i-1):                          #*****
        print("*",end="")
        j+=1
    j=0
    print()'''
#Program to pring VITAP in a single sided manner
"""list1="VIT AMARAVATI"
for i in range(1,14):
    print((list1[0:i]))
    i+=1"""
#Program to diff the age groups
#4. Program to merge two lists and sort it
'''a=[]
c=[]
n1=int(input("Enter the number of elements: "))
for i in range(1,n1+1):
    b=int(input("Enter element"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("enter numbers"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is :",new)

#program to sort the list according to the second element
list=[['A',34],['B',21],['C',26]]
for i in range(0,len(list)):
    for j in range(0,len(list)-i-1):
        if(list[j][1]>list[j+1][1]):
           temp=list[j]
           list[j]=list[j+i]
           list[j+1]=temp
print(list)'''

#5.python program to find the second largest number in a list using bubble sort
'''list=[]
n=int(input("Enter number of elements"))
for i in range(1,n+1):
    b=int(input("Enter number"))
    list.append(b)
for i in range(0,len(list)):
    for j in range(0,len(list)-i-1):
        if(list[j]>list[j+1]):
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print("The second lagest number ",list[n-2])'''

#6.Write a python program to sort a list according to the length of the elements
'''list=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=input("Enter elements")
    list.append(b)
list.sort(key=len)
print(list)'''

#7.write a python program to find the union of two lists
'''list1=[]
num1=int(input("Enter the size of the list1: ")
         
for i in range(num1):
    element=int(input("Enter any number"))
    list1.append(element)                             #error
list2=[]
num2=int(input("enter size of the list2: "))
for i in range(num2):
    element=int(input("enter any number"))
    list2.append(element)
union=list(set().union(list1,list2))'''

#8.Writea program to find the intersectionn of two lines
'''def intersection_list(list1,list2):
    list3=[value for value in list1 if value in list2]
    return list3
list1=[40,90,11,58,31,66,28,54,79]
list2=[58,90,54,31,45,11,66,28,26]
intersection=intersection_list(list1,list2)
print("The intersection of two lists is:",intersection)'''
#9.python program to print all odd indexed elements of a list
'''arr=[1,2,3,4,5,6,7,8,9,10]
print("Elements of a given array present on odd position:");
for i in range(1,len(arr),2):
    print(arr[i])'''
#Practical week 8
#5. Write a python program to replace the last value of tuples in a list.
"""for i in range(len(s)):
    t=list(s[i])
    t[-1]=100
    s[i]=tuple(t)
print(s)"""

"""
tup = (1,2,3,4)
print(tup[3],tup[-4])"""

#2.Write a python program to find the repeated items of a tuple
'''lst=(2,3,5,3,2,5,7,8,9,0)
newlst=[]
for i in lst:
    j = lst.count(i)
    if j > 1:
        if i in lst:
            continue
        newlst.append(i)
print(newlst)'''
#1.Write a python program to get the 4ht element and 4th element from last of a tuple.
"""t=('w','3','r','5','d','f','d')
print(t)
element4=t[3]
print(element4)
last4th=t[-4]
print(last4th)"""
#3.write a python program to check whether an element exists within a tuple.
"""nt= (4,6,8,11,22,43,58,99,16)
print("Tuples Items =",nt)
n = int(input("enter tuple to check"))
result = n in nt
print("does our number contains the",n,"?",result)"""
#4. Write a Python program to unzip a list of tuples into individual lists.
"""l = [(1,2),(3,4),(8,9)]
print(list(zip(*l)))"""

#6. Write a Python program to remove an empty tuple(s) from a list of tuples
"""L = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
L = [t for t in L if t]
print(L)"""
#7.Write a Python program to convert a list of tuples into a dictionary.
"""s=[('Key 1', 1), ('Key 2', 2), ('Key 3', 3), ('Key 4', 4), ('Key 5', 5)]
T=dict(s)
print(T)"""
#8.Write a Python program to find the highest 3 values of corresponding keys in a dictionary 
"""from collections import Counter
d1= {'t':3,'u':4,'t':6,'o':5,'r':21}
k = Counter(d1)
high = k.most_common(3)
print("dictionary with highest value")
print("Keys:Values")
for i in high:
    print(i[0],":",i[1],"")
    """
#pallindrome
"""def pallindrome(X):
    a=X[::-1]
    return a
X=input("enter a string")
a=pallindrome(X)
if X==a:
    print("the string enter is a pallindrome")
else:
    print("the strin entered is not a pallindrome")"""

#6ht in ques.paper
"""file=open("file_name",'a')
list1=[]
ls2=["tarunscbe@gmail.com","jojo.x.@gmail.com","hemanth.gay.x@gmail.com"]
list1.append(ls2)
file.write(list1    )
file=open("file_name",'r')
print(file.read())"""
"""def finding(n):
    sum=0
    while(n!=0):
        p=n%10
        sum=sum+p
        n=n//10
    return sum
print(finding(899898))"""
#prime
"""def prime(n):
    if (n==1):
        print("no")
    elif (n>=1):
        for i in range(2,n+1):
            if n%i==0:
                print("no")
            else:
                print(i )
print(prime(25))"""
"""def factorial(n):
    if n<=0:
        return 1
    if n>0:
        fct=n*factorial(n-1)
    return fct
print(factorial(6))"""


