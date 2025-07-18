def log_negative_leap(time):
    with open("leapsec_log.txt", "a") as f:
        f.write(f"[WARNING] Negative leap second detected at {time}\n")
    print(f"[ALERT] Negative leap second at {time}")
