from tkinter import *
import random
widow=Tk()
widow.title("ÇEKİLİŞ")
widow.geometry("490x500+500+200")
widow.resizable(False,False)
frame=Frame(widow,bg="purple")
frame.grid(row=0)
katılımcılar=Label(frame,text="Participants:", bg="purple", fg="white",font=("", "11", "bold"))
katılımcılar.grid(row=0,column=0,padx=2)
textkişiler=Text(frame,height=7,width=45)
textkişiler.grid(row=0,column=1,padx=15,pady=15)

frame2=Frame(widow,bg="purple")
frame2.grid(row=1)

def çekiliş():
    kişiler=textkişiler.get("1.0",END)
    liste=kişiler.split()
    liste2=kişiler.split()
    textbox.delete("1.0",END)
    textbox.insert(END, "---The result is coming---")
    sayı=1
    for i in liste:
        a=random.choice(liste2)
        while i==a:
            a=random.choice(liste2)

        textbox.insert(END,"\n"+str(sayı)+")from "+i+" to "+a+"\n")

        liste2.remove(a)
        sayı+=1
textbox=Text(frame2,height=20,width=35)
textbox.grid(row=1,column=0,padx=9,pady=17)
button=Button(frame2,text="çekilişi başlat",width=15,height=4,command=çekiliş)
button.grid(row=1,column=1,padx=38)
widow.mainloop()
