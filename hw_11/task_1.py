
    # 1. Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
    # 2. To each file append a random number between 1 and 100.
    # 3. Create a summary file (summary.txt) that contains name of the file and number in that file:
    #     A.txt: 67
    #     B.txt: 12
    #     ...
    #     Z.txt: 98

import random


def rand(a, b):
    rand = random.randint(a, b)
    return rand


with open("summary.txt", "a") as file1:

    for i in range(65, 91):
        name = chr(i)
        with open(f"{name}.txt", "w") as file:
            number = str(rand(1, 100))
            file.write(number)
        file1.write(f"{name}.txt: {number}\n")

