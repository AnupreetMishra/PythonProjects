str = input("Enter a the string: ")
char = input("Enter the cahracter: ")
count = 0
for i in range(len(str)):
  if(str[i] == char):
    count = count+1
print("given character is occurred", count, "times")