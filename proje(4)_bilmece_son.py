# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 18:44:08 2022

@author: yiitk
"""

from tkinter import *
import time
import random


dosya = open('Yeni Metin Belgesi.txt',"r",encoding="utf-8")
oku = dosya.read()
a=''
b=[]
c=[]

m=0
oku=list(oku)
for i in oku:
    if i[0] !='\n' and i[0]!=']':
        a+=i[0]
    elif i[0]=='\n':
        a=''
    else:
        a+=']'
        b.append(a)
        a=''

def planlama(x):

    for i in x:
        global m
        m+=1
        if m<6 or i=='[':
            pass
        elif i!=']':
            global a
            a+=i
        else:
            g=''
            f=[]
            for i in a:
                if i!=',':
                    g+=i
                else:
                    f.append(g)
                    g=''
    m=0
    a=''
    return f
c.append(planlama(b[0]))
c.append(planlama(b[1]))


pencere = Tk()
pencere.geometry('500x400-50+50')
bilmece_cevap=c

soru=[]
pn=0
m=0
t4=0


def basla():
    soru=[]
    indexing=random.randrange(len(bilmece_cevap[0]))
    soru.append(bilmece_cevap[0][indexing])
    soru.append(bilmece_cevap[1][indexing])
    global a
    global t1
    t1 = time.time()
    a=soru
    textsru.delete(1.0,END)
    entry.delete(1.0,END)
    textsru.insert(1.0,soru[0])
    
def devam():
    global t2
    t2=time.time()
    global pn
    text2.delete(1.0,END)
    text2.insert(1.0,t2-t1)
    cevap=str(entry.get(1.0,CURRENT))
    t3=t2-t1
    global t4
    t4+=t3
    global m
    m+=1
    if cevap.casefold()==a[1].casefold() and t3 < 10:
        text1.delete(1.0,END)
        text1.insert(1.0,'doğru cevap')
        pn+=1
        text3.delete(1.0,END)
        text3.insert(1.0,pn)
        basla()
    elif t3 >= 10:
        text1.delete(1.0,END)
        text1.insert(1.0,'zaman aşımı')
        pn-=1
        text3.delete(1.0,END)
        text3.insert(1.0,pn)
        basla()
    else:
        text1.delete(1.0,END)
        text1.insert(1.0,'yanlış cevap')
        pn-=1
        text3.delete(1.0,END)
        text3.insert(1.0,pn)
        basla()
        
def sonlandır():
    textnw=Text(pencere,height=2,width=25)
    textnw.place(x=200,y=350)
    textnw.insert(END,f'final puanı {pn}\nsoru başına zaman {t4/m}')

label=Label(pencere)
label.config(text=(f'soru'),font=("Arial",15))
label.place(x=20,y=20)

textsru=Text(pencere,height=4,width=15)
textsru.place(x=20,y=80)

text1=Text(pencere,height=1,width=15)
text1.place(x=200,y=100)



label=Label(pencere)
label.config(text=(f'[geçen zaman ]'),font=("Arial",15))
label.place(x=200,y=20)

text2=Text(pencere,height=1,width=10)
text2.place(x=400,y=20)

text3=Text(pencere,height=1,width=10)
text3.place(x=400,y=50)

label=Label(pencere)
label.config(text=(f'[puan ]'),font=("Arial",15))
label.place(x=200,y=50)

label=Label(pencere)
label.config(text=(f'cevap'),font=("Arial",15))
label.place(x=20,y=200)

entry=Text(pencere,height=1,width=15)
entry.place(x=20,y=250)

buton=Button(pencere)
buton.config(text="Başla",bg="black",fg="white",command=basla)
buton.place(x=20,y=300)

buton=Button(pencere)
buton.config(text="Devam",bg="black",fg="white",command=devam)
buton.place(x=100,y=300)

buton=Button(pencere)
buton.config(text="sonlandır",bg="black",fg="white",command=sonlandır)
buton.place(x=50,y=350)

mainloop()
