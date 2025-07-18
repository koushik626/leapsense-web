def detect_skipped_second(prev_time, current_time):
    delta = (current_time - prev_time).total_seconds()
    if delta < 0.5:  # A second was skipped (went too fast)
        return True
    return False
