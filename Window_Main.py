import time
from tkinter import CENTER
from tkinter.constants import NW

import Window as window_calculation
import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('main')
        self['background'] = '#EBEBEB'
        self.conf = {'padx': (10, 30), 'pady': 10}
        self.bold_font = 'Helvetica 13 bold'
        self.put_frames()
        self.geometry('400x300')
        self.minsize(400, 300)
        self.maxsize(401,301)


    def put_frames(self):
        self.airplane = Frame_Airplane(self).place(relx=0, rely=0, relwidth=1, relheight=0.3)
        self.start = Frame_Start(self).place(relx=0, rely=0.3,relwidth=1,relheight=0.6)
        self.name_author = Frame_Auther(self).place(relx=0, rely=0.6, relwidth=1, relheight=1)
class Frame_Airplane(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()
        #self.drive()

    def put_widgets(self):
        self.L_airplane = tk.Label(text='\u2708', justify='center')
        self.L_airplane.grid(row='0', column='0', padx=200, pady=30)
        #self.canvas = tk.Canvas(self)
        #self.canvas.pack(anchor=CENTER, expand=1)
        #self.air = self.canvas.create_window(10,20,anchor=NW,window=self.L_airplane,width=10,height=10)
    #def drive(self):
        #self.canvas.move(self.air, 90, 0)
        #time.sleep(1)
        #self.L_airplane.place(x=10, y=10)
        #self.step()

    #def step(self):
     #   x_ = 10
     #   y_ = 10
     #   while x_ < self.winfo_screenwidth():
      #      pass

class Frame_Start(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()

    def put_widgets(self):
        self.entry = tk.Button(self,text = 'приступить к расчёту', command=self.start)
        self.entry.grid(row=1, column=1, padx=120, pady=30)
    def start(self):
        window_calculation.start()




class Frame_Auther(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self['background'] = self.master['background']
        self.put_widgets()
    def put_widgets(self):
        self.PAC_L = tk.Label(self, text = "Управления ПАК СУ")
        self.BBC = tk.Label(self,text='ВВС ЦНИИ ВВС')
        self.RF = tk.Label(self,text='Минообороны Росиии')
        self._raz = tk.Label(self, text='Разработчик: \nЛосунцов\nИван Александрович', justify='left')

        self.PAC_L.grid(row='0',column='0', sticky='w', padx=10)
        self.BBC.grid(row='1', column='0', sticky='w', padx=10)
        self.RF.grid(row='2', column='0', sticky='w', padx=10)
        self._raz.grid(row='1',column='2', sticky='e',padx=60, pady=1)

app = App()
#print(emoji.emojize('Python is :red_reart:'))
#print(emoji.emojize('Python is :airplane_departure:'))
#print(emoji.demojize('🛫'))
#print(emoji.replace_emoji(':airplane_departure:'))
app.mainloop()