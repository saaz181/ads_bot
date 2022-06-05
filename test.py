import winsound
import random

while True:
    frequency = random.randint(500, 5000)
    duration = random.randint(500, 1000)
    winsound.Beep(frequency, duration)
