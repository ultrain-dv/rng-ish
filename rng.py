import random
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

while True:
    rng = random.randint(1, 100)

    os.system("clear")

    print(rng)

    print("-----------")
    
    print("Press Enter To Roll")
    print("To Exit, the program. Press 2")

    rinput = input("[?]: ")
    if rinput == "":
        os.system("clear")

    elif rinput == "2":
        os.system("clear")
        quit()

    else:
        os.system("clear")