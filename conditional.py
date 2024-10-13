marks=int(input("Enter your marks:"))
if marks>=90:
    print("Grade: A")
elif marks>=80:
    print("Grade: B")
elif marks>=70:
    print("Grade: C")
else:
    print("Fail")

day_of_week=input("Enter day of the week:").lower()

if day_of_week =='saturday' or day_of_week=='sunday':
    print("i will learn devOps live!")
else:
    print(" iwill practice devOps!!!!!!")


#calculator with coditional statemnt

num1= int(input("enter no.1 "))
num2=int(input("enter num2:"))
operation=input("choose option( '+','-','*','/','%')")
if operation=='+':
    sum=num1+num2
    print("addition:",sum)
elif operation=='-':
    diff=num1-num2
    print("subtraction:", sub)

elif operation=='*':
    product=num1*num2
    print("product:", product)
elif operation=='/':
    div=num1/num2
    print("division:",div)
elif operation=='%':
    rem=num1%num2
    print("remainder is:",rem)
else:
    print("invalid option")