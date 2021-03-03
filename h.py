import time
import sys
import os

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
        beechMein = '-'   
        return str(t.tm_mday) + beechMein + (getMonthName(t.tm_mon) ) +beechMein + str(t.tm_year)
    return "fault"


def samay(arg=time.time()):
 #   @@@desc: samay('12') ya samay ('24') use karna


    t = time.localtime() 
    if t.tm_min < 10:
         min = '0'+ str(t.tm_min)
    else: 
        min = str(t.tm_min)
    if t.tm_hour < 10:
         hour  = '0'+ str(t.tm_hour)
    else:
        hour = str(t.tm_hour) #repeat below
        
    if arg == "24hr" or arg =="24":
        return hour + min
    if arg=="12hr" or arg =="12":
        ampm="am"
        if t.tm_hour>12:
            hour = str(t.tm_hour -12)
            ampm = 'pm'
        return hour + ':' + min + ' '+ ampm
    return arg #localtime() return kar diya agar koi argument nhi diya to

#filesystem
def fileList( str="./", recursive=False):
    a = os.scandir(str)
    r = []
    for i in a:
        if i.is_file():
            r.append(i.path)
    return r

def folderList( str="./", recursive=False):
    a = os.scandir(str)
    r = []
    for i in a :
        if i.is_dir():
            r.append(i.path)
    return r
    
def fileKhojo():
    pass
def fileBanao():
    pass
def fileType():
    pass
def fileInfo():
    pass
def fileHatao():
    pass
def nayaFolder():
    pass
def clone():
    pass
def hatao():
    pass
#textprocessing
#sanitizing
def sanitize(variable , spec):
    pass
#graphics 
def drawing():
    pass
#gui
#utility
#search and filter
#parser
#networking
#database




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
    print("samay('24hr') -> " + samay('24hr'))
    print("samay('24') -> " + samay('24'))
    print("samay('12') -> " + samay('12'))
    print("samay('12hr') -> " + samay('12hr'))
    print("samay function tested OK")
    s1 = samay()
    print(s1)
    #time.sleep(1.0) //time ruk jaata hai kya ? , differnce nahi dikha raha hai
    s2 = samay()
    print(s2)
    s = s2-s1
    print("time difference :" + str(s) )
    print ("samay() function tested OK")


    #filesystem function trest karne ke liye
    print("\n\nfilesystem functions test")
    k= fileList("C:\\")
    print("C:\ ke files: ")
    print (k)
    print("bina argument ke file LIst ")
    k= fileList()
    print (k)
    k = folderList("C:\\")
    print("C:\ ke folders: ")
    print (k)
    k = folderList()
    print("bina argument ke folder LIst ")
    print("filesystem functions \tfileList() \tfolderList() \ntested OK")


#filesystem testerd OK


