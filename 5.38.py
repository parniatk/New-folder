#(Simulation: clock countdown)
import time

#Get the number of seconds from the user
total_seconds = int(input("Enter the number of seconds "))

# Counter to display the number of seconds

countdown = total_seconds

while countdown > 0:
    print(f"Seconds left :{countdown}")
    time.sleep(1)  
    countdown -= 1

print ("Time is up")