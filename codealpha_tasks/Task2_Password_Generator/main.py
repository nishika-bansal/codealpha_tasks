import random
import string

length = int(input("Enter Password Length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ''.join(
    random.choice(characters)
    for i in range(length)
)

print("Generated Password:")
print(password)