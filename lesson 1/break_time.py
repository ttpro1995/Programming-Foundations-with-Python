import webbrowser
import time
# open web browser every 30 minute
current_time = time.ctime() # get current time
print ("start time = " + current_time)
i = 0
while(i<5):
    time.sleep(1800)
    url="https://www.youtube.com/watch?v=spb2349fZiM" 
    webbrowser.open(url)
    i=i+1
    

