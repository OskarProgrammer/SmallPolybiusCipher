from os import system
system("cls")
sentence = input("Podaj wyraz jaki chcesz zakodowac: ")

lista=[]
def wypisanie(lista):
    print("",end="  ")
    for x in range(0,len(lista)):
        print(x+1,end=" ")
    print()
    for x in range(0,len(lista)):
        print(x+1,end=" ")
        for j in range(0,len(lista[x])):
            print(lista[x][j],end=" ")
        print()
    

sentence=list(sentence)

alfabet="abcdefghijklmnopqrstuvwxyz"

for x in range(5):
    lista.append([])
    for  j in range(5):
        lista[x].append(" ")
i=0
z=0
for x in range(0,len(lista)):
    
    for j in range(0,len(lista[x])):
        i+=1
        if alfabet[i-1]=="i":
            lista[x][j]="i/j"
            i+=1
            z+=1
            continue
        else:
            lista[x][j]=alfabet[i-1]


final=str()
for m in range(0,len(sentence)):
    for x in range(0,len(lista)):
        for j in range(0,len(lista[x])):
            if sentence[m]==lista[x][j]:
                final+=str(x+1)+str(j+1)
                final+=" "
            elif (sentence[m]=="i" or sentence[m]=="j")and(lista[x][j]=="i/j"):
                final+=str(24)
                final+=" "
    if sentence[m]==" ":
        final+="-"
        final+=" "
wypisanie(lista)

print(f"Twoje haslo to: {final} ")
print("Myslnik oznacza spacje")
