#1
employees_var = open("employees.txt", "r")
print(employees_var.readable())
#2
print(employees_var.readline())
#3
print(employees_var.read())
#4
employees_var.close()
#5
employees_var = open("employees.txt", "r")

for for_var in employees_var.readlines():
    print(for_var)

employees_var.close()
