import datetime
import calendar

s=input()
born = datetime.datetime.strptime(s, '%d %m %Y').weekday() 
print(calendar.day_name[born]) 

