from tkinter import *
from tkinter import messagebox
#from tkinter import ttk
import DataBasy3
from os import system

ST = Tk()
ST.title('BOLENTIN DE NOTOS')
ST.geometry('600x300+450+250')
ST.configure(bg='white')
ST.resizable(width=False, height=False)
ST.attributes('-alpha', 0.9)
ST ['bg'] = 'black'


frame1 = Frame(ST, bg='white', width=379, height=300)
frame2 = Frame(ST, bg='white', width=218, height=300)#light blue
frame3 = Frame(frame1, bg='white', width=400, height=30)
frame1.pack(side=RIGHT)
frame2.pack(side=LEFT)
frame3.place(x=0, y=0)

im = PhotoImage(file="download.png")
w = Label(frame2, image=im)
w.im = im
w.place(x=0, y=100)

lb1 = Label(frame2, text='''CALENDARIO DE 
NOTAS 2019''', bg='white', foreground='blue', font='Arial 15 bold')
lb1.place(x=5, y=20)

im2 = PhotoImage(file="nota.png")
w2 = Label(frame1, image=im2)
w2.im2 = im2
w2.place(x=95, y=110)

lb2 = Label(frame1, text='Aluno', bg='white', font='Arial 14 bold')
lb3 = Label(frame1, text='Serie', bg='white', font='Arial 14 bold')
lb4 = Label(frame1, text='NT 1ª e 2ª Unidade', bg='white', font='Arial 14 bold')
lb5 = Label(frame1, text='NT 3ª e 4ª Unidade', bg='white', font='Arial 14 bold')
lb6 = Label(frame1, text='NOTAS DETALHADAS DOS ALUNOS', bg='white', foreground='blue', font='Arial 15 bold')

ent1 = Entry(frame1)
ent2 = Entry(frame1)
ent3 = Entry(frame1)
ent4 = Entry(frame1)

lb2.place(x=15, y=70)
lb3.place(x=10, y=100)
lb4.place(x=10, y=130)
lb5.place(x=10, y=160)
lb6.place(x=10, y=30)

ent1.place(x=175, y=70)
ent2.place(x=175, y=100)
ent3.place(x=175, y=130)
ent4.place(x=175, y=160)

def sair():
    ST.destroy()

def verP():
    system('sqlitebrowser')

def RegistroDatabasy():
    Aluno = ent1.get()
    Serie = ent2.get()
    Primeira = ent3.get()
    Segunda = ent4.get()

    if (Aluno == '' and Serie == '' and Primeira == '' and Segunda == ''):
        messagebox.showerror(title='Erro ao adiciona', message='Vocé deixou Algun Campo vasio!!!')

    else:
        DataBasy3.cursor.execute('''
        INSERT INTO Boletin_Academico(Aluno, Serie, Primeira, Segunda ) VALUES(?, ?, ? ,?)
        ''', (Aluno, Serie, Primeira, Segunda ))
        DataBasy3.conn.commit()
        messagebox.showinfo(title='Boletin_Academico', message='Nota adicionado ao Boletin_Academico')

bt = Button(frame1, text='ADICIONA', font='Arial 10 bold', bg='yellow', command=RegistroDatabasy)
bt.place(x=140, y=240)

bt0 = Button(frame3, text='Ver Todas as Notas', width=20, foreground='blue', bg='white', command=verP)
bt0.pack(side=LEFT)

bt1 = Button(frame3, text='Fecha Programa', bg='white', width=25, foreground='blue', command=sair)
bt1.pack(side=RIGHT)

ST.mainloop()