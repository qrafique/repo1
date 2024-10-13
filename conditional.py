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