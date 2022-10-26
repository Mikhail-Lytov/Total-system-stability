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

type_RP_frane_forming = 1
type_V_frane_forming = 1
level_frane_forming = 1

index_V = 1
level_V = 1

application_moving = 1
level_moving = 1

tool = 2
level_repair_evacuation = 1
type_repair_evacuation = 1

number_repair_tools = []
cost_repair_facilities = []
number_repairmen = []
cost_preparation = []

number_repair_tools_v = []
cost_repair_facilities_v = []
number_repairmen_v = []
cost_preparation_v = []

number_repair_evacuation = []
cost_repair_evacuation = []

number_repair_evacuation_v = []
cost_repair_evacuation_v = []


def result_enter():
    result = calculation.calculation()
    L_result = ttk.Label(frame_consol, text=str(result))
    L_result.grid(row='1', column='0')
    print(result)


def evacuation_enter():
    global number_repair_evacuation
    global cost_repair_evacuation
    global number_repair_evacuation_v
    global cost_repair_evacuation_v
    global tool
    global level_repair_evacuation
    global type_repair_evacuation
    element_number_repair_evacuation = Enter_number_repair_evacuation.get()
    element_cost_repair_evacuation = Enter_cost_repair_evacuation.get()
    try:
        number_repair_evacuation.append(element_number_repair_evacuation)
        cost_repair_evacuation.append(element_cost_repair_evacuation)
    except ValueError:
        print('error repair_evacuation_next')

    number_repair_evacuation_v.append(number_repair_evacuation)
    cost_repair_evacuation_v.append((cost_repair_evacuation))
    if type_repair_evacuation == 1:
        type_repair_evacuation = 2

    elif type_repair_evacuation == 2:
        type_repair_evacuation = 1
        level_repair_evacuation += 1
        calculation.add_number_repair_and_evacuation_facilities(number_repair_evacuation_v)
        calculation.add_cost_repair_and_evacuation_facilities(cost_repair_evacuation_v)
        number_repair_evacuation_v = []
        cost_repair_evacuation_v = []
    number_repair_evacuation = []
    cost_repair_evacuation = []
    tool = 2
    L_submission.configure(text='РП ' + str(type_repair_evacuation) + '-го типа')
    L_number_repair_evacuation.configure(
        text='Количество ремонтно-эвак\nсредств ' + str(tool) + '-го типа в РО\n' + str(
            level_repair_evacuation) + '-го уровня')
    L_cost_repair_evacuation.configure(text='Стоимость ремонтно-эвак\nсредств ' + str(tool) + '-го типа')


def evacuation_next():
    global tool
    global number_repair_evacuation
    global cost_repair_evacuation
    element_number_repair_evacuation = Enter_number_repair_evacuation.get()
    element_cost_repair_evacuation = Enter_cost_repair_evacuation.get()
    try:
        number_repair_evacuation.append(element_number_repair_evacuation)
        cost_repair_evacuation.append(element_cost_repair_evacuation)
    except ValueError:
        print('error repair_evacuation_next')

    tool += 1
    L_number_repair_evacuation.configure(
        text='Количество ремонтно-эвак\nсредств ' + str(tool) + '-го типа в РО\n' + str(
            level_repair_evacuation) + '-го уровня')
    L_cost_repair_evacuation.configure(text='Стоимость ремонтно-эвак\nсредств ' + str(tool) + '-го типа')


