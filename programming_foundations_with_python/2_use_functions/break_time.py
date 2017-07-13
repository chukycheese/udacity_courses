# 9. Squashing the Bug

import webbrowser
webbrowser.open('https://youtu.be/uYbns3auKyw')

# 10. Making the Program Wait
import webbrowser
import time

time.sleep(3)
webbrowser.open('https://youtu.be/uYbns3auKyw')

# 11. Adding a Loop
import webbrowser
import time

for i in range(3):
    time.sleep(3)
    webbrowser.open('https://youtu.be/uYbns3auKyw')

total_breaks = 3
break_count = 0
print("This program started on" + time.ctime())
while (break_count < total_breaks):
    time.sleep(3)
    webbrowser.open('https://youtu.be/uYbns3auKyw')
    break_count += 1

# 12. Making the Program Wait Longer
