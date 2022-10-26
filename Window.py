import collections
import tkinter as tk
from tkinter import ttk
import calculation

ITEM_INDEX_WORK_LEVEL_OF_SUBORDINATION = [thing for thing in range(31)]
ITEM_TYPE = [1, 2]
APPLICATION = [thing for thing in range(31)]

flag_b = True
B = []
T_work = []
C_work_repair = []
cost_kilometer = []
distance_transport = []
distance_transportation_km = []
cost_transportation_km = []
number_transport = []

index_repair_work = 1
level_repair_work = 1

index_V = 1
level_V = 1


application_moving = 1
level_moving = 1


def moving_next():
    global application_moving
    global level_moving
    element_cost_kilometer = Entry_cost_kilometer.get()
    element_distance = Entry_cost_distance.get()
    element_distance_transportation_km  = Entry_distance_transportation_km.get()
    element_cost_transportation_km = Entry_cost_transportation_km.get()
    element_number_transport = Entry_number_transport.get()
    try:
        cost_kilometer.append(float(element_cost_kilometer))
        distance_transport.append((float(element_distance)))
        distance_transportation_km.append(float(element_distance_transportation_km))
        cost_transportation_km.append(float(element_cost_transportation_km))
        number_transport.append((float(element_number_transport)))
    except ValueError:
        print('Ошибка ввода в moving next')
    application_moving += 1
    L_frame_moving_cost_kilometer.configure(text='Стоимость 1 км перещения РПМТ\n' + str(level_moving) + '-го уровня по ' + str(application_moving) + '-й заявке')
    L_frame_moving_distance.configure(text='Расстояние между РО\n' + str(level_moving) + '-го уровня по ' + str(application_moving) + '-й заявке')
    L_distance_transportation_km.configure(text='Расстояние между РО ' + str(level_moving) + '-го уровня,\nи местонахождением объекта ремонта\nпо ' + str(application_moving) + '-й заяке', font=('Helvetica',10),justify='left')
    L_cost_transportation_km.configure(text='Стоимость одного км транспортировки\nобразца средства АТО в РПСТ РО\n' + str(level_moving) +'-го уровня по ' + str(application_moving) + '-й заявке', font=('Helvetica',10),justify='left')
    L_number_transport.configure(text='количество образцов средств АТО,\nнаправляемых для ремонта в РПСТ\nРО ' + str(level_moving) + '-го уровня по ' + str(application_moving) + '-й заявке', font=('Helvetica',10),justify='left')

def entr_moving():
    global application_moving
    global level_moving
    global cost_kilometer
    global distance_transport
    global distance_transportation_km
    global cost_transportation_km
    global number_transport
    element_cost_kilometer = Entry_cost_kilometer.get()
    element_distance = Entry_cost_distance.get()
    element_distance_transportation_km = Entry_distance_transportation_km.get()
    element_cost_transportation_km = Entry_cost_transportation_km.get()
    element_number_transport = Entry_number_transport.get()
    try:
        cost_kilometer.append(float(element_cost_kilometer))
        distance_transport.append((float(element_distance)))
        distance_transportation_km.append(float(element_distance_transportation_km))
        cost_transportation_km.append(float(element_cost_transportation_km))
        number_transport.append((float(element_number_transport)))
    except ValueError:
        print('Ошибка ввода в moving next')

    calculation.add_km_travel(cost_kilometer)
    calculation.add_distance(distance_transport)
    calculation.add_distance_transportation(distance_transportation_km)
    calculation.add_cost_km_transpot(cost_transportation_km)
    calculation.add_number_samples_funds(number_transport)
    level_moving += 1

    L_frame_moving_cost_kilometer.configure(
        text='Стоимость 1 км перещения РПМТ\n' + str(level_moving) + '-го уровня по ' + str(
            application_moving) + '-й заявке')
    L_frame_moving_distance.configure(
        text='Расстояние между РО\n' + str(level_moving) + '-го уровня по ' + str(application_moving) + '-й заявке')
    L_distance_transportation_km.configure(
        text='Расстояние между РО ' + str(level_moving) + '-го уровня,\nи местонахождением объекта ремонта\nпо ' + str(
            application_moving) + '-й заяке', font=('Helvetica', 10), justify='left')
    L_cost_transportation_km.configure(
        text='Стоимость одного км транспортировки\nобразца средства АТО в РПСТ РО\n' + str(
            level_moving) + '-го уровня по ' + str(application_moving) + '-й заявке', font=('Helvetica', 10),
        justify='left')
    L_number_transport.configure(text='количество образцов средств АТО,\nнаправляемых для ремонта в РПСТ\nРО ' + str(
        level_moving) + '-го уровня по ' + str(application_moving) + '-й заявке', font=('Helvetica', 10),
                                 justify='left')
    cost_kilometer = []
    distance_transport = []
    distance_transportation_km = []
    cost_transportation_km = []
    number_transport = []