def forming_enter():
    global number_repair_tools_v
    global cost_repair_facilities_v
    global number_repairmen_v
    global cost_preparation_v
    global number_repair_tools
    global cost_repair_facilities
    global number_repairmen
    global cost_preparation
    global type_V_frane_forming
    global level_frane_forming
    global type_RP_frane_forming
    element_number_repair_tools = Enter_number_repair_tools.get()
    element_cost_repair_facilities = Enter_cost_repair_facilities.get()
    element_number_repairmen = Enter_number_repairmen.get()
    element_cost_preparation = Enter_cost_preparation.get()
    try:
        number_repair_tools.append(float(element_number_repair_tools))
        cost_repair_facilities.append(float(element_cost_repair_facilities))
        number_repairmen.append(float(element_number_repairmen))
        cost_preparation.append(float(element_cost_preparation))
        number_repairmen_v.append(number_repairmen)
        cost_repair_facilities_v.append(cost_repair_facilities)
        number_repairmen_v.append(number_repairmen)
        cost_preparation_v.append(cost_preparation)
    except ValueError:
        print('ошибка forming_enter')
    if type_V_frane_forming == 1:
        type_V_frane_forming = 2
    elif type_V_frane_forming == 2:
        type_V_frane_forming = 1
        level_frane_forming += 1
        calculation.add_number_repair_tools(number_repair_tools_v)
        calculation.add_cost_repair_tools(cost_repair_facilities_v)
        calculation.add_number_repairmen(number_repairmen_v)
        calculation.add_cost_repairmen(cost_preparation_v)
        number_repair_tools_v = []
        cost_repair_facilities_v = []
        number_repairmen_v = []
        cost_preparation_v = []
    number_repair_tools = []
    cost_repair_facilities = []
    number_repairmen = []
    cost_preparation = []

    type_RP_frane_forming = 1
    L_number_repair_tools.configure(text='количество средств ремонта' + str(
        type_RP_frane_forming) + '-го типа\nв РП ' + str(type_V_frane_forming) + '-го типа ' + str(
        level_frane_forming) + '-го уровня подчинения')
    L_cost_repair_facilities.configure(text='стоимость средств ремонта ' + str(
        type_RP_frane_forming) + '-го типа\nв РП ' + str(type_V_frane_forming) + '-го типа')
    L_number_repairmen.configure(text='количество ремонтников в РП ' + str(type_V_frane_forming) + '-го типа\n' + str(
        level_frane_forming) + '-го уровня подчинения')
    L_cost_preparation.configure(text='усреднённая стоимость подготовки\nспециалиста-ремонтника\n' + str(
        type_V_frane_forming) + '-го типа ' + str(
        level_frane_forming) + '-го уровня подчинения')


def forming_next():
    global type_RP_frane_forming
    element_number_repair_tools = Enter_number_repair_tools.get()
    element_cost_repair_facilities = Enter_cost_repair_facilities.get()
    element_number_repairmen = Enter_number_repairmen.get()
    element_cost_preparation = Enter_cost_preparation.get()

    try:
        number_repair_tools.append(float(element_number_repair_tools))
        cost_repair_facilities.append(float(element_cost_repair_facilities))
        number_repairmen.append(float(element_number_repairmen))
        cost_preparation.append(float(element_cost_preparation))
    except ValueError:
        print('ошибка forming_next')
    type_RP_frane_forming += 1
    L_number_repair_tools.configure(text='количество средств ремонта' + str(
        type_RP_frane_forming) + '-го типа\nв РП ' + str(type_V_frane_forming) + '-го типа ' + str(
        level_frane_forming) + '-го уровня подчинения')
    L_cost_repair_facilities.configure(text='стоимость средств ремонта ' + str(
        type_RP_frane_forming) + '-го типа\nв РП ' + str(type_V_frane_forming) + '-го типа')
    L_number_repairmen.configure(text='количество ремонтников в РП ' + str(type_V_frane_forming) + '-го типа\n' + str(
        level_frane_forming) + '-го уровня подчинения')
    L_cost_preparation.configure(text='усреднённая стоимость подготовки\nспециалиста-ремонтника\n' + str(
        type_V_frane_forming) + '-го типа ' + str(
        level_frane_forming) + '-го уровня подчинения')


def moving_next():
    global application_moving
    global level_moving
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
    application_moving += 1
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
frame_B.place(relx=0, rely=0, relwidth=0.45, relheight=0.18)

frame_belt_work = tk.Frame(window, width=300, height=75, bg='yellow')
frame_belt_work.place(relx=0.45, rely=0, relwidth=0.55, relheight=0.18)

frame_moving = tk.Frame(window, width=225, height=150, bg='blue')
frame_moving.place(relx=0, rely=0.18, relwidth=0.5, relheight=0.8)

frame_forming = tk.Frame(window, width=225, height=150, bg='green')
frame_forming.place(relx=0.5, rely=0.18, relwidth=0.5, relheight=0.55)

frame_repair_evacuation = tk.Frame(window, width=225, height=150, bg='white')
frame_repair_evacuation.place(relx=0.5, rely=0.55, relwidth=0.5, relheight=0.8)

frame_consol = tk.Frame(window, width=450, height=100, bg='black')
frame_consol.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

## Фрейм B

L_B = tk.Label(frame_B, text='B_РП ' + str(level_V) + '-уровня ' + str(index_V) + '-го типа')
L_B.grid(row='0', column='0', sticky='w', padx=10, pady=5)

L_frame_B_B_enter = ttk.Entry(frame_B, justify=tk.RIGHT, width=16)
L_frame_B_B_enter.grid(row='0', column='1', sticky='e', padx=10, pady=5)

enter_frame_B = ttk.Button(frame_B, text='Ввести', command=entr_frame_B)  ## потом допишу ввод
enter_frame_B.grid(row='2', column='1', sticky='e', padx=10, pady=5)

# фрейм ремонта

