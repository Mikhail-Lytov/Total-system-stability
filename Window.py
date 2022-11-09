import tkinter as tk
from tkinter import ttk, BOTH, END
import calculation


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("расчёт")
        self['background'] = '#EBEBEB'
        self.conf = {'padx': (10, 30), 'pady': 10}
        self.bold_font = 'Helvetica 13 bold'
        self.put_frames()
        self.geometry('860x640')
        self.minsize(300, 300)
    def refresh(self):
        all_frames = [f for f in self.children]
        for f_name in all_frames:
            if '!frameconsol' in f_name:
                self.nametowidget(f_name).destroy()
        #self.put_frames()
        self.frame_consol = FrameConsol(self).place(relx=0, rely=0.8, relwidth=1, relheight=0.2)
    def put_frames(self):
        # self.add_form_frame = AddForm(self).grid
        self.frameB = Frame_b(self).place(relx=0, rely=0, relwidth=0.45, relheight=0.18)

        self.frame_belt_work = FrameBeltWork(self).place(relx=0.45, rely=0, relwidth=0.55, relheight=0.18)

        self.frame_moving = FrameMoving(self).place(relx=0, rely=0.18, relwidth=0.5, relheight=0.8)

        self.frame_forming = FrameForming(self).place(relx=0.5, rely=0.18, relwidth=0.5, relheight=0.55)

        self.frame_repair_evacuation = FrameRepairEvacuation(self).place(relx=0.5, rely=0.55, relwidth=0.5,
                                                                         relheight=0.8)

        self.frame_consol = FrameConsol(self).place(relx=0, rely=0.8, relwidth=1, relheight=0.2)


