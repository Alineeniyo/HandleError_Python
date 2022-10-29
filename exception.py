# import imp
from typing import Reversible
import sys  

try:
    x =int(input("X= ")) 
    y =int(input("X= "))
except ValueError:
    print("Error: Invalid input her by me")
    sys.exit(-1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error : Cannot divide ny zero by 0:")
    sys.exit(1)
print(f"The answer of {x} / {y} = {result}")