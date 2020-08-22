import random

u = "abcdefghijkl\
                mnopqrstuvwxyz1234\
                567890ABCDEFGHIJKLM\
                NOPQRSTUVWXYZ!@#$%^&*()_-+=*,.<>?:;"
passwordlen = 16
password = "".join(random.sample(u,passwordlen))
print(password)