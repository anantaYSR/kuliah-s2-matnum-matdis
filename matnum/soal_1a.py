a=3
b=5
c=5
d=2
total1=44
total2=29
print("------------------------")
print("-- Metode Subtitusi --")
print("------------------------")
print(f"{a}x + {b}y = {total1}")
print(f"{c}x + {d}y = {total2}")
print("------------------------")
print(f"{c}x + {d}y = {total2}")
print(f"{c}x = {total2} - {d}y")
dbagic = d / c
total2bagic = total2 / c
print(f"x = {total2bagic} - {dbagic}y")
print("------------------------")
print(f"{a}x + {b}y = {total1}")
print(f"{a}({total2bagic} - {dbagic}y) + {b}y = {total1}")
ac = total2bagic * a
adc = a * dbagic
print(f"{ac} - {adc}y + {b}y = {total1}")
print(f"-{adc}y + {b}y = {total1} - {ac}")
total1kurangac = total1 - ac
adckurangb = -adc + b
print(f"{adckurangb}y = {total1kurangac}")
ketemu_y = total1kurangac / adckurangb
print(f"y = {ketemu_y}")
print("------------------------")
print(f"x = {total2bagic} - {dbagic}y")
print(f"x = {total2bagic} - {dbagic}({ketemu_y})")
dcy = dbagic * ketemu_y
print(f"x = {total2bagic} - {dcy}")
ketemu_x = total2bagic - dcy
print(f"x = {ketemu_x}")
print("------------------------")
print(f"Jadi, x = {ketemu_x} dan y = {ketemu_y}")