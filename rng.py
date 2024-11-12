import random
import os

while True:
    rng = random.randint(1, 10)

    os.system("clear")
    
    print("1. Roll \n2. Exit")
    
    rinput = input("[?]: ")
    if rinput == "1":
        print("Rolling...")
        os.system("clear")
        time.sleep(1)
        print(rng)
        os.system('pause')

        
    elif rinput == "2":
        quit() 
    else:
        os.system("clear")