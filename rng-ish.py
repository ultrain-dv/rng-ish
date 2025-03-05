import random
import os
from rich.console import Console
from rich.text import Text
from rich.panel import Panel

console = Console()

while True:
    rng = random.randint(1, 100)

    os.system("clear")

    rnoutput = Text(f"{rng}", style="bold #add8e6", justify="center")
    console.print(Panel(rnoutput, border_style="#00008B"))
    
    console.print("Press Enter To Roll", style="bold #add8e6")
    console.print("To Exit, the program. [bold red]Press 2[/bold red]")

    rinput = input("[?]: ")
    if rinput == "":
        os.system("clear")

    elif rinput == "2":
        os.system("clear")
        quit()

    else:
        os.system("clear")
