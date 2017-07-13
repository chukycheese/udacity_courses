# 12. Making the program wait longer
import webbrowser
import time

total_breaks = 3
break_count = 0
print("This program started on" + time.ctime())
while (break_count < total_breaks):
    time.sleep(10) # Changed from 3 secs to 10 secs
    webbrowser.open('https://youtu.be/uYbns3auKyw')
    break_count += 1
