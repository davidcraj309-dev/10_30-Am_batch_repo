print("========================================")
print("   WELCOME TO EMPLOYEE MANAGEMENT SYSTEM")
print("========================================")

print()


employees = []


employees.extend([
    {
    "id": 101,
    "name": "David",
    "department": "GenAi",
    "salary": 1000000,
},
{
     "id": 102,
     "name": "Yesu",
     "department": "HR",
     "salary": 35000,
    
},
{
     "id": 104,
     "name": "Arun",
     "department": "Marketing",
     "salary": 32000,
}
])

print()

#------------- ADD EMPLOYEE- 1----------------------- 

def add_employee(**details):
  print("========================================")
  print("             ADD EMPLOYEE")
  print("========================================")

  for key,value in details.items():
       print(key, ":",value)

  employees.append(details)
  print()
  print("Employee Added Successfully🎉")


#---------------VIEW EMPLOYEE- 2----------------------

def view_employee(employees):
  print("========================================")
  print("             VIEW EMPLOYEE")
  print("========================================")

  for data in employees:
     print(data)


#----------------SEARCH EMPLOYEE- 3-------------------

def search_employee(employees):
  print("========================================")
  print("             SEARCH EMPLOYEE")
  print("========================================")
  entered_id = int(input("Enter Employee ID: "))

  for employee in employees:
     if employee["id"] == entered_id:
        print("Employee Found Successfully!")
        print(employee)
        break
     
  else:
    print("Employee Not Found!")


#----------------Update Employee- 4--------------------

def update_employee(employees):
    print("========================================")
    print("             UPDATE EMPLOYEE")
    print("========================================")
    entered_id = int(input("Enter Employee ID: "))
    new_salary = int(input("Enter new salary: "))
    
    for employee in employees:
        if employee["id"] == entered_id:
          employee["salary"] =new_salary
          print("Employee Updated")
          print(employee)
          break
    else:
       print("Employee Not Found!")  


#-------------Delete Employee- 5---------------------

def delete_employee(employees):
    print("========================================")
    print("             DELETE EMPLOYEE")
    print("========================================")
    entered_id = int(input("Enter Employee ID: "))

    
    for employee in employees:
        if employee["id"] == entered_id:
            employees.remove(employee)
            print("Employee Deleted Successfully🎉!")
            print()
            print(employees)
            break
    else:
       print("Employee Not Found!")

     
#-----------------TOTAL SALARY- 6---------------------

def total_salary(employees):
    print("========================================")
    print("             TOTAL SALARY")
    print("========================================")

    total = 0

    for employee in employees:
       total += employee["salary"] 
    print("Total Employee Salary:",total)

#----------------HIGHEST SALARY- 7--------------------

def highest_salary(employees):
    print("========================================")
    print("             HIGHEST SALARY")
    print("========================================")

    highest = 0
    for employee in employees:
        if employee["salary"]>highest:
           highest = employee["salary"]
           employee_name_high = employee["name"]
           employe_department = employee["department"]

    print("Employee name:",employee_name_high)
    print("Employee department:",employe_department)
    print("Highest Employee Salary:",highest)
    



#------------- USER INPUT CHOICE ----------------------

while True:
    print()
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Total Salary")
    print("7. Highest Salary")
    print("8. Exit")

    print()

    choice = input("Enter your choice: ")

    if choice == "1":
        employee_id = int(input("Enter Employee Id: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Employee Department: ")
        salary = int(input("Enter Salary: "))

        add_employee(
            id=employee_id,
            name=name,
            department=department,
            salary=salary
        )

    elif choice == "2":
        view_employee(employees)

    elif choice == "3":
        search_employee(employees)

    elif choice == "4":
        update_employee(employees)

    elif choice == "5":
        delete_employee(employees)

    elif choice == "6":
        total_salary(employees)

    elif choice == "7":
        highest_salary(employees)

    elif choice == "8":
        print("Thank you for using Employee Management System! 😊")
        break