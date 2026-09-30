"""
atumanyire_ange.py
Demo script using the atumanyire_ange_calc package installed from TestPyPI.
"""

import atumanyire_ange_calc
from atumanyire_ange_calc import operations

print("atumanyire_ange_calc version:", atumanyire_ange_calc.__version__)
print("add(10, 25)               =", operations.add(10, 25))
print("multiply(3, 4)            =", operations.multiply(3, 4))
print("average([10, 20, 30, 40]) =", operations.average([10, 20, 30, 40]))
