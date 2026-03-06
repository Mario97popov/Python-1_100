from pipeline_utils import clean_name, assess_batch

print(clean_name("  orders pipeline  "))
print(assess_batch(500, 5.0))


'''
Create a file called pipeline_utils.py that contains:

1. A function called clean_name(name) that strips whitespace
   and converts to title case
2. A function called assess_batch(record_count, null_percentage)
   that returns "PASS", "WARNING", or "REJECT" using the same
   rules as Task 6
3. A function called summarise(batches) that prints the total
   number of batches and how many are each status

Then at the bottom, under if __name__ == "__main__":
test all three functions with your own sample data and print
the results.

The key requirement: if someone imports pipeline_utils.py
from another file, none of the test code should run.
Create a second file called main.py that imports and uses
clean_name and assess_batch from pipeline_utils.py to prove
the import works cleanly.
'''