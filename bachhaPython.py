import time

#python ko aasani se aur turant vyavahar karne ke liye library

# 1. time aur date ke liye function etc
def getMonthName(month_number):
    monthList = ["Jan" , "Feb" , "Mar" , "Apr" , "May" , "Jun" , "Jul" , "Aug", "Sep" , "Oct" ,"Nov" , "Dec"]
    return monthList[month_number]

def date(format="/"): 
    #aaj ka date return karega
    #@@@format: date('/')  ya date('simple') ya date('-') ya date('naam')
    t= time.localtime()
    if format== "simple" or format=="/": #dd/mm/yyyy format me
        beechMein = '/'
        return str(t.tm_mday) + beechMein + str(t.tm_mon) + beechMein + str(t.tm_year)
    if format=="-": #dd-mm-yyyy format me
        beechMein = '-'
        return str(t.tm_mday) + beechMein + str(t.tm_mon) + beechMein + str(t.tm_year)
    if format=="naam":  # dd MON yyyy format me   
        beechMein = ' '   
        return str(t.tm_mday) + beechMein + (getMonthName(t.tm_mon) ) +beechMein + str(t.tm_year)
    return "fault"


def samay(arg=time.time()):
    t = time.localtime() 
    if t.tm_min < 10: t.tm_min  = '0'+ str(t.tm_min)
    if t.tm_hour < 10: t.tm_hour  = '0'+ str(t.tm_hour)

    if arg == "24hr" or arg =="24":
        return str(t.tm_hour) + str(t.tm_min)
    if arg=="12hr" or arg =="12":
        ampm="am"
        if t.tm_hour<12:
             hour =  t.tm_hour
        else: 
            hour = 24-t.tm_hour
            ampm = 'pm'
        return str(hour) + ':' +str(t.tm_min) + ' '+ ampm
    return arg

#filesystem
def file():

def fileType():

def fileInfo():

def fileDelete():

def files():

#sanitizing
def sanitize(variable , spec):

#graphics 
def drawing():
#gui
#utility
#search and filter
#parser
#networking




#testing ke liye 
if __name__ == "__main__":

    #date() function ke liye
    print("testing date function: ")
    c =  date('naam')
    d =  date('/')
    e =  date('-')
    f =  date('simple')

    print(c)
    print(d)
    print(e)
    print(f)
    print(date())
    print("date() function tested OK \n")

    #samay() function ke liye
    print("testing samay function: ")
    print("samay('24hr') -> " +samay('24hr'))
    print("samay('24') -> "+ samay('24'))
    print("samay('12') -> "+ samay('12'))
    print("samay('12hr') -> "+ samay('12hr'))
    print("samay function tested OK")
    s1 = samay()
    print(s1)
    #time.sleep(1.0) //time ruk jaat hai kya , differnce nahi dikha raha hai
    s2 = samay()
    print(s2)
    s = s2-s1
    print("time difference :" + str(s) )
