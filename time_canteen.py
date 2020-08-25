from datetime import *
from input_fun import*
import calendar


def list_to_datetime(list_time):
    return datetime.datetime(list_time[0], list_time[1], list_time[2],\
                    list_time[3], list_time[4], list_time[5], list_time[6])

def transform_from_datetime(date):
    string = str(date)
    year, month, day = string[0:10].split("-")
    year = int(year)
    month = int(month)
    day = int(day)
    hour, min, sec = string[11:19].split(":")
    hour = int(hour)
    min = int(min)
    sec = int(sec)
    return [year, month, day, hour, min, sec]
#preparation functions





#this classin charge of the time
#it enables you to input a new time, then count the time also
#it can also give the time now, just remember to speicify NOW=1
#default value of time is the time when the object is created
#remeber to update the time before you use it
class time_canteen(object):
    def __init__(self,year=None,month=None,day=None,hour=None,min=None,sec=None):
        self.time = list()
        self.time_start = datetime.now()
        self.time_tab = datetime.now()
        self.operating_time = input_operate()
        self.breakfast = input_meal("breakfast.txt")
        self.lunch = input_meal("lunch.txt")
        self.dinner = input_meal("dinner.txt")

    def get_time(self):
        print("time called")
        return self.time

    #Please either specify the new time or indicate that NOW=1, or else it gives error
    def input_time(self,year=None,month=None,day=None,hour=None,min=None,sec=None,NOW=1):
        print("input_time called",self.time)
        if year==None and NOW==0:
            print("Invalid input for 'input time")
            return int(a)#a error as a reminder
        if NOW == 1:
            self.time = transform_from_datetime(datetime.now())
        else:
            self.time = [year, month, day, hour, min, sec]
            self.time_start = datetime(year, month, day, hour, min, sec)
        self.time_tab = datetime.now()#used to count the time passed since the user input time
        print(self.time)
        return self.time
    #enables you to change the time stored in class, to user-defined time

    def update_time(self,NOW=1):
        print("update_time called",self.time)
        if NOW==1:
            self.time = transform_from_datetime(datetime.now())
            return self.time
        # get and change the time stored in class to now
        if NOW==0:
            datetime_now = datetime.now()
            datetime_pass = datetime_now - self.time_tab
            self.time = transform_from_datetime(datetime_pass + self.time_start)
            return self.time
    #get the new time, when user define a time, time after the defined is considered


    #give you the day when you input time, by default it will give you a string
    #to give number, use String=0
    #
    def get_day(self,year, month, day,String=1):
        dayNum = calendar.weekday(year, month, day)
        # returns a number indicate which day is it
        if String == 0:
            return dayNum+1
        else:
            day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            return day[dayNum]
            #output a string of which day is it


    #want a specific time--enter the time and NOW=0
    #want the time stored and counted -- don't enter anything and NOW=0
    #want now -- NOW=1
    #this function is designed to get the menu when stall is open, please use get_stall to check frist before using it
    def get_menu(self,stall=None,year=None,month=None,day=None,hour=None,min=None,sec=None,NOW=1):
        print("get_menu called",self.time)
        if year==None and NOW==0:
            self.update_time(NOW=0)
            year, month, day, hour, min, sec = self.time
        if NOW==1:
            self.update_time(NOW=1)
            year, month, day, hour, min, sec = self.time
        # check if you want the time stored in the class
        time = hour*100+min
        #changing format of time, from h,m to hhmm
        stall_info = self.operating_time[stall]
        t1 = stall_info[4]#time between breakfast and lunch
        t2 = stall_info[5]
        #get the time that seperates breakfast, lunch and dinner
        today = self.get_day(year,month,day,String=1)
        if time < t1:
            return self.breakfast[stall][today]
        if time < t2:
            return self.lunch[stall][today]
        return self.dinner[stall][today]


    #want a specific time--enter the time and NOW=0
    #want the time stored and counted -- don't enter anything and NOW=0
    #want now -- NOW=1
    #this method is designed to get the stores that are open, list will be returned in the end
    def get_stall(self,year=None,month=None,day=None,hour=None,min=None,sec=None, NOW=1):
        print("get_stall called",self.time)
        if NOW==0 and year==None:
            self.update_time(NOW=0)
            year, month, day, hour, min, sec = self.time
        if NOW==1:
            self.update_time(NOW=1)
            year,month,day,hour,min,sec = self.time
        list_stall = list()
        today = self.get_day(year, month, day,String=0)
        now = 100*hour + min
        #transform time from h,m to hhmm
        list_day = {"Monday": 1, "Tuesday": 2, "Wednesday": 3, "Thursday": 4, "Friday": 5, "Saturday": 6, "Sunday": 7}
        #this enable you to convert day to number, so that you can compare the day
        for name, value in self.operating_time.items():
            start_day = list_day[value[2]]
            end_day = list_day[value[3]]
            # by comparing the start and end operating days and hours, we get know which stalls are open
            if start_day <= today and today <= end_day:
                start_time = int(value[0])
                end_time = int(value[1])
                if start_time-1 <= now and now <= end_time-1:
                    list_stall.append(name)
        return list_stall