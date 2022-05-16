#input hasil
k=int(input('Input k : '))
n=int(input('Input n : '))

#perhitungan permutasi
list1=[]
i=0
if k==0:
    list1.append(1)
elif k!=0:
    while True:
        hasilpermutasi=(n-i)
        list1.append(hasilpermutasi)
        i+=1
        if((n-i)+k)==n:
            break

#perhitungan kombinasi
list2=[]
j=0
if k==0:
    list1.append(1)
elif k!=0:
    while True:
        hasilpermutasi=(k-j)
        list2.append(hasilpermutasi)
        j+=1
        if(k-j)==0:
            break

#Menghitung hasil
def hasil(data):
    r=1
    for x in data:
        r=r*x
        return r

#Hasil
print(f'P({n},{k})={hasil(list1)}')
print(f'P({n},{k})={hasil(list1)/hasil(list2)}')