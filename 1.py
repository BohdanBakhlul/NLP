import re

print("Enter your first name")
x = input()
if (not bool(re.match(r'(\b[A-Z]([a-z])*\b)', x))):
    print("Error")
print("Enter your last name")
x1 = input()
if (not bool(re.match(r'(\b[A-Z]([a-z])*\b)', x1))):
    print("Error")
print("Enter your city")
x2 = input()
if (not bool(re.match(r'^(\b[A-Z]\w*\s*)+$', x2))):
    print("Error")
print("Enter your phone number")
x3=input()
if (not bool(re.match(r'(\+\d{2} \(\d{2}\) \d{3}-\d{2}-\d{3})', x3))):
    print("Error")
print("Enter your post code")
x4=input()
if (not bool(re.match(r'(\d{2}-\d{3})', x4))):
    print("Error")
