import tkinter as tk
from tkinter import ttk

index_REM = ''
level_REM = ''

index_V = ''
level_V = ''

def submission_clicks_B(event):
    global level_V
    global index_V
    level_V = combobox_frame_B_level_of_subordination.get()
    L_frame_B_B.configure(text='B ' + str(level_V) + '-уровня ' + str(index_V) + '-го типа')

def submission_divisions_B(event):
    global level_V
    global index_V
    index_V = combobox_frame_B_v_comb.get()
    L_frame_B_B.configure(text='B ' + str(level_V) + '-уровня ' + str(index_V) + '-го типа')
def entr_frame_belt_wor(event):
    pass
def type_evacuation_def(event):
    print('тут')


def entr():
    print('ввод')


def submission_divisions(event):
    global level_REM
    global level_REM
    index = combobox_frame_belt_work_v_comb.get()
    L_frame_belt_work_C_rem.configure(text='Средняя стоимость часа функционирования\nремонтного подразделения'
                                           ' ' + str(index) + '-го типа')



def submission_clicks(event):
    global level_REM
    level = combobox_frame_belt_work_level_of_subordination.get()


window = tk.Tk()
window.title('frame')
window.geometry('860x640')
window.minsize(300, 250)

## Разметка страницы

frame_B = tk.Frame(window, width=150, height=75, bg='red')
frame_B.place(relx=0, rely=0, relwidth=0.45, relheight=0.22)

frame_belt_work = tk.Frame(window, width=300, height=75, bg='yellow')
frame_belt_work.place(relx=0.45, rely=0, relwidth=0.55, relheight=0.22)
'''
frame_repair_tools = tk.Frame(window,width=300,height=75,bg='black')
frame_repair_tools.place(relx=0.45,rely=0.18,relwidth=0.55,relheight=0.22)
'''
frame_transport = tk.Frame(window, width=225, height=150, bg='blue')
frame_transport.place(relx=0, rely=0.22, relwidth=0.5, relheight=0.6)

frane_forming = tk.Frame(window, width=225, height=150, bg='green')
frane_forming.place(relx=0.5, rely=0.22, relwidth=0.5, relheight=0.6)

frame_consol = tk.Frame(window, width=450, height=100, bg='black')
frame_consol.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

# фрейм для записи В

item_index_work_level_of_subordination = [thing for thing in range(31)]
item_v = [1, 2]

L_B = tk.Label(frame_B, text='B')
L_B.grid(row='1', column='0', sticky='w', padx=10, pady=5)

L_frame_B_level_of_subordination = tk.Label(frame_B, text='уровень подчинения')
L_frame_B_level_of_subordination.grid(row='0', column='0', sticky='w', padx=10, pady=10)

combobox_frame_B_level_of_subordination = ttk.Combobox(frame_B,
                                                               values=item_index_work_level_of_subordination, width=3)
combobox_frame_B_level_of_subordination.grid(row='0', column='1', sticky='e', padx=13, pady=10)
combobox_frame_B_level_of_subordination.bind('<<ComboboxSelected>>', submission_clicks_B)

L_frame_B = tk.Label(frame_B, text='тип поздразделения')
L_frame_B.grid(row='1', column='0', sticky='w', padx=20, pady=10)

combobox_frame_B_v_comb = ttk.Combobox(frame_B, values=item_v, width=3)
combobox_frame_B_v_comb.grid(row='1', column='1', sticky='e', padx=20, pady=10)
combobox_frame_B_v_comb.bind('<<ComboboxSelected>>', submission_divisions_B)

L_frame_B_B = tk.Label(frame_B, text='B')
L_frame_B_B.grid(row='3', column='0', sticky='w', padx=10, pady=10)

L_frame_B_B_entr = ttk.Entry(frame_B, justify=tk.RIGHT, width=16)
L_frame_B_B_entr.grid(row='3',column='1',sticky='e',padx=10,pady=10)

### Второй фрейм

L_frame_belt_work_level_of_subordination = tk.Label(frame_belt_work, text='уровень подчинения')
L_frame_belt_work_level_of_subordination.grid(row='0', column='0', sticky='w', padx=10, pady=5)

combobox_frame_belt_work_level_of_subordination = ttk.Combobox(frame_belt_work,
                                                               values=item_index_work_level_of_subordination, width=3)
combobox_frame_belt_work_level_of_subordination.grid(row='0', column='1', sticky='e', padx=13, pady=5)
combobox_frame_belt_work_level_of_subordination.bind('<<ComboboxSelected>>', submission_clicks)

L_frame_belt_work = tk.Label(frame_belt_work, text='тип поздразделения')
L_frame_belt_work.grid(row='1', column='0', sticky='w', padx=10, pady=5)

combobox_frame_belt_work_v_comb = ttk.Combobox(frame_belt_work, values=item_v, width=3)
combobox_frame_belt_work_v_comb.grid(row='1', column='1', sticky='e', padx=10, pady=5)
combobox_frame_belt_work_v_comb.bind('<<ComboboxSelected>>', submission_divisions)

# this frame_belt_work
L_frame_belt_work_T = tk.Label(frame_belt_work, text='T_рем')
L_frame_belt_work_T.grid(row='2', column='0', sticky='w', padx=10, pady=5)


L_frame_belt_work_C_rem = tk.Label(frame_belt_work, text='Средняя стоимость часа функционирования\nремонтного '
                                                         'подразделения ' + '_' + '-го типа')
L_frame_belt_work_C_rem.grid(row='3', column='0', sticky='e', padx=10, pady=5)

Entry_belt_work_T = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_T.grid(row='2', column='1', sticky='e', padx=0, pady=5)

Entry_belt_work_C_rem = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_C_rem.grid(row='3', column='1', sticky='e', padx=0, pady=5)

button_frame_belt_work = ttk.Button(frame_belt_work, text='Ввести', command=entr_frame_belt_wor)
button_frame_belt_work.grid(row='4', column='1', sticky='e', padx=10, pady=5)


'''
# this frame repair tools
L_frame_repair_tools_typ_evacuation = tk.Label(frame_repair_tools,text='Тип средства')
L_frame_repair_tools_typ_evacuation.grid(row='0',column='0',sticky='w',padx=0,pady=0)

item_type_evacuation = [thing for thing in range(2,31)]
combobox_frame_repair_tools_type_evacuation = ttk.Combobox(frame_repair_tools, values=item_type_evacuation, width=3)
combobox_frame_repair_tools_type_evacuation.grid(row='0', column='1', sticky='e', padx=10, pady=0)
combobox_frame_repair_tools_type_evacuation.bind('<<ComboboxSelected>>', type_evacuation_def)

L_frame_repair_tools_number_evacuation = tk.Label(frame_repair_tools,text='Количество ремонтно-эвакуационных\n средств'
                                                                          '_-го типа в РО _-го уровня')
L_frame_repair_tools_number_evacuation.grid(row='1',column='0',sticky='w',padx=0,pady=10)

L_frame_repair_tools_cost_evacuation = tk.Label(frame_repair_tools,text='стоимость ремонтно-эвакуационных\n'
                                                                        ' средств _-го типа')
L_frame_repair_tools_cost_evacuation.grid(row='2',column='0',sticky='w',padx=0,pady=10)
'''

window.mainloop()
# В крации черную рамку перенести подальше от C_форм, в красную рамку добавить В_РП и получается, что формулу
# 2.5.3 мы доделали