class FrameConsol(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        #self.button_result = ttk.Button(self, text='результат', command=self.result_enter)
        #self.button_result.grid(row='0', column='0')
        columns = ['type', 'coll']
        # Тут будет таблица с данными из калькулятор с добавленными элементами из данной таблицы
        #блица будет обновляемая
        tree = ttk.Treeview(self, columns = columns, show='headings')

        #tree.grid(row='0', column='0')
        tree.heading('type', text='Тип', anchor='center')
        tree.heading('coll',text = 'Данные', anchor='center')
        tree.insert('', END,values=['hour_operation', calculation.hour_operation])
        tree.insert('', END, values=['B', calculation.B])
        tree.insert('', END, values=['T_work', calculation.T_work])
        tree.insert('', END, values=['number_repair_tools', calculation.number_repair_tools])
        tree.insert('', END, values=['cost_repair_tools', calculation.cost_repair_tools])
        tree.insert('', END, values=['number_repairmen', calculation.number_repairmen])
        tree.insert('', END, values=['cost_repairmen', calculation.cost_repairmen])
        tree.insert('', END, values=['number_repair_and_evacuation_facilities', calculation.number_repair_and_evacuation_facilities])
        tree.insert('', END, values=['cost_and_evacuation_facilities', calculation.cost_and_evacuation_facilities])
        tree.insert('', END, values=['cost_km_travel', calculation.cost_km_travel])
        tree.insert('', END, values=['distance_travel', calculation.distance_travel])
        tree.insert('', END, values=['cost_km_transpot', calculation.cost_km_transpot])
        tree.insert('', END, values=['distance_transportation', calculation.distance_transportation])
        tree.insert('', END, values=['number_samples_funds', calculation.number_samples_funds])
        scroll = ttk.Scrollbar(self, command=tree.yview)
        tree.configure(yscrollcommand=scroll.set)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(expand=tk.YES, fill=tk.BOTH)
    #def result_enter(self):
    #    result = calculation.calculation()
    #    self.L_result = ttk.Label(self, text=str(result))
    #   self.L_result.grid(row='1', column='0')
    #    print(result)


class FrameRepairEvacuation(tk.Frame):
    number_repair_evacuation = []
    cost_repair_evacuation = []

    number_repair_evacuation_v = []
    cost_repair_evacuation_v = []
    tool = 2
    level_repair_evacuation = 1
    type_repair_evacuation = 1

    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.L_submission = ttk.Label(self, text='РП ' + str(self.type_repair_evacuation) + '-го типа')
        self.L_number_repair_evacuation = ttk.Label(self,
                                                    text='Количество ремонтно-эвак\nсредств ' + str(
                                                        self.tool) + '-го типа в РО\n' + str(
                                                        self.level_repair_evacuation) + '-го уровня')
        self.L_cost_repair_evacuation = ttk.Label(self,
                                                  text='Стоимость ремонтно-эвак\nсредств ' + str(
                                                      self.tool) + '-го типа')

        self.L_submission.grid(row='0', column='0', sticky='w', padx=10, pady=4)
        self.L_number_repair_evacuation.grid(row='1', column='0', sticky='w', padx=10, pady=4)
        self.L_cost_repair_evacuation.grid(row='2', column='0', sticky='w', padx=10, pady=4)

        self.Enter_number_repair_evacuation = ttk.Entry(self, justify=tk.RIGHT, width=10)
        self.Enter_cost_repair_evacuation = ttk.Entry(self, justify=tk.RIGHT, width=10)

        self.Enter_number_repair_evacuation.grid(row='1', column='1', sticky='e', padx=10, pady=4)
        self.Enter_cost_repair_evacuation.grid(row='2', column='1', sticky='e', padx=10, pady=4)

        self.button_evacuation_enter = ttk.Button(self, text='следующий уровень/тип',
                                                  command=self.evacuation_enter)
        self.button_evacuation_next = ttk.Button(self, text='Следующий тип средств',
                                                 command=self.evacuation_next)

        self.button_evacuation_enter.grid(row='3', column='0', sticky='w', padx=10, pady=4)
        self.button_evacuation_next.grid(row='3', column='1', sticky='e', padx=10, pady=4)

    def evacuation_enter(self):
        element_number_repair_evacuation = self.Enter_number_repair_evacuation.get()
        element_cost_repair_evacuation = self.Enter_cost_repair_evacuation.get()
        try:
            self.number_repair_evacuation.append(float(element_number_repair_evacuation))
            self.cost_repair_evacuation.append(float(element_cost_repair_evacuation))
        except ValueError:
            print('error repair_evacuation_next')

        self.number_repair_evacuation_v.append(self.number_repair_evacuation)
        self.cost_repair_evacuation_v.append((self.cost_repair_evacuation))
        if self.type_repair_evacuation == 1:
            self.type_repair_evacuation = 2

        elif self.type_repair_evacuation == 2:
            self.type_repair_evacuation = 1
            self.level_repair_evacuation += 1
            calculation.add_number_repair_and_evacuation_facilities(self.number_repair_evacuation_v)
            calculation.add_cost_repair_and_evacuation_facilities(self.cost_repair_evacuation_v)
            self.number_repair_evacuation_v = []
            self.cost_repair_evacuation_v = []
        self.number_repair_evacuation = []
        self.cost_repair_evacuation = []
        self.tool = 2
        self.L_submission.configure(text='РП ' + str(self.type_repair_evacuation) + '-го типа')
        self.L_number_repair_evacuation.configure(
            text='Количество ремонтно-эвак\nсредств ' + str(self.tool) + '-го типа в РО\n' + str(
                self.level_repair_evacuation) + '-го уровня')
        self.L_cost_repair_evacuation.configure(text='Стоимость ремонтно-эвак\nсредств ' + str(self.tool) + '-го типа')
        self.master.refresh()

    def evacuation_next(self):

        element_number_repair_evacuation = self.Enter_number_repair_evacuation.get()
        element_cost_repair_evacuation = self.Enter_cost_repair_evacuation.get()
        try:
            self.number_repair_evacuation.append(float(element_number_repair_evacuation))
            self.cost_repair_evacuation.append(float(element_cost_repair_evacuation))
        except ValueError:
            print('error repair_evacuation_next')

        self.tool += 1
        self.L_number_repair_evacuation.configure(
            text='Количество ремонтно-эвак\nсредств ' + str(self.tool) + '-го типа в РО\n' + str(
                self.level_repair_evacuation) + '-го уровня')
        self.L_cost_repair_evacuation.configure(text='Стоимость ремонтно-эвак\nсредств ' + str(self.tool) + '-го типа')


class FrameForming(tk.Frame):
    number_repair_tools_v = []
    cost_repair_facilities_v = []
    number_repairmen_v = []
    cost_preparation_v = []

    number_repair_tools = []
    cost_repair_facilities = []
    number_repairmen = []
    cost_preparation = []

    type_RP_frane_forming = 1
    type_V_frane_forming = 1
    level_frane_forming = 1

    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.L_number_repair_tools = ttk.Label(self, text='количество средств ремонта' + str(
            self.type_RP_frane_forming) + '-го типа\nв РП ' + str(self.type_V_frane_forming) + '-го типа ' + str(
            self.level_frane_forming) + '-го уровня подчинения', font=('Helvetica', 10), justify='left')
        self.L_cost_repair_facilities = ttk.Label(self, text='стоимость средств ремонта ' + str(
            self.type_RP_frane_forming) + '-го типа\nв РП ' + str(self.type_V_frane_forming) + '-го типа',
                                                  font=('Helvetica', 10),
                                                  justify='left')
        self.L_number_repairmen = ttk.Label(self,
                                            text='количество ремонтников в РП ' + str(
                                                self.type_V_frane_forming) + '-го типа\n' + str(
                                                self.level_frane_forming) + '-го уровня подчинения',
                                            font=('Helvetica', 10),
                                            justify='left')
        self.L_cost_preparation = ttk.Label(self,
                                            text='усреднённая стоимость подготовки\nспециалиста-ремонтника\n' + str(
                                                self.type_V_frane_forming) + '-го типа ' + str(
                                                self.level_frane_forming) + '-го уровня подчинения',
                                            font=('Helvetica', 10),
                                            justify='left')

        self.L_number_repair_tools.grid(row='0', column='0', sticky='w', padx=10, pady=3)
        self.L_cost_repair_facilities.grid(row='1', column='0', sticky='w', padx=10, pady=3)
        self.L_number_repairmen.grid(row='2', column='0', sticky='w', padx=10, pady=3)
        self.L_cost_preparation.grid(row='3', column='0', sticky='w', padx=10, pady=3)

        self.Enter_number_repair_tools = ttk.Entry(self, justify=tk.RIGHT, width=10)
        self.Enter_cost_repair_facilities = ttk.Entry(self, justify=tk.RIGHT, width=10)
        self.Enter_number_repairmen = ttk.Entry(self, justify=tk.RIGHT, width=10)
        self.Enter_cost_preparation = ttk.Entry(self, justify=tk.RIGHT, width=10)

        self.Enter_number_repair_tools.grid(row='0', column='1', sticky='w', padx=10, pady=3)
        self.Enter_cost_repair_facilities.grid(row='1', column='1', sticky='w', padx=10, pady=3)
        self.Enter_number_repairmen.grid(row='2', column='1', sticky='w', padx=10, pady=3)
        self.Enter_cost_preparation.grid(row='3', column='1', sticky='w', padx=10, pady=3)

        self.button_frame_forming_enter = ttk.Button(self, text='Ввести', command=self.forming_enter)
        self.button_frame_forming_enter.grid(row='4', column='0', sticky='w', padx=10, pady=3)

        self.button_frame_forming_next = ttk.Button(self, text='следующий вид\nремонта', command=self.forming_next)
        self.button_frame_forming_next.grid(row='4', column='1', sticky='w', padx=10, pady=3)

    def forming_next(self):
        element_number_repair_tools = self.Enter_number_repair_tools.get()
        element_cost_repair_facilities = self.Enter_cost_repair_facilities.get()
        element_number_repairmen = self.Enter_number_repairmen.get()
        element_cost_preparation = self.Enter_cost_preparation.get()

        try:
            self.number_repair_tools.append(float(element_number_repair_tools))
            self.cost_repair_facilities.append(float(element_cost_repair_facilities))
            self.number_repairmen.append(float(element_number_repairmen))
            self.cost_preparation.append(float(element_cost_preparation))
        except ValueError:
            print('ошибка forming_next')
        self.type_RP_frane_forming += 1
        self.L_number_repair_tools.configure(text='количество средств ремонта' + str(
            self.type_RP_frane_forming) + '-го типа\nв РП ' + str(self.type_V_frane_forming) + '-го типа ' + str(
            self.level_frane_forming) + '-го уровня подчинения')
        self.L_cost_repair_facilities.configure(text='стоимость средств ремонта ' + str(
            self.type_RP_frane_forming) + '-го типа\nв РП ' + str(self.type_V_frane_forming) + '-го типа')
        self.L_number_repairmen.configure(
            text='количество ремонтников в РП ' + str(self.type_V_frane_forming) + '-го типа\n' + str(
                self.level_frane_forming) + '-го уровня подчинения')
        self.L_cost_preparation.configure(text='усреднённая стоимость подготовки\nспециалиста-ремонтника\n' + str(
            self.type_V_frane_forming) + '-го типа ' + str(
            self.level_frane_forming) + '-го уровня подчинения')

    def forming_enter(self):
        element_number_repair_tools = self.Enter_number_repair_tools.get()
        element_cost_repair_facilities = self.Enter_cost_repair_facilities.get()
        element_number_repairmen = self.Enter_number_repairmen.get()
        element_cost_preparation = self.Enter_cost_preparation.get()
        try:
            self.number_repair_tools.append(float(element_number_repair_tools))
            self.cost_repair_facilities.append(float(element_cost_repair_facilities))
            self.number_repairmen.append(float(element_number_repairmen))
            self.cost_preparation.append(float(element_cost_preparation))
            self.number_repairmen_v.append(self.number_repairmen)
            self.cost_repair_facilities_v.append(self.cost_repair_facilities)
            self.number_repair_tools_v.append(self.number_repair_tools)
            self.cost_preparation_v.append(self.cost_preparation)
        except ValueError:
            print('ошибка forming_enter')
        if self.type_V_frane_forming == 1:
            self.type_V_frane_forming = 2
        elif self.type_V_frane_forming == 2:
            self.type_V_frane_forming = 1
            self.level_frane_forming += 1
            print(self.number_repair_tools_v)
            calculation.add_number_repair_tools(self.number_repair_tools_v)
            calculation.add_cost_repair_tools(self.cost_repair_facilities_v)
            calculation.add_number_repairmen(self.number_repairmen_v)
            calculation.add_cost_repairmen(self.cost_preparation_v)
            self.number_repair_tools_v = []
            self.cost_repair_facilities_v = []
            self.number_repairmen_v = []
            self.cost_preparation_v = []
        self.number_repair_tools = []
        self.cost_repair_facilities = []
        self.number_repairmen = []
        self.cost_preparation = []

        self.type_RP_frane_forming = 1
        self.L_number_repair_tools.configure(text='количество средств ремонта' + str(
            self.type_RP_frane_forming) + '-го типа\nв РП ' + str(self.type_V_frane_forming) + '-го типа ' + str(
            self.level_frane_forming) + '-го уровня подчинения')
        self.L_cost_repair_facilities.configure(text='стоимость средств ремонта ' + str(
            self.type_RP_frane_forming) + '-го типа\nв РП ' + str(self.type_V_frane_forming) + '-го типа')
        self.L_number_repairmen.configure(
            text='количество ремонтников в РП ' + str(self.type_V_frane_forming) + '-го типа\n' + str(
                self.level_frane_forming) + '-го уровня подчинения')
        self.L_cost_preparation.configure(text='усреднённая стоимость подготовки\nспециалиста-ремонтника\n' + str(
            self.type_V_frane_forming) + '-го типа ' + str(
            self.level_frane_forming) + '-го уровня подчинения')
        self.master.refresh()


class FrameMoving(tk.Frame):
    application_moving = 1
    level_moving = 1
    cost_kilometer = []
    distance_transport = []
    distance_transportation_km = []
    cost_transportation_km = []
    number_transport = []

    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.L_frame_moving_cost_kilometer = tk.Label(self, text='Стоимость 1 км перещения РПМТ\n' + str(
            self.level_moving) + '-го уровня по ' + str(self.application_moving) + '-й заявке', font=('Helvetica', 10),
                                                      justify='left')
        self.L_frame_moving_distance = tk.Label(self, text='Расстояние между РО ' + str(
            self.level_moving) + '-го уровня,\nпройденное РПМТ в ходе выполнения\nремонта в полевых условиях по\n' + str
            (self.application_moving) + '-й заявке', font=('Helvetica', 10), justify='left')
        self.L_distance_transportation_km = ttk.Label(self, text='Расстояние между РО ' + str(
            self.level_moving) + '-го уровня,\nи местонахождением объекта ремонта\nпо ' + str(
            self.application_moving) + '-й заяке',
                                                      font=('Helvetica', 10), justify='left')
        self.L_cost_transportation_km = ttk.Label(self,
                                                  text='Стоимость одного км транспортировки\nобразца средства АТО в '
                                                       'РПСТ РО\n' + str(
                                                      self.level_moving) + '-го уровня по ' + str(
                                                      self.application_moving) + '-й заявке',
                                                  font=('Helvetica', 10), justify='left')
        self.L_number_transport = ttk.Label(self,
                                            text='количество образцов средств АТО,\nнаправляемых для ремонта в '
                                                 'РПСТ\nРО ' + str(
                                                self.level_moving) + '-го уровня по' + str(
                                                self.application_moving) + '-й заявке',
                                            font=('Helvetica', 10), justify='left')

        self.L_frame_moving_cost_kilometer.grid(row='0', column='0', sticky='w', padx=10, pady=3)
        self.L_frame_moving_distance.grid(row='1', column='0', sticky='w', padx=10, pady=3)
        self.L_distance_transportation_km.grid(row='2', column='0', sticky='w', padx=10, pady=3)
        self.L_cost_transportation_km.grid(row='3', column='0', sticky='w', padx=10, pady=3)
        self.L_number_transport.grid(row='4', column='0', sticky='w', padx=10, pady=3)

        self.Entry_cost_kilometer = ttk.Entry(self, justify=tk.RIGHT, width=10)
        self.Entry_cost_kilometer.grid(row='0', column='1', sticky='e', pady=3)

        self.Entry_cost_distance = ttk.Entry(self, justify=tk.RIGHT, width=10)
        self.Entry_cost_distance.grid(row='1', column='1', sticky='e', pady=3)

        self.Entry_distance_transportation_km = ttk.Entry(self, justify=tk.RIGHT, width=10)
        self.Entry_cost_transportation_km = ttk.Entry(self, justify=tk.RIGHT, width=10)
        self.Entry_number_transport = ttk.Entry(self, justify=tk.RIGHT, width=10)

        self.Entry_distance_transportation_km.grid(row='2', column='1', sticky='e', padx=10, pady=3)
        self.Entry_cost_transportation_km.grid(row='3', column='1', sticky='e', padx=10, pady=3)
        self.Entry_number_transport.grid(row='4', column='1', sticky='e', padx=10, pady=3)
        self.button_frame_moving_enter = ttk.Button(self, text='Следующий уровень\n(ввести уровень)',
                                                    command=self.entr_moving)
        self.button_frame_moving_enter.grid(row='5', column='0', sticky='w', pady=3, padx=10)

        self.button_frame_moving_next = ttk.Button(self, text='следующая заявка', command=self.moving_next)
        self.button_frame_moving_next.grid(row='5', column='1', sticky='e', pady=3)

        self.button_result = ttk.Button(self, text='посчитать результат', command=self.result_enter)
        self.button_result.grid(row='6', column='0', padx=30, pady=20)

    def result_enter(self):
        self.result = calculation.calculation()
        self.L_result = ttk.Label(self, text=str(self.result))
        self.L_result.grid(row='7', column='0')
        print(self.result)
        result_class = Popup(self, self.result)

    def moving_next(self):
        element_cost_kilometer = self.Entry_cost_kilometer.get()
        element_distance = self.Entry_cost_distance.get()
        element_distance_transportation_km = self.Entry_distance_transportation_km.get()
        element_cost_transportation_km = self.Entry_cost_transportation_km.get()
        element_number_transport = self.Entry_number_transport.get()
        try:
            self.cost_kilometer.append(float(element_cost_kilometer))
            self.distance_transport.append((float(element_distance)))
            self.distance_transportation_km.append(float(element_distance_transportation_km))
            self.cost_transportation_km.append(float(element_cost_transportation_km))
            self.number_transport.append((float(element_number_transport)))
        except ValueError:
            print('Ошибка ввода в moving next')
        self.application_moving += 1
        self.L_frame_moving_cost_kilometer.configure(
            text='Стоимость 1 км перещения РПМТ\n' + str(self.level_moving) + '-го уровня по ' + str(
                self.application_moving) + '-й заявке')
        self.L_frame_moving_distance.configure(
            text='Расстояние между РО\n' + str(self.level_moving) + '-го уровня по ' + str(
                self.application_moving) + '-й заявке')
        self.L_distance_transportation_km.configure(
            text='Расстояние между РО ' + str(
                self.level_moving) + '-го уровня,\nи местонахождением объекта ремонта\nпо ' + str(
                self.application_moving) + '-й заяке', font=('Helvetica', 10), justify='left')
        self.L_cost_transportation_km.configure(
            text='Стоимость одного км транспортировки\nобразца средства АТО в РПСТ РО\n' + str(
                self.level_moving) + '-го уровня по ' + str(self.application_moving) + '-й заявке',
            font=('Helvetica', 10),
            justify='left')
        self.L_number_transport.configure(
            text='количество образцов средств АТО,\nнаправляемых для ремонта в РПСТ\nРО ' + str(
                self.level_moving) + '-го уровня по ' + str(self.application_moving) + '-й заявке',
            font=('Helvetica', 10),
            justify='left')

    def entr_moving(self):
        element_cost_kilometer = self.Entry_cost_kilometer.get()
        element_distance = self.Entry_cost_distance.get()
        element_distance_transportation_km = self.Entry_distance_transportation_km.get()
        element_cost_transportation_km = self.Entry_cost_transportation_km.get()
        element_number_transport = self.Entry_number_transport.get()
        try:
            self.cost_kilometer.append(float(element_cost_kilometer))
            self.distance_transport.append((float(element_distance)))
            self.distance_transportation_km.append(float(element_distance_transportation_km))
            self.cost_transportation_km.append(float(element_cost_transportation_km))
            self.number_transport.append((float(element_number_transport)))
        except ValueError:
            print('Ошибка ввода в moving next')

        calculation.add_km_travel(self.cost_kilometer)
        calculation.add_distance(self.distance_transport)
        calculation.add_distance_transportation(self.distance_transportation_km)
        calculation.add_cost_km_transpot(self.cost_transportation_km)
        calculation.add_number_samples_funds(self.number_transport)
        self.level_moving += 1

        self.L_frame_moving_cost_kilometer.configure(
            text='Стоимость 1 км перещения РПМТ\n' + str(self.level_moving) + '-го уровня по ' + str(
                self.application_moving) + '-й заявке')
        self.L_frame_moving_distance.configure(
            text='Расстояние между РО\n' + str(self.level_moving) + '-го уровня по ' + str(
                self.application_moving) + '-й заявке')
        self.L_distance_transportation_km.configure(
            text='Расстояние между РО ' + str(
                self.level_moving) + '-го уровня,\nи местонахождением объекта ремонта\nпо ' + str(
                self.application_moving) + '-й заяке', font=('Helvetica', 10), justify='left')
        self.L_cost_transportation_km.configure(
            text='Стоимость одного км транспортировки\nобразца средства АТО в РПСТ РО\n' + str(
                self.level_moving) + '-го уровня по ' + str(self.application_moving) + '-й заявке',
            font=('Helvetica', 10),
            justify='left')
        self.L_number_transport.configure(
            text='количество образцов средств АТО,\nнаправляемых для ремонта в РПСТ\nРО ' + str(
                self.level_moving) + '-го уровня по ' + str(self.application_moving) + '-й заявке',
            font=('Helvetica', 10),
            justify='left')
        self.cost_kilometer = []
        self.distance_transport = []
        self.distance_transportation_km = []
        self.cost_transportation_km = []
        self.number_transport = []
        self.master.refresh()


class FrameBeltWork(tk.Frame):
    index_repair_work = 1
    level_repair_work = 1
    T_work = []
    C_work_repair = []

    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.L_frame_belt_work_T = tk.Label(self,
                                            text='T_рем ' + str(self.level_repair_work) + '-уровня ' + str(
                                                self.index_repair_work) + ''
                                                                          '-го типа',
                                            font=('Helvetica', 10))
        self.L_frame_belt_work_T.grid(row='0', column='0', sticky='w', padx=10, pady=5)

        self.L_frame_belt_work_C_repair = tk.Label(self,
                                                   text='Средняя стоимость часа функционирования\nремонтного '
                                                        'подразделения '
                                                        ' ' + str(self.index_repair_work) + '-го типа',
                                                   font=('Helvetica', 10))
        self.L_frame_belt_work_C_repair.grid(row='1', column='0', sticky='e', padx=10, pady=5)

        self.Entry_belt_work_T = ttk.Entry(self, justify=tk.RIGHT, width=16)
        self.Entry_belt_work_T.grid(row='0', column='1', sticky='e', padx=0, pady=5)

        self.Entry_belt_work_C_repair = ttk.Entry(self, justify=tk.RIGHT, width=16)
        self.Entry_belt_work_C_repair.grid(row='1', column='1', sticky='e', padx=0, pady=5)

        self.button_frame_belt_work = ttk.Button(self, text='Ввести', command=self.entr_frame_belt_work)
        self.button_frame_belt_work.grid(row='2', column='1', sticky='e', padx=10, pady=5)

    def entr_frame_belt_work(self):

        element_T_work = self.Entry_belt_work_T.get()
        element_C_repair = self.Entry_belt_work_C_repair.get()
        if self.index_repair_work == 1:
            print(self.T_work)
            try:
                self.T_work.append(float(element_T_work))
                self.C_work_repair.append(float(element_C_repair))
            except ValueError:
                print('entr_frame_belt_work')
            self.index_repair_work = 2
        elif self.index_repair_work == 2:
            try:
                self.T_work.append(float(element_T_work))
                self.C_work_repair.append(float(element_C_repair))
            except ValueError:
                print('entr_frame_belt_work')
            calculation.add_T_work(self.T_work)
            calculation.add_hour_operation(self.C_work_repair)
            self.index_repair_work = 1
            self.level_repair_work += 1
            self.T_work = []
            self.C_work_repair = []
        self.L_frame_belt_work_C_repair.configure(
            text='Средняя стоимость часа функционирования\nремонтного подразделения'
                 ' ' + str(self.index_repair_work) + '-го типа')
        self.L_frame_belt_work_T.configure(
            text='T_рем ' + str(self.level_repair_work) + '-уровня ' + str(self.index_repair_work) + ''
                                                                                                             '-го типа')
        self.master.refresh()

class Frame_b(tk.Frame):
    B = []
    level_V = 1
    index_V = 1

    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.L_B = tk.Label(self, text='B_РП ' + str(self.level_V) + '-уровня ' + str(self.index_V) + '-го типа')
        self.L_B.grid(row='0', column='0', sticky='w', cnf=self.master.conf)

        self.L_frame_B_B_enter = ttk.Entry(self, justify=tk.RIGHT, width=16, validate='key', validatecommand=(self.register(self.validate_comand), '%P'))
        self.L_frame_B_B_enter.grid(row='0', column='1', sticky='e', cnf=self.master.conf)

        self.enter_frame_B = ttk.Button(self, text='Ввести', command=self.entr_frame_B)  ## потом допишу ввод
        self.enter_frame_B.grid(row='2', column='1', sticky='e', cnf=self.master.conf)

    def validate_comand(self, input):
        try:
            x = float(input)
            return True
        except ValueError:
            return False
    def entr_frame_B(self):
        result = self.L_frame_B_B_enter.get()
        if self.index_V == 1:
            try:
                self.B.append(float(result))
            except ValueError:
                print("error")  # ошибка
            self.index_V = 2
        elif self.index_V == 2:
            try:
                self.B.append(float(result))
            except ValueError:
                print("error")  # ошибка
            calculation.add_B_RP(self.B)
            self.B = []
            self.index_V = 1
            self.level_V += 1
        self.L_B.configure(text='B ' + str(self.level_V) + '-уровня ' + str(self.index_V) + '-го типа')
        self.master.refresh()

class Popup:
    def __init__(self, master, result):
        self.master = master
        pop = tk.Toplevel(master)
        lb = tk.Label(pop, text=result, font='100')
        lb.pack(pady=50,padx=50, expand=True)

def start():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    start()
