import random
import os
import time

while True:

    os.system("clear")
    
    print("1. Roll \n2. Exit")
    
    rinput = input("[?]: ")
    if rinput == "1":

        print("Rolling begins in 10 seconds.")
        time.sleep(2)
        print("Rolling...")
        while True:
            rng = random.randint(1, 10000)
            time.sleep(1)
            os.system("clear")
            print(rng)
            time.sleep(1)

        
    elif rinput == "2":
        quit() 
    else:
        os.system("clear")
