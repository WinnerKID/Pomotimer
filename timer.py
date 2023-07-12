import time
import subprocess

print("Pomodoro Timer\n")

first = input("Enter your first timer(minutes): ")
second = input("Enter your first timer(minutes): ")

# Convert inputs to integers
try:
    first = int(first)
    second = int(second)
except ValueError:
    print("Invalid input. Please enter integers.")
    exit()

# Verify that the inputs are positive
if first <= 0 or second <= 0:
    print("Timers should be greater than zero.")
    exit()

# Function to play the beep sound
def play_beep():
    subprocess.Popen(["paplay", "/usr/share/sounds/freedesktop/stereo/complete.oga"])

# Timer function
def start_timer():
    # First beep after 25 minutes
    time.sleep(first * 60)  # Convert 25 minutes to seconds
    play_beep()

    # Second beep after 5 minutes
    time.sleep(second * 60)  # Convert 5 minutes to seconds
    play_beep()

# Start the timer
start_timer()
