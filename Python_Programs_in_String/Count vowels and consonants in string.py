string = input("Enter the string: ")
count_vowels = 0
consonants = 0
for i in string:
  if i in  ('a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U'):
    count_vowels = count_vowels+1
  elif i.isalpha():
    consonants = consonants+1

print("Count Vowels: ",count_vowels, "Count Consonants: ",consonants)