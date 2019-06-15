from tkinter import *
from sqlite3 import *

con = connect('kuharicabaza.db') 
c = con.cursor() 



master = Tk()
master.title("KUHARICA") 
master.geometry("800x850")
master.configure(background='#949494')




naslov = Label(master, text=" Dobro došli u Kuharicu! ", font=("Times New Roman",32,"bold italic"), fg="white", bg="black", bd="5").place(relx=0.5, rely=0., relwidth=0.8, relheight=0.10, anchor="n")



L0 = Label(master, text="Dodaj novi recept:", font=("Times New Roman", 24, "bold") , bd="5", relief="sunken" ).place(relx=0.25, rely=0.12, relwidth=0.40, relheight=0.06, anchor='n')

L1 = Label(master, text = "Naziv recepta", font=("Times New Roman",16, "bold"), bd="3", relief="sunken").place(relx=0.1, rely=0.20, relwidth=0.18, relheight=0.04, anchor='n')

L2 = Label(master, text = "Recept", font=("Times New Roman",16, "bold"), bd="3", relief="sunken").place(relx=0.1, rely=0.30, relwidth=0.18, relheight=0.04, anchor='n')


naziv_recepta = Entry(master, bd="5")
#naziv_recepta = Text(master, bd="5",)
naziv_recepta.place(relx=0.35, rely=0.20, relwidth=0.25, relheight=0.04, anchor='n')


recept = Entry(master, bd="5")
recept.place(relx=0.35, rely=0.30, relwidth=0.25, relheight=0.5, anchor='n')





L4 = Label(master, text="Pretraži recepte:", font=("Times New Roman", 24, "bold") , bd="5", relief="sunken").place(relx=0.75, rely=0.12, relwidth=0.40, relheight=0.06, anchor='n')

L5 = Label(master, text = "Naziv recepta", font=("Times New Roman",16, "bold" ), bd="3", ).place(relx=0.60, rely=0.20, relwidth=0.18, relheight=0.04, anchor='n')


pretraga_recepta = Entry(master, bd="5",relief="sunken" )

pretraga_recepta.place(relx=0.85, rely=0.20, relwidth=0.25, relheight=0.04, anchor='n')





frame = Frame(master)
frame.place(relx=0.75, rely=0.35, relwidth=0.48, relheight=0.5, anchor='n')
            
Lb = Listbox(frame, height = 12, width = 53,font=("Times New Roman", 12), selectmode="single") 
Lb.pack(side = LEFT, fill = Y)
            
scroll = Scrollbar(frame, orient = VERTICAL)
scroll.config(command = Lb.yview)
scroll.pack(side = RIGHT, fill = Y)
Lb.config(yscrollcommand = scroll.set)


Lb.insert(0 , )


        

def dodaj_recept():
        print("Dodali ste recept")

        c.execute('INSERT INTO recepti (naziv_recepta, recept) VALUES (?, ?)',
                  (naziv_recepta.get(), recept.get() ))
        con.commit()

        naziv_recepta.delete(0, END)
        recept.delete(0, END)
        
       


def pretraga():
        print("Pretražili ste")
        
        c.execute('SELECT * FROM recepti WHERE naziv_recepta = ?', (pretraga_recepta.get(),))
        #if c.fetchall():
         #   L8 = Label(master, text="Recept pronaðen", font=("arial",10), fg="green", relief="raised", bd="5", width="17").place(relx=0.75, rely=0.30 ,relwidth=0.40, relheight=0.04, anchor='n')
        #else:
         #   L8 = Label(master, text="Recept nije pronaðen", font=("arial",10), fg="red", relief="raised", bd="5").place(relx=0.75, rely=0.30 ,relwidth=0.40, relheight=0.04, anchor='n')
            
        a = c.execute('SELECT naziv_recepta FROM recepti WHERE naziv_recepta LIKE (?)', (pretraga_recepta.get(),))
        podaci = c.fetchall()
        for a in podaci:
                Lb.insert(1,a)

        con.commit()

        pretraga_recepta.delete(0, END)
        

def ispis():
        print("Ispisali ste sve postojeće recepte")
        c.execute('SELECT naziv_recepta FROM recepti ORDER BY naziv_recepta ASC')
        podaci = c.fetchall()
            
        for row in podaci:
                Lb.insert(1,row)         

        con.commit()

def otvori():
       idx = Lb.curselection()[0]
       c.execute('SELECT * FROM recepti ORDER BY naziv_recepta ASC')
       podaci = c.fetchall()
       recept = podaci[idx]
       naslov_prikaza = recept[0]
       tekst_prikaza = recept [1]
       

       print("Otvorili ste recept: "+  str(naslov_prikaza))
       
       recept_prikaz = Toplevel(master)
       recept_prikaz.title((naslov_prikaza)) 
       recept_prikaz.geometry("400x350")
       recept_prikaz.configure(background='#949494')
       display = Label(recept_prikaz, text=(str(naslov_prikaza)+"\n"+"\n"+str(tekst_prikaza)), font=("times new roman",16) )
       display.pack()
       





gumb1 = Button(master, text="Spremi",
               command=dodaj_recept,
               font=("Times New Roman", 12, "bold"),
               relief="raised")
gumb1.place(relx=0.35, rely=0.82,relwidth=0.10, relheight=0.04, anchor='n' )


gumb2 = Button(master, text="Pretraži",
               command=pretraga,
               font=("Times New Roman", 12, "bold"),
               relief="raised")
gumb2.place(relx=0.85, rely=0.25 ,relwidth=0.10, relheight=0.04, anchor='n' )


gumb3 = Button(master, text="Prikaži sve recepte",
               command=ispis,
               font=("Times New Roman", 12, "bold"),
               relief="raised")
gumb3.place(relx=0.75, rely=0.3 ,relwidth=0.43, relheight=0.04, anchor='n' )

gumb4 = Button(master, text="Otvori",
               command=otvori,
               font=("Times New Roman", 12, "bold"),
               relief="raised")
gumb4.place(relx=0.85, rely=0.870 ,relwidth=0.10, relheight=0.04, anchor='n' )



     







master.mainloop()
c.close()
con.close()
