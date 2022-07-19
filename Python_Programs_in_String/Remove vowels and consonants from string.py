string = input("Enter the string: ")
result = ''
for i in string:
  if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    i = ''
  result = result+i 
print("String after removing vowels: ", result)