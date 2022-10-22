import tkinter as tk
from tkinter import ttk

ITEM_INDEX_WORK_LEVEL_OF_SUBORDINATION = [thing for thing in range(31)]
ITEM_TYPE = [1, 2]

index_repair_work = ''
level_repair_work = ''

index_V = ''
level_V = ''

def entr_frame_belt_wor(event):
    pass


def submission_level_B(event):
    global level_V
    global index_V
    pass##Уровень подчинения для B
    level_V = combobox_frame_B_level_of_subordination.get()
    L_B.configure(text='B ' + str(level_V) + '-уровня ' + str(index_V) + '-го типа')

def type_B(event):#тип B
    global level_V
    global index_V
    index_V = combobox_frame_B_v_comb.get()
    L_B.configure(text='B ' + str(level_V) + '-уровня ' + str(index_V) + '-го типа')

def submission_level_C_repair(event):
    global index_repair_work
    global level_repair_work

    level_repair_work = combobox_frame_belt_work_level_of_subordination.get()
    L_frame_belt_work_C_repair.configure(text='Средняя стоимость часа функционирования\nремонтного подразделения'
                                           ' ' + str(index_repair_work) + '-го типа')
    L_frame_belt_work_T.configure(text='T_рем ' + str(level_repair_work) + '-уровня ' + str(index_repair_work) + ''
                                        '-го типа')

def type_C_repair(event):
    global index_repair_work
    global level_repair_work

    index_repair_work = combobox_frame_belt_work_v_comb.get()
    L_frame_belt_work_C_repair.configure(text='Средняя стоимость часа функционирования\nремонтного подразделения'
                                              ' ' + str(index_repair_work) + '-го типа')
    L_frame_belt_work_T.configure(text='T_рем ' + str(level_repair_work) + '-уровня ' + str(index_repair_work) + ''
                                                                                                                 '-го типа')


window = tk.Tk()
window.title('frame')
window.geometry('860x640')
window.minsize(300, 300)

## Разметка страницы

frame_B = tk.Frame(window, width=150, height=75, bg='red')
frame_B.place(relx=0, rely=0, relwidth=0.45, relheight=0.27)

frame_belt_work = tk.Frame(window, width=300, height=75, bg='yellow')
frame_belt_work.place(relx=0.45, rely=0, relwidth=0.55, relheight=0.27)
'''
frame_repair_tools = tk.Frame(window,width=300,height=75,bg='black')
frame_repair_tools.place(relx=0.45,rely=0.18,relwidth=0.55,relheight=0.22)
'''
frame_transport = tk.Frame(window, width=225, height=150, bg='blue')
frame_transport.place(relx=0, rely=0.27, relwidth=0.5, relheight=0.6)

frane_forming = tk.Frame(window, width=225, height=150, bg='green')
frane_forming.place(relx=0.5, rely=0.27, relwidth=0.5, relheight=0.6)

frame_consol = tk.Frame(window, width=450, height=100, bg='black')
frame_consol.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

## Фрейм B

L_B = tk.Label(frame_B, text='B')
L_B.grid(row='3', column='0', sticky='w', padx=10, pady=5)

L_frame_B_level_of_subordination = tk.Label(frame_B, text='уровень подчинения')
L_frame_B_level_of_subordination.grid(row='0', column='0', sticky='w', padx=10, pady=10)

L_frame_B_type = tk.Label(frame_B, text='тип подразделения')
L_frame_B_type.grid(row='1', column='0', sticky='w', padx=10, pady=10)

combobox_frame_B_level_of_subordination = ttk.Combobox(frame_B, values=ITEM_INDEX_WORK_LEVEL_OF_SUBORDINATION, width=3)
combobox_frame_B_level_of_subordination.grid(row='0', column='1', sticky='e', padx=13, pady=10)
combobox_frame_B_level_of_subordination.bind('<<ComboboxSelected>>', submission_level_B)

combobox_frame_B_v_comb = ttk.Combobox(frame_B, values=ITEM_TYPE, width=3)
combobox_frame_B_v_comb.grid(row='1', column='1', sticky='e', padx=20, pady=10)
combobox_frame_B_v_comb.bind('<<ComboboxSelected>>', type_B)

L_frame_B_B_enter = ttk.Entry(frame_B, justify=tk.RIGHT, width=16)
L_frame_B_B_enter.grid(row='3', column='1', sticky='e', padx=10, pady=10)

enter_frame_B = ttk.Button(frame_B, text='Ввести', command=entr_frame_belt_wor) ## потом допишу ввод
enter_frame_B.grid(row='4',column='1',sticky='e',padx=10,pady=10)

#фрейм ремонта

L_frame_belt_work_level_of_subordination = tk.Label(frame_belt_work, text='уровень подчинения')
L_frame_belt_work_level_of_subordination.grid(row='0', column='0', sticky='w', padx=10, pady=5)

L_frame_belt_work = tk.Label(frame_belt_work, text='тип поздразделения')
L_frame_belt_work.grid(row='1', column='0', sticky='w', padx=10, pady=5)

L_frame_belt_work_T = tk.Label(frame_belt_work, text='T_рем')
L_frame_belt_work_T.grid(row='2', column='0', sticky='w', padx=10, pady=5)

L_frame_belt_work_C_repair = tk.Label(frame_belt_work, text='Средняя стоимость часа функционирования\nремонтного '
                                                         'подразделения ' + '_' + '-го типа')
L_frame_belt_work_C_repair.grid(row='3', column='0', sticky='e', padx=10, pady=5)

combobox_frame_belt_work_level_of_subordination = ttk.Combobox(frame_belt_work,
                                                               values=ITEM_INDEX_WORK_LEVEL_OF_SUBORDINATION,
                                                               width=3)
combobox_frame_belt_work_level_of_subordination.grid(row='0', column='1', sticky='e', padx=13, pady=5)
combobox_frame_belt_work_level_of_subordination.bind('<<ComboboxSelected>>', submission_level_C_repair)

combobox_frame_belt_work_v_comb = ttk.Combobox(frame_belt_work, values=ITEM_TYPE, width=3)
combobox_frame_belt_work_v_comb.grid(row='1', column='1', sticky='e', padx=10, pady=5)
combobox_frame_belt_work_v_comb.bind('<<ComboboxSelected>>', type_C_repair)

Entry_belt_work_T = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_T.grid(row='2', column='1', sticky='e', padx=0, pady=5)

Entry_belt_work_C_repair = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_C_repair.grid(row='3', column='1', sticky='e', padx=0, pady=5)

button_frame_belt_work = ttk.Button(frame_belt_work, text='Ввести', command=entr_frame_belt_wor)
button_frame_belt_work.grid(row='4', column='1', sticky='e', padx=10, pady=5)

window.mainloop()
