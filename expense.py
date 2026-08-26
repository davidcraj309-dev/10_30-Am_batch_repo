name = input("Enter your name: ")

food = int(input("Enter Food expense: "))
travel = int(input("Enter travel expense: "))
shopping = int(input("Enter shopping expense: "))
other = int(input("Enter other expense: "))

print("\n-------- Expense Summary --------\n")

print("Name:", name)
print("Food:", food)
print("Travel:", travel)
print("Shopping:", shopping)
print("Other:", other)

total_expense = food + travel + shopping + other

print("Total Expense:", total_expense)



if total_expense > 500:
    print("Your expenses reached daily limit")
else:
    print("Your expenses are within the limit")