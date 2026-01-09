#1 if number is zero print like "entered number is zero"
n=int(input())
if n==0:
    print("Entered number is zero")
print("program done")
    
#2 check if number is zero or not
num=int(input("Enter a number:"))
if num==0:
    print("Number is zero")
else:
   print("Number is not zero")

# 2nd approach
num=int(input("Enter a number:"))
if num!=0:
    print("Number is not zero")
else:
    print("Number is zero")

#check if number is even or odd
num=int(input("Enter a number:"))
if num%2==0:              
    print("number is even")
else:
    print("number is odd ")

num=int(input("enter a number:"))
if (num%2==0 and num>-1):
    print("It is positive and it is even")
elif (num%2==0 and num<0):
    print("It is negative and it is even")
elif (num%2!=0 and num>-1):
    print("It is positive  and it is odd")
elif (num%2!=0 and num<0):
    print("It is negative and it is odd")
else:
    print("program done")


