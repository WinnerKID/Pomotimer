import time
import os
import subprocess

print("Pomodoro Timer\n")

first       = input("Enter your first timer(minutes): ")
second      = input("Enter your first timer(minutes): ")
num_repeats = input("Enter the number of times the timer will repeat: ")

# Convert inputs to integers
try:
    first       = int(first) - 1
    second      = int(second) - 1
    num_repeats = int(num_repeats)
    
except ValueError:
    # Verify that the inputs are positive
    if first <= 0 or second <= 0 or num_repeats <= 0:
        print("Timers and repeat count should be greater than zero.")
        exit()

# Function to play the beep sound
def play_beep():
    # Get the path to the complete.oga file relative to the timer.py script
    sound_path = os.path.join(os.path.dirname(__file__), "complete.oga")
    subprocess.Popen(["paplay", sound_path])


# Timer function
def start_timer():
    for _ in range(num_repeats):
        timers = [first, second]
        for timer in timers:
            remaining_minutes = timer
            while remaining_minutes >= 0:
                for remaining_seconds in range(59, -1, -1):
                    print(f"\rCountdown: {remaining_minutes:02d}:{remaining_seconds:02d} remaining", end="", flush=True)
                    time.sleep(1)  # 1 second
                remaining_minutes -= 1
            print()  # Print a new line after countdown completion
            play_beep()

# Start the timer
start_timer()
