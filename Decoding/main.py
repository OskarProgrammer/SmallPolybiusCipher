#polibiusza szyfr
from os import system

def wypisz(list):
    print("",end="")
    for x in range (0,len(list)):
        print(f"{x+1:6}",end=" ")
    print("")
    for  x in range(0,len(list)):
        print(str(x+1)+"    ",end="")
        for j in range(0,len(list[x])):
            print(f"{list[x][j]:6}",end=" ")
        print()

spacja=" "

alfabet="abcdefghijklmnopqrstuvwxyz"

list=[]

coor=[]

print("KAZDA KOLEJNA LITERE ZAPISUJ DWOMA CYFRAMI POLACZONYMI")
print("ZE SOBA BEZ SPACJI, JESLI CHCESZ ZROBIC SPACJE W ZAPISIE")
print("PO PROSTU ZROB SPACJE LUB DWIE, A PROGRAM AUTOMATYCZNIE TO ZAREJESTRUJE")
print("KAZDA KOLEJNA LITERE ZATWIERDZAJ ENTEREM ")
print("NATOMIAST JESLI CHCESZ WYJSC Z TRYBU PODAWANIA KOLEJNYCH DWOCH CYFR")
print("PODAJ LICZBE Z PRZEDZIALU OD (-NIESKONCZONOSCI DO 10)")
print("(OD 56 DO + NIESKONCZONOSCI)")
sentence=input("Podaj to co chcesz zakodowac albo zdekodowac: ")
if (str(sentence).isspace()==True) or (int(sentence)  in range (11,56)):
    coor.append(sentence)
else:   
    pass
system("cls")

while (str(sentence).isspace()==True) or (int(sentence)  in range (11,56)) : 
    sentence=input("Podaj to co chcesz zakodowac albo zdekodowac: ")
    coor.append(sentence)
    system("cls")
if len(coor)==0:
    pass
else:
    del coor[len(coor)-1]

for x in range(5):
    list.append([])
    for  j in range(5):
        list[x].append(" ")
i=0
z=0
for x in range(0,len(list)):
    
    for j in range(0,len(list[x])):
        i+=1
        if alfabet[i-1]=="i":
            list[x][j]="i/j"
            i+=1
            z+=1
            continue
        else:
            list[x][j]=alfabet[i-1]
final=str()
for x in range(0,len(coor)):
    if coor[x]=="  " or coor[x]==" ":
        final+=" "  
    else:
        coor[x]=str(coor[x])
        first=coor[x][0]
        second=coor[x][1]
        if list[int(first)-1][int(second)-1]=="i/j":
            litera="i"
        else:
            litera=(list[int(first)-1][int(second)-1])
        final+=litera
###34 43 25 11 42 " " 55 55 ==> oskar zz
wypisz(list)
system("pause")
system("cls")
print(f"Twoj wyraz to: {final}")
print("UWAGA LITERA i W WYRAZIE MOZE OZNACZAC j")


