string = input("Enter the string: ")
result = ''
char = input("Enter the character which replaced by the space: ")
for i in string:
  if i == ' ':
    i = char
  result = result + i
print("Replaced string = ", result)