def entr_frame_belt_work():
    global index_repair_work
    global level_repair_work
    global T_work
    global C_work_repair
    element_T_work = Entry_belt_work_T.get()
    element_C_repair = Entry_belt_work_C_repair.get()
    if index_repair_work == 1:
        print(T_work)
        try:
            T_work.append(float(element_T_work))
            C_work_repair.append(float(element_C_repair))
        except ValueError:
            print('entr_frame_belt_work')
        index_repair_work = 2
    elif index_repair_work == 2:
        try:
            T_work.append(float(element_T_work))
            C_work_repair.append(float(element_C_repair))
        except ValueError:
            print('entr_frame_belt_work')
        calculation.add_T_work(T_work)
        calculation.add_hour_operation(C_work_repair)
        index_repair_work = 1
        level_repair_work += 1
        T_work = []
        C_work_repair = []
    L_frame_belt_work_C_repair.configure(text='Средняя стоимость часа функционирования\nремонтного подразделения'
                                              ' ' + str(index_repair_work) + '-го типа')
    L_frame_belt_work_T.configure(text='T_рем ' + str(level_repair_work) + '-уровня ' + str(index_repair_work) + ''
                                                                                                                 '-го типа')



def entr_frame_B():
    global index_V
    global level_V
    global flag_b
    global B
    result = L_frame_B_B_enter.get()
    if index_V == 1:
        try:
            B.append(float(result))
        except ValueError:
            print("error")  # ошибка
        index_V = 2
    elif index_V == 2:
        try:
            B.append(float(result))
        except ValueError:
            print("error")  # ошибка
        calculation.add_B_RP(B)
        B = []
        index_V = 1
        level_V += 1
    L_B.configure(text='B ' + str(level_V) + '-уровня ' + str(index_V) + '-го типа')
    print(result)



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
frame_moving = tk.Frame(window, width=225, height=150, bg='blue')
frame_moving.place(relx=0, rely=0.27, relwidth=0.5, relheight=0.8)


frane_forming = tk.Frame(window, width=225, height=150, bg='green')
frane_forming.place(relx=0.5, rely=0.27, relwidth=0.5, relheight=0.6)

frame_consol = tk.Frame(window, width=450, height=100, bg='black')
frame_consol.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

## Фрейм B

L_B = tk.Label(frame_B, text='B ' + str(level_V) + '-уровня ' + str(index_V) + '-го типа')
L_B.grid(row='0', column='0', sticky='w', padx=10, pady=5)

L_frame_B_B_enter = ttk.Entry(frame_B, justify=tk.RIGHT, width=16)
L_frame_B_B_enter.grid(row='0', column='1', sticky='e', padx=10, pady=5)

enter_frame_B = ttk.Button(frame_B, text='Ввести', command=entr_frame_B) ## потом допишу ввод
enter_frame_B.grid(row='2',column='1',sticky='e',padx=10,pady=5)

#фрейм ремонта

L_frame_belt_work_T = tk.Label(frame_belt_work, text='T_рем ' + str(level_repair_work) + '-уровня ' + str(index_repair_work) + ''
                                                                                                                 '-го типа',font=('Helvetica',10))
L_frame_belt_work_T.grid(row='0', column='0', sticky='w', padx=10, pady=5)

