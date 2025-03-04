import random
import os


while True:
    rng = random.randint(1, 999999999999)

    os.system("clear")
    
    print(rng)
    print("----------------")
    print("Press Enter To Roll \n2. Exit")
    
    rinput = input("[?]: ")
    if rinput == "":
        os.system("clear")

    elif rinput == "2":
        quit()

    else:
        os.system("clear")
