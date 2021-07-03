import random

structure_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
structure_2 = "abcdefghijklmnopqrstuvwxyz"
structure_3 = "!@#$%^&*()"
structure_4 = "0123456789"

create_password = structure_1 + structure_2 + structure_3 + structure_4
length = 20
password = "".join(random.sample(create_password,length))
print(password)