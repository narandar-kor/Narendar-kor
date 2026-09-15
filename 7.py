S_name = input("Enter Student name : ")
Roll_no = int(input("Enter Student Roll_no. : "))

sub1 = int(input("Enter first subject marks : "))
sub2 = int(input("Enter second subject marks : "))
sub3 = int(input("Enter third subject marks : "))
sub4 = int(input("Enter fourth subject marks : "))
sub5 = int(input("Enter fifth subject marks : "))

Total_marks = sub1+sub2+sub3+sub4+sub5
percentage = (Total_marks/500)*100

if percentage>=80:
    Grade = "A-1"
elif percentage>=70:
    Grade = "A"
elif percentage>=60:
    Grade = "B"
elif percentage>=50:
    Grade = "C"
elif percentage>=40:
    Grade = "D"
else:
    Grade = "Fail"


a=sub1<40 or sub2<40 or sub3<40 or sub4<40 or sub5<40
if a:
    result = "Fail"
else:
    result = "Pass"


print("\n\n<<<<<<<<<<- MARK SHEET ->>>>>>>>>>\n")
print("Student name : ",S_name)
print("Student Roll_no. : ",Roll_no)
print("\n1st Subject marks : ",sub1)
print("2st Subject marks : ",sub2)
print("3st Subject marks : ",sub3)
print("4st Subject marks : ",sub4)
print("5st Subject marks : ",sub5)
print("\nPercentage : ",percentage)
print("Grade : ",Grade)
print("Result : ",result)


