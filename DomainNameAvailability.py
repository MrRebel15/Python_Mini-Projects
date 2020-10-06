from tkinter import *
import whois
import sys

def Domain_info():
    try:
        domain=whois.whois(str(domain_input.get()))
        if domain.domain_name==None:
            sys.exit(1)
    except:
        result="This Domain is Available"
    else:
        result="Oops! This Domain is Already Taken"
    answer.set(result)



window=Tk()
window.geometry("600x200")                     #width*Height of window
window.resizable(False,False)                  #Making window Resizble or not
window.title("Domain Name Availability")       #Name of the Window


Website_url=Label(window,text="Website Url :- ",font=("TimesNewRoman","16"))
Website_url.grid(row=1,column=1)
domain_input=Entry(window,font=("TimesNewRoman","16"))
domain_input.grid(row=1,column=2,pady=6)

btnn=Button(window,text="Check Domain",padx=8,pady=4,font=("TimesNewRoman","16"),command=Domain_info)
btnn.grid(row=2,column=2,pady=6)

answer=StringVar(window)
label1=Label(window,textvariable=answer,font=("TimesNewRoman","16"))
label1.grid(row=3,column=2,pady=6)


window.mainloop()