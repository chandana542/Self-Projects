import tkinter as tk

root=tk.Tk()

root.title('Calculator Program')
root.geometry('600x600')

def bg():
    root.config(bg='#0B0033')

bg()

def val(i):
    text_box.insert('end', i)
    return i

def evaluate():
    exp=text_box.get('1.0', 'end-1c')
    result=eval(exp)
    text_box.delete('1.0', 'end')
    text_box.insert('1.0',result)

def clear():
    text_box.delete('1.0','end')

label = tk.Label(root,text='Calculator',font=('Arial',30,'bold'),fg='skyblue',bg='#0B0033')
label.pack()

text_box = tk.Text(root,height=2,font=('Arial',20))
text_box.pack(padx=20,pady=20)

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

btn1 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='1',command=lambda: val('1'))
btn1.grid(row=0,column=0,sticky='nsew')

btn2 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='2',command=lambda: val('2'))
btn2.grid(row=0,column=1,sticky='nsew')

btn3 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='3',command=lambda: val('3'))
btn3.grid(row=0,column=2,sticky='nsew')

btn4 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='+',command=lambda: val('+'))
btn4.grid(row=0,column=3,sticky='nsew')

btn5 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='4',command=lambda: val('4'))
btn5.grid(row=1,column=0,sticky='nsew')

btn6 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='5',command=lambda: val('5'))
btn6.grid(row=1,column=1,sticky='nsew')

btn7 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='6',command=lambda: val('6'))
btn7.grid(row=1,column=2,sticky='nsew')

btn8 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='-',command=lambda: val('-'))
btn8.grid(row=1,column=3,sticky='nsew')

btn9 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='7',command=lambda: val('7'))
btn9.grid(row=2,column=0,sticky='nsew')

btn10 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='8',command=lambda: val('8'))
btn10.grid(row=2,column=1,sticky='nsew')

btn11 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='9',command=lambda: val('9'))
btn11.grid(row=2,column=2,sticky='nsew')

btn12 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='x',command=lambda: val('*'))
btn12.grid(row=2,column=3,sticky='nsew')

btn13 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='0',command=lambda: val('0'))
btn13.grid(row=3,column=0,sticky='nsew')

btn14 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='÷',command=lambda: val('/'))
btn14.grid(row=3,column=1,sticky='nsew')

btn15 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='=',command=evaluate)
btn15.grid(row=3,column=2,sticky='nsew')

btn16 = tk.Button(frame, font=('Arial',20),bg='#0B0033',fg='white',text='C',command=clear)
btn16.grid(row=3,column=3,sticky='nsew')

for i in range(4):
    frame.columnconfigure(i, weight=1)
    frame.rowconfigure(i, weight=1)


root.mainloop()