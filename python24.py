import random
random.seed(42)

max_retries = 5
attempts = 0

while attempts < max_retries:
    attempts += 1
    random_num = random.randint(1, 10)
    if random_num > 7:
        print(f"Attempt {attempts}: rolled {random_num} - success!")
        print(f"Pipeline succeeded after {attempts} attempts.")
        break
    else:
        print(f"Attempt {attempts}: rolled {random_num} - retrying...")
else:
    print(f"Pipeline failed after {max_retries} attempts.")
'''
You are simulating a pipeline retry mechanism. A pipeline keeps
retrying until it succeeds or hits a maximum number of attempts.

Your script should:
1. Set max_retries to 5 and attempts to 0
2. On each attempt generate a random number between 1 and 10
   using random.randint(1, 10)
3. If the number is greater than 7 the pipeline succeeds - print
   the success message and stop retrying
4. If attempts reaches max_retries without success - print the
   failure message and stop
5. Print each attempt regardless of outcome

Expected output:
Attempt 1: rolled 2 - retrying...
Attempt 2: rolled 10 - success!
Pipeline succeeded after 2 attempts.
'''