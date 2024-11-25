import random
import os
import time


while True:
    rng = random.randint(1, 999999999999)

    999999999999
    os.system("clear")
    
    print("1. Roll \n2. Exit \nOr press Enter to Roll")
    
    rinput = input("[?]: ")
    if rinput == "1":
        os.system("clear")
        print(rng)
        time.sleep(1)

    elif rinput == "":
        os.system("clear")
        print(rng)
        time.sleep(1)

    elif rinput == "2":
        quit()

    else:
        os.system("clear")
