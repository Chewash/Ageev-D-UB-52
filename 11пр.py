from tkinter import*
from tkinter import ttk
from tkinter.ttk import Combobox
from tkinter.ttk import Radiobutton
from tkinter import messagebox
from tkinter import scrolledtext
def zagr():
    with open('abc.txt') as file:
        txt.insert('1.0',file.read())
    file.close()
def schet():
    if combo.get()=='+':
        F=int(txt1.get())+int(txt2.get())
    if combo.get()=='-':
        F=int(txt1.get())-int(txt2.get())
    if combo.get()=='*':
        F=int(txt1.get())*int(txt2.get())
    if combo.get()=='/':
        F=int(txt1.get())/int(txt2.get())
    r4.configure(text=str(F))
def vibor():
    messagebox.showinfo("Ваш выбор", "Вы выбрали: "+str(selected.get()))
    
window = Tk()
window.title("Агеев Даниил Валерьевич")
window.geometry("500x500")

menu=Menu(window)
new_item=Menu(menu)
new_item.add_command(label='загрузить',command=zagr)
menu.add_cascade(label="файл",menu=new_item)
window.config(menu=menu)

tab_control=ttk.Notebook(window)

#1 вкладка
tab1=ttk.Frame(tab_control)
tab_control.add(tab1,text="Калькулятор")
tab_control.pack(expand=1,fill="both")

r1=Label(tab1,text="введите число 1")
r1.grid(column=0,row=0)
txt1=Entry(tab1,width=10)
txt1.grid(column=1,row=0)

combo=Combobox(tab1)
combo['values']=('','+','-','*','/')
combo.current(0)
combo.grid(column=1,row=2)

r2=Label(tab1,text="введите число 2")
r2.grid(column=0,row=3)
txt2=Entry(tab1,width=10)
txt2.grid(column=1,row=3)

btn=Button(tab1,text="Вывести ответ",command=schet)
btn.grid(column=0,row=4)

r3=Label(tab1,text="Ваш ответ: ")
r3.grid(column=0,row=5)

r4=Label(tab1,text="")
r4.grid(column=1,row=5)


#2
tab2=ttk.Frame(tab_control)
tab_control.add(tab2,text="Выбор")
selected=IntVar()
rad1=Radiobutton(tab2,text='Первый',value=1,variable=selected)
rad1.grid(column=0,row=1)
rad2=Radiobutton(tab2,text='Второй',value=2,variable=selected)
rad2.grid(column=0,row=3)
rad3=Radiobutton(tab2,text='Третий',value=3,variable=selected)
rad3.grid(column=0,row=5)

btn=Button(tab2,text="Показать выбор",command=vibor)
btn.grid(column=0,row=7)



#3
tab3=ttk.Frame(tab_control)
tab_control.add(tab3,text="Текст")
txt=scrolledtext.ScrolledText(tab3,width=55,height=10)
txt.grid(column=0,row=0)



window.mainloop()
