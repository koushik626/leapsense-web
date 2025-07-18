# LeapSense: Negative Leap Second Detector

## Overview
LeapSense is a simple Python project that detects when a negative leap second may have occurred by monitoring system clock behavior.

## How it Works
- Checks system time every second
- If time skips (i.e., jumps ahead by more than 1 second), it logs a warning

## Run the Project

```bash
python main.py
```

## Files
- `main.py`: Runs the detection loop
- `clock_monitor.py`: Provides current time
- `leap_detector.py`: Checks for skipped seconds
- `logger.py`: Logs detections
