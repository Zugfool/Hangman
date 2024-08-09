import os
import random

os.chdir("C:\\Users\\egeme\\OneDrive\\Masaüstü\\PYHTON\\Benim_kodlar\\Hangman")
a = open("hangman.txt",encoding="utf8")
okuma= a.read()
okuma=okuma.strip().split()
real_list=[]

for i in okuma:
    if i.isalpha()==True:
        i=i.lower()
        real_list.append(i) 
    elif i[-1]==",":
        i=i.replace(",","")
        i=i.lower()
        real_list.append(i)
a.close()

pick=random.choice(real_list)

start=""
for i in range(len(pick)):
    start+="-"
print(start)

can=7
place=[]
tahminler=[]
        
while can>=0:
    og= False
    while og== False:
        tahmin= str(input(f"Harf tahmin edin. Kelimeyi bulmak için {can} şansınız var: "))
        if tahmin not in tahminler:
            og= True
        else:
            print("Zaten bu harfi daha önce denemiştiniz. \n")
        tahminler.append(tahmin)
    if tahmin.lower() in pick:
        for i in range(len(pick)):
            if pick[i]==tahmin.lower():
                place.append(i)
    else:
        can=can-1
    space=""
    for i in range(len(pick)):
        if i not in place:
            space+="-"
        else:
            space+=pick[i]
    if space.isalpha()==True:
        print(f"Tebrik ederim, KAZANDINIZ, hem de daha {can} denemeniz vardı.")
        print(pick)
        break
    print(space + "\n")
    if can==0:
        print(f"KAYBETTİNİZ. Doğru kelime: {pick}")
        break
