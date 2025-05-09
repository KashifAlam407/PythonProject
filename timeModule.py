import time

print(time.gmtime(0))   ## it give the epoch time (january 1, 1970)

print(time.time())   ## it give the current time in seconds since epoch

print(time.ctime())  ## it give the current time with 24 character time string

print(time.ctime(1627908313.717886))  ## the code to convert a specified timestamp into a human redable date and time format.

# print(time.sleep(5))   ## it delay the execution for 5 seconds 

print(time.localtime(1627987508.6496193))  ## it returns the struct_time object in local time.

print(time.mktime(time.localtime(1627987508.6496193)))  ## it is the inverse function of time.localtime() 
print(time.mktime(time.gmtime(1627987508.6496193)))   ## it is the inverse function of time.localtime()

print(time.gmtime(1627987508.6496193))   ## used to convert time in struct_time expressed in seconds since the epoch.

from time import gmtime, strftime, localtime
print(strftime("%a, %d %b %Y %H:%M:%S", gmtime(1627987508.6496193)))   ## Converting struct_time object to a string using strftime() method
print(strftime("%a, %d %b %Y %H:%M:%S", localtime(1627987508.6496193)))

print(time.asctime(time.gmtime(1627987508.6496193)))  ## converting tuple to time.struct_time object to string
print(time.asctime(time.localtime(1627987508.6496193)))  ## converting tuple to time.struct_time object to string

string = "Tue, 03 Aug 2021 10:45:08"
print(time.strptime(string, "%a, %d %b %Y %H:%M:%S"))    ## converting string to struct_time object












