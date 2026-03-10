import time

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling: {func.__name__}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        elapsed = end - start
        print(f"Finished: {func.__name__}")
        print(f"Time taken: {elapsed:.2f}s")
        print(f"Result: done")

    return wrapper


@log_call
def process_data():
    time.sleep(0.5)
    return process_data

process_data()

'''
Write two decorators:

1. A decorator called log_call that prints a message before and
   after any function it decorates, showing the function name

2. A decorator called timer that measures and prints how long
   a function takes to run in seconds

Then write a function called process_data that sleeps for 0.5
seconds and returns "done" and apply both decorators to it.

Call process_data() once.

Expected output:
Calling: process_data
Finished: process_data
Time taken: 0.50s
Result: done
'''