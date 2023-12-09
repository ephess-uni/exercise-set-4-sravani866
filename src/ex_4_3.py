""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Your docstring here.  Replace the pass keyword below with your implementation.
    """
    shutdown_events = get_shutdown_events(logfile)

    if len(shutdown_events) < 2:
        raise ValueError("Insufficient shutdown events to calculate time difference.")
    
        
    try:
        first_shutdown_time = logstamp_to_datetime(shutdown_events[0].split(' ', 2)[1])
        last_shutdown_time = logstamp_to_datetime(shutdown_events[-1].split(' ', 2)[1])

        time_difference = last_shutdown_time - first_shutdown_time
        return time_difference
    except ValueError as e:
        raise ValueError(f"Error parsing date stamps: {e}")


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    try:
        result = time_between_shutdowns(FILENAME)
        print(f'Time between first and last shutdowns: {result}')
    except Exception as e:
        print(f'Error: {e}')
