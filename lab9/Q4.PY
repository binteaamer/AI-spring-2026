import random

states = ["Sunny", "Cloudy", "Rainy"]
transition = {
    "Sunny":   [0.6, 0.3, 0.1],
    "Cloudy":  [0.3, 0.4, 0.3],
    "Rainy":   [0.2, 0.3, 0.5]
}

def next_state(current):
    probs = transition[current]
    return random.choices(states, probs)[0]

current = "Sunny"
weather = [current]

for i in range(9):  
    current = next_state(current)
    weather.append(current)

print("Weather for 10 days:")
for i in range(10):
    print("Day", i+1, ":", weather[i])
rainy_days = 0
for w in weather:
    if w == "Rainy":
        rainy_days += 1

print("\nTotal Rainy Days:", rainy_days)