L_frame_belt_work_T = tk.Label(frame_belt_work,
                               text='T_рем ' + str(level_repair_work) + '-уровня ' + str(index_repair_work) + ''
                                                                                                              '-го типа',
                               font=('Helvetica', 10))
L_frame_belt_work_T.grid(row='0', column='0', sticky='w', padx=10, pady=5)

L_frame_belt_work_C_repair = tk.Label(frame_belt_work,
                                      text='Средняя стоимость часа функционирования\nремонтного подразделения'
                                           ' ' + str(index_repair_work) + '-го типа', font=('Helvetica', 10))
L_frame_belt_work_C_repair.grid(row='1', column='0', sticky='e', padx=10, pady=5)

Entry_belt_work_T = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_T.grid(row='0', column='1', sticky='e', padx=0, pady=5)

Entry_belt_work_C_repair = ttk.Entry(frame_belt_work, justify=tk.RIGHT, width=16)
Entry_belt_work_C_repair.grid(row='1', column='1', sticky='e', padx=0, pady=5)

button_frame_belt_work = ttk.Button(frame_belt_work, text='Ввести', command=entr_frame_belt_work)
button_frame_belt_work.grid(row='2', column='1', sticky='e', padx=10, pady=5)

## стоимость транспортировки 2.5.4

##2.5.5 + 2.5.6

L_frame_moving_cost_kilometer = tk.Label(frame_moving, text='Стоимость 1 км перещения РПМТ\n' + str(
    level_moving) + '-го уровня по ' + str(application_moving) + '-й заявке', font=('Helvetica', 10), justify='left')
L_frame_moving_distance = tk.Label(frame_moving, text='Расстояние между РО ' + str(
    level_moving) + '-го уровня,\nпройденное РПМТ в ходе выполнения\nремонта в полевых условиях по\n' + str(
    application_moving) + '-й заявке', font=('Helvetica', 10), justify='left')
L_distance_transportation_km = ttk.Label(frame_moving, text='Расстояние между РО ' + str(
    level_moving) + '-го уровня,\nи местонахождением объекта ремонта\nпо ' + str(application_moving) + '-й заяке',
                                         font=('Helvetica', 10), justify='left')
L_cost_transportation_km = ttk.Label(frame_moving,
                                     text='Стоимость одного км транспортировки\nобразца средства АТО в РПСТ РО\n' + str(
                                         level_moving) + '-го уровня по ' + str(application_moving) + '-й заявке',
                                     font=('Helvetica', 10), justify='left')
L_number_transport = ttk.Label(frame_moving,
                               text='количество образцов средств АТО,\nнаправляемых для ремонта в РПСТ\nРО ' + str(
                                   level_moving) + '-го уровня по' + str(application_moving) + '-й заявке',
                               font=('Helvetica', 10), justify='left')

L_frame_moving_cost_kilometer.grid(row='0', column='0', sticky='w', padx=10, pady=3)
L_frame_moving_distance.grid(row='1', column='0', sticky='w', padx=10, pady=3)
L_distance_transportation_km.grid(row='2', column='0', sticky='w', padx=10, pady=3)
L_cost_transportation_km.grid(row='3', column='0', sticky='w', padx=10, pady=3)
L_number_transport.grid(row='4', column='0', sticky='w', padx=10, pady=3)

Entry_cost_kilometer = ttk.Entry(frame_moving, justify=tk.RIGHT, width=10)
Entry_cost_kilometer.grid(row='0', column='1', sticky='e', pady=3)

Entry_cost_distance = ttk.Entry(frame_moving, justify=tk.RIGHT, width=10)
Entry_cost_distance.grid(row='1', column='1', sticky='e', pady=3)

Entry_distance_transportation_km = ttk.Entry(frame_moving, justify=tk.RIGHT, width=10)
Entry_cost_transportation_km = ttk.Entry(frame_moving, justify=tk.RIGHT, width=10)
Entry_number_transport = ttk.Entry(frame_moving, justify=tk.RIGHT, width=10)

Entry_distance_transportation_km.grid(row='2', column='1', sticky='e', padx=10, pady=3)
Entry_cost_transportation_km.grid(row='3', column='1', sticky='e', padx=10, pady=3)
Entry_number_transport.grid(row='4', column='1', sticky='e', padx=10, pady=3)
button_frame_moving_enter = ttk.Button(frame_moving, text='Следующий уровень\n(ввести уровень)', command=entr_moving)
button_frame_moving_enter.grid(row='5', column='0', sticky='w', pady=3, padx=10)

button_frame_moving_next = ttk.Button(frame_moving, text='следующая заявка', command=moving_next)
button_frame_moving_next.grid(row='5', column='1', sticky='e', pady=3)

