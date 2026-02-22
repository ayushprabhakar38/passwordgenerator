# Code logic by Ayush Prabhakhar 

import random
import string

while True:
    try:
        length = int(input("Enter password length: ").strip())
        if length <= 0:
            print("Length must be positive.")
            continue
        break
    except ValueError:
        print("Invalid input. Enter a number.")

base = input("Enter a word/text to transform into a memorable password: ").strip()

def ask(q):
    while True:
        a = input(q + " (y/n): ").strip().lower()
        if a == "y":
            return True
        if a == "n":
            return False
        print("Enter y or n.")

while True:
    use_upper = ask("Include uppercase letters?")
    use_lower = ask("Include lowercase letters?")
    use_digits = ask("Include numbers?")
    use_symbols = ask("Include symbols?")
    pools = []
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append(string.punctuation)
    if pools:
        break
    print("Select at least one character type.")

subs = {"a":"@","i":"1","e":"3","o":"0","s":"$","l":"7","t":"+"}

password = []
for ch in base:
    low = ch.lower()
    if low in subs and random.random() < 0.6 and use_symbols:
        password.append(subs[low])
    else:
        if use_upper and use_lower:
            password.append(ch.upper() if random.random() < 0.5 else ch.lower())
        elif use_upper:
            password.append(ch.upper())
        elif use_lower:
            password.append(ch.lower())
        else:
            password.append(ch)

allchars = "".join(pools)

while len(password) < length:
    password.append(random.choice(allchars))

if len(password) > length:
    password = password[:length]

random.shuffle(password)
print("".join(password))