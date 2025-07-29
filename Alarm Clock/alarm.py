import datetime
import time
from playsound import playsound

def alarm_clock():
    print(" Welcome to the Alarm Clock!")
    
    alarm_time = input("Enter the alarm time (HH:MM:SS in 24-hour format): ").strip()

    try:
        alarm_hour, alarm_minute, alarm_second = map(int, alarm_time.split(":"))
    except ValueError:
        print(" Invalid time format. Please use HH:MM:SS (e.g., 07:30:00).")
        return

    print(f" Alarm is set for {alarm_time}. Monitoring time... (Press Ctrl+C to stop)\n")

    while True:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f" Current time: {current_time}", end="\r")

        if current_time == alarm_time:
            print("\n Time's up! Playing alarm...")
            try:
                playsound("alarm.mp3")
            except:
                print(" Could not play alarm sound. Make sure 'alarm.mp3' exists.")
            break

        time.sleep(1)

if __name__ == "__main__":
    alarm_clock()
