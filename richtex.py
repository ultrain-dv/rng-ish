import random
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

while True:
    rng = random.randint(1, 999999999999)

    os.system("clear")

    rnoutput = Text(f"{rng}", style="bold #90ee90" justify="center")
    console.print(Panel(rnoutput, border_style="red"))
    
    print("Press Enter To Roll \n2. Exit")
    
    rinput = input("[?]: ")
    if rinput == "":
        os.system("clear")

    elif rinput == "2":
        os.system("clear")
        quit()

    else:
        os.system("clear")