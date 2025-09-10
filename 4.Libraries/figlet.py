from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit('Invalid usage')
elif len(sys.argv) == 1:
    f = random.choice(figlet.getFonts())
    figlet.setFont(font=f)
elif len(sys.argv) == 3:
    if (sys.argv[1] != '-f' and sys.argv[1] != '--font') or sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid usage')
    figlet.setFont(font=sys.argv[2])
    
print(figlet.renderText(input('Input: ')))