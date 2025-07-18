import time

timer = int(input("Set timer for how many seconds: "))

while timer != 0.0:
    seconds = timer % 60
    minutes = int(timer / 60) % 60
    hours = int(timer / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    timer -= 1
    time.sleep(1)

print("Timer ended")

