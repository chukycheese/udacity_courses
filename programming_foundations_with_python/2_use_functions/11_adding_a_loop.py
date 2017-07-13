# 11. Adding a Loop
import webbrowser
import time

# Using a for-loop
print("This program started on" + time.ctime())
for i in range(3):
    time.sleep(3)
    webbrowser.open('https://youtu.be/uYbns3auKyw')

# Using a while-loop
total_breaks = 3
break_count = 0
print("This program started on" + time.ctime())
while (break_count < total_breaks):
    time.sleep(3)
    webbrowser.open('https://youtu.be/uYbns3auKyw')
    break_count += 1
