from typing import Callable
import time


def wait_until(predicate: Callable, error_message: str = None, timeout=10, poll_frequency=0.5):
    start = time.time()
    while True:
        try:
            return_value = predicate()
            if return_value:
                return return_value
        except:
            time.sleep(poll_frequency)
        if time.time() - start > timeout:
            raise TimeoutError(error_message)
        time.sleep(poll_frequency)
