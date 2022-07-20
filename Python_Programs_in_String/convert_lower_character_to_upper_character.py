string = input("Enter the string: ")
result = ''
for i in string:
  if i.islower():
    i = i.upper()
  result = result+i
print("converted sttring:", result)