from clock_monitor import get_current_time
from leap_detector import detect_skipped_second
from logger import log_negative_leap
import time

print("Starting LeapSense...")

previous_time = get_current_time()

while True:
    time.sleep(1)
    current_time = get_current_time()

    if detect_skipped_second(previous_time, current_time):
        log_negative_leap(current_time)

    previous_time = current_time
