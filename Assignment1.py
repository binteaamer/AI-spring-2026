
//Q1
name= input("Enter student name: ")
marks= int(input ("enter marks: "))
if marks >=85 :
  grade= "a"
elif marks >=70:
  grade="b"
elif marks>= 50:
  grade="c"
else :
    grade= "fail"

print("student name:", name)
print ("marks: ", marks)
print("grade: ", grade)


//Q2
n= int(input("Enter a numbeer: "))
count = 0
print("Even numbers: ")
for i in range (1, n+1):
    if i%2==0:
      print(i)
      count+=1
print("total even numbers: ", count)

//q3
students = {}
for i in range(3):
    name = input("enter student name: ")
    marks= int(input ("enter marks"))
    students[name] = marks
  
print("student records:")
for name, marks in students.items():
  print(name, ":", marks)

//q4
choice = 0

while choice != 3:
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Result:", num1 + num2)

    elif choice == 2:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        print("Result:", num1 - num2)

    elif choice == 3:
        print("Exit program")

    else:
        print("invalid choice")

//q5p
def calculate_average(marks):
    total = 0
    count = 0
    
    for m in marks:
        total = total + m
        count = count + 1
    
    average = total / count
    return average

markslist = [87, 90, 78]
result = calculate_average(markslist)

print("Marks:", markslist)
print("Average marks:", result)

