# Metode Numerik Nomor 1

from sympy import * 

x,y = symbols("x, y")

kofesien = Matrix([[3,5],[5,2]])
print(kofesien)

variabel = Matrix([[x],[y]])
print(variabel)

konstanta=Matrix([[44],[29]])
print(konstanta)

print(solve(kofesien * variabel - konstanta))