#1 Welcome message
print("Welcome to my Python program!")
#2 Hours studied input
hours_studied = input(" Enter amount of hours youd studied today")
#3 Weekly goal calculation
hours_studied = float(hours_studied)
weekly_studied = hours_studied * 7
#4 display
print(f"If you keep this momentum, you will study {weekly_studied} hours this week!")
#5 Error handling 
try:
    hours_studied = float(hours_studied)
except ValueError:
    print("Please enter a valid integer for hours studied.")
    exit()
# 6 Final Cleanup and comments
# The code has 6 sections
#1 Welcome message
#2 Hours studied input
#3 Weekly goal calculation
#4 display
#5 Error handling  
#6 Final Cleanup and comments