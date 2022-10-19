import tkinter as tk
from tkinter import ttk

def entr():
    print('ввод')

def call(event):
    index = combobox_frame_belt_work_v_comb.get()
    L_frame_belt_work_C_rem.configure(text='Средняя стоимость часа функционирования\nремонтного подразделения'
                                           ' ' + str(index) + '-го типа')


def call_1(event):
    index = combobox_frame_belt_work_level_of_subordination .get()
    print(index)

window = tk.Tk()
window.title('frame')
window.geometry('860x640')
window.minsize(300, 250)

frame_B = tk.Frame(window,width=150,height=150,bg='red')
frame_B.place(relx=0,rely=0, relwidth=0.3, relheight=0.4)

frame_belt_work = tk.Frame(window,width=300,height=150,bg='yellow')
frame_belt_work.place(relx=0.3,rely=0,relwidth=0.7,relheight=0.4)

frame_transport = tk.Frame(window, width=225,height=150,bg='blue')
frame_transport.place(relx=0,rely=0.4,relwidth=0.5,relheight=0.6)

frane_forming = tk.Frame(window,width=225,height=150,bg='green')
frane_forming.place(relx=0.5,rely=0.4,relwidth=0.5,relheight=0.6)

frame_consol = tk.Frame(window,width=450,height=100,bg='black')
frame_consol.place(relx=0,rely=0.8,relwidth=1,relheight=0.2)

L_B = tk.Label(frame_B,text='B')
L_B.grid(row='1',column='2',sticky='w',padx=10,pady=5)
L_B_index = tk.Label(frame_B,text='PH' + str('h'))
L_B_index.grid(row='2',column='2',sticky='w',padx=13,pady=5)

item  = [1,2]
item_1 = [thing for thing in range(31)]

L_frame_belt_work_level_of_subordination = tk.Label(frame_belt_work,text='уровень подчинения')
L_frame_belt_work_level_of_subordination.grid(row='0',column='0',sticky='w',padx=10,pady=10)
combobox_frame_belt_work_level_of_subordination = ttk.Combobox(frame_belt_work,values=item_1, width=3)
combobox_frame_belt_work_level_of_subordination.grid(row='0',column='3',sticky='e',padx=10,pady=10)
combobox_frame_belt_work_level_of_subordination.bind('<<ComboboxSelected>>', call_1)

L_frame_belt_work = tk.Label(frame_belt_work,text='тип поздразделения')
L_frame_belt_work.grid(row='1',column='0',sticky='w',padx=10,pady=10)
combobox_frame_belt_work_v_comb = ttk.Combobox(frame_belt_work,values=item, width=3)
combobox_frame_belt_work_v_comb.grid(row='1',column='3',sticky='e',padx=10,pady=10)
L_frame_belt_work_T = tk.Label(frame_belt_work,text='T_рем')
L_frame_belt_work_T.grid(row='2',column='0',sticky='w',padx=10,pady=10)

combobox_frame_belt_work_v_comb.bind('<<ComboboxSelected>>', call)

L_frame_belt_work_C_rem = tk.Label(frame_belt_work,text='Средняя стоимость часа функционирования\nремонтного подразделения ' + '_' + '-го типа')
L_frame_belt_work_C_rem.grid(row='3',column='0',sticky='e',padx=10,pady=10)

Entry_belt_work_T = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_T.grid(row='2',column='3',sticky='e',padx=0,pady=10)

Entry_belt_work_C_rem = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_C_rem.grid(row='3',column='3',sticky='e',padx=0,pady=10)

button_frame_belt_work = ttk.Button(frame_belt_work, text='Ввести', command=entr)
button_frame_belt_work.grid(row='4',column='2',sticky='n',padx=10,pady=10)
window.mainloop()