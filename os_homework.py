import _thread
import platform
import requests
import os 

b = os.getpid()
print("The pid of this process is:",b)


if(platform.system() == "Linux"):
   print("Your operating system is Linux..", os.getloadavg() )
   load1, load5, load15 = os.getloadavg()
   if (len(os.sched_getaffinity(0)) - load5 < 1):
      print("program finisned")
   exit();
else:
   print("Your operating system is not Linux")






array = ["https://api.github.com", "http://bilgisayar.mu.edu.tr/", "https://www.python.org/", "http://akrepnalan.com/ceng2034","https://github.com/caesarsalad/wow"]




def myThread():
   count = 0
   while count < len(array):

      print("satatus code of the website you are trying to connect is:",requests.get(array[count]).status_code)
      count += 1



try:
   _thread.start_new_thread(myThread, ( ))
except:
   print("Error: unable to start thread")

while 1:
   pass
