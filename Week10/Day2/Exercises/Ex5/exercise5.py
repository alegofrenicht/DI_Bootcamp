# Exercise 5 : Amount Of Time Left Until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

import datetime

today = datetime.datetime.today()
date = datetime.datetime.strptime('2024-01-01 00:00:00', "%Y-%m-%d %H:%M:%S")
jan_01 = date - today
print(f"The 1st of January is in {jan_01.days} days  and {int(jan_01.seconds / 3600)} hours")
