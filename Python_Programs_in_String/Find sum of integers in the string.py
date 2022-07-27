string = input("Enter the string: ")
sum = 0
for i in string:
  if i.isdigit():
    sum = sum+int(i)
print("Sum of integers:",sum)