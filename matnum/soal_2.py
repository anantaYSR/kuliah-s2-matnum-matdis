#deklarasi dan awal program
P = [[], [], []]
x = 0
print("\n==Penghitung Interpolasi Kuadrattik==")

#Perulangan input 3 titik dan niai x unutk mencari nilai x
for x in range(3):
    inp = float(input(
        "\n Masukan nilai x titik "+str(x+1)+" : "
    ))
    P[x].append(inp)
    inp = float(input(
        " Masukan nilai y titik "+str(x+1)+" : "
    ))
    P[x].append(inp)
    print(" > Titik"+str(x+1), "(P"+str(x+1)+") = (", P[x][0], ";", P[x][1], ")")
x = float(input(
    "\n Masukan nilai x : "
))
print(" > Nilai x = "+str(x))

#Penerapan rumus
x1 = P[0][0]
y1 = P[0][1]
x2 = P[1][0]
y2 = P[1][1]
x3 = P[2][0]
y3 = P[2][1]
y = y1*(x-x2)*(x-x3) / (x1-x2)*(x1-x3) + y2*(x-x1)*(x-x3) / (x2-x1)*(x2-x3) + y3*(x-x1)*(x-x2) / (x3-x1)*(x3-x2)

#Hasil
print("\n Nilai y adalah : "+str(y)+"\n > Titik ( "+str(x)+"; "+str(y)+" )")