# 2.5.6
L_number_repair_tools = ttk.Label(frame_forming, text='количество средств ремонта' + str(
    type_RP_frane_forming) + '-го типа\nв РП ' + str(type_V_frane_forming) + '-го типа ' + str(
    level_frane_forming) + '-го уровня подчинения', font=('Helvetica', 10), justify='left')
L_cost_repair_facilities = ttk.Label(frame_forming, text='стоимость средств ремонта ' + str(
    type_RP_frane_forming) + '-го типа\nв РП ' + str(type_V_frane_forming) + '-го типа', font=('Helvetica', 10),
                                     justify='left')
L_number_repairmen = ttk.Label(frame_forming,
                               text='количество ремонтников в РП ' + str(type_V_frane_forming) + '-го типа\n' + str(
                                   level_frane_forming) + '-го уровня подчинения', font=('Helvetica', 10),
                               justify='left')
L_cost_preparation = ttk.Label(frame_forming, text='усреднённая стоимость подготовки\nспециалиста-ремонтника\n' + str(
    type_V_frane_forming) + '-го типа ' + str(level_frane_forming) + '-го уровня подчинения', font=('Helvetica', 10),
                               justify='left')

L_number_repair_tools.grid(row='0', column='0', sticky='w', padx=10, pady=3)
L_cost_repair_facilities.grid(row='1', column='0', sticky='w', padx=10, pady=3)
L_number_repairmen.grid(row='2', column='0', sticky='w', padx=10, pady=3)
L_cost_preparation.grid(row='3', column='0', sticky='w', padx=10, pady=3)

Enter_number_repair_tools = ttk.Entry(frame_forming, justify=tk.RIGHT, width=10)
Enter_cost_repair_facilities = ttk.Entry(frame_forming, justify=tk.RIGHT, width=10)
Enter_number_repairmen = ttk.Entry(frame_forming, justify=tk.RIGHT, width=10)
Enter_cost_preparation = ttk.Entry(frame_forming, justify=tk.RIGHT, width=10)

Enter_number_repair_tools.grid(row='0', column='1', sticky='w', padx=10, pady=3)
Enter_cost_repair_facilities.grid(row='1', column='1', sticky='w', padx=10, pady=3)
Enter_number_repairmen.grid(row='2', column='1', sticky='w', padx=10, pady=3)
Enter_cost_preparation.grid(row='3', column='1', sticky='w', padx=10, pady=3)

button_frame_forming_enter = ttk.Button(frame_forming, text='Ввести', command=forming_enter)
button_frame_forming_enter.grid(row='4', column='0', sticky='w', padx=10, pady=3)

button_frame_forming_next = ttk.Button(frame_forming, text='следующий вид\nремонта', command=forming_next)
button_frame_forming_next.grid(row='4', column='1', sticky='w', padx=10, pady=3)

L_submission = ttk.Label(frame_repair_evacuation, text='РП ' + str(type_repair_evacuation) + '-го типа')
L_number_repair_evacuation = ttk.Label(frame_repair_evacuation,
                                       text='Количество ремонтно-эвак\nсредств ' + str(tool) + '-го типа в РО\n' + str(
                                           level_repair_evacuation) + '-го уровня')
L_cost_repair_evacuation = ttk.Label(frame_repair_evacuation,
                                     text='Стоимость ремонтно-эвак\nсредств ' + str(tool) + '-го типа')

L_submission.grid(row='0', column='0', sticky='w', padx=10, pady=4)
L_number_repair_evacuation.grid(row='1', column='0', sticky='w', padx=10, pady=4)
L_cost_repair_evacuation.grid(row='2', column='0', sticky='w', padx=10, pady=4)

Enter_number_repair_evacuation = ttk.Entry(frame_repair_evacuation, justify=tk.RIGHT, width=10)
Enter_cost_repair_evacuation = ttk.Entry(frame_repair_evacuation, justify=tk.RIGHT, width=10)

Enter_number_repair_evacuation.grid(row='1', column='1', sticky='e', padx=10, pady=4)
Enter_cost_repair_evacuation.grid(row='2', column='1', sticky='e', padx=10, pady=4)

button_evacuation_enter = ttk.Button(frame_repair_evacuation, text='следующий уровень/тип', command=evacuation_enter)
button_evacuation_next = ttk.Button(frame_repair_evacuation, text='Следующий тип средств', command=evacuation_next)

button_evacuation_enter.grid(row='3', column='0', sticky='w', padx=10, pady=4)
button_evacuation_next.grid(row='3', column='1', sticky='e', padx=10, pady=4)

button_result = ttk.Button(frame_consol, text='результат', command=result_enter)
button_result.grid(row='0', column='0')

window.mainloop()