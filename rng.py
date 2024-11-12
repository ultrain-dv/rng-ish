import random
import os
import time

while True:
    rng = random.randint(1, 999999999999)

    999999999999
    os.system("clear")
    
    print("1. Roll \n2. Exit")
    
    rinput = input("[?]: ")
    if rinput == "1":
        print("Rolling...")
        time.sleep(1)
        os.system("clear")
        print(rng)
        time.sleep(1)

        
    elif rinput == "2":
        quit() 
    else:
        os.system("clear")
