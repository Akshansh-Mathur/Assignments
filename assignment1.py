#TASK 1: Print area of circle
r = float(input("enter radius = "))
Area = 3.14*(r*r)
print(Area)

#TASK2: Print Filename
x = input("Input The Filename: ")
f_exts = x.split(".")
print("The extention of the file is : " + repr(f_exts[-1]))

