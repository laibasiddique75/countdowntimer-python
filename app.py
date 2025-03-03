import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)  # Minutes and seconds calculate ho rahe hain
        time_format = '{:02d}:{:02d}'.format(mins, secs)  # Format time into MM:SS
        print(time_format, end="\r")  # Overwrite previous output
        time.sleep(1)  # Wait for 1 second (delay)
        seconds -= 1  # Reduce time by 1 second

    print("00:00 \nTime's Up!")  # Display when countdown ends

# User input for timer
total_seconds = int(input("Enter time in seconds for countdown: "))
countdown_timer(total_seconds)