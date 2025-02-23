weather_cond = input("What's the weather condition (Rainy, Sunny, or Foggy): ")

trav_speed = int(input("What speed is the car traveling at?: "))

if trav_speed > 70 :
    if weather_cond.strip().lower() == "rainy" or weather_cond.strip().lower() == "foggy":
        print("High chance of accident!")
    else:
        print("Low chance of acciddent.")

speeds = [30, 45, 65, 70, 85, 90]

i = 0
for speed in speeds:
    if speed > 60:
        i += 1
print(f"There are {i} cars traveling greater than 60 mph.")

accident_prob = {"morning": 0.1, "afternoon": 0.2, "night": 0.5}

time = input("What is the time of day (morning, afternoon, or night)?: ")

if time.strip().lower() in accident_prob:
    print(f"The probability of an accident at {time} is {accident_prob[time]}.")
else:
    print("Unknown time of day.")