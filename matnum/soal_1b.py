x1 = int(input("x1: "))
y1 = int(input("y1: "))
hasil1 = int(input("hasil: "))
print("==========")
x2 = int(input("x2: "))
y2 = int(input("y2: "))
hasil2 = int(input("hasil: "))
if x1 > x2:
    a = x1/x2
    X2 = a * x2
    Y2 = a * y2
    hasil3 = a * hasil2
    x = x1-X2
    y = y1-Y2
    hasil = hasil1-hasil3
    hasil = hasil/y
    Y = hasil
else:
    a = x2/x1
    X1 = a * x1
    Y1 = a * y1
    hasil3 = a * hasil1
    x = x2-X1
    y = y2-Y1
    hasil = hasil2-hasil3
    hasil = hasil/y
    Y = hasil
if y1 > y2:
    a = y1/y2
    X2 = a * x2
    Y2 = a * y2
    hasil3 = a * hasil2
    x = x1-X2
    y = y1-Y2
    hasil = hasil1-hasil3
    hasil = hasil/x
    X = hasil
else:
    a = y2/y1
    X1 = a * x1
    Y1 = a * y1
    hasil3 = a * hasil1
    x = x2-X1
    y = y2-Y1
    hasil = hasil2-hasil3
    hasil = hasil/x
    X = hasil
print("==========")
print(f"Hasil penyelesaian dari {x1}x + {y1}y = {hasil1} dan {x2}x + {y2}y = {hasil2} adalah x = {X} dan y = {Y}")