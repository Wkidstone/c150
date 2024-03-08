from tkinter import *
import random
root=Tk()
root.title("Random country and city")

root.geometry("800x500")
c_in=Entry(root)
ci_in=Entry(root)
c=Label(root)
ci=Label(root)
r_c=Label(root)
r_ci=Label(root)

country_n=[]
cities_n=[]

def country():
    c_n = c_in.get()
    country_n.append(c_n)
    c["text"]="Countries: " + str(country_n)
    ci_n = ci_in.get()
    cities_n.append(ci_n)
    ci["text"]="Cities: " +str(cities_n)
    

def random_cci():
    l_c=len(country_n)
    ran_c=random.randint(0, l_c-1)
    random_c=country_n[ran_c]
    r_c['text']= "Random Country : " + str(random_c)
    l_ci=len(cities_n)
    ran_ci=random.randint(1,l_ci-1)
    random_ci=cities_n[ran_ci]
    r_ci["text"]= "Random City : " +str(random_ci)


button=Button(root,text="Display Country And City Names", command= country)
button1=Button(root,text="Display a Random City And Country",command= random_cci)
button.place(relx=0.5,rely=0.4, anchor=CENTER)
c_in.place(relx=0.5,rely=0.2, anchor=CENTER)
ci_in.place(relx=0.5,rely=0.3,anchor=CENTER)
c.place(relx=0.5,rely=0.5, anchor=CENTER)
ci.place(relx=0.5,rely=0.6,anchor=CENTER)
button1.place(relx=0.5,rely=0.7,anchor=CENTER)
r_c.place(relx=0.5,rely=0.8,anchor=CENTER)
r_ci.place(relx=0.5,rely=0.9,anchor=CENTER)
 



root.mainloop()