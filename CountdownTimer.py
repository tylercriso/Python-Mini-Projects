import time

countdown_time = int(input("Enter the countdown time in seconds: "))

while countdown_time > 0:
    print(f"Time remaining: {countdown_time} seconds")
    countdown_time -= 1
    time.sleep(1)
print("Countdown finished!")