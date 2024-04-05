from string import ascii_letters, digits, punctuation
from itertools import product

value = ascii_letters + digits + punctuation
n = 20

for i in range(1, n + 1):
    for j in product(value, repeat=i):
        word = "".join(j)
        with open('password.txt', "a") as p:
            p.write(word)
            p.write("\n")
