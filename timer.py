import time
import os
import subprocess
import threading
import PySimpleGUI as sg
import platform

# Function to play the beep sound
def play_beep():
    sound_path = os.path.join(os.path.dirname(__file__), "complete.oga")

    # Check the platform and use the appropriate command to play the sound
    if platform.system() == "Windows":
        # Windows command using the start command to play the sound
        subprocess.Popen(["start", "/min", "mplay32", "/play", sound_path], shell=True)
    elif platform.system() == "Darwin":  # macOS
        subprocess.Popen(["afplay", sound_path])
    else:  # Assume Unix-based systems, will work for distribution that uses pulseaudio
        subprocess.Popen(["paplay", sound_path])

# Timer function
def start_timer_thread(window, first, second, num_repeats):
    def update_countdown(window, remaining_minutes, remaining_seconds):
        time_string = f"\rCountdown: {remaining_minutes:02d}:{remaining_seconds:02d} remaining"
        window["-OUTPUT-"].update(time_string)

    for _ in range(num_repeats):
        timers = [first, second]
        for timer in timers:
            for remaining_minutes in range(timer, -1, -1):
                for remaining_seconds in range(59, -1, -1):
                    update_countdown(window, remaining_minutes, remaining_seconds)
                    time.sleep(1)  # 1 second
            play_beep()

# Theme
sg.theme('DarkTanBlue')   # Add a touch of color

# GUI Layout
layout = [
    [sg.Text("Pomodoro Timer", justification='center',size=(55,1))],
    [sg.Text("First timer:            "), sg.InputText(key="-FIRST-")],
    [sg.Text("Second timer:       "), sg.InputText(key="-SECOND-")],
    [sg.Text("Number of repeats:"), sg.InputText(key="-REPEATS-")],
    [sg.Button("Start")],
    [sg.Text(size=(30, 2), key="-OUTPUT-")]  # Element to display countdown status
]

# Create the window and set resizable attribute to True
window = sg.Window("PomoTimer", layout, size=(250, 200), resizable=True)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    first = int(values["-FIRST-"]) - 1
    second = int(values["-SECOND-"]) - 1
    num_repeats = int(values["-REPEATS-"])

    if first <= -1 or second <= -1 or num_repeats <= -1:
        sg.popup("Timers and repeat count should be greater than zero.")
    else:
        window["-OUTPUT-"].update("")  # Clear previous output
        # Start the timer in a separate thread
        threading.Thread(target=start_timer_thread, args=(window, first, second, num_repeats), daemon=True).start()

window.close()
