import random

temperatures = []

for i in range(7):
    temperatures.append(random.randint(26, 40))

days_of_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

good_days = []
good_days_count = 0

for i in range(len(temperatures)):
    if temperatures[i] % 2 == 0:
        good_days_count += 1
        good_days.append(days_of_the_week[i]) 

highest_temp = max(temperatures)
lowest_temp = min(temperatures)
highest_temp_day = days_of_the_week[temperatures.index(highest_temp)]
lowest_temp_day = days_of_the_week[temperatures.index(lowest_temp)]

average_temp = sum(temperatures) / len(temperatures)
above_avg_days=[]
for i in range(len(temperatures)):
    if temperatures[i] > average_temp:
        above_avg_days.append(days_of_the_week[i])

print("Temperatures for the week:", temperatures)
print("Good days for Shelly:", good_days,good_days_count ,"days")
print("Highest temperature:", highest_temp, "on", highest_temp_day)
print("Lowest temperature:", lowest_temp, "on", lowest_temp_day)
print("Average temperature:", average_temp)
print("Days with temperatures above the average:", above_avg_days)
