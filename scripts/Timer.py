# -*- coding: utf-8 -*-
"""
Created: May 2020

@author: Ryan Clement (RRCC)
"""

##### Imports #####
from time import perf_counter as sTime

##### Classes #####
class TimerError(Exception):
    """
        * Custom exception used to report errors in
          instantiations of Timer class.
        * Timer is derived from Exception class.
    """
# END: TimerError

class Timer:
    """
    Based on Python's time.perf_counter().
    """
    def __init__(self, type=None):
        # print("Initializing: Timer Instance.")
        self._start_time = None
        self.type = type

    def __del__(self):
        pass
        # print("Deleting Timer instance.")

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError(f"Timer is running. Use .stop() to stop it.")

        self._start_time = sTime()

    def stop(self):
        """Stop the timer, and report the elapsed time."""
        if self._start_time is None:
            raise TimerError(f"Timer is not running. Use .start() to start it")

        elapsed_time = sTime() - self._start_time
        self._start_time = None
        if self.type is not None:
            outText = "Elapsed "+self.type+" time: {:0.6f} seconds"
        else:
            outText = "Elapsed time: {:0.6f} seconds"

        print(outText.format(elapsed_time))
# END: Timer