L_frame_belt_work_C_repair = tk.Label(frame_belt_work, text='Средняя стоимость часа функционирования\nремонтного подразделения'
                                              ' ' + str(index_repair_work) + '-го типа',font=('Helvetica',10))
L_frame_belt_work_C_repair.grid(row='1', column='0', sticky='e', padx=10, pady=5)


Entry_belt_work_T = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_T.grid(row='0', column='1', sticky='e', padx=0, pady=5)

Entry_belt_work_C_repair = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_C_repair.grid(row='1', column='1', sticky='e', padx=0, pady=5)

button_frame_belt_work = ttk.Button(frame_belt_work, text='Ввести', command=entr_frame_belt_work)
button_frame_belt_work.grid(row='2', column='1', sticky='e', padx=10, pady=5)

## стоимость транспортировки 2.5.4

##2.5.5 + 2.5.6

L_frame_moving_cost_kilometer = tk.Label(frame_moving,text='Стоимость 1 км перещения РПМТ\n' + str(level_moving) + '-го уровня по ' + str(application_moving) + '-й заявке', font=('Helvetica',10),justify='left')
L_frame_moving_distance = tk.Label(frame_moving,text='Расстояние между РО ' + str(level_moving) + '-го уровня,\nпройденное РПМТ в ходе выполнения\nремонта в полевых условиях по\n' + str(application_moving) + '-й заявке',font=('Helvetica',10),justify='left')
L_distance_transportation_km = ttk.Label(frame_moving, text='Расстояние между РО ' + str(level_moving) + '-го уровня,\nи местонахождением объекта ремонта\nпо ' + str(application_moving) + '-й заяке', font=('Helvetica',10),justify='left')
L_cost_transportation_km = ttk.Label(frame_moving,text='Стоимость одного км транспортировки\nобразца средства АТО в РПСТ РО\n' + str(level_moving) +'-го уровня по ' + str(application_moving) + '-й заявке', font=('Helvetica',10),justify='left')
L_number_transport = ttk.Label(frame_moving, text='количество образцов средств АТО,\nнаправляемых для ремонта в РПСТ\nРО ' + str(level_moving) + '-го уровня по' + str(application_moving) + '-й заявке', font=('Helvetica',10),justify='left')

L_frame_moving_cost_kilometer.grid(row='0',column='0',sticky='w',padx=10,pady=3)
L_frame_moving_distance.grid(row='1',column='0',sticky='w',padx=10,pady=3)
L_distance_transportation_km.grid(row='2',column='0',sticky='w',padx=10,pady=3)
L_cost_transportation_km.grid(row='3',column='0',sticky='w',padx=10,pady=3)
L_number_transport.grid(row='4',column='0',sticky='w',padx=10,pady=3)

Entry_cost_kilometer = ttk.Entry(frame_moving,justify=tk.RIGHT, width=10)
Entry_cost_kilometer.grid(row='0',column='1',sticky='e',pady=3)

Entry_cost_distance = ttk.Entry(frame_moving,justify=tk.RIGHT,width=10)
Entry_cost_distance.grid(row='1',column='1',sticky='e',pady=3)

Entry_distance_transportation_km = ttk.Entry(frame_moving,justify=tk.RIGHT,width=10)
Entry_cost_transportation_km = ttk.Entry(frame_moving,justify=tk.RIGHT,width=10)
Entry_number_transport  = ttk.Entry(frame_moving,justify=tk.RIGHT,width=10)

Entry_distance_transportation_km.grid(row='2',column='1',sticky='e',padx=10,pady=3)
Entry_cost_transportation_km.grid(row='3',column='1',sticky='e',padx=10,pady=3)
Entry_number_transport.grid(row='4',column='1',sticky='e',padx=10,pady=3)
button_frame_moving_enter = ttk.Button(frame_moving,text='Следующий уровень\n(ввести уровень)', command=entr_moving)
button_frame_moving_enter.grid(row='5',column='0',sticky='w',pady=3,padx=10)

button_frame_moving_next = ttk.Button(frame_moving,text='следующая заявка', command=moving_next)
button_frame_moving_next.grid(row='5',column='1',sticky='e', pady=3)

#2.5.6
window.mainloop()
