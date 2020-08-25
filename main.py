from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk,Image
from time_canteen import *


LARGE_FONT= ("Verdana", 12)


# time_now = time_canteen()
# time_defined = time_canteen()
list_time=[2019,11,2,22,00,59]
timeCanteen = time_canteen()
# time_fixed = time_canteen()
mode=1
store_displaying = "Macdonalds"
# change time intruction
# mode0: fix_time mode
# mode1: demo mode
#mode2: now mode


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.geometry("400x700")

        self.container.pack(side="top", fill="both", expand = True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, TodayPage, DrinksPage, CalcWaitTimePage, \
                  inputTimePage,OpHoursPage, MalayPage, EconRicePage, \
                  MacsPage, WesternPage):

            frame = F(self.container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        background_image = Image.open("ns.png").resize((1054, 700), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label1 = tk.Label(self, text="Welcome to North Spine Food Court System",\
                         font=LARGE_FONT, background='yellow')
        label1.pack()

        label2 = tk.Label(self, font=LARGE_FONT, background='yellow')
        label2.pack()

        def calling_input(mode_input):
            # frame = inputTimePage(parent,controller,mode=mode)
            # frame.grid(row=0, column=0, sticky="nsew")
            global mode
            mode = mode_input
            if mode<2:
                controller.show_frame(inputTimePage)
            else:
                controller.show_frame(TodayPage)

        button = tk.Button(self, text="View Today's Stalls",
                           command=lambda: calling_input(2))
        button.pack()

        button_fix_input = tk.Button(self, text="View Stalls by other Dates",
                                     command=lambda: calling_input(0))
        button_fix_input.pack()

        button_time = tk.Button(self, text="Special Case Demo",
                                command=lambda: calling_input(1))
        button_time.pack()

        button_op = tk.Button(self, text="Operating hours", command=lambda: controller.show_frame(OpHoursPage))
        button_op.pack()

        button3 = tk.Button(self, text="Exit",
                           command=self.on_cancel)
        button3.pack()

        def current_datetime():
            now = datetime.now()#changed datetime to ""
            label2.configure(text = "Current date and time : " + now.strftime("%d/%m/%Y %H:%M:%S"))
            label2.after(200, current_datetime)
        current_datetime()

    def on_cancel(self):
        quit()


class inputTimePage(tk.Frame):
    def __init__(self, parent, controller):
        # parent here is the container above while controller is the seaof... class
        tk.Frame.__init__(self, parent)
        list_str = ["year","month","day","hour","min","sec"]
        #create the labels
        x=0
        for v in list_str:
            v = tk.Label(self,text = v)
            v.grid(row=x,column=0)
            x +=1
        print(list_str)
        #create the buttons
        x=0
        list_entry=[]
        for v in list_str:
            list_entry.append(tk.Entry(self,text=v))
            list_entry[-1].grid(row=x,column=1)
            x+=1

        def check_input_time():
            try:
                list_time_input = list()
                for entry in list_entry:
                    t = int(entry.get())
                    list_time_input.append(t)
                print(list_time_input)
                year, month, day, hour, min, sec = list_time_input
                datetime(year=year, month=month, day=day, hour=hour, minute=min, second=sec)
                global list_time
                list_time = list_time_input
                # give faults when invalid date is given
                if(mode==1):
                    timeCanteen.input_time(year,month,day,hour,min,sec,NOW=0)
                    controller.show_frame(TodayPage)
                else:
                    timeCanteen.input_time(year,month,day,hour,min,sec,NOW=0)
                    controller.show_frame(TodayPage)
            except:
                # for entry in list_entry:
                #     entry.delete(0,tk.END)
                pass

        button_submit = tk.Button(self, text="Submit", command=check_input_time)
        button_submit.grid(row=6,column = 0)

        button_exit = tk.Button(self, text = "exit",command = lambda: controller.show_frame(StartPage))
        button_exit.grid(row =6, column = 1)



class TodayPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        background_image = Image.open("ns.png").resize((1054,700), Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)


        #background_image =Image.open("Drinks.jpeg").resize((791,700),Image.ANTIALIAS)
        # background_image = ImageTk.PhotoImage(background_image)
        # background_label = tk.Label(self, image=background_image)
        # background_label.photo = background_image
        # background_label.place(x=0, y=0, relwidth=1, relheight=1)




        #getting the photos
        list_photo = ["Malay.jpg","rice.jpg","Macs.jpg","drinks.jpg","western.jpg"]
        list_stall_name = ["Malay stall","Economical rice","Macdonalds","Drinks stall","Western food"]
        list_button ={}
        Pages=(MalayPage, EconRicePage, MacsPage, DrinksPage, WesternPage)


        for num in range(5):
            list_photo[num] = ImageTk.PhotoImage(Image.open(list_photo[num]))


        # list_photo[num] = ImageTk.PhotoImage(Image.open(list_photo[num]))
        list_button[list_stall_name[0]] = tk.Button(self,text=list_stall_name[0],font=LARGE_FONT,
                                         image=list_photo[0],height=100,width=200,
                                         command = lambda:controller.show_frame(MalayPage))
        list_button[list_stall_name[1]] = tk.Button(self, text=list_stall_name[1], font=LARGE_FONT,
                                                      image=list_photo[1],height=100,width=200,
                                                      command=lambda: controller.show_frame(EconRicePage))
        list_button[list_stall_name[2]] = tk.Button(self, text=list_stall_name[2], font=LARGE_FONT,
                                                      image=list_photo[2],height=100,width=200,
                                                      command=lambda: controller.show_frame(MacsPage))
        list_button[list_stall_name[3]] = tk.Button(self, text=list_stall_name[3], font=LARGE_FONT,
                                                      image=list_photo[3],height=100,width=200,
                                                      command=lambda: controller.show_frame(DrinksPage))
        list_button[list_stall_name[4]] = tk.Button(self, text=list_stall_name[4], font=LARGE_FONT,
                                                      image=list_photo[4],height=100,width=200,
                                                      command=lambda: controller.show_frame(WesternPage))

        label2 = tk.Label(self, font=LARGE_FONT, background='yellow')

        for num in range(5):
            # list_photo[num] = ImageTk.PhotoImage(Image.open(list_photo[num]))
            # list_button[list_stall_name[num]] = tk.Button(self,text=list_stall_name[num],font=LARGE_FONT,
            #                              #image=list_photo[num],#height=100,width=100,
            #                              command = lambda:controller.show_frame(Pages[num]))
            # print(list_stall_name[num])
            # print(Pages[num])
            list_button[list_stall_name[num]].photo = list_photo[num]
        print(list_button)

        #here we set the defalut for the time
        timeCanteen.input_time(NOW=1)
        def refresh():
            # get the stall that is open
            # here we need to consider the mode
            list_stall=list()
            if mode==0:
                print("mode: 0")
                global list_time
                year,month,day,hour,min,sec=list_time
                #list_stall = timeCanteen.get_stall(year,month,day,hour,min,sec,NOW=0)
                list_stall = timeCanteen.get_stall(year,month,day,hour,min,sec,NOW=0)
            if mode==1:
                print("mode: 1")
                list_stall = timeCanteen.get_stall(NOW=0)
            if mode==2:
                print("mode: 2")
                list_stall = timeCanteen.get_stall(NOW=1)
            print(list_stall)
            list_stall_open = []
            #setting the size of buttons and others
            x_pixel = 300
            y_pixel = 100
            gap = 5
            y = 0

            #mordrating the buttons and place them on
            # for button_stall in list_button.values():
                # button_stall.configure(height=y_pixel, width=x_pixel)
            for value in list_button.values():
                value.place(x=50, y=y + 50)
                y += y_pixel + gap

            #delete buttons that is close
            #do this after placing process can avoid flashing of the buttons
            list_stall_close = ["Malay stall","Economical rice","Macdonalds","Drinks stall","Western food"]
            for stall in list_stall:
                list_stall_close.remove(stall)
            for stall in list_stall_close:
                list_button[stall].place_forget()

            #placing the label that shows the time

            label2.pack()
            year,month,day,hour,min,sec = timeCanteen.get_time()
            label2.configure(text="Current date and time : " +datetime(year,month,day,hour,min,sec).strftime("%d/%m/%Y %H:%M:%S"))
            label2.after(1000, refresh)
        refresh()

        #button for you to go back home
        button2 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.place(x=150,y=600)



class DrinksPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Drinks Stall", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        background_image =Image.open("Drinks.jpeg").resize((791,700),Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def drinksinfo():
            tk.messagebox.showinfo("Drinks Stall", \
                                   "Escape the heat! Get your local favourite drinks like ice milo and teh ping or grab a quick bite like kaya toast.")

        button1 = tk.Button(self,text='Show Stall Info',command=drinksinfo)
        button1.pack()

        button2 = tk.Button(self, text="Get Waiting Time",
                            command=lambda: controller.show_frame(CalcWaitTimePage))
        button2.pack()


        button3 = tk.Button(self, text="View Stall Menu",
                            command=lambda: menu("Drinks stall"))
        button3.pack()

        button4 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button4.pack()


class MalayPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Malay Stall", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        background_image =Image.open("Malay.jpeg").resize((791,700),Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def malayinfo():
            tk.messagebox.showinfo("Malay Stall", \
                                   "Halal and Sedap! Our stall features classic halal dishes like nasi lemak and prata.")

        button1 = tk.Button(self,text='Show Stall Info',command=malayinfo)
        button1.pack()
        
        button2 = tk.Button(self, text="Get Waiting Time",
                            command=lambda: controller.show_frame(CalcWaitTimePage))
        button2.pack()



        button3 = tk.Button(self, text="View Stall Menu",
                            command=lambda: menu("Malay stall"))
        button3.pack()

        button4 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button4.pack()


class EconRicePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Economical Rice", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        background_image =Image.open("Rice.jpeg").resize((791,700),Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def econriceinfo():
            tk.messagebox.showinfo("Economical Rice Stall", \
                                   "Cheap but Tasty! Choose from a variety of affordable and delicious dishes like sweet and sour pork and steamed egg.")

        button1 = tk.Button(self,text='Show Stall Info',command=econriceinfo)
        button1.pack()
        
        button2 = tk.Button(self, text="Get Waiting Time",
                            command=lambda: controller.show_frame(CalcWaitTimePage))
        button2.pack()



        button3 = tk.Button(self, text="View Stall Menu",
                            command=lambda: menu("Economical rice"))
        button3.pack()

        button4 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button4.pack()


class MacsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Macdonalds", font=LARGE_FONT)
        label.pack(pady=10,padx=10)



        background_image =Image.open("Macs.jpeg").resize((791,700),Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        def macsinfo():
            tk.messagebox.showinfo("Macdonalds", \
                                   "Fast Comfort Food! The iconic fast food restaurant features well-loved classics such as Fillet-O-Fish and McFlurry.")

        button1 = tk.Button(self,text='Show Stall Info',command=macsinfo)
        button1.pack()
        button2 = tk.Button(self, text="Get Waiting Time",
                            command=lambda: controller.show_frame(CalcWaitTimePage))
        button2.pack()

        button3 = tk.Button(self, text="View Stall Menu",
                            command=lambda: menu("Macdonalds"))
        button3.pack()

        button4 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button4.pack()


class WesternPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Western food", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        background_image =Image.open("Western.jpeg").resize((791,700),Image.ANTIALIAS)
        background_image = ImageTk.PhotoImage(background_image)
        background_label = tk.Label(self, image=background_image)
        background_label.photo = background_image
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        def westerninfo():
            tk.messagebox.showinfo("Western Stall", \
                                   "Worth your money! Although slightly more expensive, this stall features hot and delicious food such as chicken chop and fish n chips.")

        button1 = tk.Button(self,text='Show Stall Info',command=westerninfo)
        button1.pack()

        button2 = tk.Button(self, text="Get Waiting Time",
                            command=lambda: controller.show_frame(CalcWaitTimePage))
        button2.pack()



        button3 = tk.Button(self, text="View Stall Menu",
                            command=lambda: menu("Western food"))
        button3.pack()

        button4 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button4.pack()


def menu(str):
    global store_displaying
    store_displaying = str
    print(store_displaying)
    stall=list()
    if mode==0:
        global list_name
        year,month,day,hour,min,sec = list_time
        stall = timeCanteen.get_stall(year,month,day,hour,min,sec,NOW=0)
    if mode==1:
        stall = timeCanteen.get_stall(NOW=0)
    if mode==2:
        stall = timeCanteen.get_stall(NOW=1)
    if str in stall:
        menu = MenuPage(app.container, app)
        menu.grid(row=0, column=0, sticky="nsew")
        menu.tkraise()
    else:
        app.show_frame(TodayPage)



class MenuPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(background='powder blue')
        label1 = tk.Label(self, text="Menu", font='Hekvetica 25 bold', background='yellow')
        label1.pack()
        global store_displaying

        dict_menu = {}
        if mode==0:
            global list_time
            year,month,day,hour,min,sec = list_time
            dict_menu = timeCanteen.get_menu(stall=store_displaying,year=year,month=month,day=day,hour=hour,min=min,NOW=0)
        if mode==1:
            dict_menu = timeCanteen.get_menu(store_displaying,NOW=0)
        if mode ==2:
            dict_menu = timeCanteen.get_menu(store_displaying,NOW=1)

        list_label = []
        i = 0
        for name, value in dict_menu.items():
            label = tk.Label(self, text=name + ": $" + str(value))
            label.pack()

        def exit():
            self.after(100,self.destroy())
            controller.show_frame(TodayPage)

        button_exit = tk.Button(self, text="Back to Home",
                        command=exit)
        button_exit.pack()


class CalcWaitTimePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        L1 = tk.Label(self, text="Input number of people in queue")
        L1.pack()
        E1 = tk.Entry(self, bd =5)
        E1.pack()

        def printtext():
            try:
                user_input = int(E1.get())
                if user_input >= 0:
                    wait_time = user_input * 5
                    tk.messagebox.showinfo("Approximate Waiting Time", \
                                            str(wait_time) + " min")
                else:
                    tk.messagebox.showinfo("Approximate Waiting Time", \
                                           "Invalid input. Please enter a number that is at least 0")
            except:
                    tk.messagebox.showinfo("Approximate Waiting Time", \
                                           "Invalid input. Please enter a valid number.")





        b = tk.Button(self,text='Calculate',command=printtext)
        b.pack()

        button1 = tk.Button(self, text="Back to Canteen",
                            command=lambda: controller.show_frame(TodayPage))
        button1.pack()

        button2 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button2.pack()


class OpHoursPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(background='powder blue')
        label1 = tk.Label(self, text="Operating Hours", font='Hekvetica 25 bold', background='yellow')
        label1.pack()
        label2 = tk.Label(self, \
                          text="Drinks Stall: Monday to Saturday, 0700 to 2200")
        label2.pack()
        label3 = tk.Label(self, \
                          text="Economical Rice: Monday to Saturday, 0700 to 2200")
        label3.pack()
        label4 = tk.Label(self, \
                          text="Macdonalds: Monday to Sunday, 0700 to 2400")
        label4.pack()
        label5 = tk.Label(self, \
                          text="Malay Stall: Monday to Saturday, 0700 to 2200")
        label5.pack()
        label6 = tk.Label(self, \
                          text="Western Food: Monday to Saturday, 1100 to 2200")
        label6.pack()

        button_exit = tk.Button(self, text="Back to Home", command=lambda: controller.show_frame(StartPage))
        button_exit.pack()


app = SeaofBTCapp()
app.mainloop()
