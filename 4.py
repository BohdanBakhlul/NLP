import re

print("Enter text: ")
x = input()
emails = re.findall(r'[\w\.-]+@[\w\.-]+', x)
print(emails)

