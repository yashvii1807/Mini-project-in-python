import random
import string

#print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

# val = random.choice(['a', 'b', 'c', 'd'])
# print(val)


pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charValues)
print("Your random password is: ", password)    


#list comprehension [function for i in range(n)]
# res = [random.choice(charValues) for i in range(pass_len)]
# print(res)

